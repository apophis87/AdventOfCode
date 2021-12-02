# Get the map
map = []
with open('map.txt') as file:
    for line in file.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        map.append(list(line))

# Checking map method according to the slope provided
def checkSlopes(right, down):
    counter = 0
    k = 0
    for i in range(0, len(map)-1, down):
        if map[i+down][(k+right) % len(map[0])] == '#':
            counter = counter + 1
        k = k + right
    return counter

# Slopes to check
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

# Multiplying the number of trees
product = 1
for slope in slopes:
    product = product * checkSlopes(slope[0], slope[1])

print(product)
