adapters = []
with open('adapters.txt') as file:
    for line in file:
        adapters.append(int(line.split('\n')[0]))

# Add 0 to the list
adapters.append(0)
# Sort list
adapters.sort()

# Initial values of the differences
ones = 0
twos = 0
threes = 1 # because of the internal adapter having always three more

# Go through the list recording differeces in sorted list
for k in range(len(adapters)-1):
    diff = adapters[k+1]-adapters[k]
    if diff == 1:
        ones = ones + 1
    if diff == 2:
        twos = twos + 1
    if diff == 3:
        threes = threes + 1

print('Result: ', ones*threes)
