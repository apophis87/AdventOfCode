# Reading puzzle input and formatting data to be used in the program
with open('input.txt') as file:
    input_data = file.readlines()

input_data = [i.split('\n')[0] for i in input_data] # remove EOL char

lines = []
for item in input_data:
    start_point, end_point = item.split(' -> ')
    x1_char, y1_char = start_point.split(',')
    x2_char, y2_char = end_point.split(',')
    lines.append([int(x1_char), int(y1_char), int(x2_char), int(y2_char)])


# Extracting orthogonal lines from list
orthogonal_lines = []
for item in lines:
    if item[0] == item[2] or item[1] == item[3]:
        orthogonal_lines.append(item)

# Extracting diagonal lines at 45 deg from list
diagonal_lines = []
for item in lines:
    # For 45 deg absolute difference for x and y must be same
    if abs(item[0]-item[2]) == abs(item[1]-item[3]):
        diagonal_lines.append(item)

# Define an empty map with zeros (list of list)
map_size = 1000
map_lines = []
for _ in range(map_size):
    map_lines.append(map_size * [0])

# Determine all the points in between the given start and end points for each line
orthogonal_lines_points = []
for item in orthogonal_lines:
    [x1, y1, x2, y2] = item
    if x1 == x2:
        line_points = [(x1, y) for y in range(min(y1, y2), max(y1, y2)+1)]
    if y1 == y2:
        line_points = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    orthogonal_lines_points.append(line_points)

# Determine all the points in between the given start and end points for each line for diagonal lines
diagonal_lines_points = []
for item in diagonal_lines:
    [x1, y1, x2, y2] = item
    if x1 < x2:
        x_points = [x for x in range(x1, x2 + 1)]
    if x1 > x2:
        x_points = [x for x in range(x2, x1 + 1)]
        x_points.reverse()
    if y1 < y2:
        y_points = [y for y in range(y1, y2 + 1)]
    if y1 > y2:
        y_points = [y for y in range(y2, y1 + 1)]
        y_points.reverse()

    diagonal_lines_points.append(zip(x_points, y_points))


# Increase count at each line point coordinate on the map map_lines
for line in orthogonal_lines_points:
    for point in line:
        map_lines[point[0]][point[1]] += 1

for line in diagonal_lines_points:
    for point in line:
        map_lines[point[0]][point[1]] += 1

# # Show map
# import numpy as np
# f = np.array(map_lines)
# import matplotlib.pyplot as plt
# plt.imshow(f, origin='upper')
# plt.colorbar()
# plt.show()

# Count overlapping points
overlaps = 0
for row in range(map_size):
    for column in range(map_size):
        if map_lines[row][column] > 1:
            overlaps += 1

print(overlaps)
