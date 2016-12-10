"""Get number of vowles in string."""


def get_count(input_str):
    """Get number of vowles in string."""
    num_vowels = 0
    a = list(input_str)
    for i in a:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            num_vowels += 1
    return num_vowels
