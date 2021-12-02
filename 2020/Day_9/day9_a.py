# XMAS encryption:
# preamble 25 numbers
# any number after is a sum of any two numbers immediately previous to it
# the two numbers summed don't have the same value

import itertools
# Get the numbers into a list
xmas = []
with open('xmas.txt') as file:
    for line in file:
        xmas.append(int(line.split('\n')[0]))

# print(xmas[-1])
# Go through the list in a 25 items moving window
for i in range(25, len(xmas)):
    # Get the combinations
    com = itertools.combinations(xmas[i-25:i], 2)
    sums = []
    # Note all the sums in a list
    for val in com:
        sums.append(sum(val))
    # Check if the actual element is in the list of sums
    if xmas[i] not in sums:
        print(xmas[i])
        break




