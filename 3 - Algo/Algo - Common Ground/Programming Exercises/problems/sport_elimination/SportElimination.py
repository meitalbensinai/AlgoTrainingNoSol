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


def sport_elimination_solution(wins: List[int], losses: List[int], games_left: List[List[int]]) -> List[int]:
    """ find the teams that can advance to the playoffs

    :param wins: amount of current wins for each team
    :param losses: amount of current losses for each team
    :param games_left: amount of games left between every pair of teams. this matrix is symmetric and on the diagonal
    all values are 0.
    :return: list of the relevant teams
    """
    pass
