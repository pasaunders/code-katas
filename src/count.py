"""Get number of vowles in string."""


def get_count(input_str):
    """Get number of vowels in string."""
    num_vowels = 0
    for i in input_str:
        if i in 'aeiou':
            num_vowels += 1
    return num_vowels
