"""Remove the first and last char from a string."""


def remove_char(s):
    """Remove the first and last char from a string."""
    a = list(s)
    del a[-1]
    del a[0]
    return "".join(a)
