#!/usr/bin/python3
"""method that checks if all boxes can be opened"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """
    opened_boxes = set([0])

    keys_to_check = [0]

    while keys_to_check:
        current_box = keys_to_check.pop()

        # Iterate over keys in the current box
        for key in boxes[current_box]:
            # Checks if the key opens a new box and that box is not opened yet
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                keys_to_check.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)