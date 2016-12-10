"""Calculate how many years for population to hit value p."""


def nb_year(p0, percent, aug, p):
    """Calculate how many years for population to hit value p."""
    perc = (float(percent) / 100)
    count = 0
    while p0 < p:
        new_people = p0 * perc + aug
        p0 += new_people
        count += 1
    return count
