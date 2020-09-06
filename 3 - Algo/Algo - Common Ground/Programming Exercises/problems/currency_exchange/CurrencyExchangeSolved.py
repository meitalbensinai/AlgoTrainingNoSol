"""
problem formalization:

"In economics and finance, arbitrage is the practice of taking advantage of a price difference between two or more
markets" (Wikipedia).
In practice, we will be talking about arbitrage in currency exchange - where by only converting some currencies, we can
increase the value of the money we hold. For example, if 1 dollar can be converted to 3.54 NIS, and NIS can be converted
to 0.29 dollars, than by a chain of converts we can convert: 1 dollar -> 3.54 NIS -> 1.0266 dollars, and increase our
money worth.

given the convert table between N different currencies, determine whether an Arbitrage is possible.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: [[1, 3.54],
        [0.29, 1]]
output: True

-----------------------------------------------------------------------------------------------------------------------


Limitations:

time - 2 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 6 test:
- tests 1-4 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 5-6 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import numpy as np
import networkx as nx


def currency_exchange_solution(t: List[List[float]]) -> bool:
    """ Determine if an arbitrage is possible

    :param t: table for converting between currencies. if t[i][j] = x, it means that 1 of current i equals x of
    currency j.
    :return: True if an arbitrage is possible, else False
    """

    """
    idea:
    we can create a graph with n nodes and n^2 edges, such that the edge from node i to node j has weight t[i][j].
    we are looking for a cycle of currencies i1, i2, ..., i_k, i1 such that t[i1][i2]*...*t[i_k][i1] > 1 - so actually,
    we are looking for a cycle that the multiplication of it's weights is bigger than one.
    
    let's try to convert this condition into negative sum cycle, that we can easily detect (using bellman-ford).
    we know that log operation (on any base) converts multiplication operation into summing - log(a*b) = log(a) + log(b)
    and in addition log(1) = 0.
    so, if we use log(t[i][j]) as the weight of an edge, we are looking now for a positive cycle. by using -log(t[i][j])
    we convert the problem into looking for the existence of negative cycle.
    """

    n = len(t)
    g = nx.DiGraph()
    g.add_nodes_from(range(n))

    for i in range(n):
        for j in range(n):
            g.add_weighted_edges_from([(i, j, -np.log(t[i][j]))])

    return nx.negative_edge_cycle(g)  # since bellman ford requires a source, this method adds a new node that is
    # connected to all nodes, and runs bellman ford with it as the source
