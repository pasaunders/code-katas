"""Recursive solution to finding the remainder of a number divided by 13."""
from itertools import cycle


def thirt(n):
    evaluated = sum([a * b for a, b in zip(reversed([int(digit) for digit in str(n)]), cycle([1, 10, 9, 12, 3, 4]))])
    return evaluated if evaluated == n else thirt(evaluated)
