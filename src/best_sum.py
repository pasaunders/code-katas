"""Dynamic programming exercise. Returns the maximum distance traveled within a limit, not using more than a specified number of items."""

from collections import defaultdict


def choose_best_sum(capacity, maxitems, items_list):
    number_items = len(items_list)
    dynamic_table = {}
    for i in range(capacity + 1):
        dynamic_table[i] = {}
        for j in range(number_items + 1):
            dynamic_table[i][j] = defaultdict(int)
    for j in range(number_items):
        for i in range(1, capacity + 1):
            for l in range(1, maxitems + 1):
                if items_list[j] > i:
                    dynamic_table[i][j + 1][l] = dynamic_table[i][j][l]
                else:
                    if j < l:
                        dynamic_table[i][j + 1][l] = max(dynamic_table[i][j][l], dynamic_table[i - items_list[j]][j][l] + items_list[j])
                    else:
                        prev = []
                        for m in range(0, j + 1):
                            prev.append(dynamic_table[i - items_list[j]][m][l - 1])
                        dynamic_table[i][j + 1][l] = max(dynamic_table[i][j][l], max(prev) + items_list[j])
    return dynamic_table[capacity][number_items][maxitems]
