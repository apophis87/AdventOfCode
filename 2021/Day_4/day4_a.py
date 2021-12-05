# Read the list of drawn numbers
with open('numbers.txt') as file:
    drawn_numbers = file.readline().split(',')

# Read boards
with open('boards.txt') as file:
    boards = file.readlines()


# Make a list of lists in which each element contains the five bingo rows as lists
boards = [b.split('\n')[0] for b in boards]  # remove EOL character
boards = [b for b in boards if b != ''] # remove empty strings
boards = [b.split() for b in boards]  # list of lists
boards = [[int(i) for i in b] for b in boards] # typecast list elements to integers

boards_list = [] # list containing bingo boards
for i in range(int(len(boards)/5)):
    boards_list.append(boards[5*i: 5*i+5])


class Board:
    def __init__(self, board_list):
        self.board_list = board_list
        # 5 x 5 list with zeros for marking numbers
        self.board_check = []
        # Initialize with zeros
        for _ in range(0, 5):
            self.board_check.append(5 * [0])

    def check_board(self, number):
        for row_index, row in enumerate(self.board_list):
            for column_index, column in enumerate(row):
                if column == number:
                    self.board_check[row_index][column_index] = 1

    def check_bingo(self):
        # Checking rows
        for row in self.board_check:
            if sum(row) == 5:
                return True
            else:
                continue
        # Checking columns
        # Transposed board_check
        board_check_t = [list(i) for i in zip(*self.board_check)]
        for row in board_check_t:
            if sum(row) == 5:
                return True
            else:
                continue
        return False

    def sum_board(self):
        board_sum = 0
        for row_index, row in enumerate(self.board_check):
            for column_index, column in enumerate(row):
                if column == 0:
                    board_sum += self.board_list[row_index][column_index]

        return board_sum

    def print_board(self):
        print(8 * '*', " Bingo Board ", 7 * '*')
        for row in self.board_list:
            print(row)
        print(30 * '*')

    def print_check_board(self):
        for row in self.board_check:
            print(row)


if __name__ == '__main__':

    bingo_boards = []
    for board in boards_list:
        bingo_boards.append(Board(board))

    for number in drawn_numbers:
        for bingo_board in bingo_boards:
            bingo_board.check_board(int(number))
            if bingo_board.check_bingo():
                bingo_board.print_board()
                winning_board_sum = bingo_board.sum_board()
                break
        else:
            continue
        last_number = int(number)
        break

    print(last_number * winning_board_sum)
