# Create Class Circle
# It will cycle through for num number of times


class Circle:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.index = 0

    def __iter__(self):
        return self


# We failed to define the class with a helper function.

class Circle:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num

    def __iter__(self):
        return CircleGenerator(self.seq, self.num)

class CircleGenerator:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.index = 0

    def __next__(self):
        if self.index >= self.num:
            raise StopIteration
        else:
            val = self.seq[self.index % len(self.seq)]
            self.index += 1
            return val

# Here's an alternative version where __iter__ returns a generator expression.

class Circle:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num

    def __iter__(self):
        n = len(self.seq)
        #needs to be x%n to prevent dviide by zero
        return (self.seq[x % n] for x in range(self.num))

if __name__ == "__main__":
    c = Circle('alpha', 20)
    for x in c:
        print(x)

        


