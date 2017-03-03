"""Codewars tests converted to run in pytest."""

import pytest

results_table = [
    [[0, 0, 0, 1], 1],
    [[0, 0, 1, 0], 2],
    [[1, 1, 1, 1], 15],
    [[0, 1, 1, 0], 6]
]


@pytest.mark.parametrize('data, result', results_table)
def test_binary_array(data, result):
    """Function paramatrized to cover codewars test cases."""
    from binary_array import binary_array_to_number
    assert binary_array_to_number(data) == result
