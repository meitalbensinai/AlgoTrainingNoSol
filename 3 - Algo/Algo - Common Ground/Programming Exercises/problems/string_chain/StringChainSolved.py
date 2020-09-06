"""
problem formalization:

you are given a list of strings. we say that 2 strings can be chained if the last letter of one of them is the first
letter of the next one ('hola', 'angle' -> 'holangle'). Check if the list of strings (in any order) can be chained in
a circle (every string can be chained to the next one, and the last string can be chained to the first one).

Create an EFFICIENT algorithm to solve the task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: ['banana', 'apple', 'egb']
output: True

input: ['sharon', 'itay', 'ziv']
output: False

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 0.1 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 6 test:
- tests 1-3 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- test 4-6 is not visible to you, and need to pass it without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import networkx as nx


def string_chain_solution(lst: List[str]) -> bool:
    """ Checks if the list of string can be chained

    :param lst: list of lowercase no-spaces strings
    :return: True if chaining is possible else False
    """

    """
    idea:
    we create a graph with 26 nodes representing the alphabet. each string will be represented by an edge connecting
    the node of the first letter to the node of the last letter.
    then, we need to check if the graph contains an euler circuit (closed loop going exactly once through every
    edge). this is true if:
    1. the in-degree and out-degree of each node is the same
    2. the graph is strongly connected.
    
    notice that we need to use nx.MultiDiGraph in order to create a directed graph allowing parallel edges.
    """

    g = nx.MultiDiGraph()
    for string in lst:
        first = string[0]
        last = string[-1]
        g.add_edge(first, last)

    for node in g.nodes:
        if g.out_degree(node) != g.in_degree(node):
            return False

    return nx.is_strongly_connected(g)
