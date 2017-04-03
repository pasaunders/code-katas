import string


def is_pangram(s):
    letters = set(filter(lambda x: x in string.ascii_lowercase, s.lower()))
    if ''.join(sorted(letters)) == string.ascii_lowercase:
        return True
    return False
