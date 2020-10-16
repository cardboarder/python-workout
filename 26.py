# Write a function that takes a string in prefix notation (operator and two numbers)
# Parse output and produce appropriate output
# Assume only valid arguments
# Implement each operation as a separate function; don't use an if statement

from operator import add, sub, mul, truediv, mod, pow 

def calc(s):
    opmap = {'+':add , '-':sub , '*':mul , '/':truediv , '%':mod , '**':pow}
    args = s.split(' ')
    return opmap[args[0]](int(args[1]), int(args[2]))

# Things to do better:
#  Assign during split to make more readable
#  Didn't need to split on whitespace (does this automatically)
#  Format dict to be more readable

def calc_two(s):
    opmap = {'+':add , 
            '-':sub , 
            '*':mul , 
            '/':truediv , 
            '%':mod , 
            '**':pow}
    op, arg1, arg2 = s.split(' ')
    return opmap[op](int(arg1), int(arg2))
