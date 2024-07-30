# simulates the lexicographic metropolis algorithm for the local search algorithm; currently inactive


""" Objective function for the local search algorithm counting how many nodes are connected and
how much power is lost in the network """
def objective(x, graph):
    num_connected_nodes = count_connected(graph)
    power_loss = np.sum(x)
    return (-num_connected_nodes, power_loss)

""" Randomly flip one bit in the vector """
def generate_candidate(x):
    new_x = np.copy(x)
    for i in range(len(x)):
        if random() < 1 / len(x):
            new_x[i] = 1 - new_x[i]
    return new_x

""" Metropolis criterion for the local search algorithm: 
input: current evaluation vector sorted by priority, candidate evaluation, 
temperature evaluates true if the candidate solution is better than the current solution 
or if the candidate solution is worse but the probability of accepting it is 
greater than a random number
< REMARK: CURRENTLY THE METROPOLIS CRITERION IS NOT USED IN THE LOCAL SEARCH ALGORITHM > """
"""

def lexico_metropolis(curr_eval, candidate_eval, t):
    for curr, cand in zip(curr_eval, candidate_eval):
        if cand < curr:
            return True
        elif cand > curr:
            return False
    return np.exp((sum(curr_eval) - sum(candidate_eval)) / t) > random()


""" Search for an optimal switch configuration in the network """
def local_search_with_connected_nodes(length_of_vector, graph, max_iterations=1000, temp=1.0):
    curr_solution = np.random.randint(0, 2, size=length_of_vector)
    print(curr_solution)
    curr_eval = objective(curr_solution, graph)

    for i in range(1, max_iterations + 1):
        t = temp / float(i + 1)
        candidate_solution = generate_candidate(curr_solution)
        candidate_eval = objective(candidate_solution, graph)

        if lexico_metropolis(curr_eval, candidate_eval, t):
            curr_solution = candidate_solution
            curr_eval = candidate_eval

    return curr_eval