"""Convert codewars kata tests to pytest."""

import pytest

output_table = [
    [1, "1.00"],
    [2, "1.25"],
    [3, "1.39"]
]


@pytest.mark.parametrize('input, output', output_table)
def test_series(input, output):
    """Test that series_sum outputs according to the expected formula."""
    from sum_terms import series_sum
    print(input)
    assert series_sum(input) == output
