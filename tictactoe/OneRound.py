from GameUtils import *


def play_round(game, player1, player2):
    game.current_mark = player1.my_mark
    game.board, game.current_row, game.current_column = play_turn(game, player1)
    if game.game_won():
        print_board(game.board)
        return {"game_state": True,
                "message": "O-s have won!"}

    elif game.game_tied():
        return {"game_state": True,
                "message": "It's a tie!"}

    game.current_mark = player2.my_mark
    game.board, game.current_row, game.current_column = play_turn(game, player2)
    if game.game_won():
        print_board(game.board)
        return {"game_state": True,
                "message": "X-s have won!"}

    elif game.game_tied():
        return {"game_state": True,
                "message": "It's a tie!"}

    else:
        return {"game_state": False,
                "message": "Nobody has won yet."}


def play_turn(game_in, player):
    print_board(game_in.board)
    print("Player: %s" % player.my_mark)
    row, column = player.make_move(game_in)
    game_in.board[row][column] = player.my_mark
    game_in.move_history[player.my_mark].append([row, column])
    return game_in.board, int(row), int(column)
