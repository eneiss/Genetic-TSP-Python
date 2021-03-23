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
distance_matrix: List[List[float]] = getDistanceMatrix(cities)

# --- plot the generated cities on a scatter plot
plotCities(cities)

# --- initialize population randomly
population: List[Individual] = []
for _ in range(population_size):
    population.append(randomIndividual(gen_id=0))

# initial fitness computing
for ind in population:
    ind.computeFitness(distance_matrix)

best_fitness = []       # track the population's evolution

# main loop, where the evolutionary process occurs
for it in range(nb_iter):

    """
    Evolutionary process implemented here:
        - rank the current population members according to their fitness
        - select the mating pool and elite according to the ranking
        - make the individuals in the mating pool breed to create new individuals
        - apply random mutations to these newborn individuals
        - update the population with newborn individuals + elite of the previous generation
    """

    # --- ranking of the individuals in the current population
    ranking = getRanking(population)

    # evolution tracking
    best_individual = population[ranking.index(0)]
    best_fitness.append(best_individual.getFitness())

    # plot the best individual of each generation every now and then
    if it % (nb_iter//10) == 0:
        print(best_individual)
        best_individual.plot(cities)

    # --- mating pool selection
    mating_pool = selectMatingPool(ranking)

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

        # --- compute the fitness of new individuals only
        child.computeFitness(distance_matrix)

        new_generation.append(child)

    # end of this iteration: update population and current generation number
    population = new_generation
    for ind in population:
        ind.generation_id = it

    assert(population_size == len(population))


plotFitnessEvolution(best_fitness)
