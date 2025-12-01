class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next =next
class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(head,k):
        current = head
        while current is not None:
            if current.item == k:
                return current
            current = current.next
        return None

    def contains(head,k):
        current = head
        while current is not None:
            if current.item == k:
                return True
            current = current.next
        return False

    def add_first(head,item):
        new_head = Node(item)
        new_head.next = head
        return new_head
        '''simplified into head=Node(item,head)'''

    def remove_first(head):
        if head is None:
            return None
        else:
            return head.next

    def add_last(head,item):
        if head is None:
            return Node(item)
        else:
           current = head
           while current is not None:
               current = current.next
           current.next = Node(item)

    '''def addlast(head,tail,item):
        if head is None:
            return Node(item)
        else:
            old_tail = tail
            tail = Node(item)
            old_tail.next = tail
            return head'''

    def remove_last(head):
        if head is None:
            return None
        elif head.next is None:
            return None
        else:
            current = head
            while current.next.next is not None:
                current = current.next
            current.next = None
            return head
