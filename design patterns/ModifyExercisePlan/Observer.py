#import PlayerInform

class State:
    def genPlayer(self,trainer):
        print(f"Player 정보 생성 : {PlayerInform.player.getInfo()}")

    def update(self, trainer):
        print(f"Player 정보 업데이트 :{PlayerInform.player.getInfo()}\n")

class Trainer:
    def __init__(self):
        self.states = []

    def addState(self,state):
        self.states.append(state)

    def deleteState(self,state):
        self.states.remove(state)

    def notifyState(self):
        for st in self.states:
            st.update(self)

    def excute(self):
        self.notifyState()

trainer = Trainer()
state1=State()
state2=State()

trainer.addState(state1)
trainer.excute()