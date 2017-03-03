"""Test tickets.py."""

import pytest


lines = [
    [[25, 25, 25], "YES"],
    [[25, 50, 25], "YES"],
    [[50, 50, 50], "NO"],
    [[50, 25, 25], "NO"],
    [[25, 25, 50, 100], "YES"],
    [[100, 50, 25], "NO"],
    [[25, 25, 25, 100], "YES"],
    [[25, 100, 25, 25], "NO"],
]


@pytest.mark.parametrize('input, output', lines)
def test_tickets(input, output):
    """Test that tickets returns expected outputs for each parameter set."""
    from tickets import tickets
    assert tickets(input) == output
