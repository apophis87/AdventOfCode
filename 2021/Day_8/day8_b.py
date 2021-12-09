# Function for finding a wire mapping dictionary given the unique pattern
def find_digits(unique_pattern):
    # unique lenghts 2, 4, 3, 7 (keys) map to 1, 4, 7, 8 (values)
    unique_lengths_values = {
        2: '1',
        4: '4',
        3: '7',
        7: '8'
    }
    # mapping of digits to letters
    segment_map = {}
    # Temporary lists for processing items of lengths 5 and 6
    digits_len5 = []
    digits_len6 = []

    # Split the unique pattern string to a list
    unique_pattern = unique_pattern.split()
    for value in unique_pattern:
        if len(value) in unique_lengths_values:
            # construct the mapping of the digits to the letters using the unique length
            segment_map[unique_lengths_values[len(value)]] = value
        # store values with lengths 5 and 6 for further processing
        if len(value) == 5:
            digits_len5.append(value)
        if len(value) == 6:
            digits_len6.append(value)

    # Process items of lengths five (there are 3), which can only be digits 2, 3 or 5
    for item in digits_len5:
        # if item of length 5 contains letters of digit 1, then it is digit 3
        if set(segment_map['1']).issubset(set(item)):
            segment_map['3'] = item
        # if the difference of letters in digit 4 and 1 is a subset of the item, then it is a 5
        elif (set(segment_map['4']) - set(segment_map['1'])).issubset(set(item)):
            segment_map['5'] = item
        # last and only option is that the element is the digit 2
        else:
            segment_map['2'] = item

    # Process items of lengths six (there are 3), which can be only digits 0, 6 or 9
    # Find firstly digit 9 and remove it from the list, so that in the remaining 2 items
    # corresponding to digits 0 and 6, digit 0 can be found by checking if it contains the letters of digit 1
    for item in digits_len6:
        # if the letters of digit 4 are contained in the item, then it is a 9
        if set(segment_map['4']).issubset(set(item)):
            segment_map['9'] = item
            digits_len6.remove(item)

    for item in digits_len6:
        if set(segment_map['1']).issubset(set(item)):
            segment_map['0'] = item
        else:
            segment_map['6'] = item

    # Swap key value pairs for finding a digit given letters
    segment_map = {value: key for key, value in segment_map.items()}

    return segment_map


# This function finds the number from the output values (string) and a wire mapping (segment map)
def get_output_value(output_values, wire_mapping):
    output_number = []
    for output in output_values.split():
        for key in wire_mapping:
            if set(output) == set(key):
                output_number.append(wire_mapping[key])

    return int(''.join(output_number))


if __name__ == '__main__':
    with open("input.txt") as file:
        input_data = file.readlines()
        input_data = [line.split('\n')[0] for line in input_data]

    pattern_output_data = [(line.split(' | ')[0], line.split(' | ')[1]) for line in input_data]

    total = 0

    for item in pattern_output_data:
        unique_pattern = item[0]
        output_values = item[1]

        wire_mapping = find_digits(unique_pattern)
        total += get_output_value(output_values, wire_mapping)
    print(total)
