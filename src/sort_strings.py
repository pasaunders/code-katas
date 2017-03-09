def sort_by_length(words):
    """Take a list of strings, return a list sorted by word length."""
    return sorted(words, key=lambda word: len(word), reverse=False)
