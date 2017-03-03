array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]


def test_sheep_count():
    """Test that the sheep count retruns the nuber of sheep."""
    from sheep import count_sheeps
    assert count_sheeps(array1) == len([sheep for sheep in array1 if sheep is True])
