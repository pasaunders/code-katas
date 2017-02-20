"""Test the high_low module. Converted to pytest."""
import pytest

results = [
    [[4, 5, 29, 54, 4, 0, -214, 542, -64, 1, -3, 6, -6], "542 -214"],
    [[1, -1], "1 -1"],
    [[1, 1], "1 1"],
    [[-1, -1], "-1 -1"],
    [[1, -1, 0], "1 -1"],
    [[1, 1, 0], "1 0"],
    [[-1, -1, 0], "0 -1"],
    [[42], "42 42"],
]


@pytest.mark.parametrize('nums, result', results)
def test_high_low(nums, result):
    """Test function parametrized to replace codewars tests."""
    from high_low import high_and_low
    assert high_and_low(nums) == result
