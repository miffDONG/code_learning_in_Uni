"""
게임 내에서 사용하는 소모품을 prototype으로 구현

포션 : 
레드 - 체력 회복 
블루 - 마나 회복 

변하는 값 - 회복 종류, 회복 양, 가격, 병 모양
"""


import copy

class RecoveryPotion:
    def __init__(self):
        self.kind = None        
        self.color = None
        self.the_amount_of_recovery = None
        self.price = None
    
    def clone(self):
        return copy.deepcopy(self)
    
    def use(self):
        print(f"Recovery your {self.kind} by {self.the_amount_of_recovery}")

    def buy(self):
        print(f"buy {self.kind}Potion at {self.price}")


class vitalPotion(RecoveryPotion):
    def __init__(self):
        super().__init__()
        self.kind = 'vital'
        self.color = 'red'

class manaPotion(RecoveryPotion):
    def __init__(self):
        super().__init__()
        self.kind = 'mana'
        self.color = 'Blue'


RedPotion = vitalPotion()
smallRedPotion = RedPotion.clone()
smallRedPotion.the_amount_of_recovery = 70
smallRedPotion.price = 170

smallRedPotion2 = smallRedPotion.clone()

smallRedPotion.buy()
smallRedPotion.use()
print()

smallRedPotion2.buy()
print()

bigRedPotion = RedPotion.clone()
bigRedPotion.the_amount_of_recovery = 150
bigRedPotion.price = 250

bigRedPotion.buy()
bigRedPotion.use()
print()

BluePotion = manaPotion()
smallBluePotion = BluePotion.clone()
smallBluePotion.the_amount_of_recovery = 90
smallBluePotion.price = 190

smallBluePotion.buy()
smallBluePotion.use()