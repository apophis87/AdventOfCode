from math import radians, sin, cos

nav = []
with open('navigation.txt') as file:
    for line in file:
        nav.append(line.split('\n')[0])


waypoint_north = 1
waypoint_east = 10
pos_North = 0
pos_East = 0
direction = [1, 0] # [east, north] = -[west, south]


def changeDir(vector, motion):
    angle = radians(int(motion[1:]))
    if motion[0] == 'R':
        angle = (-1) * angle

    way_east = vector[0] * round(cos(angle)) - vector[1] * round(sin(angle))
    way_north = vector[0] * round(sin(angle)) + vector[1] * round(cos(angle))

    return way_east, way_north


for motion in nav:
    # print('Before  pE: ', pos_East, 'pN: ', pos_North, 'wpE: ', waypoint_east, 'wpN: ', waypoint_north)
    # print(motion)
    if motion[0] == 'E':
        waypoint_east = waypoint_east + int(motion[1:])
    if motion[0] == 'W':
        waypoint_east = waypoint_east - int(motion[1:])
    if motion[0] == 'N':
        waypoint_north = waypoint_north + int(motion[1:])
    if motion[0] == 'S':
        waypoint_north = waypoint_north - int(motion[1:])
    if motion[0] == 'R' or motion[0] == 'L':
        waypoint_east, waypoint_north = changeDir([waypoint_east, waypoint_north], motion)
    if motion[0] == 'F':
        pos_East = pos_East + waypoint_east * int(motion[1:])
        pos_North = pos_North + waypoint_north * int(motion[1:])
    # print('After  pE: ', pos_East, 'pN: ', pos_North, 'wpE: ', waypoint_east, 'wpN: ', waypoint_north)


print(abs(pos_North) + abs(pos_East))