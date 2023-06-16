#Templete pattern
#import PlayerInform

class BasicPlan:
    def __init__(self):
        self.warmUpList = ['High knees','Butt kicks', 'Lunges Leg Swings','Jogging in Place']
        self.mainExList = ['Lay up 20/20','Three steps', 'Sprint in Place' , 'Dribbel drill' , 'strategy scrimmage' ]
        self.coolDownList = ['Hamstring Stretches','Calf Stretches','Hip Flexor Stretches','Static Stretches']

    def exercisePlan(self):
        self.warmUp()
        self.mainEx()
        self.coolDown()
        self.addPlan()
        self.done()
    
    def warmUp(self):
        print("\nwarm up start")
        for i in range(len(self.warmUpList)):
            print(f" {i+1}. {self.warmUpList[i]} ",end='')

    
    def mainEx(self):
        print("\nmain exercise start")
        for i in range(len(self.mainExList)):
            print(f" {i+1}. {self.mainExList[i]}",end='')

    
    def coolDown(self):
        print("\ncool down start")
        for i in range(len(self.coolDownList)):
            print(f" {i+1}. {self.coolDownList[i]}",end='')

    def done(self):
        print("You have carried out all your plans.")
    
    def addPlan(self):
        pass

class BodyPlan(BasicPlan):
    def __init__(self):
        super().__init__()
        #default = 전신운동 / use also weight loss or weight up
        self.healthPlan = ['Squat','Bench press','Shoulder press','Deadlift']
    
    def setForJump(self):
        self.healthPlan = ['Squat', 'Lunge', 'Box Jump', 'Step Up' , 'Dumbbel Vertical Leap']

    def setForShoot(self):
        self.healthPlan = ['Deadlift' , 'Pull up' , 'Shoulder Press', 'Side Lateral Raise','Arm Curl']

    def setForWeightUp(self):
        self.healthPlan.append(" you have to eat more ")

    def addPlan(self):
        # print("\nthis plan is added for you. Do this plan after Basic Plan")
        for i in range(len(self.healthPlan)):
            print(f" {i+1}. {self.healthPlan[i]}",end='')
        # print("\nfor your performance\n")

class SkillPlan(BasicPlan):
    def __init__(self):
        super().__init__()
        self.skillPlan = None

    def setDribbel(self):
        self.skillPlan = ['Cone Dribble and Finish', 'Two-Ball Dribble', '1-on-1 Dribble Attack','Dribble Combo Moves']

    def setShoot(self):
        self.skillPlan = ['Spot Shooting', 'Range Shooting', 'Game-like Shooting']

    def addPlan(self):
        # print("\ntouch the ball more. get used to")
        for i in range(len(self.skillPlan)):
            print(f" {i+1}. {self.skillPlan[i]}",end='')
        # print("\nfor your performance\n")

    
class injuryPlan(BasicPlan):
    def __init__(self):
        super().__init__()
        self.rehabilitation = None

    def setJoint(self):
        self.rehabilitation = '\ngo to hospital and get professional treatment'

    def addPlan(self):
        print("\nfocus on your recovery")
        print(self.rehabilitation)
        print("The most important thing is not to be injured\n")

    def exercisePlan(self):
        self.addPlan()

basic = BasicPlan()
basic.exercisePlan()

print('\n\n')
weUp = BodyPlan()
weUp.exercisePlan()
print('\n\n')
sk = SkillPlan()
sk.setShoot()
sk.exercisePlan()
print('\n\n') 
inj = injuryPlan()
inj.setJoint()
inj.exercisePlan()


