# List of days until each lanternfish creates a new lanternfish
# fishes = [3, 4, 3, 1, 2]

# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = file.read()

input_data = input_data.split(',')
fishes = [int(i) for i in input_data]

end_day = 80
for day in range(end_day - 1):
    for index, fish in enumerate(fishes):
        fishes[index] -= 1
    # print(fishes)

    new_fishes = 0
    for index, fish in enumerate(fishes):
        if fish == 0:
            fishes[index] = 7
            new_fishes += 1

    fishes.extend(new_fishes * [9])

print(len(fishes))

