from typing import List, Tuple
import matplotlib.pyplot as plt
import random
from sys import stderr

from parameters import *

"""
Represents an individual in our population (in our case, a path going through
each city exactly once)
"""


class Individual:

    # used to assign an individual id for each individual
    __nb_individuals = 0

    def __init__(self, route, generation_id):
        # list of city indexes, sorted by visit order
        self.route: List[int] = route
        self.generation_id = generation_id
        self.id = Individual.__nb_individuals
        self._fitness: float = 0
        Individual.__nb_individuals += 1

    # get or compute the individual's fitness
    def getFitness(self) -> float:

        if self._fitness > 0:   # fitness already computed
            return self._fitness
        else:                   # fitness not computed yet
            raise Exception("Tried to get the fitness of an individual whose fitness has not been computed yet.")

    # computes the fitness value for the given individual
    # note: the higher its fitness, the better the individual is
    # -> fitness and path length must have opposite variations
    def computeFitness(self, dist_mat):
        length = 0
        for i in range(nb_cities - 1):
            city1_index = self.route[i]
            city2_index = self.route[i + 1]
            length += dist_mat[city1_index][city2_index]

        # don't forget to come back to the starting point! (I did)
        length += dist_mat[self.route[nb_cities - 1]][self.route[0]]

        self._fitness = 1000000 / length  # arbitrary factor to keep fitness readable
        return self._fitness

    # plots an individual on a 2D plot
    def plot(self, cities) -> None:
        x_values = [cities[point][0] for point in self.route]
        y_values = [cities[point][1] for point in self.route]
        # don't forget to come back to the starting point! (I did)
        x_values.append(cities[self.route[0]][0])
        y_values.append(cities[self.route[0]][1])

        plt.title(f"Gen. {self.generation_id} no {self.id}, fitness: {self.getFitness()}")
        plt.plot(x_values, y_values)
        plt.show()

    # applies the individual a random mutation according to the mutation rate
    def mutate(self) -> None:
        pass        # todo delete this once you're done
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # TODO complete the method body here !
        #   hint: a possibility would be to swap two cities with a chance of mutation_rate
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # convenient for printing
    def __str__(self):
        return f"Individual no {self.id} (gen. {self.generation_id}), fitness: {self._fitness}"

    # printing stuff too
    def __repr__(self):
        return self.__str__()
