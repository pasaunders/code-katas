"""Tests for the parenthetical challenge."""


import pytest

TEST_INPUTS = [['('], [')']]

TEST_STRINGS = [['(a)(b)(c)', 0], [')()(', -1], ['()(()', 1]]


@pytest.fixture(scope='module', params=TEST_STRINGS)
def t(request):
    """Practice parametrizing fixtures."""
    from parenthetics import paren
    return paren(request.param)


def test_init():
    """Test for successful instantiation."""
    from parenthetics import Queue
    my_queue = Queue()
    assert isinstance(my_queue, Queue)


def test_enqueue():
    """Test for successful enqueue method."""
    from parenthetics import Queue
    q = Queue()
    q.enqueue('(')
    assert q.length == 1


def test_dequeue():
    """Test for successful dequeue method."""
    from parenthetics import Queue
    q = Queue()
    q.enqueue(0)
    assert q.dequeue() == 0


@pytest.mark.parametrize('input, expected', TEST_STRINGS)
def test_func(input, expected):
    """Test for expected returns."""
    from parenthetics import paren
    assert paren(input) == expected
