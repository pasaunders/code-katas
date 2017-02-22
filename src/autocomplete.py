"""Attempt at creating an autocomplete class."""

from trie import Trie


class Autocomplete(object):
    """Takes a vocab list on init., provides methods to autocomplete."""

    def __init__(self, vocab, max_completions=5):
        """Initialize autocomplete."""
        self.vocab = vocab
        self.max_completions = max_completions
        self._stored_vocab = Trie()
        for item in vocab:
            self._stored_vocab.insert(item)

    def complete_me(self, word):
        """Autocomplete a word based on self.vocab."""
        first_letter = self._stored_vocab.root
        for character in word:
            if character in first_letter.children:
                first_letter = first_letter.children[character]
            else:
                return []
        word_suggestions = []
        word_choices = self._search(word, first_letter, word_suggestions)
        return word_choices

    def _search(self, word, first_letter, word_suggestions):
        """Traverse trie based on provided word, return suggested words up to max_completions."""
        if first_letter.end:
            word_suggestions.append(word)
        elif not first_letter.children:
            word_suggestions.append(word)

        if len(word_suggestions) >= self.max_completions:
            return word_suggestions

        for i, (key, node) in enumerate(first_letter.children.items()):
            extended_word = word + key
            self._search(extended_word, node, word_suggestions)
        return word_suggestions
