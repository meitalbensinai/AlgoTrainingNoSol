"""
problem formalization:

you are given a tree with N nodes and N-1 edges. Nodes are numbered from 0 (root) to N-1.
You are allowed to 'rotate' the tree by defining any of it's nodes as the root.
We define the depth of the tree to be the length of the path from the root to the farthest leaf in the tree.
for every node, we define the depth of the node to be the depth of the tree rotated around this node as a root.

Count how many nodes has the same depth as the root.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in tree.jpg
output: 2

* The nodes with the depth of 3 (the depth of the root) are root itself and node 3.
* The process of rotation/root changing is shown in rotated_tree.jpg

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 2 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 7 test:
- tests 1-4 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 5-7 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

import networkx as nx
import numpy as np
import os


def rotations_solution(path_to_tree: str) -> int:
    """ Count how many nodes in the tree has the same depth as the root

    :param path_to_tree: path to the pickle file with the tree input
    :return: amount of node with the same depth as the root
    """

    """
    idea:
    trivial solution can solve the problem by performing DFS for every node - takes O(n^2) time.
    
    we will solve the problem with dynamic programming in O(n) time.
    we will define two arrays, in_arr and out_arr:
    
    1. in_arr[i] will represent the the deepest branch we achieve when we travel from node i downwards in the original
    tree (into it's subtree).
    2. out_arr[i] will represent the deepest branch we can achieve when we travel from node i upward through its parent.
    
    then, the depth of tree with node i as it's root will be max(in[i], out[i]).
    
    every array will be computed over one search of the tree, and the dynamic building of the arrays is explained
    inside the solution.
    """
    t: nx.DiGraph = nx.read_gpickle(os.path.join(os.getcwd(), path_to_tree))

    n = len(t.nodes())
    source = 0
    in_arr = np.zeros(n)
    second_best_in_arr = np.zeros(n)  # storing the second best in value, motivation explained later
    out_arr = np.zeros(n)

    # Level 1 - compute in_arr
    # for node i, in_arr[i] will be 1 + the maximum of in_arr value of its children
    # leaves will be assigned with in_arr value of 0

    for node in nx.dfs_postorder_nodes(t):
        if node == source:
            continue
        parent = list(t.pred[node])[0]
        if 1 + in_arr[node] > in_arr[parent]:
            second_best_in_arr[parent] = in_arr[parent]
            in_arr[parent] = 1 + in_arr[node]
        else:
            second_best_in_arr[parent] = max(second_best_in_arr[parent], 1 + in_arr[node])

    # Level 2 - compute out_arr
    # for node i, out_arr[i] can be one of two options:
    # 1. we go to it's parent, and from it's parent continue out: 1 + out_arr[parent]
    # 2. we go to it's parent, and from it's parent going downwards: 1 + in_arr[parent]
    # problem! we cannot look at in_arr, because it may choose to go back to node...
    # so, we create a second_best_in_arr. if in_arr[parent] == 1 + in[node], we use second_best_in_arr[parent] instead.

    for node in nx.dfs_preorder_nodes(t):
        if node == source:
            continue
        parent = list(t.pred[node])[0]
        first_option = 1 + out_arr[parent]
        second_option = 1 + in_arr[parent] if in_arr[parent] != 1 + in_arr[node] else 1 + second_best_in_arr[parent]
        out_arr[node] = max(first_option, second_option)

    depths = np.array([max(in_arr[node], out_arr[node]) for node in t.nodes])
    return int(np.sum(depths == depths[0]))
