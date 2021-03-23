"""
Constant parameters used in the genetic algorithm and problem constraints
"""

# --- problem parameters
grid_size = 200
nb_cities = 100

# --- genetic algorithm parameters
# -> can be tweaked (almost) freely to study convergence speed and algorithm efficiency
rng_seed = 42
population_size = 10
nb_iter = 50000
mating_pool_proportion: float = 0.4
elite_proportion: float = 0.2
mutation_rate = 0.6

# derived parameters (used to simplify expressions for a better understanding)
mating_pool_size = int(mating_pool_proportion * population_size)
elite_size = int(elite_proportion * population_size)
