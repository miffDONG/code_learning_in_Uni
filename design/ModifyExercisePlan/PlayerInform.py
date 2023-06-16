#builder pattern

import Observer
import PositionSpacInfo

class Player:
    def __init__(self,height,weight,muscleMass,position,injuryBool):
        self.height = height
        self.weight = weight
        self.muscleMass = muscleMass
        self.position = position
        self.injury = injuryBool
        self.ballControl = False

    def getInfo(self):
        return (self.position,self.height,self.weight,self.muscleMass,self.injury,self.ballControl)

class PlayerBuilder:
    def __init__(self):
        self.height = None
        self.weight = None
        self.muscleMass = None
        self.position = None
        self.injury = None
        self.ballControl = None
    def setHeight(self, height):
        self.height = height
        return self

    def setWeight(self,weight):
        self.weight = weight
        return self

    def setmuscleMass(self,muscleMass):
        self.muscleMass = muscleMass
        return self
    
    def setPosition(self,position):
        self.position = position
        return self
    
    def setInjury(self,injuryBool):
        self.injury = injuryBool
        return self
    
    def setballControl(self, ballControl):
        self.ballControl = ballControl

    def build(self):
        player = Player(self.height,self.weight,self.muscleMass,self.position,self.injury)
        return player
    


player = PlayerBuilder().setHeight(170).setWeight(60).setmuscleMass(30).setPosition("Guard").setInjury(False).build()

print(player.getInfo())