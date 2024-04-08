"""swap node"""
class Node:
    """Node class for linked list"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def swap_pairs(head):
    """Swap node pairs in linked list"""
    if head is not None and head.next is not None:
        pair, new_head, head.next.next = head.next.next, head.next, head
        head.next = swap_pairs(pair)
        return new_head
    return head
