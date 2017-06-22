"""Kata to implement length and count functions for a linked list."""


class Node(object):
    """Node for building a linked list."""

    def __init__(self, data):
        """Initialize the node with given data."""
        self.data = data
        self.next = None


def length(node):
    """Determine the length of a linked list."""
    if not node:
        return 0
    length = 1
    while node.next is not None:
        length += 1
        node = node.next
    return length


def count(node, data):
    """Determine number of nodes with given value in linked list."""
    count = 1
    while node.next is not None:
        if node.data == data:
            count += 1
        node = node.next
    return count
