#!/usr/bin/python3
"""The prime game"""


def play_turn(x):
    """Plays a certain number of turns"""
    games = [_ for _ in range(1, x + 1)]
    turn = 'm'
    ben = 0
    maria = 0
    winner = None
    if games == [1]:
        return 'ben'
    while games != []:
        lowest = games[1]
        games = [_ for _ in games if _ % lowest != 0]
        if turn == 'm':
            maria += 1
            winner = 'maria'
            turn = 'b'
        else:
            winner = 'ben'
            turn = 'm'
            ben += 1
        if games == [1]:
            return winner
            if ben > maria:
                return 'ben'
            elif maria > ben:
                return 'maria'
            else:
                return None


def isWinner(x, nums):
    """Finds the winner in a number of turns"""
    ben = 0
    maria = 0
    if x != len(nums):
        return None
    if not nums or nums == [] or x <= 0:
        return None
    for i in range(x):
        winner = play_turn(nums[i])
        if winner == 'maria':
            maria += 1
        elif winner == 'ben':
            ben += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None