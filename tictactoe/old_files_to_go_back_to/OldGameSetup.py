def new_game():
    if input("Type quit to quit the game or anything else to play again\n").lower() == "quit":
        return False
    else:
        return True


def setup_game():
    if input("Default setup is a 3 x 3 board where you need 3 in a row to win. "
             "Press c if you want to change this or anything else to continue.\n").lower() == "c":
        return configure_game()
    else:
        game = {"win_limit": 3,
                "rows": 3,
                "columns": 3,
                "current_row": "",
                "current_column": "",
                "current_mark": "",
                "board": []}
        game["board"] = build_board(game)
        return game


def configure_game():
    game = {"rows": int(input("How many rows do you want?")),
            "columns": int(input("How many columns do you want?")),
            "win_limit": int(input("How many in a row to win?")), "current_row": "", "current_column": "",
            "current_mark": "", "board": []}
    game["board"] = build_board(game)
    print("You will need %d in a row to win. " % game["win_limit"])
    return game


def build_board(game):
    for x in range(game["columns"] + 1):
        game["board"].append([" "] * (game["rows"] + 1))
    x_axis = ["*", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for row in game["board"]:
        game["board"][game["board"].index(row)][0] = str(len(game["board"]) - game["board"].index(row) - 1)
    for col_ind in range(len(game["board"][0])):
        game["board"][len(game["board"]) - 1][col_ind] = x_axis[col_ind]
    return game["board"]


def game_won_long(game):
    # Win in any row?
    game_state = check_win_long(game["board"], game["win_limit"], game["current_mark"], 0, 1)
    if not game_state:
        # Win in any column?
        game_state = check_win_long(game["board"], game["win_limit"], game["current_mark"], 1, 0)
        if not game_state:
            # Win in any / diagonal?
            game_state = check_win_long(game["board"], game["win_limit"], game["current_mark"], -1, 1)
            if not game_state:
                # win in any \ diagonal?
                game_state = check_win_long(game["board"], game["win_limit"], game["current_mark"], 1, 1)
                if game_state:
                    print("diagonal\\")
            else:
                print("diagonal/")
        else:
            print("column")
    else:
        print("row")
    return game_state


def check_win_long(board, win_limit, player, x_dir, y_dir):
    game_state = False
    for col_ind in range(len(board[0])):
        for row_ind in range(len(board)):
            counter = 0
            analysed_col = col_ind
            analysed_row = row_ind
            while 0 <= analysed_col < len(board[0]) and 0 <= analysed_row < len(board) \
                    and board[analysed_row][analysed_col] == player:
                counter += 1
                analysed_row += x_dir
                analysed_col += y_dir
                if counter == win_limit:
                    game_state = True
    return game_state


def game_won(game):
    # Win in row?
    game_state = check_consecutive(game, 0, 1)
    if not game_state:
        # Win in column?
        game_state = check_consecutive(game, 1, 0)
        if not game_state:
            # Win in / diagonal?
            game_state = check_consecutive(game, -1, 1)
            if not game_state:
                # Win in \ diagonal?
                game_state = check_consecutive(game, 1, 1)
                if game_state:
                    print("diagonal\\")
            else:
                print("diagonal/")
        else:
            print("column")
    else:
        print("row")
    return game_state


def check_consecutive(game, x_dir, y_dir):
    game_state = False
    board = game["board"]
    player = game["current_mark"]
    win_limit = game["win_limit"]
    current_row = game["current_row"]
    current_column = game["current_column"]


    d_bot = len(board) - current_row - 2
    d_left = current_column - 1
    d_right = len(board[0]) - current_column - 1
    d_top = current_row
    if (x_dir == 1 and y_dir == 1) or x_dir == 0 or y_dir == 0:
        start_distance = min(win_limit, d_top, d_left)
        end_distance = min(win_limit, d_bot, d_right)
        start_row = current_row - x_dir * min(win_limit, d_top, d_left)
        start_column = current_column - y_dir * min(win_limit, d_top, d_left)
        end_row = current_row + x_dir * min(win_limit, d_bot, d_right)
        end_column = current_column + y_dir * min(win_limit, d_bot, d_right)
    else:
        start_distance = min(win_limit, d_bot, d_left)
        end_distance = min(win_limit, d_top, d_right)
        start_row = current_row - x_dir * min(win_limit, d_bot, d_left)
        start_column = current_column - y_dir * min(win_limit, d_bot, d_left)
        end_row = current_row + x_dir * min(win_limit, d_top, d_right)
        end_column = current_column + y_dir * min(win_limit, d_top, d_right)
        # print("start row is: %d\nstart column is: %d\nend row is %d\nend column is: %d"
        #       % (start_row, start_column, end_row, end_column))
    start_row = current_row - x_dir * start_distance
    start_column = current_column - y_dir * start_distance
    end_row = current_row + x_dir * end_distance
    end_column = current_column + y_dir * end_distance



    # if x_dir == 0 or y_dir == 0:
    #     # print("one of %d and %d is 0" % (x_dir, y_dir))
    #     start_row = max(current_row - win_limit * x_dir, 0)
    #     end_row = min(current_row + win_limit * x_dir, len(board) - 2)
    #     start_column = max(current_column - win_limit * y_dir, 1)
    #     end_column = min(current_column + win_limit * y_dir, len(board) - 1)
    #     # print("start row is: %d\nstart column is: %d\nend row is %d\nend column is: %d"
    #     #       % (start_row, start_column, end_row, end_column))
    #
    # if abs(x_dir) == 1 and abs(y_dir) == 1:
    #     # print("%d and %d are either 1 or -1" % (x_dir, y_dir))
    #     d_bot = len(board) - current_row - 2
    #     d_left = current_column - 1
    #     d_right = len(board[0]) - current_column - 1
    #     d_top = current_row
    #     if x_dir == 1 and y_dir == 1:
    #         start_row = current_row - x_dir * min(win_limit, d_top, d_left)
    #         start_column = current_column - y_dir * min(win_limit, d_top, d_left)
    #         end_row = current_row + x_dir * min(win_limit, d_bot, d_right)
    #         end_column = current_column + y_dir * min(win_limit, d_bot, d_right)
    #     elif x_dir == -1 and y_dir == 1:
    #         start_row = current_row - x_dir * min(win_limit, d_bot, d_left)
    #         start_column = current_column - y_dir * min(win_limit, d_bot, d_left)
    #         end_row = current_row + x_dir * min(win_limit, d_top, d_right)
    #         end_column = current_column + y_dir * min(win_limit, d_top, d_right)
    #         # print("start row is: %d\nstart column is: %d\nend row is %d\nend column is: %d"
    #         #       % (start_row, start_column, end_row, end_column))

    counter = 0
    analysed_row = start_row
    analysed_col = start_column
    possibility = max(abs(end_row - analysed_row) + counter, abs(end_column - analysed_col) + counter) + 1
    # print("possible length of consecutive places at the start of this check is %d" % possibility)

    while possibility >= win_limit:
        if board[analysed_row][analysed_col] == player:
            print("yo")
            counter += 1
        else:
            print("ho")
            counter = 0
        analysed_row += x_dir
        analysed_col += y_dir
        possibility = max(abs(end_row - analysed_row) + counter, abs(end_column - analysed_col) + counter) + 1
        print(counter)
        print(possibility)
        if counter == win_limit:
            game_state = True
            break
    return game_state


def game_tied(board_in):
    for row in board_in:
        for column in row:
            if column == " ":
                return False
    return True
