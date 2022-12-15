with open('input.txt') as file:
    # Read the values
    pairs = file.read().splitlines()

tot_fully_contained = 0 # how many assignment pairs does one range fully contain the other (part 1)
tot_overlapping = 0 # how many assignment pairs do the ranges overlap (part 2)

for pair in pairs:
    p1, p2 = pair.split(',')
    p1s, p1e = p1.split('-')
    p2s, p2e = p2.split('-')
    range_1 = set(range(int(p1s), int(p1e)+1))
    range_2 = set(range(int(p2s), int(p2e) + 1))

    # Check for subsets and count (part 1)
    if range_1.issubset(range_2) or range_2.issubset(range_1):
        tot_fully_contained += 1

    # Check and count overlapping -> intersection not empty
    if range_1.intersection(range_2):
        tot_overlapping += 1


print("Solution part 1: ",tot_fully_contained)
print("Solution part 2: ",tot_overlapping)





