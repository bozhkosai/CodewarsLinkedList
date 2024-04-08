"""split"""
class Node:
    """Node class for linked list"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Context:
    """Context class for linked list"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """Alternating split linked list"""
    if head is not None and head.next is not None:
        first, second, new_head = head, head.next, head.next.next
        new_first, new_second = first, second
        while new_head:
            new_first.next = new_head
            new_first = new_first.next
            new_head = new_head.next
            if new_head is not None:
                new_second.next = new_head
                new_second = new_second.next
                new_head = new_head.next
        new_first.next, new_second.next = None, None
        return Context(first, second)
    raise ValueError
