def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """
    dict_piles = {
                  'A': [],
                  '2': [],
                  '3': [],
                  '4': [],
                  '5': [],
                  '6': [],
                  '7': [],
                  '8': [],
                  '9': [],
                  'T': [],
                  'J': [],
                  'Q': [],
                  'K': [],
                  }
    for card in cards:
        dict_piles[card].append(card)
    final_list = dict_piles['A'] + dict_piles['2'] + dict_piles['3'] + dict_piles['4'] + dict_piles['5'] + dict_piles['6'] + dict_piles['7'] + dict_piles['8'] + dict_piles['9'] + dict_piles['T'] + dict_piles['J'] + dict_piles['Q'] + dict_piles['K']
    return final_list