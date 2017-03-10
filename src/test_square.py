"""Codewars test converted to pytest and expanded."""

import pytest

data_table = [
    [-1, False],
    [0, False],
    [1, False],
    [4, True],
    [25, True],
]


@pytest.mark.parametrize('input, output', data_table)
def test_opposite(input, output):
    """Test opposite kata function works."""
    from square import is_square
    assert is_square(input) == output
