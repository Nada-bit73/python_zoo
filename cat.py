

from animals import Animals


class Cat(Animals):

    def __init__(self,name,age=3, healthLevel=0, happinessLevel=0):
        super().__init__(name,age,healthLevel, happinessLevel)
        self.healthLevel = 8
        self.happinessLevel = 4


    