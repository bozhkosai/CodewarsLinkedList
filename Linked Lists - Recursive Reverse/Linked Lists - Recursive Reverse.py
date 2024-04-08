"""recursive reverse linked list"""
class Node:
    """Node class for linked list"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def reverse(head):
    """Reverse linked list"""
    if head is not None and head.next is not None:
        new_head = reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head
    return head
