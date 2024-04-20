import numpy as np
from numpy import asarray
from numpy import exp
from numpy import fabs
from numpy.random import randn
from numpy.random import rand
import random

# Objective function
def objective(x):
    return sum(x)

# Simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size ,temp, init):
    # Generate an initial point
    best = [1,1,1,1,1,1]
    # Evaluate the initial point
    best_eval = objective(best)
    # Current working solution
    curr, curr_eval = best, best_eval
    # Run the algorithm
    for i in range(n_iterations):
        # Take a step (mutation); flip vector from 0 to 1 or 1 to 0 with probability 1/len(curr)
        candidate = curr.copy()
        for j in range(len(candidate)):
            # Generate a new candidate point
            if rand() < 1.0/len(curr):
                candidate[j] = 1 - candidate[j]
        #candidate = curr + randn(len(bounds)) * step_size
        # Evaluate candidate point
        candidate_eval = objective(candidate)
        # Print the candidate point and its evaluation in a single line
        print('>%d f(%s) = %.5f' % (i, candidate, candidate_eval))
        # Check for new best solution
        if candidate_eval < best_eval:
            # Store new best point
            best, best_eval = candidate, candidate_eval
            print('New best f(%s) = %.5f' % (best, best_eval))
        # Difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        # Calculate temperature for current epoch
        t = temp / float(i + 1)
        # Calculate Metropolis acceptance criterion
        metropolis = exp(-diff / t)
        # Check if we should keep the new point
        if diff < 0 or rand() < metropolis:
            # Store the new current point
            curr, curr_eval = candidate, candidate_eval
    return (best, best_eval)

# Set random seed
random.seed(1)

# Define the search space
lb = -1.0
ub = 1.0
bounds = asarray([[lb, ub]])

# Define parameters
n_iterations = 100
step_size = 0.15
temp = 1.5
init = 0.65

# Perform the simulated annealing search
best_solution, best_score = simulated_annealing(objective, bounds, n_iterations, step_size, temp, init)
print("Best Solution:", best_solution)
print("Objective Function Value:", best_score)