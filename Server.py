from LFUCache import LFUCache


class Server:
    def __init__(self, x, y, vals, number):
        self.cache = LFUCache(2)
        self.storage = vals
        self.x = x
        self.y = y
        self.number = number
        self.lookup = {}
        self.neighbor = set()

    def addNeighbor(self, server, distance):
        self.neighbor.add((server, distance))

    def updateCache(self, val):
        self.cache.put(val, val)

    def addLookup(self, data, dest):
        self.lookup[data] = dest
