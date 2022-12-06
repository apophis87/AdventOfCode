# A = Rock
# B = Paper
# C = Scissors
#
# X = Rock
# Y = Paper
# Z = Scissors
#
# total score = sum score each round = shape selected (X, Y, Z) + outcome of round (win, tie, lose)
# points for shapes:
# rock = 1
# paper = 2
# scissors = 3
#
# points for outcomes:
# win = 6
# draw = 3
# lose = 0

# Define dictionary with combinations and points

points_dict = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6
}

with open('input.txt') as file:
    # Read the values
    match_list_raw = file.read().splitlines()
    matches = [(match.split()[0], match.split()[1]) for match in match_list_raw]

    points = [points_dict.get(match) for match in matches]
    print("Solution part 1: ", sum(points))