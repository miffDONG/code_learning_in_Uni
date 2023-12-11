import pygame
import MyVector as mv #vector 클래스

#딕셔너리. 색의 rgb를 value로 저장해 둠으로써 후에 사용하기 편함.
rgb = {
    'BLACK':(0, 0, 0),
    'WHITE':(255, 255, 255),
    'BLUE':(0, 0, 255),
    'GREEN':(0, 255, 0),
    'RED':(255, 0, 0),
    'YELLOW':(255,255,0)
}

"""
implementor

Actor class를 Base Class로 삼고 Hero, Enermy, NPC는 Actor class를 상속받아
각각 다른 역할을 가진 인터페이스를 구현한다.
"""
class Actor:
    
    def __init__(self, x, y):
        self.pos = mv.MyVector(x, y)
        self.name = ""
        self.skill = ""

    def setPos(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def move(self, delta):
        self.pos = self.pos + delta
    
    def setName(self, name):
        self.name = name
    
    def setSkill(self, skill):
        pass

#concrete implementor 1
class Hero(Actor):

    def setSkill(self, skill):
        self.skill = skill

#concrete implementor 2
class Enermy(Actor):

    def setSkill(self, skill):
        self.skill = skill


#concrete implementor 3
"""
NPC는 hero, enermy와 달리 공격을 하지 않고 quest를 준다.
다른 요소를 가진 객체여서 따로 quest를 설정해준다.
"""
class NPC(Actor):

    def __init__(self,x,y):
        super().__init__(x,y)
        self.quest = ""

    def setQuest(self, quest):
        self.quest = quest


#abstraction
"""
게임환경 설정. 
디스플레이 , 게임 플레이에 필요한 요소들을 포함.
"""
class GameFramework:

    def __init__(self):
        self.pygame = pygame
        self.screen = 0

        #스크린 크기
        self.nY = 0 
        self.nX = 0

        self.hero = 0 #기능을 실제로 수행하는 위임자

        print("init")

    def setDisplay(self, nX, nY): 
        self.nY = nY
        self.nX = nX
        self.screen = self.pygame.display.set_mode([self.nX, self.nY])
        self.pygame.display.set_caption("Prince") #게임창의 이름


    def setHero(self, hero:Actor):
        self.hero = hero

    def ready(self):
        self.pygame.init() #pygame 초기화

    # 다각형을 그리는 함수.
    def drawPolygon(self, color, points, thickness):
        self.pygame.draw.polygon(self.screen, color, points, thickness)

    # 캐릭터가 생성되는 위치인 0,0을 가리키는 삼각형 형성.
    def drawEdges(self):
        p1 = mv.MyVector(0, 0)
        p2 = mv.MyVector(0, 10)
        p3 = mv.MyVector(10, 0)
        
        self.drawPolygon(rgb["WHITE"], [p1.vec(), p2.vec(), p3.vec()], 1)

    # 게임 내에 구현되는 인스턴스 (hero, monster etc..)를 글로 나타냄.
    def printText(self, msg, color, pos):
        font= self.pygame.font.SysFont("consolas",20)
        textSurface     = font.render(msg,True, color, None) #self.pygame.Color(color)
        textRect        = textSurface.get_rect()
        textRect.topleft= pos
        self.screen.blit(textSurface, textRect)

    #게임 실행
    def launch(self):
        pass


"""
각 하위 concrete implement를 생성하는 property를 포함. bridge 역할로써 서로 연결한다.
GameFramework의 하위 class인 3개의 concrete Abstraction으로 기능의 다양성을 구현함.
pygame module을 사용해서 새로운 창에서 시작되는 게임을 실행시킴.
키보드 입력에 따른 변화를 포함.

screen color가 객체별로 구별되는 특성으로써 사용. 
"""

#refined abstraction 1
class WhiteGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(60) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: #alt + f4
                    print("종료")
                    done = True

                elif event.type == self.pygame.KEYDOWN: #키를 눌렀을때
                    print("key down")
                    if event.key == self.pygame.K_LEFT: #어떤키가 눌렸는가?
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                self.hero.move(delta) #주인공의 위치가 업데이트가 됨

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["WHITE"]) #특성을 살린 부분
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()


#refined abstraction 2
class BlackGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(30) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:
                    print("key up")
                    if event.key == self.pygame.K_LEFT:
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                self.hero.move(delta)

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["BLACK"]) #특성화된 부분
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()

#refined abstraction 3
class YellowGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(60) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: #alt + f4
                    print("종료")
                    done = True

                elif event.type == self.pygame.KEYDOWN: #키를 눌렀을때
                    print("key down")
                    if event.key == self.pygame.K_LEFT: #어떤키가 눌렸는가?
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                self.hero.move(delta) #주인공의 위치가 업데이트가 됨

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["YELLOW"]) #특성을 살린 부분
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()




"""
facade pattern

세부사항을 모두 포함 한 class를 생성해서 사용자는 쉽게 사용할 수 있도록 함.
display , hero , monster , npc 생성자 생성 후
launch 함수를 입력하면 각각 세부사항을 설정하고 게임 실행.

***
display 색은 외부에서 설정할 수 있도록 입력.
hero에 이름과 학번을 설정.
***
"""

class Game_launch():
    def __init__(self,displayColor):
        self.displayColor = displayColor
        self.hero = Hero(0,0)
        self.monster = Enermy(50,50)
        self.npc = NPC(10, 10)

    def launch(self):
        if self.displayColor == 'YELLOW':
            game = YellowGame()
        elif (self.displayColor == 'WHITE'):
            game = WhiteGame()
        elif (self.displayColor == 'BLACK'):
            game = BlackGame()

        game.ready()   
        game.setDisplay(1000, 700)
        game.drawEdges()


        self.hero.setName("kim hyundong")
        self.hero.setSkill("201901208")

        self.monster.setName("weak moster")
        self.monster.setSkill("hit the body")
        print('몬스터 이름 : ',self.monster.name)
        print('몬스터 스킬 : ',self.monster.skill)

        self.npc.setName("NPC")
        self.npc.setQuest("kill monster")
        print('npc 이름 : ',self.npc.name)
        print('npc 퀘스트 : ',self.npc.quest)
        print('npc 스킬 : ',self.npc.skill)

        game.setHero(self.hero)
        game.launch()





print("BLACK WHITE YELLOW 원하는 화면 색을 입력하세요")
color = input()

game = Game_launch(color)
game.launch()





