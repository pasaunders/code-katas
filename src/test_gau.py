import pytest


results_table = [
    [1, 1],
    [100, 5050],
    [0, None],
    [1.5, None],
    [-1, None],
    ['word', None]
]


@pytest.mark.parametrize('input, output', results_table)
def test_kata(input, output):
    """Test that the function outputs exected results based on inputs."""
    from gau import f
    assert f(input) == output


@pytest.mark.parametrize('input, output', results_table)
def test_one_line_kata(input, output):
    """Test that the function outputs exected results based on inputs."""
    from gau import one_line
    assert one_line(input) == output
