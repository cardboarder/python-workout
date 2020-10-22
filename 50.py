# implement generator function called mychain
# that does what itertools.chain does

def mychain(*args):
    for iterable in args:
        for item in iterable:
            yield item


if __name__ == "__main__":

    x = mychain('1234', 'alphabet', dict(x=1, y=2, z=3))
    for item in x:
        print(item)
