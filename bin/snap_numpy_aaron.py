#!/usr/bin/env python3

import numpy as np
import time


def remove_evens(orig, even):
    a = np.array(orig)
    cleaned = np.delete(a, even)
    return cleaned


# the length of our input range
input_range = 10000000

# starting the timer
start_time = time.time()

# list comprehension to make our mega-list
original_list = [x for x in range(input_range)]

# list comprehension to make our evens list
evens_list = [x for x in range(10000000) if x % 2 == 0]

# calling the method to remove the evens from the original list.
evens_removed = remove_evens(original_list, evens_list)

# end timer
total_time = time.time() - start_time

print("we removed {0} even integers from a list generated with a length of {1} "
      "in {2} seconds. Numpy is fast!".format(len(evens_list), input_range, total_time))

print('\n')

time.sleep(2)
print('and if we want a sample of our list to validate numpy removed the evens?')
time.sleep(2)

print(evens_removed[:30])
