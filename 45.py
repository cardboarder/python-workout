#
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

class Zoo:
    def __init__(self):
        self.cages = []
        
    def __repr__(self):
        #print all cages (so we need to invoke the print from our other function?)
        #return "hello"
        return '\n'.join(str(x) for x in self.cages)

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def animals_by_color(self, color):
        hits = []
        for cage in self.cages:
            for animal in cage.storage:
                if animal.color == color:
                    hits.append(animal.species)
        return hits

    def animals_by_legs(self):
        #get total leg count
        legs = 0
        for cage in self.cages:
            for animal in cage.storage:
                legs += animal.legs
        return legs

# After reviewing solution, here's a version with nested list comprehension
# Much less code needed and still very readable.

class Zoo:
    def __init__(self):
        self.cages = []
        
    def __repr__(self):
        return '\n'.join(str(x) for x in self.cages)

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def animals_by_color(self, color):
        return [animal.species
                for cage in self.cages
                for animal in cage.storage
                if animal.color == color]

    def animals_by_legs(self):
        return sum(animal.legs
                for cage in self.cages
                for animal in cage.storage)

if __name__ == "__main__":
    sheep = Sheep('black')
    wolf = Wolf('black')
    snake = Snake('black')
    parrot = Parrot('black')

    cage1 = Cage()
    cage2 = Cage()
    cage1.add_animals(sheep, wolf)
    cage2.add_animals(snake, parrot)

    z = Zoo()
    z.add_cages(cage1, cage2)

    print(z)
    print(z.animals_by_color('black'))
    print(z.animals_by_legs())


