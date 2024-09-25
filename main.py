import numpy as np
from random import random
import matplotlib.pyplot as plt
from Operations import *
from IEEE69BusDist import BusList, LineList, RootList
from DistribObjects import *
from DistribObjects import Bus, Line


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


# Create an example of a bit vector with length 69 and mostly ones

set_priorities(BusList)
graph69 = build_graph(RootList, BusList, LineList)

n = count_connected(graph69)
#print("connected nodes",n)
#i = local_search_with_connected_nodes(69, graph69)

p = count_priorities(graph69)
print("priorities",p)

# Create a bit vector with length 69, mostly ones
# The bits denote whether or not the lines are on or off
bit_vector_69 = [1] * 64 + [0, 0, 1, 0, 1,0,0,0,1]  # 65 ones and 4 zeros

# Ensure the bit vector has the correct length
assert len(bit_vector_69) == len(LineList)

# Build the graph with the line bitmask
graph69 = build_graph(RootList, BusList, LineList, bit_vector_69)

# Count the connected buses
connected_count = count_connected(graph69)
print(f"Total connected buses: {connected_count}")

# Set priorities for the buses in the first subgraph
set_priorities(graph69['buses'][0])

# Count priority 1 and priority 2 nodes
priority_count = count_priorities(graph69)
print(f"Priority 1 nodes: {priority_count[1]}")
print(f"Priority 2 nodes: {priority_count[2]}")

# create a weighted objective function from the two priority counts
def objective_weighted_sum(RootList, BusList, LineList, x):
    graph69 = build_graph(RootList, BusList, LineList, x)
    priority_count = count_priorities(graph69)
    return priority_count[1] * 100 + priority_count[2]

# Test the objective function and output the result with some description
print("Objective function value:")
print(objective_weighted_sum(RootList, BusList, LineList, bit_vector_69))





# ---------------------- Run the local search algorithm ----------------------

# Example mask with length 69 (allow changes only where mask[i] == 1)
# In this example, allow changes everywhere
# mask = [1] * (len(LineList))
# In this example, allow changes everywhere, except in the last 4 bits
mask = [1] * (len(LineList)-4) + [0,0,0,0]
start_switch_vector = bit_vector_69  # 65 ones and 4 zeros (length 73)
optimized_vector, optimized_objective = local_search_with_mask(start_switch_vector, mask, RootList, BusList, LineList)

# ---------------------- Output the results ----------------------



# Output the optimized bit vector and its objective function value
print("Optimized bit vector:", optimized_vector)
print("Length of optimized bit vector:", len(optimized_vector))
print("Sum of optimized bit vector (Number of closed switches):", sum(optimized_vector))
print("Optimized objective function value:", optimized_objective)


# Build the graph with the optimized bit vector
graph69 = build_graph(RootList, BusList, LineList, optimized_vector)



# Count the connected buses
connected_count = count_connected(graph69)
print(f"Total connected buses: {connected_count}")

# Count priority 1 and priority 2 nodes
priority_count = count_priorities(graph69)
print(f"Priority 1 nodes: {priority_count[1]}")
print(f"Priority 2 nodes: {priority_count[2]}")



