# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = [line.split('\n')[0] for line in file.readlines()]

# Gamma rate = most common bit in each position for all the binary numbers
# Epsilon rate = least common bit = inverse of gamma rate
# Power consumption is the multiplication of the decimal representations of gamma and epsilon rates

# Count bits in positions
count = [0]*len(input_data[1])

for row in input_data:
    for position, value in enumerate(row):
        count[position] += int(value)

occurrences_list = [i/len(input_data) for i in count] # ration of counted ones to total number of bits (lines in input)
gamma_list = [b'1' if i > 0.5 else b'0' for i in occurrences_list] # most common bit for each position
epsilon_list = [b'0' if i > 0.5 else b'1' for i in occurrences_list] # least common bit for each position
gamma = b''.join(gamma_list)    # joining list
epsilon = b''.join(epsilon_list)    # joining list
gamma_rate = int(gamma, 2) # converting to int
epsilon_rate = int(epsilon, 2) # converting to int

# Final answer
power_consumption = gamma_rate * epsilon_rate
print(f"Advent of Code Day 3 Part 1 answer: {power_consumption}")
