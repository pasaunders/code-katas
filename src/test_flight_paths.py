"""Test flight path kata."""

import pytest


def test_parse_json_returns_something():
    """Test if function parsing json returns something."""
    from flight_paths import read_airports
    assert read_airports()


def test_parse_json_returns_graph():
    """Test if function parsing json returns a dictionary."""
    from flight_paths import read_airports
    assert isinstance(read_airports(), dict)


def test_flight_path_returns_formatted_string():
    """Test if flight_path returns a string."""
    from flight_paths import flight_path
    data = flight_path('Chicago', 'New York City')
    assert isinstance(data, str)

def test_flight_path_returns_right_cities():
    """Test if flight_path returns expected cities."""
    from flight_paths import flight_path
    data = flight_path('Chicago', 'New York City')
    assert 'Chicago' in data and 'New York City' in data
