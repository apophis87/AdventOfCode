# Binary Boarding

def checkSeating(seat):

    upper_row = 127
    lower_row = 0
    # Finding the row
    for i in range(7):
        if seat[i] == 'F':
            upper_row = upper_row - (upper_row-lower_row) // 2 - 1
        if seat[i] == 'B':
            lower_row = lower_row + (upper_row-lower_row) // 2 + 1

    # print(lower_row)
    upper_col = 7
    lower_col = 0
    # Finding the column
    for i in range(7, 10):
        if seat[i] == 'L':
            upper_col = upper_col - (upper_col-lower_col) // 2 - 1
        if seat[i] == 'R':
            lower_col = lower_col + (upper_col-lower_col) // 2 + 1

    # print(lower_col)

    seat_id = lower_row * 8 + lower_col
    # print(seat_id)

    return seat_id

# Open file with seating information
# and store the seat_id in a list
seat_ids = []
with open('seating.txt') as file:
    for line in file.readlines():
        seat_ids.append(checkSeating(line))

# Sort the list
seat_ids.sort()
# print(seat_ids)
# Go through the list checking for the missing seat
for i in range(1, len(seat_ids)-1):
    if seat_ids[i-1] == seat_ids[i] - 1:
        if seat_ids[i+1] == seat_ids[i] + 1:
            pass
        else:
            # print(seat_ids[i-1], seat_ids[i], seat_ids[i+1])
            if seat_ids[i-1] + 1 != seat_ids[i]:
                print(seat_ids[i-1] + 1)
            else:
                print(seat_ids[i+1] - 1)
