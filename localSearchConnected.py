
import numpy as np
from random import random
import matplotlib.pyplot as plt
from Operations import *
from IEEE69BusDist import *
from DistribObjects import *
from DistribObjects import Bus, Line

def objective(x, graph):
    num_connected_nodes = count_connected(graph)
    power_loss = np.sum(x)
    return (-num_connected_nodes, power_loss)


def generate_candidate(x):
    new_x = np.copy(x)
    for i in range(len(x)):
        if random() < 1 / len(x):
            new_x[i] = 1 - new_x[i]
    return new_x


def lexico_metropolis(curr_eval, candidate_eval, t):
    for curr, cand in zip(curr_eval, candidate_eval):
        if cand < curr:
            return True
        elif cand > curr:
            return False
    return np.exp((sum(curr_eval) - sum(candidate_eval)) / t) > random()


def local_search_with_connected_nodes(length_of_vector, graph, max_iterations=1000, temp=1.0):
    curr_solution = np.random.randint(0, 2, size=length_of_vector)
    curr_eval = objective(curr_solution, graph)

    for i in range(1, max_iterations + 1):
        t = temp / float(i + 1)
        candidate_solution = generate_candidate(curr_solution)
        candidate_eval = objective(candidate_solution, graph)

        if lexico_metropolis(curr_eval, candidate_eval, t):
            curr_solution = candidate_solution
            curr_eval = candidate_eval

    return curr_eval
