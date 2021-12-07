# This code is copied from Lukasz Walczak and was not implemented by me

# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = file.read()
input_data = input_data.split(',')
list_of_fish = [int(i) for i in input_data]

print(list_of_fish)
print(len(list_of_fish))
print(max(list_of_fish))
print(min(list_of_fish))

fish_age = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for a in list_of_fish:
    if a == 1:
        fish_age[a] += 1
    elif a == 2:
        fish_age[a] += 1
    elif a == 3:
        fish_age[a] += 1
    elif a == 4:
        fish_age[a] += 1
    elif a == 5:
        fish_age[a] += 1

print(f'Day 0: {fish_age}')
number_of_days = 256
following_days = 0

while number_of_days > 0:
    following_days += 1
    to_be_born = fish_age[0]
    fish_age[0] = fish_age[1]
    fish_age[1] = fish_age[2]
    fish_age[2] = fish_age[3]
    fish_age[3] = fish_age[4]
    fish_age[4] = fish_age[5]
    fish_age[5] = fish_age[6]
    fish_age[6] = (fish_age[7] + to_be_born) # to_be_born from the original number of fishes
    fish_age[7] = fish_age[8]
    fish_age[8] = to_be_born

    print(f'Day: {following_days}: {fish_age}')
    fish_summary = 0
    for key in fish_age:
        fish_summary += fish_age[key]
    print(f'Fish summary: {fish_summary}')
    number_of_days -= 1
    # answerfor 256 days: 1675781200288
