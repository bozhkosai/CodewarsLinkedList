class Node:
    """node"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def loop_size(node):
    """loop size"""
    visited = {}
    index = 0
    while node not in visited:
        visited[node] = index
        index += 1
        node = node.next
    return index - visited[node]
