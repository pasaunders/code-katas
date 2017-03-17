import pytest


lines = [
    [[5, 78, 52, 900, 1], 207],
    [[5, 25, 50, 75], 39],
    [[2], 2],
    [[1, 1, 1, 1, 9999], 2001],
    [[0], 0]
]


@pytest.mark.parametrize('input, output', lines)
def test_average(input, output):
    """Test that the average function correctly averages and round a list of ints."""
    from scores import average
    assert average(input) == output
