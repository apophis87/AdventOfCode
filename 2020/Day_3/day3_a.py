# Get the map
map = []
with open('map.txt') as file:
    for line in file.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        map.append(list(line))

# Checking the trees in a loop
counter = 0
k = 0
for i in range(len(map)-1):
    if map[i+1][(k+3) % len(map[0])] == '#':
        counter = counter + 1
    k = k + 3

print(counter)
