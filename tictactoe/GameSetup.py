from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from GameUtils import read_int
from Game import Game


def new_game():
    if input("Type quit to quit the game or anything else to play again\n").lower() == "quit":
        return False
    else:
        return True


def setup_game():
    if input("Default setup is a 3 x 3 board where you need 3 in a row to win. "
             "Press c if you want to change this or press enter else to continue.\n").lower() == "c":
        game = configure_game()
    else:
        game = Game(3, 3, 3, "", "", "", "")
        game.board = game.build_board()

    player1 = choose_player(input("Is the first player a computer player ('c') or a human player ('h')"), "O", "X")
    player2 = choose_player(input("Is the second player a computer player ('c') or a human player ('h')"), "X", "O")
    return game, player1, player2


def choose_player(kind, my_mark, their_mark):
    if kind == "h":
        return HumanPlayer(my_mark)
    elif kind == "c":

        # Currently available difficulties are:
        diff_low = 1
        diff_high = 2

        difficulty = read_int(
            "How clever do you want the computer to be? "
            "(1 and 2 i.e. stupid & slightly less so are the only current options)")

        while not diff_low <= difficulty <= diff_high:
            difficulty = read_int(
                "That is not a valid option. Please enter a number between %d and %d" % (diff_low, diff_high))
        return ComputerPlayer(my_mark, their_mark, difficulty)
    else:
        print("Error with option, returning human player as default")
        return HumanPlayer(my_mark)


def configure_game():
    game = Game(read_int("How many in a row to win?"), read_int("How many rows do you want?"),
                read_int("How many columns do you want?"), "", "", "", "")
    game.board = game.build_board()
    print("You will need %d in a row to win. " % game.win_limit)
    return game
