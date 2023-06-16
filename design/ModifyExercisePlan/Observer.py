import PlayerInform
import Observer

class State:
    def update(self, trainer):
        if trainer.register == False:    
            print(f"Player 정보 생성 :")
            trainer.genInfo()
            trainer.register = True
        else:
            print(f"Player 정보 업데이트 :")
            trainer.changeInfo()

class Trainer:
    def __init__(self):
        self.states = []
        self.register = False

    def addState(self,state):
        self.states.append(state)

    def deleteState(self,state):
        self.states.remove(state)

    def notifyState(self):
        for st in self.states:
            st.update(self)

    def genInfo(self):
        pass 

    def changeInfo(self):
        pass

class PlayerAchive(Trainer):
    def __init__(self):
        super().__init__()
        self.success = False

    def setSuccess(self,Success):
        self.success = Success
        return self
    
    def genInfo(self):
        print("선수의 신체정보가 등록되었습니다. 계획을 작성합니다.")

    def changeInfo(self):
        print("선수의 신체정보가 변경되었습니다.")
        if self.success == False:
            print("아직 목표에 달성하지 못했습니다. 수정된 계획을 작성합니다.")
        else:
            print("목표에 달성했습니다. 고생하셨습니다.")


trainer = PlayerAchive()
state1=State()

trainer.addState(state1)
trainer.addState(state1)
trainer.notifyState()
