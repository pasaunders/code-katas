"""Record and return printer error rate as a fraction."""


def printer_error(s):
    """Take a string of letters a-m are good, n-z are errors."""
    errors = 0
    good_letters = list(map(chr, range(97, 110)))
    for letter in s:
        if letter in good_letters:
            continue
        errors += 1
    return "{}/{}".format(errors, len(s))
