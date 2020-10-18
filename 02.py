
# Create function that takes a sequence and returms the sum

def mysum(*args):
    total = 0
    for arg in args:
        total += arg 
    return total

# optional exercises
# reimplement the function so that it takes a list and an arbitrary number 
def mysum_two(numbers, start=0):
    for num in numbers:
        start += num
    return start

if __name__ == "__main__":
    print("Summing 1, 2, 3, 4 starting from 100:", mysum_two([1, 2, 3, 4], 100))
    
