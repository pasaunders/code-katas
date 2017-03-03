"""Take an array repesenting a binary number, convert it to an int."""


def binary_array_to_number(bin_array):
    """Convert an array of 1s and 0s into binary and then int."""
    number_string = "".join(map(str, bin_array))
    return int(number_string, 2)
