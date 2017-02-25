"""Build a pyramid out of characters in an input string."""


class pyramid(object):
    """Takes a string. Outputs based on a pyramid built out of the string's characters."""

    def __init__(self, string):
        """Initialize the pyramid."""
        self.build_string = string

    def from_the_side(self):
        """Build a pyramid of letters viewed from the side, first letter lowest."""
        printout = [[] for i in range(len(self.build_string))]
        for idx, row in enumerate(printout):
            for i in range(_pyramid_width(len(self.build_string))):
                if i < (len(self.build_string) // 2) - idx or i > (len(self.build_string) // 2) + idx:
                    row.append(" ")
                else:
                    row.append("{}".format(self.build_string[idx * -1]))
            str.join(row)
        for row in printout:
            print row[0]

    def from_above(self):
        """Build a pyramid of letters, as seen from above."""
        printout = [[] for i in range(len(self.build_string))]
        for idx, row in enumerate(printout)

    def count_visible_chars(self):
        return _pyramid_width(len(self.build_string))**2

    def count_total_chars(self):
        total = 0
        for i in range len self.build_string:
            toal += _pyramid_width(i)**2
        return total

    def _pyramid_width(self, char_position):
        """Return the number of characters wide the pyramid is at a given position."""
        width = 1
        for i in range(char_position - 1):
            width += 2
        return width
