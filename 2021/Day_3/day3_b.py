# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    input_data = [line.split('\n')[0] for line in file.readlines()]


# This function computes which occurs more than the other per position
def most_of_bits(input_data):
    # Count bits in positions
    count = [0] * len(input_data[1])

    for row in input_data:
        for position, value in enumerate(row):
            count[position] += int(value)

    occurrences_list = [i / len(input_data) for i in count]
    return ['1' if i >= 0.5 else '0' for i in occurrences_list]


def least_of_bits(input_data):
    # Count bits in positions
    count = [0] * len(input_data[1])

    for row in input_data:
        for position, value in enumerate(row):
            count[position] += int(value)

    occurrences_list = [i / len(input_data) for i in count]
    return ['0' if i >= 0.5 else '1' for i in occurrences_list]


def apply_criteria(data, fun):
    for pos in range(len(data[1])):
        temp_list = []
        # print("Position ", pos)
        criteria_applied = fun(data)
        filter_for = criteria_applied[pos]
        # print("Filtering for ", filter_for)
        for item in data:
            if item[pos] == filter_for:
                # print("Item found: ",  item)
                temp_list.append(item)

        data = temp_list
        # print("Length of input data ", len(input_data))
        del temp_list

        if len(data) == 1:
            # print("One item remaining: ", input_data)
            break

        # print(40*"*")

    return int(data[0], 2)


if __name__ == '__main__':
    # life support rating = oxygen generator rating * co2 scrubber rating  lsr = ogr * csr
    ogr = apply_criteria(input_data, most_of_bits)
    csr = apply_criteria(input_data, least_of_bits)
    lsr = ogr * csr
    print(f"Advent of Code Day 3 Part 2 answer: {lsr}")



