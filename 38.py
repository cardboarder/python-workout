
# Define a class Scoop that that has single attribute 'flavor'

class Scoop:

    def __init__(self, _flavor):
        self.flavor = _flavor


# Create a function that creates and returns three instances of Scoop class

def create_scoops(scoop_names):
    #assumes list of scoop name strings
    return [Scoop(flavor) for flavor in scoop_names]

if __name__ == "__main__":
    
    scoops = create_scoops(["pasta", "squid ink", "yellow"])
    for i, scoop in enumerate(scoops):
        print(f"The flavor of scoop no. {i} is {scoop.flavor}")

