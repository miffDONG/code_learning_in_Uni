
class PositionSpacInfo:
    def __init__(self):
        self.height = None
        self.weight = None
        self.muscleMass = None
        self.position = 'Guard'

    def setGuardSpac(self,height):
        self.height = height
        self.weight = 0.55 * height + 0.36
        self.muscleMass = 0.25 *self.weight + 20.7
    
    def setForwardSpac(self,height):
        self.height = height
        self.weight = 0.62 * height + 0.36
        self.muscleMass = 0.29*self.weight +19.2
        
    def setCenterSpac(self,height):
        self.height = height
        self.weight = 0.69 * height + 0.33
        self.muscleMass = 0.31 * self.weight + 19.5