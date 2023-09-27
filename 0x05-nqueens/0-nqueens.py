#!/usr/bin/python3
"""This attempts to solve the n-queens problem"""
import sys


def calc_pos(queen, lenght):
    """Calculates all attack moves of a queen
    Args:
        queen (list): the queen in question
        lenght (int): the board dimensions
    Returns:
        list: All possible moves
    """
    vert = []
    res = []
    hor = []
    diag = []
    diag2 = []
    for i in range(queen[0] + 1, lenght):
        vert.append([i, queen[1]])
    for i in range(queen[0] - 1, -1, -1):
        vert.append([i, queen[1]])
    res.extend(vert)
    for i in range(queen[1] + 1, lenght):
        hor.append([queen[0], i])
    for i in range(queen[1] - 1, -1, -1):
        hor.append([queen[0], i])
    res.extend(hor)
    j = queen[1] + 1
    for i in range(queen[0] + 1, lenght):
        if j < lenght and i < lenght:
            diag.append([i, j])
        else:
            break
        j += 1
    j = queen[1] + 1
    for i in range(queen[0] - 1, -1, -1):
        if j < lenght and i > -1:
            diag.append([i, j])
        else:
            break
        j += 1
    res.extend(diag)
    j = queen[1] - 1
    for i in range(queen[0] - 1, -1, -1):
        if j > -1 and i > -1:
            diag2.append([i, j])
        else:
            break
        j -= 1
    j = queen[1] - 1
    for i in range(queen[0] + 1, lenght):
        if j > -1 and i < lenght:
            diag2.append([i, j])
        else:
            break
        j -= 1
    res.extend(diag2)
    return res


def generate(length):
    """Generates an empty board for visualization
    Args:
        l (int): the board dimensions
    Returns:
        list: a matrix of empty spaces
    """
    return [[" " * 9 for _ in range(length)] for _ in range(length)]


def priB(b):
    """A print function to visualize the placements
    of the queens
    Args:
        b (list): the board dimensions
    """
    vas = " " * 9
    marker = ("+---------" * len(b)) + "+"
    for line in b:
        print(marker)
        for i in range(3):
            print('|', end="")
            for xa in line:
                y = " " * 9 if i != 1 else xa if xa != 0 else " " * 9
                print(y, end="|")
            print()
    print(marker)


def check(queens, N, curr):
    """Checks if a queen is in a valid position
    Args:
        queens (list): current queen
        N (int): the board dimensions
        curr (list): the positions
    Returns:
        bool: True or false depending on outcome
    """
    for x in queens:
        if curr in (calc_pos(x, N)):
            return False
    return True


def nqueens(board, N, col, queens, res):
    """Finds the number of possible permutations to
    solve the problem
    Args:
        board (list): a matrix representing the board
        N (int): the board's dimensions
        col (int): current column
        queens (list): a list of all queens
        res (list): the result
    Returns:
        bool: false to control the recursion
    """
    if col >= N:
        # priB(board) # Uncomment this to see a visualization of the process
        res.append(queens.copy())
        return False
    for i in range(N):
        if check(queens, N, [i, col]):
            # board[i] [col] = "    Q    " #Uncomment this too
            queens.append([i, col])
            if nqueens(board, N, col + 1, queens, res):
                return True
            board[i][col] = 0
            queens.remove([i, col])
    return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        var = int(sys.argv[1])
        if var < 4:
            print("N must be at least 4")
            sys.exit(1)
        res = []
        b = generate(var)
        nqueens(b, var, 0, [], res)
        for item in res:
            print(item)
    except ValueError:
        print("N must be a number")
        sys.exit(1)