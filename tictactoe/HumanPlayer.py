from GameUtils import *


class HumanPlayer:

    def __init__(self, my_mark):
        self.my_mark = my_mark

    def make_move(self, game_in):
        move = input("What's your move? (in form A1)\n")

        while not (2 <= len(move) <= 4) or not valid(move[1], move[0], game_in.board):
            print("This is your move: " + move.upper())
            move = input("That's not valid. Please enter move in the form A1.\n")

        move_row, move_column = convert_to_index(move[1], move[0], game_in.board)

        while not HumanPlayer.empty(move_row, move_column, game_in.board):
            print("This is your move: " + move.upper())
            move = input("That space is already occupied. Please enter a different move.\n")
            move_row, move_column = convert_to_index(move[1], move[0], game_in.board)

        return move_row, move_column

    @staticmethod
    def empty(row_in, column_in, board_in):
        if board_in[row_in][column_in] == " ":
            return True
