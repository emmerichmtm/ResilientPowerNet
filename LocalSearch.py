import numpy as np
from numpy.random import rand
import random


# Objective function (Binary Vector)
def objective(solution):
    # For simplicity, the objective function is a bit vector
    return np.sum(solution)


# Simulated annealing algorithm
def simulated_annealing(objective, solution_length, n_iterations, temp):
    # Generate an initial solution
    curr_solution = [random.choice([0, 1]) for _ in range(solution_length)]
    curr_eval = objective(curr_solution)
    best_solution = curr_solution

    best_eval = curr_eval

    for i in range(n_iterations):
        # Generate a candidate solution by flipping a random bit
        candidate_solution = curr_solution.copy()
        index_to_flip = random.randint(0, solution_length - 1)
        candidate_solution[index_to_flip] = 1 - candidate_solution[index_to_flip]

        # Evaluate candidate solution
        candidate_eval = objective(candidate_solution)

        # Calculate temperature for current iteration
        t = temp / float(i + 1)

        # Calculate Metropolis acceptance criterion
        metropolis = np.exp((curr_eval - candidate_eval) / t)

        # Check if we should accept the candidate solution
        if candidate_eval < curr_eval or rand() < metropolis:
            curr_solution = candidate_solution
            curr_eval = candidate_eval

        # Update the best solution found so far
        if candidate_eval < best_eval:
            best_solution = candidate_solution
            best_eval = candidate_eval

    return best_solution, best_eval


# Set random seed for reproducibility
random.seed(42)

# Define problem parameters
solution_length = 10  # Length of the binary vector
n_iterations = 1000  # Number of iterations
temp = 1.0  # Initial temperature

# Perform simulated annealing optimization
best_solution, best_score = simulated_annealing(objective, solution_length, n_iterations, temp)

print("Best Solution:", best_solution)
print("Objective Function Value:", best_score)