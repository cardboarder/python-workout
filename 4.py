
# Write a function that takes a hex number and returns decimal equivalent
def hex_output(hexnum):

    decnum = 0
    #goes from the ones place first
    for index, digit, in enumerate(reversed(str(hexnum))):

        decnum += 16**index * int(digit)


    return decnum

if __name__ == "__main__":
    print("Testing hex of 50 (should equal 80): ", hex_output(50))
    print("Testing hex of 200 (should equal 512): ", hex_output(200))
    print("Testing hex of 20 (should equal 32): ", hex_output(20))
