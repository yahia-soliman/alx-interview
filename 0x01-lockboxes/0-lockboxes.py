#!/usr/bin/python3
"""
Having a list of `n` boxes numbered from `0` to `n - 1`
Each box may contain keys to other boxes

How can you know if it is possible to open all the boxes
knowing that:
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
"""


def canUnlockAll(boxes):
    """Check if all lockboxes can be opened
    - Return True if all boxes can be opened, else return False
    """
    opened = [0]
    n_of_boxes = len(boxes)

    for box_idx in opened:
        for key in boxes[box_idx]:
            if key not in opened or key >= n_of_boxes:
                opened.append(key)

    return len(opened) == n_of_boxes
