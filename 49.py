# 49 - Elapsed since
# Write a function whose argument must be iterable
# For each iteration, return a (x, y) tuple
    # x should be seconds since last iteration
        # first timing should be 0
    # y is the next item

from time import perf_counter, sleep

def iter_timer(iterable):
    for item in iterable:
        current_time = perf_counter()
        try:
            delta = current_time - last_time 
        except:
            delta = 0
        last_time = current_time 
        yield (delta, item)

# solution version

def elapsed_since(iterable):
    last_time = None
    for item in iterable:
        current_time = perf_counter()
        # i didn't know you could do this?
        delta = current_time - (last_time or current_time)
        last_time = current_time
        yield (delta, item)

for s in iter_timer('arosientaoiershdaio'):
    print(s)

for s in elapsed_since('arosientaoiershdaio'):
    print(s)
    sleep(1)

