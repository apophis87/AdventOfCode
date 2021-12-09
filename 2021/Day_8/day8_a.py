with open("input.txt") as file:
    input_data = file.readlines()
    input_data = [line.split('\n')[0] for line in input_data]

data = [(line.split(' | ')[0], line.split(' | ')[1]) for line in input_data]


unique_digit_lengths = [2, 4, 3, 7] # corresponding to digits 1, 4, 7, 8

unique_digits = 0   # how many digits in the output value are unique i.e 1, 4, 7, 8
for (_, output_values) in data:
    output = output_values.split(' ')
    for value in output:
        if len(value) in unique_digit_lengths:
            unique_digits += 1


print(unique_digits)