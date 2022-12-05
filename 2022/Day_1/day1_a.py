# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = [int(line) for line in file.readlines()]