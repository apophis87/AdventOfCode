with open("input_test.txt") as file:
    grid = [line.split('\n')[0] for line in file.readlines()]

X_MAX = len(grid[0])
Y_MAX = len(grid)

evaluated_positions = {}
tot = 0


def cost(pos_x, pos_y):
    global tot
    global grid

    if (pos_x, pos_y) in evaluated_positions:
        return evaluated_positions.get((pos_x, pos_y))

    if (pos_x, pos_y) == (X_MAX - 1, Y_MAX - 1):
        return int(grid([pos_x][pos_y]))

    if 0 <= pos_x < X_MAX and 0 <= pos_y < Y_MAX:
        tot_cost = int(grid[pos_x][pos_y]) + min(cost(pos_x - 1, pos_y), cost(pos_x + 1, pos_y), cost(pos_x, pos_y - 1),
                                                 cost(pos_x, pos_y + 1))
        evaluated_positions[(pos_x, pos_y)] = tot_cost
        return tot_cost


if __name__ == '__main__':
    print(cost(0, 0))