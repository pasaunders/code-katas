"""Tests the binary addition kata solution."""

import pytest


PARAMS_TABLE_BINARY = [
    [1, 1, '10'],
    [0, 1, '1'],
    [1, 0, '1'],
    [2, 2, '100'],
    [51, 12, '111111'],
]


@pytest.mark.parametrize('n, m, result', PARAMS_TABLE_BINARY)
def test_add_binary(n, m, result):
    """Test each addition and result provided by codewars."""
    from binary_addition import add_binary
    assert add_binary(n, m) == result
