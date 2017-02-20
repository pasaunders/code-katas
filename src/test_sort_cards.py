"""Convert sort cards kata tests to run in pytest."""

import pytest

output_table = [
    [list('39A5T824Q7J6K'), list('A23456789TJQK')],
    [list('Q286JK395A47T'), list('A23456789TJQK')],
    [list('54TQKJ69327A8'), list('A23456789TJQK')]
]


@pytest.mark.parametrize('input, output', output_table)
def test_cards(input, output):
    """Test that the function sorts cards by value."""
    from sort_cards import sort_cards
    assert sort_cards(input) == output
