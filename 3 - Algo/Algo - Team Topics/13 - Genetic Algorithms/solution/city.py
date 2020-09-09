import numpy as np


class City:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist(self, city) -> float:
        return np.linalg.norm(np.array([self.x, self.y]) - np.array([city.x, city.y]))
