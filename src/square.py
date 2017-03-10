def is_square(n):    
    if n <= 1:
        return False
    return (int(n ** 0.5)) ** 2 == n