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

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    command = input()
    if command.startswith("push"):
        x = int(command.split()[1])
        pq.push(x)
    elif command == "pop":
        print(pq.pop())
    elif command == "size":
        print(pq.size())
    elif command == "empty":
        print(1 if pq.empty() else 0)
    else:
        print(pq.top())