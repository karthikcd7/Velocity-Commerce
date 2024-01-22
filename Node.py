class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.occurences = 1
        self.next, self.prev = None, None