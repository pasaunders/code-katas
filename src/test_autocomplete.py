"""Test autocomplete engine kata."""

import pytest

TEST_VOCAB = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final']


@pytest.fixture
def ace():
    """Fixture instantiating basic autocomplete engine."""
    from autocomplete import Autocomplete
    return Autocomplete(TEST_VOCAB)


def test_init():
    """Test autocomplete instantiation with vocabulary."""
    from autocomplete import Autocomplete
    test_autocomplete = Autocomplete(TEST_VOCAB)
    for word in TEST_VOCAB:
        assert word in test_autocomplete.vocab


def test_autocomplete(ace):
    """Test complete_me method of autocomplete."""
    assert ace.complete_me('f') == ['fix', 'fit', 'fist', 'finch', 'final']


def test_set_completions():
    """Test that reduced max completions limit returns."""
    from autocomplete import Autocomplete
    comp = Autocomplete(TEST_VOCAB, 3)
    assert comp.complete_me('f') == ['fix', 'fit', 'fist']
