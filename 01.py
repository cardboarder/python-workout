from random import randint

def guessing_game():
    #choose random integer between 1 and 100
    chosen = randint(0, 100)
    
    guess = None
    while not guess or guess != chosen:

        guess = int(input("Guess an integer between 0 and 100:"))

        if guess < chosen:
            print("Too low. Guess again.")

        elif guess > chosen:
            print("Too high. Guess again.")

        elif guess == chosen:
            print("Just right!")
            break

#the version (w/ mods) used in the book: uses f strings 
def guessing_game_solution():

    #choose random integer between 1 and 100
    chosen = randint(0, 100)
    
    while True:

        guess = int(input("Guess an integer between 0 and 100:"))

        if guess < chosen:
            print(f"Your guess of {guess} was too low. Guess again.")

        elif guess > chosen:
            print(f"Your guess of {guess} was too high. Guess again.")

        elif guess == chosen:
            print(f"Your guess of {guess} was just right!")
            break

if __name__ == "__main__":
    guessing_game_solution()


