
# ask user how long it took (in minutes) to run 10km
# record
# keep asking until user inputs "<enter>"
# calculate and display average time
# display and exit
# catch any errors

# Q: How do we confirm input is equal to <enter>?
# A: We receive an empty string in taht case.

def display_mean(numlist):
    mean = sum(numlist) / len(numlist)
    print("Your average run time was: ", mean)
    return

def log_time():
    times = []
    while True:
        time = input("Enter 10km run time: ")
        if not time:
            if not times:
                print("No entries! Try again!")
            else:
                display_mean(times)
                break
        else:
            try:
                print(f"Recorded your time of {time} minutes!")
                times.append(float(time))
            except ValueError as e:
                print("That's not a valid number!")





if __name__ == "__main__":
    log_time()
