# A = Rock
# B = Paper
# C = Scissors

# total score = sum score each round = shape selected + outcome of round (win, tie, lose)
# Points for outcomes:
# win = 6
# draw = 3
# lose = 0

# Dictionary for part 1
# X = throw rock
# Y = throw paper
# Z = throw scissors

points_dict_1 = {
    ('A', 'X'): 4,      # Rock + Rock           -> draw
    ('A', 'Y'): 8,      # Rock + Paper          -> win
    ('A', 'Z'): 3,      # Rock + Scissors       -> lose
    ('B', 'X'): 1,      # Paper + Rock          -> lose
    ('B', 'Y'): 5,      # Paper + Paper         -> draw
    ('B', 'Z'): 9,      # Paper + Scissors      -> win
    ('C', 'X'): 7,      # Scissors + Rock       -> win
    ('C', 'Y'): 2,      # Scissors + Paper      -> lose
    ('C', 'Z'): 6       # Scissors + Scissors   -> draw
}

# Dictionary for part 2
# x = need to lose
# y = need to draw
# z = need to win


points_dict_2 = {
    ('A', 'X'): 3,  # Rock + need to lose -> throw scissors
    ('A', 'Y'): 4,  # Rock + need to draw -> throw rock
    ('A', 'Z'): 8,  # Rock + need to win -> throw paper
    ('B', 'X'): 1,  # Paper + need to lose  -> throw rock
    ('B', 'Y'): 5,  # Paper + need to draw -> throw paper
    ('B', 'Z'): 9,  # Paper + need to win -> throw scissors
    ('C', 'X'): 2,  # Scissors + need to lose -> throw paper
    ('C', 'Y'): 6,  # Scissors + need to draw -> throw scissors
    ('C', 'Z'): 7   # Scissors + need to win -> throw rock
}

with open('input.txt') as file:
    # Read the values
    match_list_raw = file.read().splitlines()
    matches = [(match.split()[0], match.split()[1]) for match in match_list_raw]

    points_1 = [points_dict_1.get(match) for match in matches]
    print("Solution part 1: ", sum(points_1))

    points_2 = [points_dict_2.get(match) for match in matches]
    print("Solution part 2: ", sum(points_2))