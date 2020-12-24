nav = []
with open('navigation.txt') as file:
    for line in file:
        nav.append(line.split('\n')[0])

pos_North = 0
pos_East = 0
direction = [1, 0] # [east, north] = -[west, south]


def changeDir(current_dir, motion):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # [N, E, S, W]
    move_dir = 1
    if motion[0] == 'L':
        move_dir = -1
    move = int(motion[1:]) // 90
    new_dir_index = (directions.index(current_dir) + move_dir * move) % 4

    return directions[new_dir_index]


for motion in nav:
    print('Before', direction, ' E: ', pos_East, ' N: ', pos_North)
    print(motion)
    if motion[0] == 'E':
        pos_East = pos_East + int(motion[1:])
    if motion[0] == 'W':
        pos_East = pos_East - int(motion[1:])
    if motion[0] == 'N':
        pos_North = pos_North + int(motion[1:])
    if motion[0] == 'S':
        pos_North = pos_North - int(motion[1:])
    if motion[0] == 'R' or motion[0] == 'L':
        direction = changeDir(direction, motion)
    if motion[0] == 'F':
        pos_East = pos_East + direction[0] * int(motion[1:])
        pos_North = pos_North + direction[1] * int(motion[1:])
    print('After ', direction,' E: ', pos_East, ' N: ', pos_North)



print(abs(pos_North) + abs(pos_East))