from copy import deepcopy

grid = []
with open('seating_layout.txt') as file:
    for line in file.readlines():
        line = line.split('\n')[0]
        row = [i for i in line]
        grid.append(row)


# print(grid)

# if 'L' and no adjacent seats are occupied -> IT BECOMES OCCUPIED '#'
# if '#' and 4 or more adjacent seats are occupied -> the seat becomes empty
# '.' never changes in position (it is the floor)

def printGrid(grid):
    for row in grid:
        print(''.join(row))

def countOccupied(grid):
    occSeats = 0
    for row in grid:
        occSeats = occSeats + row.count('#')
    return occSeats

def checkSeats(grid, position):
    posRow = position[0]
    posCol = position[1]
    occupied = 0
    free = 0
    try:
        for c in range(posCol - 1, posCol + 2):
            if c >= 0 and c < len(grid[:][0]):
                for r in range(posRow - 1, posRow + 2):
                    if r >= 0 and r < len(grid):
                        if not (r == posRow and c == posCol):
                            if grid[r][c] == '#':
                                occupied = occupied + 1
                            if grid[r][c] == 'L':
                                free = free + 1
    except:
        pass

    return occupied, free


def evolveGrid(grid):
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for k in range(len(grid[0][:])):
            if grid[i][k] != '.':
                occ, free = checkSeats(grid, [i, k])
                if occ == 0 and grid[i][k] == 'L':
                    new_grid[i][k] = '#'
                elif occ >= 4 and grid[i][k] == '#':
                    new_grid[i][k] = 'L'
            else:
                new_grid[i][k] = '.'
    return new_grid


limit = 1000
while limit > 0:
    new_grid = evolveGrid(grid)
    if new_grid == grid:
        # printGrid(new_grid)
        # print(1000 -limit)
        break
    else:
        grid = deepcopy(new_grid)
    limit = limit - 1

printGrid(grid)
print('There are ', countOccupied(grid), ' occupied seats.')