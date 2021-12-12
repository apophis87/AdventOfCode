import numpy as np

with open("input.txt") as file:
    input_data = [line.split('\n')[0] for line in file.readlines()]
    input_data = [[int(i) for i in list(item)] for item in input_data]
    map2d = np.matrix(input_data)


def get_adjacent_values(matrix, row, column):

    adjacent_values = []
    row_max, column_max = matrix.shape
    # Get left value if column not first
    if column != 0:
        adjacent_values.append(matrix[row, column-1])
    # Get right value if column not last
    if column != column_max-1:
        adjacent_values.append(matrix[row, column+1])
    # Get up value if row not first
    if row != 0:
        adjacent_values.append(matrix[row-1, column])
    # Get down value if row not last
    if row != row_max-1:
        adjacent_values.append(matrix[row+1, column])

    return adjacent_values


if __name__ == '__main__':

    risk_levels_sum = 0

    rows, cols = map2d.shape
    for row in range(rows):
        for col in range(cols):
            adjacent = get_adjacent_values(map2d, row, col)
            if map2d[row, col] < min(adjacent):
                risk_levels_sum += map2d[row, col] + 1

    print(risk_levels_sum)

