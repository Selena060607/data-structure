class Node:
    def __init__(self, item, nxt=None):
        self.item = item
        self.next = nxt


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self.size() == 0

    '''stack operations'''

    def push(self, item):
        old_tail = self._tail
        self._tail = Node(item)
        if old_tail is None:
            self._head = self._tail
        else:
            old_tail.next = self._tail
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Remove from empty linked list')
        else:
            if self._head is self._tail:
                # only one element
                self._head = None
                self._tail = None
            else:
                walk = self._head
                while walk.next is not self._tail:
                    walk = walk.next
                walk.next = None
                self._tail = walk
            self._size -= 1

    '''queue operations'''

    def enqueue(self, item):
        old_tail = self._tail
        self._tail = Node(item)
        if old_tail is None:
            self._head = self._tail
        else:
            old_tail.next = self._tail
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Remove from empty linked list')
        else:
            self._head = self._head.next
            self._size -= 1
