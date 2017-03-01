"""Can a clerk with no starting change sell everyone in line a ticket if each person only has a $25, $50, or $100 bill."""


def tickets(people):
    """Take a list with values equla to a patron's bill and return a yes/no value."""
    change_available = {
        "25": 0,
        "50": 0,
        "100": 0,
    }
    for patron in people:
        if patron == 25:
            change_available["25"] += 1
        elif patron == 50 and change_available["25"] >= 1:
            change_available["25"] -= 1
            change_available["50"] += 1
        elif patron == 100:
            if change_available["25"] >= 1 and change_available["50"] >= 1:
                change_available["25"] -= 1
                change_available["50"] -= 1
                change_available["100"] += 1
            elif change_available["25"] >= 3:
                change_available["25"] -= 3
                change_available["100"] += 1
            else:
                return "NO"
        else:
            return "NO"
    return "YES"
