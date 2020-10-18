
# Write function that takes a string and translates it into Pig Latin
def pig_latin(s):
    if s[0] in 'aeiou':
        return s + 'way'

    else:
        return s[1:] +  s[0] + 'ay'
    #else if begins with other letter
        #take first letter, put at end, and add "ay"

# Things we could have done better
#  No need for else
#  F strings

# Instructor's version with f strings
def pig_latin_two(s):
    if s[0] in 'aeiou':
        return f'{s}way'
    return f'{s[1:]}{s[0]}ay'

if __name__ == "__main__":
    print('apple', pig_latin('apple'))
    print('car', pig_latin('car'))

    print('apple', pig_latin_two('apple'))
    print('car', pig_latin_two('car'))
