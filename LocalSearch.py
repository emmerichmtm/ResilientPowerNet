import numpy as np
from random import random
import matplotlib.pyplot as plt
from Operations import *
from IEEE69BusDist import *
from DistribObjects import *
from DistribObjects import Bus, Line

def objective(x):
    mid_point = len(x) // 2
    sum_first_half = np.sum(x[:mid_point])
    sum_second_half = np.sum(x)
    return (-sum_first_half, sum_second_half)


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


def simulate_annealing(length_of_vector, max_iterations=1000, temp=1.0):
    curr_solution = np.random.randint(0, 2, size=length_of_vector)
    curr_eval = objective(curr_solution)

    for i in range(1, max_iterations + 1):
        t = temp / float(i + 1)
        candidate_solution = generate_candidate(curr_solution)
        candidate_eval = objective(candidate_solution)

        if lexico_metropolis(curr_eval, candidate_eval, t):
            curr_solution = candidate_solution
            curr_eval = candidate_eval

    return curr_eval


# Simulation parameters
vector_lengths = [10, 20, 30,50,75,100]
num_trials = 50  # Number of trials per vector length
results = {length: [] for length in vector_lengths}

# Running the benchmark
for length in vector_lengths:
    for _ in range(num_trials):
        results[length].append(simulate_annealing(length))

# Preparing data for boxplots
objective_1 = {length: [-result[0] for result in results[length]] for length in vector_lengths}
objective_2 = {length: [result[1] for result in results[length]] for length in vector_lengths}

# Plotting
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 15))
for idx, obj in enumerate([objective_1, objective_2]):
    axes[idx].boxplot([obj[length] for length in vector_lengths],
                      labels=[f'{length} bits' for length in vector_lengths])
    axes[idx].set_xlabel('Vector Length')
    axes[idx].set_ylabel(f'Objective {idx + 1} Values')
#plt.tight_layout()

plt.show()
