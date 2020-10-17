# Write a version BigBowl that inherits from Bowl and takes more scoops

class Scoop:
    def __init__(self, _flavor):
        self.flavor = _flavor

class Bowl:
    max_scoops = 3
    def __init__(self, _scoops):
        self.scoops = []
        self.add_scoops(*_scoops)
   
    def __repr__(self):
        return "\n".join([scoop.flavor for scoop in self.scoops])

    def add_scoops(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)

class BigBowl(Bowl):
    max_scoops = 5
    def __init__(self, _scoops):
        super().__init__(_scoops)

# Reviewing the solution... 
# The only difference is that we had to add super() because of how we set up Bowl to take scoops during initialization.

if __name__ == "__main__":
    scoops = [Scoop(x) for x in ["pasta", "squid ink", "yellow", "a", "b", "c"]]
    bowl = Bowl(scoops)
    bigbowl = BigBowl(scoops)
    print(bowl)
    print(bigbowl)
