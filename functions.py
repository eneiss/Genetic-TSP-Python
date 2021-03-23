from math import sqrt

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


# creates the Euclidean distance matrix for each possible couple of cities
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
def getRanking(population: List[Individual]) -> List[int]:
    return [sorted(population, key=lambda e: e.getFitness(), reverse=True).index(ind) for ind in population]


# returns a list of indexes of the individuals (in the population array)
# selected to be in the current generation's mating pool
# note: current selection method is to take only the best individuals
def selectMatingPool(ranking: List[int]) -> List[int]:
    pass  # todo delete this once you're done
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TODO complete the method body here !
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# generates a child from 2 parents by keeping characteristics of both
def crossover(parent1: Individual, parent2: Individual) -> Individual:
    pass  # todo delete this once you're done
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TODO complete the method body here !
    #   hint: the crossover doesn't need to be symmetrical
    #   (no need to keep an equal amount of "genes" from parent1 and parent2)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# returns the indexes of the best individuals that will be carried on to the
# next generation (elitism), according to the algorithm parameters
def elitistSelection(ranking: List[int]) -> List[int]:
    pass  # todo delete this once you're done
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # TODO complete the method body here !
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# plots the cities on a scatter plot
def plotCities(cities) -> None:
    x_values = [cities[i][0] for i in range(len(cities))]
    y_values = [cities[i][1] for i in range(len(cities))]

    plt.title("Cities")
    plt.scatter(x_values, y_values)
    plt.show()


def plotFitnessEvolution(fitness: List[float]) -> None:
    plt.plot(fitness)
    plt.title("Fitness evolution across generations")
    plt.ylabel("Fitness")
    plt.xlabel("Generation number")
    plt.show()
    pass
