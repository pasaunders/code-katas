"""Attempt at creating an autocomplete class."""


class Autocomplete(object):
    """Takes a vocab list on init., provides methods to autocomplete."""

    def __init__(self, vocab, max_comletions=5):
        """Initialize autocomplete."""
        self.vocab = vocab

