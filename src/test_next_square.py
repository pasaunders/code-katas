"""Codewars tests for next square converted to pytest."""

import pytest

results = [
    [121, 144],
    [625, 676],
    [319225, 320356],
    [15241383936, 15241630849],
    [3, -1],
    [155, -1],
    [342786627, -1]
]


@pytest.mark.parametrize('sq, result', results)
def test_next_square(sq, result):
    """Pytest function to replace codewars tests."""
    from next_square import find_next_square
    assert find_next_square(sq) == result
