

from animals import Animals


class Bird(Animals):

#In at least one of the Animal child classes you've created, add at least one unique attribute.
#Give each animal different default levels of health and happiness
    def __init__(self,name,color="green",age=2, healthLevel=0, happinessLevel=0):
        super().__init__(name,age,healthLevel, happinessLevel)
        self.color = color
        self.healthLevel = 4
        self.happinessLevel = 5

    