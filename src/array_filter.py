"""List class with custom filters."""


class list(object):
    """Suports multiple custom array filters."""

    def __init__(self, numbers):
        # if not isinstance(numbers, list):
        #     raise TypeError('list only accepts an array')
        self.numbers = numbers

    def even(self):
        """Find even numbered array elements."""
        return [item for item in self.numbers if isinstance(item, int) and item % 2 == 0]

    def odd(self):
        """Find odd numbered array elements."""
        return [item for item in self.numbers if isinstance(item, int) and item % 2 == 1]

    def under(self, val):
        """Find array elements under a value, exclusive."""
        return [item for item in self.numbers if isinstance(item, int) and item < val]

    def over(self, val):
        """Find array elements over a value, exclusive."""
        return [item for item in self.numbers if isinstance(item, int) and item > val]

    def in_range(self, start, stop):
        """Return array elements between start and stop, inclusive."""
        return [item for item in self.numbers if isinstance(item, int) and item >= start and item <= stop]
