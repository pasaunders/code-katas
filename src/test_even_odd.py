"""Codewars tests converted to run in pytest."""

import pytest

test_num = [
    [2, 'Even'],
    [0, 'Even'],
    [7, 'Odd'],
    [1, 'Odd']
]


@pytest.mark.parametrize('n, result', test_num)
def test_even_odd(n, result):
    """Test that even_odd returns the right string for each number."""
    from even_odd import even_or_odd
    assert even_or_odd(n) == result
