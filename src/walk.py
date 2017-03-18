def isValidWalk(walk):
    """determine if walk is valid"""
    if len(walk) is not 10:
        return False
    validity = {'n': 0, 's': 0, 'w': 0, 'e': 0}

    for item in walk:
        if item is 'n':
            validity['n'] += 1
        elif item is 'w':
            validity['w'] += 1
        elif item is 's':
            validity['s'] += 1
        elif item is 'e':
            validity['e'] += 1
        else:
            raise ValueError('input walk contained invalid direction')
    if validity['n'] == validity['s'] and validity['e'] == validity['w']:
        return True
    else:
        return False
