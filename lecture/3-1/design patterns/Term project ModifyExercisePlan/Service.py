import ExercisePlan
from PlayerInform import Observer, Player 
import PositionSpacInfo

class SetPlan:
    def __init__(self):
        self.plan = None
        self.controlBodyPlan = 0
        self.controlSkillPlan = 0

    def controlAddPlan(self,player,goal):
        if player.injury == False:
            if(abs(goal.gapMuscleMass)>2 or abs(goal.gapWeight)>4):
                self.plan = ExercisePlan.BodyPlan() 
                self.setBodyPlan()
            else:
                #ballControl능력이 있으면 True
                if(player.ballControl == False):
                    self.plan = ExercisePlan.SkillPlan()
                    self.setSkillPlan()
                else:
                    self.plan = ExercisePlan.BasicPlan()
        else:
            self.plan = ExercisePlan.injuryPlan()
        
        return self

    def setBodyPlan(self):
        if self.controlBodyPlan%3 == 0:
            self.plan.setWholeBody()
            
        elif self.controlBodyPlan%3 == 1:
            self.plan.setForJump()
        else:
            self.plan.setForShoot()

        self.controlBodyPlan +=1
        return self

    def setSkillPlan(self):
        if self.controlSkillPlan%2 == 0:
            self.plan.setDribbel()
        else:
            self.plan.setShoot()

        self.controlSkillPlan +=1
        return self

class Service(Observer):
    def __init__(self):
        self.player = None
        self.goal = None
        self.plan = None  

    def genPlayer(self, height, weight, muscleMass, position, injury, ballControl):
        self.player = Player(height, weight, muscleMass, position, injury, ballControl)
        self.player.attach(self)
        self.plan= SetPlan()
        self.update()
        return self

    def modPlayer(self, weight, muscleMass, position, injury, ballControl):
        self.player.setWeight(weight)
        self.player.setMuscleMass(muscleMass)
        self.player.setPosition(position)
        self.player.setInjury(injury)
        self.player.setBallControl(ballControl)
        return self

    def update(self):
        playerInfo = self.player.getInfo()
        position, height, weight, muscleMass, injury, ballControl = playerInfo
        self.goal = PositionSpacInfo.GoalBuilder().setHeight(height).setWeight(weight).setMuscleMass(muscleMass).setPosition(position).buildGoal()
        self.plan.controlAddPlan(self.player, self.goal)
        return self
    
