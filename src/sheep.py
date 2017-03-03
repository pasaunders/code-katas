"""Count entries of True are there in the list."""


def count_sheeps(array_of_sheeps):
    """Count entries of True are there in the list."""
    count = 0
    for i in array_of_sheeps:
        if i is True:
            count += 1
    return count
