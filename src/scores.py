"""Average the values in a list and round to the nearest whole number."""


def average(scores):
    return int(round(sum(scores)/len(scores)))
