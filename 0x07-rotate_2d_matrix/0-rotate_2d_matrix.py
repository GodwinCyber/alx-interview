#!/usr/bin/python3
"""Rotate 2D Matrix Module"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix: Given an n X n 2D matrix,
        rotate it 90 degrees clockwise
    Cases:
        Prototype: def rotate_2d_matrix(matrix):
        Do not return anything. The matrix must be edited in place
        You can assume the matrix will have 2 dimensions
        and will not be empty
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # move bottom element to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # move right element to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # move/assign top element to right
            matrix[i][-layer - 1] = top
