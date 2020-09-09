from typing import List
from city import City
from pool import Pool
from matplotlib import pyplot as plt
import pandas as pd


def load(data_path: str) -> List[City]:
    data = pd.read_csv(data_path, sep=' ')
    cities = []
    for x, y in data[['x', 'y']].values:
        cities.append(City(x, y))
    return cities


def draw_results(pool: Pool):
    plt.plot(range(len(pool.best_route_by_generation)), pool.best_route_by_generation)
    plt.plot(range(len(pool.best_route_by_generation)), [33523] * len(pool.best_route_by_generation), color='r')
    plt.xlabel('generation')
    plt.ylabel('shortest path so far')
    plt.title('solve TSP with genetic algorithm')
    plt.show()


if __name__ == '__main__':
    cities = load('data.csv')
    pool = Pool(cities, 100)
    pool.run(1500)
    draw_results(pool)
