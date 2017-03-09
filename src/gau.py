"""Add all integers from 1 to n."""


def f(n):
    if type(n) is not int or n < 1:
        return None
    result = 0
    for i in range(n):
        result += (i + 1)
    return result


def one_line(n):
    """Single line solution from codewars results."""
    return n * (n + 1) // 2 if (isinstance(n, int) and n > 0) else None
