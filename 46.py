# Create your own implementation of enumerate, MyEnumerate

class MyEnumerate:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index  >= len(self.iterable):
            raise StopIteration
        else:
            tup = (self.index, self.iterable[self.index])
            self.index += 1
            return tup


if __name__ == "__main__":
    e = MyEnumerate('alphabet soup')
    for i, c in e:
        print(i, c)

        



