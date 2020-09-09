from typing import List
from city import City
import numpy as np


class Route:

    def __init__(self, cities: List[City], order=None):
        self.order = order if order else list(np.random.permutation(len(cities)))
        self.cities = [cities[i] for i in self.order]
        self.length = self.get_length()

    def get_length(self):
        return np.sum([b.dist(a) for a, b in zip(self.cities, self.cities[1:])]) + self.cities[-1].dist(self.cities[0])

    def fitness(self):
        return 1/self.length