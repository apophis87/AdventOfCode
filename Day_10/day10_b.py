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


# Go through the list recording differeces in sorted list
removables = []
for k in range(1, len(adapters)-1):
    diff = adapters[k + 1] - adapters[k - 1]
    if diff <= 3:
        removables.append(adapters[k])




total = 1
count = 1
print(removables)
removables.append(removables[-1]+4)
for l in range(len(removables)-1):
    if removables[l+1] - removables[l] <= 3:
        # print(removables[l+1])
        count = count + 1
    else:
        if count == 3:
            total = total * 7
        if count <= 2:
            total = total * 2**count

        count = 1


print(total)