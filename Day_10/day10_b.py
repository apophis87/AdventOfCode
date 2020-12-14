import itertools

adapters = []
with open('adapters.txt') as file:
    for line in file:
        adapters.append(int(line.split('\n')[0]))

# Add 0 to the list
adapters.append(0)
# Sort list
adapters.sort()
# Add last number (highest since the list is sorted) +3
adapters.append(adapters[-1] + 3)
print(adapters)
# Initial values of the differences
ones = 0
twos = 0
threes = 1  # because of the internal adapter having always three more

# Go through the list recording differeces in sorted list
removables = []
for k in range(1, len(adapters)-1):
    diff = adapters[k + 1] - adapters[k - 1]
    if diff <= 3:
        removables.append(adapters[k])
total = 0
print(removables)
for l in range(len(removables)):
    count = 0
    for item in itertools.combinations(removables, l):
        drop = False
        a = adapters.copy()
        for element in item:
            a.remove(element)
            # print('Remove ', element )
        # print(a)
        for s in range(len(a)-1):
            gap = a[s+1]-a[s]
            if gap > 3:
                drop = True
                break
        if drop == False:
            count = count + 1
    total = total + count
    print(len(removables)-l)
print(total)