"""Codewars tests converted to run in pytest."""


def test_count():
    """Test that the get_count function returns the expected number."""
    from count import get_count
    assert get_count('abracadabra') == 5
