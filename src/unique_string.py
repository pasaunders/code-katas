"""Find one string in a list with unique characters."""

from itertools import combinations


def find_uniq(arr):
    """Sort through each combination of three strings.

    If a set of one doesn't match the other two sets, return it.
    """
    for first, second, third in combinations(arr, 3):
        if set(first.lower()) != set(second.lower()):
            if set(first.lower()) != set(third.lower()):
                return first
            return second
        if set(first.lower()) != set(third.lower()):
            return third
    return None


def find_uniq2(arr):
    """Claire's improved version."""
    from collections import Counter
    count = Counter(''.join(arr).lower())
    matching = [s for s in arr if min(count, key=count.get) in s.lower()]
    return matching[0]
