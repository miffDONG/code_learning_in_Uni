import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END

    def push_front(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    def push_back(self,new_data):
        if self.begin() == self.end():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self,node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return next_node

    def insert(self,node,new_data):
        if node == self.end():
            self.push_back(new_data)

        elif node == self.begin():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node

    def begin(self):
        return self.head

    def end(self):
        return self.tail

    
n,m = tuple(map(int,input().split()))
str = input()

DL = DoublyLinkedList()
for i in str:
    DL.push_back(i)

iter = DL.end()

for _ in range(m):
    s = input()
    if s.startswith("L"):
        if iter != DL.begin():
            iter = iter.prev

    elif s.startswith("R"):
        if  iter != DL.end():
            iter = iter.next
    
    elif s.startswith("D"):
        if iter != DL.end():
            iter = DL.erase(iter)

    else:
        DL.insert(iter,s[2])


iter = DL.begin()
while iter != DL.end():
    print(iter.data,end="")
    iter = iter.next