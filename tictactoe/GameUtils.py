def print_board(board):
    print("\n")
    for row in board:
        if board.index(row) == len(board)-1:
            print(" "+"|".join(row))
        else:
            print(" "+"|".join(row))
            # print(" "+"--"*len(board[0]))
    print("\n")


def convert_to_index(row_in, column_in, board):
    try:
        column_index = board[len(board) - 1].index(column_in.upper())
    except ValueError:
        column_index = "no such row"
    row_index = "no such column"

    for j in range(len(board)):
        if board[j][0] + "" == row_in:
            row_index = j

    return row_index, column_index


def valid(row_in, column_in, board):
    if row_exists(row_in, board) and column_exists(column_in, board):
        return True
    return False


def row_exists(row_in, board):
    for row in board:
        if row[0] == row_in:
            return True
    return False


def column_exists(column_in, board):
    for column in board[len(board)-1]:
        if column == column_in.upper():
            return True
    return False


def read_int(message):
    i = input(message)
    while not i.isdigit():
        i = input("That is not valid. Please enter an integer")
    return int(i)
