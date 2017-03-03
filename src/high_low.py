"""Return the highest and lowest numbers from a string of numbers."""


def high_and_low(numbers):
    """Return high and low int from a list as a string."""
    high = max(numbers)
    low = min(numbers)
    return "{} {}".format(high, low)
