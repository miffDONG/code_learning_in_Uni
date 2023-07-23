
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Player(Subject):
    def __init__(self, height, weight, muscleMass, position, injuryBool, ballControl):
        self.height = height
        self.weight = weight
        self.muscleMass = muscleMass
        self.position = position
        self.injury = injuryBool
        self.ballControl = ballControl
        self.observers = []

    def getInfo(self):
        return (self.position, self.height, self.weight, self.muscleMass, self.injury, self.ballControl)

    def setWeight(self, weight):
        self.weight = weight
        self.notify()
        return self

    def setMuscleMass(self, muscleMass):
        self.muscleMass = muscleMass
        self.notify()
        return self
    
    def setInjury(self, injuryBool):
        self.injury = injuryBool
        self.notify()
        return self
    
    def setPosition(self, position):
        self.position = position
        self.notify()
        return self

    def setBallControl(self, ballControl):
        self.ballControl = ballControl
        self.notify()
        return self

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass
