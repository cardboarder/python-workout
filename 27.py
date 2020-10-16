import random

def create_password_generator(characters):
    #returns a function that takes integer argument
    def create_password(length):
        #takes integer and returns password of length x
        return ''.join([random.choice(characters) for x in range(length)])
    return create_password

if __name__ == "__main__":

    test_string = 'abcde'
    test_string2 = '1239048092#$(*@(#*@)@)(&$@$'

    mygen = create_password_generator(test_string)
    print(f"Generating pass from '{test_string}': {mygen(20)}")

    mygen = create_password_generator(test_string2)
    print(f"Generating pass from '{test_string2}': {mygen(5)}")
