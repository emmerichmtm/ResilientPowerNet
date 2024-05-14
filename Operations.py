from IEEE69BusDist import *
import numpy as np


def build_graph(RootList, BusList, LineList):
    graph = {'root':[], 'buses':[], 'lines':[]}
    for root in RootList:
        graph_lines = []
        graph_buses = [root]
        i = 0
        while (i < len(graph_buses)):
            bus1 = graph_buses[i]
            for bus2 in BusList:
                for line in LineList:
                    if (line.fbus == bus1.busnum and line.tbus == bus2.busnum) or (line.fbus == bus2.busnum and line.tbus == bus1.busnum):
                        if(line not in graph_lines):
                            graph_lines.append(line)
                        if(bus2 not in graph_buses):
                            graph_buses.append(bus2)
            i+=1

        graph['root'].append(root)
        graph['buses'].append(graph_buses)
        graph['lines'].append(graph_lines)

    return graph


def count_connected(graph):
    connected = 0
    for branch in graph:
        connected += len(branch['buses'])
    return connected


def set_priorities(buses, bus_priorities_list = None):
    if bus_priorities_list is None:
        bus_priorities_list = np.random.randint(0,2,len(buses))

    for bus, priority in zip(buses, bus_priorities_list):
        bus.priority = priority

# print(build_graph(RootList, BusList, LineList))


