"""A script to test if the parentheticals of a string are matched."""


class Queue(object):
    """A singly linked list, to hold parens."""

    def __init__(self):
        """Initialize a Queue class."""
        self.head = None
        self.length = 0

    # def enqueue(self, data):
    #     """Add a value to the queue's head."""
    #     node = Node(data, self.head)
    #     self.length += 1
    #     if self.length == 0:
    #         self.tail = node
    #     if self.length > 0:
    #         self.head.prev = node
    #     old_head = self.head
    #     self.head = node
    #     self.head.next = old_head

    def enqueue(self, val):
        """Append a val to the end of the queue."""
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = node
        self.length += 1

    def dequeue(self):
        """Remove a value from the queue's tail."""
        val = self.head.data
        self.head = self.head.next
        self.length -= 1
        return val

    def size(self):
        """Return the size of the queue."""
        return self.length

    def peek(self):
        """Look at the next value in the queue."""
        return self.tail.data


class Node(object):
    """Node to build a linked list."""

    def __init__(self, data=None, next=None):
        """Initialize a node for the queue."""
        self.data = data
        self.next = next


def paren(test_string):
    """Parentheticals: 0 for balanced, 1 for open, -1 for broken."""
    left_paren = Queue()
    right_paren = Queue()
    for i in range(len(test_string)):
        if test_string[i] == '(':
            left_paren.enqueue(i)
        elif test_string[i] == ')':
            right_paren.enqueue(i)
    while left_paren.length != 0 and right_paren.length != 0:
        if left_paren.dequeue() >= right_paren.dequeue():
            return -1
    if left_paren.length == 0 and right_paren.length == 0:
        return 0
    if left_paren.length == 0:
        return -1
    if right_paren.length == 0:
        return 1
    else:
        return 'The while loop broke.'
