from abc import *
import copy
class Product(metaclass = ABCMeta):

    @abstractmethod
    def use(self):
        pass
    
    @abstractmethod
    def clone(self):
        pass


#concrete class 1 
class UnderlinePen(Product):

    def use(self, s:str):

        n = len(s)
        print(s)
        for i in range(n):
            print("~",end="")
        print()

    def clone(self):
        return copy.deepcopy(self)

#concrete class 2 : deco를 가진 객체
#use  - deco worde deco 출력
class MessageBox(Product):
    
    def __init__(self, deco:str):
        self.deco = deco

    def use(self, s:str):
        n = len(s) + 4

        for i in range(n):
            print(self.deco,end="")
        print()
        print(self.deco, s, self.deco)
        for i in range(n):
            print(self.deco, end="")
        print()

    def clone(self):
        return copy.deepcopy(self)



class Manager:

    def __init__(self):
        self.showcase = {"a": 1}

    #dict - 이름 : 출력str
    def register(self, name:str, proto:Product):
        self.showcase[name] = proto
    
    #prototype 생성 및 clone 객체 생성
    def create(self, protoName):
        p = self.showcase[protoName]
        return p.clone()
    

manager = Manager()

m1 = MessageBox("*")
m2 = MessageBox("#")
p1 = UnderlinePen()

manager.register("msg*",m1)
manager.register("msg#", m2)
manager.register("pen", p1)
msg1 = manager.create("msg*")
msg2 = manager.create("msg#")
pen = manager.create("pen")

word = "hello"
msg1.use(word)
word = "world"
msg2.use(word)
pen.use(word)