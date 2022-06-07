

from animals import Animals


class Dog(Animals):

    def __init__(self,name,age=4, healthLevel=0, happinessLevel=0):
        super().__init__(name,age,healthLevel, happinessLevel)
        self.healthLevel = 5
        self.happinessLevel = 9

    #animals = Animals("doggy", 2, 7, 9)
    #animals.feed()



    