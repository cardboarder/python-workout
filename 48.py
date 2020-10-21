# Iterator that goes through multiple iterables
# Use generator function to create a function that
# Takes directory as argument
# Each iteration, return a string representing one line from one file
# Skip/ignore errors

import os

def dir_lines(dirname):
    full_fnames = [os.path.join(dirname, fname) for fname in os.listdir(dirname)] 
    for fname in full_fnames:
        try:
            with open(fname, 'r') as f:
                for line in f.readlines():
                    yield line
        except OSError:
            pass

    return full_fnames


for line in dir_lines('.'):
    print(line)
