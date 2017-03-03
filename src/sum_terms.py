"""Generate a list of n items, sum it and round it to two decimal places."""

from __future__ import division


def series_sum(n):
    """Generate sum and round to two decimal places a list of n items."""
    return "{:.2f}".format(sum([1 / (1 + 3 * i) for i in range(n)]))
