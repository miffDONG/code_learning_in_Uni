import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("Priority Queue is empty")

        return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("Priority Queue is empty")

        return -self.items[0]