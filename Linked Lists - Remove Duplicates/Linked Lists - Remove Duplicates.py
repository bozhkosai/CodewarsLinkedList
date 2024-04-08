"""remove"""
class Node:
    """Node class for linked list"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    """Remove duplicates from linked list"""
    if head is not None:
        new_head = head
        while new_head.next is not None:
            if new_head.data == new_head.next.data:
                new_head.next = new_head.next.next
            else:
                new_head = new_head.next
        return head
    return None
