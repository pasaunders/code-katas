"""Parse and format address book.

Return string of addresses in provided zip code as zipcode:street &
town, street & town,.../hosue number,house number, ...
if there are no entries for the zip code return zipcode:/
"""


def travel(r, zipcode):
    """Accept address list and zipcode, parse and return formatted string."""
    stops = r.split(',')
    processed_stops = [address[:-9].split(" ", 1) for address in stops if zipcode == " ".join(address.rsplit(" ", 2)[1:]) and zipcode]
    numbers = [address[0] for address in processed_stops]
    streets = [address[1] for address in processed_stops]
    if not numbers or not streets:
        return "{}:/".format(zipcode)
    return "{}:{}/{}".format(zipcode, ",".join(streets), ",".join(numbers))
