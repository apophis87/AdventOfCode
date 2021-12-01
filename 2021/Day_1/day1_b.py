# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = [int(line) for line in file.readlines()]

count = 0

new_data = []
for i in range(0, len(input_data)-(len(input_data) % 3)):
    new_data.append(input_data[i] + input_data[i+1] + input_data[i+2])

for i in range(1, len(new_data)):
    if new_data[i] > new_data[i - 1]:
        count += 1

print(count)
