"""Nb year kata tests converted to pytest."""

import pytest

results = [
    [1500, 5, 100, 5000, 15],
    [1500000, 2.5, 10000, 2000000, 10],
    [1500000, 0.25, 1000, 2000000, 94]
]


@pytest.mark.parametrize('p0, percent, aug, p, result', results)
def test_nb_year(p0, percent, aug, p, result):
    """Parametrized function covering codewars tests converted to pytest."""
    from np_year import nb_year
    assert nb_year(p0, percent, aug, p) == result
