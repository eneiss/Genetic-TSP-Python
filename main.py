from functions import *

"""
Genetic algorithm implementation for solving the TSP problem

See parameters.py for problem & algorithm parameters
"""

# cities are randomly generated on a square grid (discrete space)
# note: upper bound of randrange is exclusive, while randint is inclusive
cities: List[Tuple[int, int]] = [(random.randrange(0, grid_size), random.randrange(0, grid_size))
                                 for _ in range(nb_cities)]

# matrix of distances between cities for each possible couple of cities
distance_matrix = getDistanceMatrix(cities)
# print(*distance_matrix, sep="\n")       # debug

# --- plot the generated cities on a scatter plot
plotCities(cities)

# initialize population randomly
population: List[Individual] = []
for _ in range(population_size):
    population.append(randomIndividual(gen_id=0))

# --- main loop, where the selection/breeding process occurs
# todo maybe change for a minimum fitness or population convergence
for it in range(nb_iter):

    # for ind in population:
    #     ind.plot(cities)

    # --- ranking of the individuals in the current population
    ranking = getRanking(population, cities, distance_matrix)
    print(f"Ranking for generation {it}: {ranking}")

    # --- mating pool selection
    # mating_pool = []  # todo
    # print(f"mating_pool : {mating_pool}")

    # todo : select mating pool, apply elitism, crossover & mutate, update gen nb

    # end of this iteration: update current generation number
    for ind in population:
        ind.generation_id += 1
