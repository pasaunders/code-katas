from itertools import combinations


def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None
    combos = combinations(ls, k)
    best_distance = 0
    for item in combos:
        distance = sum(item)
        if distance <= t and distance > best_distance:
            best_distance = distance
    if best_distance == 0:
        return None
    return best_distance
