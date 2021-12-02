# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = [(line.split()[0], int(line.split()[1])) for line in file.readlines()]

# Initial positions
horizontal_pos = 0
depth = 0


for direction, amount in input_data:
    if direction == "forward":
        horizontal_pos+= amount
    if direction == "up":
        depth -= amount
    if direction == "down":
        depth += amount


print(f"Final horizontal position: {horizontal_pos}")
print(f"Final depth: {depth}")
print(f"Advent of Code Day 2 Part 1 answer: {horizontal_pos*depth}")



