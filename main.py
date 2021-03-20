from functions import *

"""
Genetic algorithm implementation for solving the TSP problem

See parameters.py for problem & algorithm parameters
"""

# todo:
#  - keep track of the evolution of fitness across generations and plot it in the end

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
    #     ind.plot(cities, distance_matrix)

    # todo : select mating pool, apply elitism, crossover & mutate, update gen nb

    # --- ranking of the individuals in the current population
    ranking = getRanking(population, cities, distance_matrix)
    # print(f"Ranking for generation {it}: {ranking}")    # debug

    # debug & visuals : plot the best individual of each generation every now and then
    if it % 50 == 0:
        best_individual = population[ranking.index(0)]
        print(best_individual)
        best_individual.plot(cities, distance_matrix)

    # --- mating pool selection
    mating_pool = selectMatingPool(ranking)
    # print(f"mating_pool : {mating_pool}")   # debug

    new_generation = []

    # --- elitism
    elite = elitistSelection(ranking)
    for ielite in elite:
        new_generation.append(population[ielite])

    # --- breeding & mutation : 'fill in' the rest of the population with new individuals
    for ichild in range(population_size - elite_size):

        # --- crossover (= breeding)
        iparent1, iparent2 = random.randrange(mating_pool_size), random.randrange(mating_pool_size)
        child = crossover(population[mating_pool[iparent1]], population[mating_pool[iparent2]])

        # --- mutation
        child.mutate()      # comment this to disable mutation

        new_generation.append(child)

    # end of this iteration: update population and current generation number
    population = new_generation
    for ind in population:
        ind.generation_id = it
