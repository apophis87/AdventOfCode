with open('input.txt') as file:
    # Read the values
    rucksacks = file.read().splitlines()

    priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priorities_sum = 0

    for rucksack in rucksacks:
        compartment_1 = set(rucksack[0:len(rucksack)//2])
        compartment_2 = set(rucksack[len(rucksack)//2:])
        common_type = compartment_1.intersection(compartment_2).pop()

        priorities_sum = priorities_sum + priorities.find(common_type)+1

    print("Solution part 1: ", priorities_sum)

    # Part 2

    group_priorities = []
    counter = 0

    for rucksack in rucksacks:
        if counter == 0:
            item_types = set(priorities)

        item_types = item_types.intersection(rucksack)
        if counter == 2:
            group_priorities.append(item_types.pop())
            counter = 0
        else:
            counter += 1

    priorities_sum2 = 0
    for item in group_priorities:
        priorities_sum2 = priorities_sum2 + priorities.find(item) + 1

    print("Solution part 2: ", priorities_sum2)




