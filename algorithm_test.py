def Gillespie_SIR(G, tau, gamma, initial_infecteds=None, 
                    initial_recovereds = None, rho = None, tmin = 0, 
                    tmax=float('Inf'), recovery_weight = None, 
                    transmission_weight = None, return_full_data = False, sim_kwargs = None):
    #tested in test_SIR_dynamics
    r'''    
    
    Performs SIR simulations for epidemics.
    
    For unweighted networks, the run time is usually slower than fast_SIR, but 
    they are close.  If we add weights, then this Gillespie implementation 
    slows down much more.  
    
    I think there are better ways to implement the algorithm to remove this.  
    This will need a new data type that allows us to quickly sample a random 
    event with appropriate weight.  I think this is doable through a binary 
    tree and it is in development.
    
    Rather than using figure A.1 of Kiss, Miller, & Simon, this uses a method 
    from Petter Holme 
        "Model versions and fast algorithms for network epidemiology"
    which focuses on SI edges (versions before 0.99.2 used a
    method more like fig A.1).  
    
            
    This approach will not work for nonMarkovian transmission.  Boguna et al
        "Simulating non-Markovian stochastic processes"
    have looked at how to handle nonMarkovian transmission in a Gillespie 
    Algorithm.  At present I don't see a way to efficientl adapt their 
    approach - I think each substep will take O(N) time.  So the full algorithm 
    will be O(N^2).  For this, it will be much better to use fast_SIR
    which I believe is O(N log N)
    
    :See Also:

    **fast_SIR** which has the same inputs but uses a different method to 
    run faster, particularly in the weighted case.
    
    :Arguments:
         
    **G** networkx Graph
        The underlying network
    **tau** positive float
        transmission rate per edge
       
    **gamma** number
        recovery rate per node
    
    **initial_infecteds** node or iterable of nodes
        if a single node, then this node is initially infected
        
        if an iterable, then whole set is initially infected
        
        if None, then choose randomly based on rho.  
        
        If rho is also None, a random single node is chosen.
        
        If both initial_infecteds and rho are assigned, then there
        is an error.
        
    **initial_recovereds** iterable of nodes (default None)
        this whole collection is made recovered.
        Currently there is no test for consistency with initial_infecteds.
        Understood that everyone who isn't infected or recovered initially
        is initially susceptible.
        
    **rho** number
        initial fraction infected. number is int(round(G.order()*rho))
        
    **tmin** number (default 0)
        starting time
            
    **tmax** number (default Infinity)
        stop time
        
    **recovery_weight** string (default None)
        the string used to define the node attribute for the weight.
        Assumes that the recovery rate is gamma*G.nodes[u][recovery_weight].
        If None, then just uses gamma without scaling.
    
    **transmission_weight** string (default None)
        the string used to define the edge attribute for the weight.
        Assumes that the transmission rate from u to v is 
        tau*G.adj[u][v][transmission_weight]
        If None, then just uses tau without scaling.

    **return_full_data** boolean (default False)
        Tells whether a Simulation_Investigation object should be returned.  

    **sim_kwargs** keyword arguments
        Any keyword arguments to be sent to the Simulation_Investigation object
        Only relevant if ``return_full_data=True``


    :Returns: 
        
    **times, S, I, R** each a numpy array
        giving times and number in each status for corresponding time

    OR if return_full_data=True:
    
    **full_data**  Simulation_Investigation object
        from this we can extract the status history of all nodes
        We can also plot the network at given times
        and even create animations using class methods.
        
    :SAMPLE USE:


    ::

        import networkx as nx
        import EoN
        import matplotlib.pyplot as plt
        
        G = nx.configuration_model([1,5,10]*100000)
        initial_size = 10000
        gamma = 1.
        tau = 0.3
        t, S, I, R = EoN.Gillespie_SIR(G, tau, gamma, 
                                    initial_infecteds = range(initial_size))
                                    
        plt.plot(t, I)
    
    '''

    if rho is not None and initial_infecteds is not None:
        raise EoN.EoNError("cannot define both initial_infecteds and rho")

    
    if return_full_data:
        infection_times = defaultdict(lambda: []) #defaults to an empty list for each node
        recovery_times = defaultdict(lambda: [])

    if transmission_weight is not None:
        def edgeweight(u,v):
            return G.adj[u][v][transmission_weight]
    else:
        def edgeweight(u,v):
            return None
    
    if recovery_weight is not None:
        def nodeweight(u):
            return G.nodes[u][recovery_weight]
    else:
        def nodeweight(u):
            return None

    tau = float(tau)  #just to avoid integer division problems in python 2.
    gamma = float(gamma)
    
    if initial_infecteds is None:
        if rho is None:
            initial_number = 1
        else:
            initial_number = int(round(G.order()*rho))
        initial_infecteds=random.sample(list(G), initial_number)
    elif G.has_node(initial_infecteds):
        initial_infecteds=[initial_infecteds]
        
    if initial_recovereds is None:
        initial_recovereds = []
        
    I = [len(initial_infecteds)]
    R = [len(initial_recovereds)]
    S = [G.order()-I[0]-R[0]]
    times = [tmin]
    
    transmissions = []
    t = tmin
    
    status = defaultdict(lambda : 'S')
    for node in initial_infecteds:
        status[node] = 'I'
        if return_full_data:
            infection_times[node].append(t)
            transmissions.append((t, None, node))
    for node in initial_recovereds:
        status[node] = 'R'
        if return_full_data:
            recovery_times[node].append(t)

    if recovery_weight is not None:
        infecteds = _ListDict_(weighted=True)
    else:
        infecteds = _ListDict_() #unweighted - code is faster for this case
    if transmission_weight is not None:
        IS_links = _ListDict_(weighted=True)
    else:
        IS_links = _ListDict_()

    for node in initial_infecteds:
        infecteds.update(node, weight_increment = nodeweight(node)) #weight is none if unweighted
        for nbr in G.neighbors(node):  #must have this in a separate loop 
                                       #from assigning status
            if status[nbr] == 'S':
                IS_links.update((node, nbr), weight_increment = edgeweight(node,nbr))
    
    total_recovery_rate = gamma*infecteds.total_weight() #gamma*I_weight_sum
    
    total_transmission_rate = tau*IS_links.total_weight()#IS_weight_sum
        
    total_rate = total_recovery_rate + total_transmission_rate
    delay = random.expovariate(total_rate)
    t += delay
    
    while infecteds and t<tmax:
        if random.random()<total_recovery_rate/total_rate: #recover
            recovering_node = infecteds.random_removal() #does weighted choice and removes it
            status[recovering_node]='R'
            if return_full_data:
                recovery_times[recovering_node].append(t)

            for nbr in G.neighbors(recovering_node):
                if status[nbr] == 'S':
                    IS_links.remove((recovering_node, nbr))
            times.append(t)
            S.append(S[-1])
            I.append(I[-1]-1)
            R.append(R[-1]+1)
        else: #transmit
            transmitter, recipient = IS_links.choose_random() #we don't use remove since that complicates the later removal of edges.
            status[recipient]='I'

            if return_full_data:
                transmissions.append((t, transmitter, recipient))
                infection_times[recipient].append(t)
            infecteds.update(recipient, weight_increment = nodeweight(recipient))

            for nbr in G.neighbors(recipient):
                if status[nbr] == 'S':
                    IS_links.update((recipient, nbr), weight_increment=edgeweight(recipient, nbr))
                elif status[nbr]=='I' and nbr != recipient: #self edge would break this without last test.elif
                    IS_links.remove((nbr, recipient))
                     
            times.append(t)
            S.append(S[-1]-1)
            I.append(I[-1]+1)
            R.append(R[-1])
            
        total_recovery_rate = gamma*infecteds.total_weight()#I_weight_sum
        total_transmission_rate = tau*IS_links.total_weight()#IS_weight_sum
        
                
        total_rate = total_recovery_rate + total_transmission_rate
        if total_rate>0:
            delay = random.expovariate(total_rate)
        else:
            delay = float('Inf')
        t += delay

    if not return_full_data:
        return np.array(times), np.array(S), np.array(I), \
                np.array(R)
    else:
        #print(infection_times)
        #print(recovery_times)
        infection_times = {node: L[0] for node, L in infection_times.items()}
        recovery_times = {node: L[0] for node, L in recovery_times.items()}
        #print(infection_times)
        #print(recovery_times)

        node_history = _transform_to_node_history_(infection_times, recovery_times, tmin, SIR = True)
        if sim_kwargs is None:
            sim_kwargs = {}
        return EoN.Simulation_Investigation(G, node_history, transmissions, possible_statuses = ['S', 'I', 'R'], **sim_kwargs)
