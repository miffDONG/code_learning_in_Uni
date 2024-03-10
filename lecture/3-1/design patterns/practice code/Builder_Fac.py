"""
Actor Hero Monster

주인공 몬스터 각각에 대한 생성을 담당하는 Builder class 구현
가정 : 생성과정이 복잡함.
"""

"""
1. 공통되는 argument를 갖는 부모 class
   하위 class에 추가 argument SETUP

2. 0 <= x,y <=100 (범위를 벗어날 시 끝 지점으로 설정 = default 값 설정)

3. Hero - 힘, 민첩, 체력 외부인자 입력 가능

4. Monster - 50 ~ 100 임의의 값으로 설정
             위치 0 ~ 100 사이 임의의 값

5. return self 사용            
 """

class Actor:
    def __init__(self, x, y, vital, agi, strength):
        self.x = x
        self.y = y

        self.vitality = vital
        self.agility = agi
        self.strength = strength

    """
    캐릭터 이동가능 범위 : 1+민첩성//20
    """
    def frontMoveX(self):
        if (self.x + self.agility//20) < 100:
            self.x += self.agility//20 +1
        else: self.x = 100
        return self.x
    
    def backMoveX(self):
        if (self.x - self.agility//20) > 0:
            self.x -= (self.agility//20 +1)
        else: self.x = 0
        return self.x
    
    def frontMoveY(self):
        if (self.y + self.agility//20) < 100:
            self.y += self.agility//20 +1
        else: self.y = 100
        return self.y
    
    def backMoveY(self):
        if (self.y - self.agility//20) > 0:
            self.y -= (self.agility//20 +1)
        else: self.y = 0
        return self.y
    
class Hero(Actor):
    def __init__(self, x,y, vital, agi, strength, skill, level, money, weapon, armour, job):
        super().__init__(x,y,vital,agi,strength)

        self.skill = skill
        self.level = level
        self.money = money
        self.weapon = weapon
        self.armour = armour
        self.job = job

    def printState(self):
        print("새로운 "+self.job+"가 탄생했습니다.")
        print("착용 중인 아이템은 "+self.weapon+" "+ self.armour + " 입니다.")

    def action(self):
        print(self.skill+" 기술을 사용 했습니다.")
    
    def moveXY(self):
        print(f"{self.job}가 x : {self.x} y : {self.y}로 이동합니다.")

    def levelUp(self):
        self.level += 1
        self.vitality += 1
        self.agility += 1
        self.strength += 1

    # 캐릭터 상태창
    def getStat(self):
        return (self.x, self.y, self.vitality, self.agility, self.strength,
                 self.skill, self.level, self.money, self.weapon, self.armour, self.job)

"""
직업 2가지 : 전사 궁수 
"""

class HeroBuilder:
    def __init__(self):
        self.x = None
        self.y = None
        self.vitality = None 
        self.agility = None
        self.strength = None
        self.skill = None
        self.level = 1
        self.money = 0
        self.weapon = None
        self.armour = None
        self.job = None

    def setX(self, x):
        if x<=100 and x>=0:
            self.x = x
        else:
            if x<0:self.x = 0
            else: self.x = 100
        return self
    
    def setY(self, y):
        if y<=100 and y>=0:
            self.y = y
        else:
            if y<0:self.y = 0
            else: self.y = 100
        return self
    
    def setVital(self,vital):
        self.vitality = vital
        return self
    
    def setAgi(self,agi):
        self.agility = agi
        return self
    
    def setStrength(self,strength):
        self.strength = strength
        return self
    
    def Build(self):
        myHero = Hero(self.x, self.y, self.vitality, 
                      self.agility, self.strength
                      ,self.skill, self.level, self.money, 
                      self.weapon, self.armour, self.job)
        return myHero
    
    
    """
    Concrete Builder 1. warrior 2. archer
    """

class warriorBuilder(HeroBuilder):
        
    def __init__(self):
        super().__init__()
        self.weapon = 'sword'
        self.armour = 'heavy armour'
        self.job = 'warrior'
        self.skill = 'slash'

class archerBuilder(HeroBuilder):
        
    def __init__(self):
        super().__init__()
        self.weapon = 'bow'
        self.armour = 'light armour'
        self.job = 'archer'
        self.skill = 'blow'




class Monster(Actor):

    def __init__(self, x, y, vital, agi, strength, residence, color, itemDropRate):
        super().__init__(x,y,vital,agi,strength)

        self.residence = residence
        self.color = color
        self.itemDropRate = itemDropRate

    def printState(self):
        print(self.residence+"지역에서 몬스터 출몰")

    def getStat(self):
        return (self.x, self.y, self.vitality, self.agility,
                self.strength, self.residence, self.color, self.itemDropRate)
    
    def action(self):
        print(f"{self.strength} 데미지의 공격을 합니다.")
    
    def moveXY(self):
        print(f"몬스터가 x : {self.x} y : {self.y}로 이동합니다.")


import random

class MonsterBuilder():
    def __init__(self):
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.vitality = random.randint(50,100)
        self.agility = random.randint(50,100)
        self.strength = random.randint(50,100)
        self.residence = None
        self.color = None
        self.itemDropRate = None
    
    
    def Build(self):
        monster = Monster(self.x, self.y, 
                          self.vitality, self.agility, 
                          self.strength, self.residence, 
                          self.color, self.itemDropRate)
        return monster
    
class redMonsterBuilder(MonsterBuilder):
    def __init__(self):
        super().__init__()
        self.residence = 'volcano'
        self.color= 'red'
        self.itemDropRate = '0.01'

class blueMonsterBuilder(MonsterBuilder):
    def __init__(self):
        super().__init__()
        self.residence = 'ocean'
        self.color= 'blue'
        self.itemDropRate = '0.02'


warior = warriorBuilder().setX(-1).setY(110).setVital(20).setAgi(10).setStrength(20).Build()
# archer = archerBuilder().setX(110).setY(-10).setVital(15).setAgi(30).setStrength(15).Build()

# print('캐릭터 위치 조정')
# print(warior.getStat())
# print('')
# print(archer.getStat())

# print('')
# print('몬스터 생성')

# redMonster = redMonsterBuilder().Build()
# blueMonster = blueMonsterBuilder().Build()

# print(redMonster.getStat())
# print('')
# print(blueMonster.getStat())

# print(warior.getStat())
# warior.backMoveX()
# warior.moveXY()
# warior = warriorBuilder().setX(30).setY(30).setVital(20).setAgi(10).setStrength(20).Build()
# archer = archerBuilder().setX(10).setY(10).setVital(15).setAgi(30).setStrength(15).Build()

# archer.printState()
# print('')
# print('처음 index[0~1] 확인 위치 x=10, y=10')
# print(archer.getStat())
# print('')
# print('frontMoveY')
# archer.frontMoveY()
# archer.moveXY()
# print('')
# print('backMoveX')
# archer.backMoveX()
# archer.moveXY()

# print('')
# print('action func')
# archer.action()
# print('')
# print('levelUp func index[2~4]확인')
# print('전')
# print(archer.getStat())
# archer.levelUp()
# print('후')
# print(archer.getStat())

redMonster = redMonsterBuilder().Build()
print(redMonster.getStat())
redMonster.backMoveX()
redMonster.moveXY()
redMonster.frontMoveX()
redMonster.moveXY()
redMonster.action()