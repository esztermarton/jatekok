from HumanPlayer import HumanPlayer
from OneRound import *
from GameUtils import *
from Game import Game


def get_all_win_states(game_in):
    all_win_states = []
    win_state = []

    # create all rows

    for i in range(game_in.columns):
        for j in range(game_in.rows - game_in.win_limit + 1):
            for k in range(game_in.win_limit):
                position = [i, j + 1 + k]
                win_state.append(position)
            all_win_states.append(win_state)
            win_state = []

    # create all columns

    for i in range(game_in.rows):
        for j in range(game_in.columns - game_in.win_limit + 1):
            for k in range(game_in.win_limit):
                position = [j + k, i + 1]
                win_state.append(position)
            all_win_states.append(win_state)
            win_state = []

    # create diagonals \

    for i in range(game_in.rows - game_in.win_limit + 1):
        for j in range(game_in.columns - game_in.win_limit + 1):
            for k in range(game_in.win_limit):
                position = [j + k, i + k + 1]
                win_state.append(position)
            all_win_states.append(win_state)
            win_state = []

    # create diagonals /

    for i in range(game_in.rows - game_in.win_limit + 1):
        for j in range(game_in.columns - game_in.win_limit + 1):
            for k in range(game_in.win_limit):
                position = [len(game.board) - k - j - 2, i + k + 1]
                win_state.append(position)
            all_win_states.append(win_state)
            win_state = []

    # for win_state in all_win_states:
    #     print(win_state)

    return all_win_states


# Test a board

# Set up game without questions

player1 = HumanPlayer("O")
player2 = HumanPlayer("X")

game = Game(3, 4, 5, "", "", "", "")

game.board = game.build_board()

all_win_states = get_all_win_states(game)

# test win states

board_temp = game.board

for i in range(len(all_win_states)):
    for j in range(len(all_win_states[i])):
        game.board[all_win_states[i][j][0]][all_win_states[i][j][1]] = "O"
    game.current_row = all_win_states[i][0][0]
    game.current_column = all_win_states[i][0][1]
    game.current_mark = "O"
    # print_board(game.board)
    print(game.game_won())
    game.board = []
    game.board = game.build_board()
