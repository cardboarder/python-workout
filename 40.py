# Write class Bowl that takes scoops. 
# Running print on it should display the ice cream flavors in our bowl.

class Scoop:
    def __init__(self, _flavor):
        self.flavor = _flavor

class Bowl:
    def __init__(self, _scoops):
        self.max_scoops = 3
        self.scoops = []
        self.add_scoops(*_scoops)
   
    def __repr__(self):
        return "\n".join([scoop.flavor for scoop in self.scoops])

    def add_scoops(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)

# Reviewing the solution... 
# We confused class attributes with instance attributes
# Here we implement the correct version

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

if __name__ == "__main__":
    scoops = [Scoop(x) for x in ["pasta", "squid ink", "yellow", "a", "b", "c"]]
    bowl = Bowl(scoops)
    print(bowl)
