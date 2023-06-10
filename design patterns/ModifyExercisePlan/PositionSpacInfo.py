#builder

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

    # 기준 재설정
    def setGuardSpac(self):
        self.position = 'Guard'
        self.goalWeight = 0.55 * self.height + 0.36
        self.goalMuscleMass = 0.25 *self.goalWeight + 20.7
    
    def setForwardSpac(self):
        self.position = 'Forward'
        self.goalWeight = 0.62 * self.height + 0.36
        self.goalMuscleMass = 0.29*self.goalWeight +19.2
        
    def setCenterSpac(self):
        self.position = 'Center'
        self.goalWeight = 0.69 * self.height + 0.33
        self.goalMuscleMass = 0.31 * self.goalWeight + 19.5

    def setGap(self):
        self.gapWeight = self.goalWeight - self.weight
        self.gapMuscleMass = self.goalMuscleMass - self.muscleMass

    def goalPrint(self):
        print(f"Best Spac of {self.position} : weight \'{self.goalWeight}\' muscleMass \'{self.goalMuscleMass}\'")

    def gapPrint(self):
        print(f"Gap with Best Spac of {self.position} : weight \'{self.gapWeight}\' muscleMass \'{self.gapMuscleMass}\'")
        if (self.gapWeight>0):
            print(f"{self.gapWeight}만큼 체중증량이 필요합니다.")
        else:
            print(f"{self.gapWeight}만큼 체중감량이 필요합니다.")

        if(self.gapMuscleMass>0):
            print(f"{self.gapMuscleMass}만큼 근육을 키워야합니다.")
        else:
            print(f"{self.gapMuscleMass}만큼 근육이 과합니다.")

    
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

# goal = GoalBuilder().setHeight(170).setWeight(60).setMuscleMass(34).setPosition('Guard').buildGoal()

# goal.goalPrint()
# goal.gapPrint()
# position = 'Guard'

# print(f"Best Spac of {position} : weight \'{weight}\' muscleMass \'{muscleMass}\'")
