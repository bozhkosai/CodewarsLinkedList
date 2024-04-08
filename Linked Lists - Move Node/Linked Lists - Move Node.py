"""move_node"""
class Node:
    """Node class for linked list"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Context:
    """Context class for linked list"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """Move node from source to dest"""
    source.next, dest = dest, source.next
    return Context(dest, source)
