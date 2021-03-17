import random

from individual import *

"""
Functions used by main.py in the different steps of the genetic algorithm
"""

# set RNG seed for a repeatable execution
random.seed(42)


# generates a random individual (route)
def randomIndividual(gen_id) -> Individual:
    # generate a random route that passes through each city exactly once
    route = list(range(nb_cities))
    random.shuffle(route)
    return Individual(route, gen_id)


# creates the distance matrix for each possible couple of cities
# (used to optimize fitness computation)
def getDistanceMatrix(cities: List[Tuple[int, int]]) -> List[List[float]]:
    res = [[None for __ in range(len(cities))] for _ in range(len(cities))]

    for i1, c1 in enumerate(cities):
        for i2, c2 in enumerate(cities[i1+1:]):
            res[i1][i2+i1+1] = sqrt(pow(c2[0] - c1[0], 2) + pow(c2[1] - c1[1], 2))
            res[i2+i1+1][i1] = res[i1][i2+i1+1]

    return res


# ugly one-liner that returns the rank of each individual of the population,
# from 0 to len(population) - 1
# e.g. result[i] = 3 means that the individual at population[i] is the 4th
# fittest individual in the current population (not 3rd because the fittest
# is ranked 0)
def getRanking(population: List[Individual], cities, dist_mat) -> List[int]:
    return [sorted(population, key=lambda e: e.getFitness(cities, dist_mat), reverse=True).index(indiv) for indiv in population]


# returns a list of indexes of the individuals (in the population array)
# selected to be in the current generation's mating pool
# note: current selection method is todo  fitness proportionate selection?
def selectMatingPool(ranking: List[int]) -> List[int]:
    pass
    # todo
    # return ranking[:int(population_size*mating_pool_proportion)]  # absolutely not

# generates a child from 2 parents by keeping characteristics of both
def crossover(parent1: Individual, parent2: Individual) -> Individual:
    # todo trou ici

    child_route = []
    child_genes = set()  # optimization for O(1) 'in'

    # note: the first/last city in the tour do not matter as long as the
    # resulting path is the same, thus we can chose any city in a tour and
    # reorder the path starting from it

    # algorithm chosen for crossover here: choose a subarray of the first
    #  parent's genes and transfer them to its child, then take the rest of
    #  the other parent's genes to fill in the missing genes
    start_gene = random.randrange(0, len(parent1.route))  # exclusive upper bound
    stop_gene = random.randint(start_gene + 1, len(parent1.route))  # inclusive upper bound

    # take genes from the first parent
    for gene in parent1.route[start_gene:stop_gene]:
        child_route.append(gene)
        child_genes.add(gene)

    # and fill in the rest with genes of the other parent
    for gene in parent2.route:
        if gene not in child_genes:
            child_route.append(gene)

    return Individual(child_route, parent1.generation_id + 1)


# applies random mutations to an individual (in-place)
def mutate(individual: Individual) -> None:
    # todo trou ici
    pass


# another one-liner that returns the indexes of the best individuals that will
# be carried on to the next generation (elitism), according to the algorithm
# parameters
def elitistSelection(ranking: List[int]):
    # todo trou ici ?
    return (i for i in range(nb_cities) if ranking[i] <= elite_proportion*population_size)


# plots the cities on a scatter plot
def plotCities(cities) -> None:
    x_values = [cities[i][0] for i in range(len(cities))]
    y_values = [cities[i][1] for i in range(len(cities))]

    plt.title("Cities")
    plt.scatter(x_values, y_values)
    plt.show()
