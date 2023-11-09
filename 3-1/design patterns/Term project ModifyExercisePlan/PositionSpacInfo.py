
class basicSpac:
    def __init__(self,height,weight,muscleMass):
        self.height = height
        self.weight = weight
        self.muscleMass = muscleMass


class PositionSpacInfo(basicSpac):
    def __init__(self,height,weight,muscleMass,position):
        super().__init__(height,weight,muscleMass)
        self.position = position
        self.goalWeight = None
        self.goalMuscleMass = None
        self.gapWeight = None
        self.gapMuscleMass = None
        self.text = None

    
    def setGuardSpac(self):
        self.position = 'Guard'
        self.goalWeight = round(0.35 * self.height + 0.36,2)
        self.goalMuscleMass = round(0.25 *self.goalWeight + 20.7,2)
        return self
    
    def setForwardSpac(self):
        self.position = 'Forward'
        self.goalWeight = round(0.43 * self.height + 0.36,2)
        self.goalMuscleMass = round(0.29 * self.goalWeight +19.2,2)
        return self
    
    def setCenterSpac(self):
        self.position = 'Center'
        self.goalWeight = round(0.49 * self.height + 0.33,2)
        self.goalMuscleMass = round(0.31 * self.goalWeight + 19.5,2)
        return self
    
    def setGap(self):
        self.gapWeight = round(self.goalWeight - self.weight,2)
        self.gapMuscleMass = round(self.goalMuscleMass - self.muscleMass,2)
        return self
    
    def goalPrint(self):
        print(f"Best Spac of {self.position} : weight \'{self.goalWeight}\' muscleMass \'{self.goalMuscleMass}\'")

    def gapText(self):
        self.text=f"Gap with Best Spac of {self.position} : weight \'{self.goalWeight}\' muscleMass \'{self.goalMuscleMass}\'"

        if abs(self.gapWeight)>4:
            if self.gapWeight<0:
                self.text+=f"\n\n{self.gapWeight}kg 만큼 체중감량이 필요합니다."
            else:
                self.text+=f"\n\n{self.gapWeight}kg 만큼 체중증량이 필요합니다."

        if abs(self.gapMuscleMass)>2:
            if self.gapMuscleMass > 0:
                self.text+=f"\n{self.gapMuscleMass}kg만큼 근육을 키워야합니다."
            else:
                pass

        return self.text
    
    def GetSpac(self):
        return(self.goalWeight,self.goalMuscleMass,self.gapWeight,self.gapMuscleMass)
    

class GoalBuilder:
    def __init__(self):
        self.height = None
        self.weight = None
        self.muscleMass = None       
        self.position = None
        self.goalWeight = None
        self.goalMuscleMass = None
        self.gapWeight = None
        self.gapMuscleMass = None

    def setHeight(self,height):
        self.height = height
        return self
    
    def setWeight(self,weight):
        self.weight = weight
        return self

    def setMuscleMass(self,muscleMass):
        self.muscleMass = muscleMass
        return self
    
    def setPosition(self,position):
        self.position = position
        return self

    def buildGoal(self):
        goal = PositionSpacInfo(self.height,self.weight,self.muscleMass,self.position)
        
        if goal.position == 'Guard':
            print("Guard spac")
            goal.setGuardSpac()
        elif goal.position == 'Forward':
            goal.setForwardSpac()
        elif goal.position == 'Center':
            goal.setCenterSpac()
        else: print('please reset position (Guard,Forward,Center)')

        goal.setGap()

        return goal
