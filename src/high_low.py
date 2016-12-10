"""Return the highest and lowest numbers from a string of numbers."""


def high_and_low(numbers):
    """Return high and low int from a list as a string."""
    a = sorted([int(i) for i in numbers.split()])
    return " ".join([str(a[-1]), str(a[0])])
