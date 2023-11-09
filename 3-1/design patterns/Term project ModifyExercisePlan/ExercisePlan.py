
class BasicPlan:
    def __init__(self):
        self.warmUpList = ['High knees', 'Butt kicks', 'Lunges Leg Swings', 'Jogging in Place']
        self.mainExList = ['Lay up 20/20', 'Three steps', 'Sprint in Place', 'Dribbel drill', 'strategy scrimmage']
        self.coolDownList = ['Hamstring Stretches', 'Calf Stretches', 'Hip Flexor Stretches', 'Static Stretches']
        self.addList = ''
        self.planText = ''


    def exercisePlan(self):
        self.planText = ""
        self.planText += self.warmUp()
        self.planText += self.mainEx()
        self.planText += self.coolDown()
        self.planText += self.addPlan()
        return self.planText

    def warmUp(self):
        result = "\nWarm-up start\n"
        for i in range(len(self.warmUpList)):
            result += f"{i+1}. {self.warmUpList[i]}\n"
        return result

    def mainEx(self):
        result = "\nMain exercise start\n"
        for i in range(len(self.mainExList)):
            result += f"{i+1}. {self.mainExList[i]}\n"
        return result

    def coolDown(self):
        result = "\nCool-down start\n"
        for i in range(len(self.coolDownList)):
            result += f"{i+1}. {self.coolDownList[i]}\n"
        return result

    def addPlan(self):
        return self.addList

    def getPlanText(self):
        return self.getPlanText

class BodyPlan(BasicPlan):
    def __init__(self):
        super().__init__()
        self.addList = None

    def setWholeBody(self):
        self.addList = ['Squat','Bench press','Shoulder press','Deadlift']
        return self
    
    def setForJump(self):
        self.addList = ['Squat', 'Lunge', 'Box Jump', 'Step Up' , 'Dumbbel Vertical Leap']
        return self
    def setForShoot(self):
        self.addList = ['Deadlift' , 'Pull up' , 'Shoulder Press', 'Side Lateral Raise','Arm Curl']
        return self
    
    def setForWeightUp(self):
        self.addList = " you have to eat more "
        return self
    
    def addPlan(self):
        result = "\nPlus Plan start\n"
        for i in range(len(self.addList)):
            result += f" {i+1}. {self.addList[i]}\n"
        return result


class SkillPlan(BasicPlan):
    def __init__(self):
        super().__init__()
        self.addList = None

    def setDribbel(self):
        self.addList = ['Cone Dribble and Finish', 'Two-Ball Dribble', '1-on-1 Dribble Attack','Dribble Combo Moves']
        return self
    def setShoot(self):
        self.addList = ['Spot Shooting', 'Range Shooting', 'Game-like Shooting']
        return self

    def addPlan(self):
        result = "\nPlus Plan start\n"
        for i in range(len(self.addList)):
            result += f" {i+1}. {self.addList[i]}\n"
        return result

    
class injuryPlan(BasicPlan):
    def __init__(self):
        super().__init__()

    def addPlan(self):
        result = "\nfocus on your recovery\n"
        result += '\ngo to hospital and get professional treatment\n'
        result += "\nThe most important thing is not to be injured\n"
        return result

    def exercisePlan(self):
        self.planText = ""
        self.planText +=self.addPlan()
        return self.planText


