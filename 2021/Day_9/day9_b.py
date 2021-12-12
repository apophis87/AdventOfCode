import numpy as np

with open("input.txt") as file:
    input_data = [line.split('\n')[0] for line in file.readlines()]
    input_data = [[int(i) for i in list(item)] for item in input_data]
    map2d = np.matrix(input_data)


def get_adjacent_values(matrix, row, column):
    adjacent_values = {'left': 9, 'right': 9, 'up': 9, 'down': 9}

    row_max, column_max = matrix.shape
    # Get left value if column not first
    if column > 0:
        adjacent_values['left'] = matrix[row, column - 1]
    # Get right value if column not last
    if column < column_max - 1:
        adjacent_values['right'] = matrix[row, column + 1]
    # Get up value if row not first
    if row > 0:
        adjacent_values['up'] = matrix[row - 1, column]
    # Get down value if row not last
    if row < row_max - 1:
        adjacent_values['down'] = matrix[row + 1, column]

    return adjacent_values


def find_basin(value_to_find, dictionary):
    keys_list = list(dictionary.keys())
    keys_list.reverse()

    for key in keys_list:
        print(f"Searching the value for key {key}")
        for value in dictionary[key]:
            print(f"Value is {value}")
            if value_to_find == value:
                print("Value found!")
                return key
        else:
            continue
    return None


if __name__ == '__main__':

    basins = {}
    basin_counter = 1

    rows, cols = map2d.shape
    for row in range(rows):
        for col in range(cols):
            # if value is 9, skip to next coordinate
            print(50 * "-")
            print(f"Processing row {row}, column {col}; value is {map2d[row, col]}")
            if map2d[row, col] != 9:
                # Get adjacent values
                adj = get_adjacent_values(map2d, row, col)
                print(f"Checking upper value: {adj['up']}")
                if adj['up'] == 9:
                    print("Upper value is 9! -> Checking left side.")
                    print(f"Left side is {adj['left']}")
                    if adj['left'] == 9:
                        print("Left side is 9! -> Make a new basin.")
                        basins[basin_counter] = []
                        basins[basin_counter].append((row, col))
                        basin_counter += 1
                        print(f"New counter is {basin_counter}. Basins are:")
                        print(basins)
                    else:
                        print("Left side is not 9. Find basin key of left side.")
                        # find in which basin the left value is part of and add it to that basin
                        basin_key = find_basin((row, col - 1), basins)
                        print("Basin key of left side is ", basin_key)
                        if basin_key:
                            basins[basin_key].append((row, col))
                            print(f"Added value {(row, col)} to basins dictionary at key {basin_key}")
                            print(basins)
                else:
                    print("Upper value is not 9.")
                    # add the the current (row, col) to the basin of the upper value
                    basin_key_up = find_basin((row - 1, col), basins)
                    if basin_key_up:
                        basins[basin_key_up].append((row, col))
                    # check the left value to the current (row, col)
                    if adj['left'] != 9:
                        # if not 9 find in which basin the left value is
                        basin_key_left = find_basin((row, col - 1), basins)
                        print(f"Value {row, col - 1} found in basin {basin_key_left}: {basins[basin_key_left]}.")
                        if basin_key_left and (basin_key_up != basin_key_left):
                            print(f"Basin key left is: {basin_key_left} and basin key up is {basin_key_up}.")
                            print("Removing left item from its basin and adding it to the basin of the upper element.")
                            basins[basin_key_up].extend(basins[basin_key_left])
                            # if the element removed from the basin of its left element was the last, remove that basin
                            if basins[basin_key_left]:
                                basins.pop(basin_key_left)
            else:
                print("Skipping this coordinate")

    # Find the 3 largest basins and multiply their sizes
    basin_size_list = []
    for basin_key in basins:
        basin_size_list.append(len(basins[basin_key]))
    # Sort the list according to sizes of basins
    basin_size_list.sort(reverse=True)
    answer = 1
    print(basin_size_list)
    for i in basin_size_list[0:3]:
        answer *= i

    print(answer)