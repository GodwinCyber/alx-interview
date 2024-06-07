#!/usr/bin/python3
"""Resolve the lockbox"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened.
    Args:
        boxes (list): List of lists, where each sublist contains keys.
    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    opened = [False] * len(boxes)
    opened[0] = True
    keys = set(boxes[0])

    while keys:
        new_keys = keys.pop()
        if new_keys < len(boxes) and not opened[new_keys]:
            opened[new_keys] = True
            keys.update(boxes[new_keys])

    return (all(opened))
