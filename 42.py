# Exercise 42: FlexibleDict

# Create a FlexibleDict class that inherits from dict
# Will convert str to int and int to str before giving up


class FlexibleDict(dict):

    def __getitem__(self, key):

        try:
            if key in self: 
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        return dict.__getitem__(self, key)


if __name__ == "__main__":

    d = FlexibleDict()
    d['1'] = 100
    d[2] = 2
    print(d[1], d['2'])
