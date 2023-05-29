class Player:
    def __init__(self,height,weight,muscleMass,position,ankleWeakness):
        self.height = height
        self.weight = weight
        self.muscleMass = muscleMass
        self.position = position
        self.ankleWeakness = ankleWeakness

class PlayerBuilder:
    def __init__(self):
        self.height = None
        self.weight = None
        self.muscleMass = None
        self.position = None
        self.ankleWeakness = None

    def setHeight(self, height):
        self.height = height

    def setWeight(self,weight):
        self.weight = weight

    def setmuscleMass(self,muscleMass):
        self.muscleMass = muscleMass

    def setPosition(self,position):
        self.position = position

    def setAnkleWeakness(self,ankleWeakness):
        self.ankleWeakness = ankleWeakness

    def build(self):
        player = Player(self.height,self.weight,self.muscleMass,self.position,self.ankleWeakness)
