"""Codewars tests converted to run in pytest."""

import pytest

results_table = [
    [[[45, 12], [55, 21], [19, -2], [104, 20]], ['Open', 'Senior', 'Open', 'Senior']],
    [[[16, 23], [73, 1], [56, 20], [1, -1]], ['Open', 'Open', 'Senior', 'Open']],
]


@pytest.mark.parametrize('data, result', results_table)
def test_open_senior(data, result):
    """Function paramatrized to cover codewars test cases."""
    from open_or_senior import open_or_senior
    assert open_or_senior(data) == result
