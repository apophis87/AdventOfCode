# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input = [int(line) for line in file.readlines()]

# Go through the list to find the product of the two numbers adding up to 2020
for i in range(len(input)):
    for j in range(i+1, len(input)):
        if input[i]+input[j] == 2020:
            print(input[i]*input[j])

