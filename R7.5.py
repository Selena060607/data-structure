class Node:
    def __init__(self, item, nxt=None):
        self.item = item
        self.next = nxt

class LinkedList:
    """A circularly linked list."""
    def __init__(self,head=None):
        self._head = head

    def count(self,head):
        count = 0
        if head is None:
            return 0
        else:
            current = head
            while current.next!= head:
                count += 1
                current = current.next
            return count
