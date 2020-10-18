#Exercises 43-45
# Zoo class containing animals
# Animals are a class. Same s.species and s.legs will be same for all animals but s.color will be different.
# Animals sometimes need to be housed with other animals

# Exercise 43
# Four animals: sheep, wolves, snake, parrots
# Create classes for each of these

class Animal:
    species = None
    legs = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"This animal is of species {self.species}. It has {self.legs} legs and is {self.color}."

class Sheep(Animal):
    species = "sheep"
    legs = 4
class Wolf(Animal):
    species = "wolf"
    legs = 4
class Snake(Animal):
    species = "snake"
    legs = 0
class Parrot(Animal):
    species = "parrot"
    legs = 2

# Lerner's solution
# He uses the class name for the species name.

class Animal_:
    def __init__(self, color, legs):
        self.species = self.__class__.__name__
        self.legs = legs
        self.color = color

    def __repr__(self):
        return f'{self.color}; {self.species}; {self.legs} legs'

class Sheep_(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

#...and so on. This seems more confusing to me, but maybe we will see later why this is useful.

if __name__ == "__main__":
    print(Sheep('black'))
    print(Wolf('black'))
    print(Snake('black'))
    print(Parrot('black'))
