from random import randint

class Die():
    """模拟掷骰子"""

    def __init__(self):
        """初始化一颗骰子"""
        self.sides = 6

    def roll_die(self,times):
        """模拟掷骰子的过程"""
        self.times = times
        rolls = []
        for time in range(1,times+1):
            roll = randint(1,self.sides)
            rolls.append(roll)
        print(rolls)

roll_1 = Die()
roll_1.sides = 10
roll_1.roll_die(10)

roll_2 = Die()
roll_2.sides = 20
roll_2.roll_die(10)