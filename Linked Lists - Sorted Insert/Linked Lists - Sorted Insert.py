"""sorted_insert"""
class Node:
    """Node class for linked list"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    """Insert node in sorted order"""
    if head is None or head.data >= data:
        new_node = Node(data)
        new_node.next = head
        return new_node
    elif head.data < data:
        head.next = sorted_insert(head.next, data)
    return head
