"""Test to see if club members are seniors."""


def open_or_senior(data):
    """Test to see if club members are seniors."""
    a = list(data)
    for i in range(len(data)):
        if a[i][0] >= 55 and a[i][1] > 7:
            a[i] = "Senior"
        else:
            a[i] = "Open"
    return a
