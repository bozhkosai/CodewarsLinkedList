class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s != "None":
        s_split = s.split(" -> ")
        return Node(int(s_split[0]), linked_list_from_string(" -> ".join(s_split[1:])))
    return None
