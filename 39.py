# Write class Bowl that takes scoops. 
# Running print on it should display the ice cream flavors in our bowl.

class Scoop:
    def __init__(self, _flavor):
        self.flavor = _flavor

class Bowl:
    def __init__(self, _scoops):
        self.scoops = []
        self.add_scoops(*_scoops)
   
    def __repr__(self):
        return "\n".join([scoop.flavor for scoop in self.scoops])

    def test(self):
        return self.scoops
    def add_scoops(self, *new_scoops):
        for new_scoop in new_scoops:
            self.scoops.append(new_scoop)

# We did some weird thing with a unpack in the constructor. Not sure if that's the right way to do things.

if __name__ == "__main__":
    scoops = [Scoop(x) for x in ["pasta", "squid ink", "yellow"]]
    bowl = Bowl(scoops)
    print(bowl)
