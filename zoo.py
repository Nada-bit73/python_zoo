
from bird import Bird
from cat import Cat
from dog import Dog


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_bird(self, name):
        self.animals.append(Bird(name))

    def add_cat(self, name):
        self.animals.append(Cat(name))

    def add_dog(self, name):
        self.animals.append(Dog(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for x in self.animals:
            x.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_bird("Nala")
zoo1.add_bird("Simba")
zoo1.add_cat("Rajah")
zoo1.add_cat("Shere Khan")
zoo1.add_dog("boboy")
zoo1.add_dog("coco")
zoo1.print_all_info()
