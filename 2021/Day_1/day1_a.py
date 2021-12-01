# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = [int(line) for line in file.readlines()]

count = 0
for i in range(1, len(input_data)):
    if input_data[i] > input_data[i - 1]:
        count += 1

print(count)
