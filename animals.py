

class Animals:
     
     
    def __init__(self,name,age, healthLevel, happinessLevel):
        self.name = name
        self.age = age
        self.healthLevel = healthLevel
        self.happinessLevel = happinessLevel
    
    #display_info method that shows the animal's name, health, and happiness. 
    def display_info(self):
        print(f"Name : {self.name} , age : {self.age} health Level : {self.healthLevel} , happinessLevel : {self.happinessLevel}")

    #It should also have a feed method that increases health and happiness by 10.
    def feed(self):
         self.healthLevel += 10
         self.happinessLevel += 10
         