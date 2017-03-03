"""Return the next square if sq is a square, -1 otherwise."""


def find_next_square(sq):
    """Return the next square if sq is a square, -1 otherwise."""
    if int(sq**(0.5)) != float(sq**(0.5)):
        return -1
    else:
        return ((sq**(0.5)) + 1)**2
