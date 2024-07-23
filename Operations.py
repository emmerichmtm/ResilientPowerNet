from IEEE69BusDist import *
import numpy as np

""" Objective function for the local search algorithm building a graph of connected to the root nodes 
and not considering the lines that are not in the bitmask """
def build_graph(RootList, BusList, LineList, line_bitmask=None):
    if line_bitmask is None:
        # If no bitmask is provided, all lines are considered on
        line_bitmask = [1] * len(LineList)

    graph = {'root':[], 'buses':[], 'lines':[]}
    for root in RootList:
        graph_lines = []
        graph_buses = [root]
        i = 0
        while (i < len(graph_buses)):
            bus1 = graph_buses[i]
            for bus2 in BusList:
                for line, mask in zip(LineList, line_bitmask):
                    if mask == 0:
                        continue
                    if ((line.fbus == bus1.busnum and line.tbus == bus2.busnum) or
                            (line.fbus == bus2.busnum and line.tbus == bus1.busnum)):
                        if(line not in graph_lines):
                            graph_lines.append(line)
                        if(bus2 not in graph_buses):
                            graph_buses.append(bus2)
            i += 1

        graph['root'].append(root)
        graph['buses'].append(graph_buses)
        graph['lines'].append(graph_lines)

    return graph


def count_connected(graph):
    connected = 0
    for buses in graph['buses']:
        connected += len(buses)
    return connected

def set_priorities(buses, bus_priorities_list=None):
    if bus_priorities_list is None:
        bus_priorities_list = np.random.randint(0, 2, len(buses))

    for bus, priority in zip(buses, bus_priorities_list):
        bus.priority = priority

def count_priorities(graph):
    priority_count = {1: 0, 2: 0}
    for buses in graph['buses']:
        for bus in buses:
            if bus.priority == 0:
                priority_count[1] += 1
            elif bus.priority == 1:
                priority_count[2] += 1
    return priority_count


