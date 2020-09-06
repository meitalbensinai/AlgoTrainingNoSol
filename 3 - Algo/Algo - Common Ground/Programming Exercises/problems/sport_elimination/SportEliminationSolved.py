"""
problem formalization:

In some sports league, teams are divided into divisions. Within each division, each team faces each rival several times.
At the end on the season, the top team in each division (the team with the highest amount of wins) proceeds to the
playoffs.
We are now sometime into the season, and you are given the current table in some division.
Fans of one of the teams want you to help them understand if their team can still make it to the playoffs.
Find out the teams that can still make it to the playoffs.

* For the exercise purpose, there is no tie-breaking rule. Every team that has the highest amount of wins makes it to
the playoffs.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

Scenario:
3 teams: 0, 1, 2. state of wins is [3, 3, 0], state of loses is [1, 1, 4] (listed according to index).
We still have 2 games between every pair of teams. Can team 2 still make it?
Result:
Yes! If team 2 wins all of its games, and teams 0-1 beat each other exactly once each, team 2 will have the
highest amount of 4 wins.

Scenario:
6 teams: state of wins is [14, 14, 9, 5, 2, 1], state of loses is [1, 1, 6, 10, 13, 14].
We still have 1 game between every pair of teams. Can team 2 still make it?
Result:
No! even if team 2 we win all 5 of its games and reach 14 wins, in the 0-1 match one of the teams will proceed to 15
wins and team 2 cannot be the winner.

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 3.5 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 6 test:
- tests 1-2 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 3-6 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import networkx as nx
import numpy as np


def sport_elimination_solution(wins: List[int], losses: List[int], games_left: List[List[int]]) -> List[int]:
    """ find the teams that can advance to the playoffs

    :param wins: amount of current wins for each team
    :param losses: amount of current losses for each team
    :param games_left: amount of games left between every pair of teams. this matrix is symmetric and on the diagonal
    all values are 0.
    :return: list of the relevant teams
    """

    """
    idea:
    we only check for possibility, so we can assume that given team will win all the rest of it's games.
    the remaining questions is if any of the other teams can beat this amount of wins through the rest of the remaining
    games that not include the given team.
    we check this criteria using nax-flow network with 4 layers (see solution.jpg)
    the first layers is just a source.
    the second layer have a node for every team pair that does not contain the given team. it's connected to the source
    such that the capacity of every edge is the amount of games left between the 2 teams.
    the third layer have a node for every team (except the given team), and every node in it is connected to the nodes
    in the second layer where this team is part of the pair. there are no capacity limits over the connections between
    the second and the third layer (capacity inf), so that the amount of of games between the two can be split any way
    between the 2 teams ('wins' are flowing in the network).
    the last layer is just a target. every node from the third layer is connected to the target with the following
    capacity:
    since the node in the third layer represents a team, the capacity will be the amount of wins we allow that team to
    achieve without passing the win-amount of the given team. it's all of given team wins (current and from the
    remaining games) minus the current amount of wins for that team. the flow network can be shown in solution.jpg.
    
    now we search for the max-flow of the network. we know that the maximum flow is bounded by the amount of all
    remaining games (that the given team is not involved in them). if the max-flow is exactly this value, and by using
    of the integrality theorem, it means that all games can take place and still the capacity limits between the 3 layer
    to target assures us that no team is going to pass ouר team's win amount.
    """

    n = len(wins)
    wins = np.array(wins)
    games_left = np.array(games_left)
    teams_that_can_advance = []
    for team in range(n):
        remained_wins = np.sum(games_left[:, team])

        network = nx.DiGraph()

        pairs = [(a, b) for a in range(n) if a != team for b in range(a, n) if b != team and b != a]  # second layer
        teams = [a for a in range(n) if a != team]  # third layer

        for a, b in pairs:
            network.add_weighted_edges_from([('s', (a, b), games_left[a, b]),
                                             ((a, b), a, np.inf),
                                             ((a, b), b, np.inf)], weight='capacity')
        for t in teams:
            network.add_weighted_edges_from([(t, 't', wins[team] + remained_wins - wins[t])], weight='capacity')

        max_flow = nx.maximum_flow_value(network, 's', 't')
        all_remaining_games = np.sum(games_left) / 2 - remained_wins  # divide by 2 because matrix is symmetric
        if max_flow == all_remaining_games:
            teams_that_can_advance.append(team)

    return teams_that_can_advance
