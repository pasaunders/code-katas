"""Codewars test converted to pytest and expanded."""

import pytest

numbers_table = [
    [-1, 1],
    [0, 0],
    [1, -1]
]


@pytest.mark.parametrize('input, output', numbers_table)
def test_opposite(input, output):
    """Test opposite kata function works."""
    from opposite import opposite
    assert opposite(input) == output
