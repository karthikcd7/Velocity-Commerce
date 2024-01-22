from Node import Node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, prev, Node):
        prevNext = prev.next
        prev.next, prevNext.prev = Node, Node
        Node.next, Node.prev = prevNext, prev

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key in self.cache:
            self.cache[key].occurences += 1
            self.moveLeft(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def moveLeft(self, node):
        cur = node.occurences
        prevLeft = node.prev
        left = prevLeft
        prevRight = node.next
        while left != self.left and left.occurences <= cur:
            left = left.prev
        if prevLeft == left:
            return
        prevLeft.next, prevRight.prev = prevRight, prevLeft
        self.insert(left, node)

    def moveRight(self, node):
        first = self.left.next
        cur = node.occurences
        prevLeft = node.prev
        left = prevLeft
        prevRight = node.next
        while left != self.left and left.occurences <= cur:
            left = left.prev
        if prevLeft == left:
            return
        prevLeft.next, prevRight.prev = prevRight, prevLeft
        self.insert(left, node)

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key].val = value
            self.cache[key].occurences += 1
            self.moveLeft(self.cache[key])
        else:
            if self.capacity == 0:
                return
            if self.capacity == len(self.cache.keys()):
                prev = self.right.prev
                prev.prev.next, self.right.prev = self.right, prev.prev
                del self.cache[prev.key]
            newNode = Node(key, value)
            self.cache[key] = newNode
            if self.left.next.occurences == 1:
                self.insert(self.left, newNode)
            else:
                prev = self.right.prev
                prev.next, self.right.prev = newNode, newNode
                newNode.next, newNode.prev = self.right, prev
                self.moveLeft(newNode)