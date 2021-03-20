from typing import List, Tuple
import matplotlib.pyplot as plt
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
        self.route: List[int] = route       # todo deep copy ?
        self.generation_id = generation_id
        self.id = Individual.__nb_individuals
        self._fitness: float = 0
        Individual.__nb_individuals += 1

    # computes the fitness value for the given individual
    # note: the higher its fitness, the better the individual is
    # -> fitness and path length must have opposite variations
    def getFitness(self, dist_mat) -> float:

        if self._fitness > 0:   # fitness already computed
            return self._fitness
        else:                   # fitness not computed yet, do it here !
            # todo >>> leave this part blank ?
            length = 0
            for i in range(nb_cities - 1):
                city1_index = self.route[i]
                city2_index = self.route[i + 1]
                length += dist_mat[city1_index][city2_index]
            # don't forget to come back to the starting point! (I did)
            length += dist_mat[self.route[nb_cities - 1]][self.route[0]]
            self._fitness = 1000 / length
            # debug
            # print(f"length of {self.id}: {length}, fitness: {self._fitness}", file=stderr)       # debug
            return self._fitness  # arbitrary factor to keep fitness close to 1

    # plots an individual on a 2D plot
    def plot(self, cities, dist_mat) -> None:
        x_values = [cities[point][0] for point in self.route]
        y_values = [cities[point][1] for point in self.route]
        # don't forget to come back to the starting point! (I did)
        x_values.append(cities[self.route[0]][0])
        y_values.append(cities[self.route[0]][1])

        plt.title(f"Gen. {self.generation_id} no {self.id}, fitness: {self.getFitness(dist_mat)}")
        plt.plot(x_values, y_values)
        plt.show()

    # convenient for printing
    def __str__(self):
        return f"Individual no {self.id} (gen. {self.generation_id}), fitness: {self._fitness}"

    # printing stuff too
    def __repr__(self):
        return self.__str__()
