import numpy as np
from random import random
import matplotlib.pyplot as plt
from Operations import *
from IEEE69BusDist import *
from DistribObjects import *
from DistribObjects import Bus, Line

# create a weighted objective function from the two priority counts
def objective_weighted_sum(RootList, BusList, LineList, x):
    # Validate x
    assert isinstance(x, list) and len(x) == len(
        LineList), "x must be a list of integers with the same length as LineList"

    graph69 = build_graph(RootList, BusList, LineList, x)

    # Ensure graph construction succeeded
    if not graph69['buses'] or not graph69['lines']:
        raise ValueError("Graph construction failed, check inputs")

    priority_count = count_priorities(graph69)

    # Check if the graph is short-circuited
    #if short_circular_check(graph69):
    #    return 0
    # check if the number of lines in graph69 is equal to the number of buses in graph69
    # IF NOT, RETURN NEGATIVE ABSOLUTE VALUE OF THE DIFFERENCE

    buses_connected = 0
    for buses in graph69['buses']:
        buses_connected += len(buses)
        print("connected buses",buses_connected)
    #  Same for lines

    lines_connected = 0
    for lines in graph69['lines']:
        lines_connected += len(lines)
        #print("connected lines",lines_connected)

    diff = buses_connected - (lines_connected+1)
    #print("diff = ", diff)
    if diff != 0:
        # print breakdown of the difference     diff = (len(graph69['lines'])-1) - (len(graph69['buses']))
        # print  diff, (len(graph69['lines'])-1), (len(graph69['buses']))
        #print("len(graph69['lines'])-1 = ", (len(graph69['lines'])-1))
        #print("len(graph69['buses']) = ", len(graph69['buses']))
        #print("in objective_weighted_sum, diff = ", diff)


        #print("in objective_weighted_sum, diff = ", diff)
        return -abs(diff)

    return priority_count[1] + 5 * priority_count[2]

def local_search_with_mask(start_switch_vector, mask, RootList, BusList, LineList, max_iterations=1000):
    """ Local search algorithm with a mask that restricts the changes that can be made to the bit vector.
     start_switch_vector: initial bit vector
     mask: bit vector that restricts the changes that can be made to the start_switch_vector
     RootList: list of root buses (generators)
     BusList: list of buses
     LineList: list of lines
     max_iterations: maximum number of iterations"""
    def get_neighbors(x, mask):
        """ Generate neighbors of a bit vector by flipping the bits where mask[i] == 1. One bit flip per neighbor """
        neighbors = []
        for i in range(len(x)):
            if mask[i] == 1:
                neighbor = x[:]
                neighbor[i] = 1 - neighbor[i]  # Flip the bit
                neighbors.append(neighbor)
        return neighbors

    # Initialize the current solution and its objective function value
    current_solution = start_switch_vector[:]
    current_objective = objective_weighted_sum(RootList, BusList, LineList, current_solution)

    # Main loop of the local search algorithm
    for _ in range(max_iterations):
        neighbors = get_neighbors(current_solution, mask)
        next_solution = None
        next_objective = current_objective

        # Find the best neighbor and update the current solution if a neighbor is better
        for neighbor in neighbors:
            neighbor_objective = objective_weighted_sum(RootList, BusList, LineList, neighbor)
            if neighbor_objective > next_objective:
                next_solution = neighbor
                next_objective = neighbor_objective

        # Terminate if no better neighbor is found; The algorithm has converged to a local optimum
        if next_solution is None:
            break  # No better neighbor found, terminate

        current_solution = next_solution
        current_objective = next_objective

    return current_solution, current_objective