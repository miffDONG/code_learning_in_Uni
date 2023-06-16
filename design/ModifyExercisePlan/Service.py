#facade pattern

import ExercisePlan
import PlayerInform
import PositionSpacInfo
import Observer

class SetPlan:
    def __init__(self):
        self.plan = ExercisePlan.BasicPlan() 
        self.position = None
        self.height = None
        self.weight = None
        self.muscleMass = None
        self.injury = None
        self.ballControl = None
        self.goalWeight = None
        self.goalMuscleMass = None
        self.gapWeight = None
        self.gapMuscleMass = None
        self.state = None


    def condition(self):
        self.position,self.height,self.weight,self.muscleMass,self.injury,self.injury = PlayerInform.Player.getInfo()

    def setGoalState(self):
        self.goalWeight,self.goalMuscleMass,self.gapWeight,self.gapMuscleMass = PositionSpacInfo.PositionSpacInfo.GetSpac()

    def controlAddClass(self):
        if self.injury == False:
            if(abs(self.gapMuscleMass)>3 or abs(self.gapWeight)>4):
                self.plan = ExercisePlan.BodyPlan()
            else:
                if(self.ballControl == False):
                    self.plan = ExercisePlan.SkillPlan()
                else:
                    pass
        else:
            self.plan = ExercisePlan.injuryPlan()

    def setBodyPlan(self):
        
        if self.gapMuscleMass>4:
            # 몸무게, 근육 부족 
            if self.gapWeight>4:
            
            #근육 부족
            else: 

        else:
            if 
            self.plan.addPlan()


class Service:
    def __init__(self):
        self.player = None
        self.Goal = None
        self.plan = None  
        # observer 보류 self.trainer = 

    def genPlayer(self,height,weight,muscleMass,Position,Injury):
        self.player = PlayerInform.PlayerBuilder.setHeight(height).setWeight(weight).setmuscleMass(muscleMass).setPosition(Position).setInjury(Injury).build()
        self.Goal = PositionSpacInfo.GoalBuilder.GoalBuilder().setHeight(height).setWeight(weight).setMuscleMass(muscleMass).setPosition(Position).buildGoal()
        #self.plan = ExercisePlan.BasicPlan() 

    