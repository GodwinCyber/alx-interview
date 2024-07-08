#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
    non-attacking queens on an N×N chessboard. Write a program
    that solves the N queens problem.
Usage:
    nqueens N
    If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line, and exit with the status 1
Args:
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a
    new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a
    new line, and exit with the status 1
Return:
    The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """Use backtracking to find all solutions"""
    if col >= len(board):
        # A solution is found, add it to the solutions list
        solutions.append(board_to_coords(board))
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0  # Backtrack


def board_to_coords(board):
    """Convert the board to a list of coordinates for the solution"""
    coords = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                coords.append([i, j])
    return coords


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
