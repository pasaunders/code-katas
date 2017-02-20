"""Codewars tests parametrized and converted to pytest."""

import pytest

output_table = [
    ['eloquent', 'loquen'],
    ['country', 'ountr'],
    ['person', 'erso'],
    ['place', 'lac'],
    ['ok', '']
]


@pytest.mark.parametrize('input, output', output_table)
def test_remove(input, output):
    """Test remove char function with specified inputs."""
    from remove_chars import remove_char
    assert remove_char(input) == output
