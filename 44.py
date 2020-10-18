# Create cages to put animals in
# Have ids for cages (don't need to enforce uniqueness)
import random, string

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

class Cage():

    def __init__(self):
        self.storage = []
        self.id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

    def __repr__(self):
        #print id number and animals in the cage
        output = f'Cage id {self.id} has:' 
        output += " ".join('\n\t\t' + x.species for x in self.storage)
        return output

    def add_animals(self, *animals):
        for animal in animals:
            self.storage.append(animal)


if __name__ == "__main__":
    sheep = Sheep('black')
    wolf = Wolf('black')
    snake = Snake('black')
    parrot = Parrot('black')

    cage = Cage()
    cage.add_animals(sheep, wolf, snake, parrot)
    print(cage)
