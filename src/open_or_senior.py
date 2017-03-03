"""Test to see if club members are seniors."""


def open_or_senior(data):
    """Test to see if club members are seniors."""
    # a = list(data)
    # for i in range(len(data)):
    stored_data = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            stored_data.append("Senior")
        else:
            stored_data.append("Open")
    return stored_data
