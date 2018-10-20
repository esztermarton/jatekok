class Game:
    def __init__(self, win_limit, rows, columns, current_row, current_column, current_mark, usage):
        self.usage = usage
        self.board = []
        self.current_mark = current_mark
        self.current_column = current_column
        self.current_row = current_row
        self.move_history = {"X": [],
                             "O": []}
        self.columns = columns
        self.rows = rows
        self.win_limit = win_limit

    def build_board(self):
        for x in range(self.columns + 1):
            self.board.append([" "] * (self.rows + 1))
        x_axis = ["*", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for row in self.board:
            self.board[self.board.index(row)][0] = str(len(self.board) - self.board.index(row) - 1)
        for col_ind in range(len(self.board[0])):
            self.board[len(self.board) - 1][col_ind] = x_axis[col_ind]
        return self.board

    def game_won(self):
        # Win in row?
        game_state = Game.check_consecutive(self, 0, 1)
        if not game_state:
            # Win in column?
            game_state = Game.check_consecutive(self, 1, 0)
            if not game_state:
                # Win in / diagonal?
                game_state = Game.check_consecutive(self, -1, 1)
                if not game_state:
                    # Win in \ diagonal?
                    game_state = Game.check_consecutive(self, 1, 1)

        return game_state

    def check_consecutive(self, x_dir, y_dir):
        game_state = False

        start_row, start_column, end_row, end_column = self.setup_check(x_dir, y_dir)
        counter, analysed_row, analysed_col = 0, start_row, start_column
        possibility = max(abs(end_row - analysed_row) + counter, abs(end_column - analysed_col) + counter) + 1

        while possibility >= self.win_limit:
            # print("Currently analysed row is %d and analysed column is %d\n possibility is %d and win_limit is %d)" % (
            #     analysed_row, analysed_col, possibility, self.win_limit))
            if self.board[analysed_row][analysed_col] == self.current_mark:
                counter += 1
            else:
                counter = 0
            # print(counter)
            analysed_row += x_dir
            analysed_col += y_dir
            possibility = max(abs(end_row - analysed_row) + counter, abs(end_column - analysed_col) + counter) + 1
            if counter == self.win_limit:
                game_state = True
                break
        return game_state

    def check_in_line(self, x_dir, y_dir, mark, row_in=0, col_in=0):
        if col_in == 0:
            row_in = self.current_row
            col_in = self.current_column
        possible_next_low, possible_next_high = [], []
        # print("x_dir is %d, y_dir is %d" % (x_dir, y_dir))
        start_row, start_column, end_row, end_column = self.setup_check(x_dir, y_dir, row_in, col_in)
        # print("start row is %d, start column is %d\nend row is %d, end column is %d" % (
        #     start_row, start_column, end_row, end_column))
        counter, analysed_row, analysed_col, possible = 0, start_row, start_column, []
        # print("Analysed row is %d, analysed column is %d, win limit is %d" % (analysed_row, analysed_col, self.win_limit))
        # print(analysed_col + self.win_limit * y_dir - 1, end_column, analysed_row + self.win_limit * x_dir - 1, end_row)
        while analysed_col + self.win_limit * y_dir - 1 <= end_column and analysed_row + self.win_limit * x_dir - 1 <= end_row:
            # print("Now within while loop, analysed row is %d, analysed column is %d" % (analysed_row, analysed_col))
            for i in range(self.win_limit):
                print("i = %d, which is the pass number for a given analysed row/column" % i)
                x, y = analysed_row + i * x_dir, analysed_col + i * y_dir
                # print("row %d, column %d" % (x, y))
                if self.board[x][y] == mark:
                    counter += 1
                elif self.board[x][y] == " ":
                    possible.append([x, y])
                else:
                    counter = 0
                    break
                    # print("counter is %d\npossible places to place counter are as follows %s" % (counter, possible))
            print(possible)
            if counter + len(possible) == self.win_limit and len(possible) < 2:
                for those in possible:
                    possible_next_high.append(those)
            elif counter + len(possible) == self.win_limit:
                print("adding to possible_next_low")
                for those in possible:
                    possible_next_low.append(those)
            counter = 0
            possible = []
            analysed_col += y_dir
            analysed_row += x_dir
        return possible_next_low, possible_next_high

    def setup_check(self, x_dir, y_dir, row_in=0, col_in=1):
        d_bot = len(self.board) - row_in - 2
        d_left = col_in - 1
        d_right = len(self.board[0]) - col_in - 1
        d_top = row_in

        if x_dir == 1 and y_dir == 1:
            start_distance = min(self.win_limit, d_top, d_left)
            end_distance = min(self.win_limit, d_bot, d_right)
        elif x_dir == -1 and y_dir == 1:
            start_distance = min(self.win_limit, d_bot, d_left)
            end_distance = min(self.win_limit, d_top, d_right)
        elif x_dir == 0:
            start_distance = min(self.win_limit, d_left)
            end_distance = min(self.win_limit, d_right)
        elif y_dir == 0:
            start_distance = min(self.win_limit, d_top)
            end_distance = min(self.win_limit, d_bot)
        else:
            print("Error with start and end distance for consecutive check")
            start_distance = "Error"
            end_distance = "Error"

        start_row = row_in - x_dir * start_distance
        start_column = col_in - y_dir * start_distance
        end_row = row_in + x_dir * end_distance
        end_column = col_in + y_dir * end_distance
        return start_row, start_column, end_row, end_column

    def game_tied(self):
        for row in self.board:
            for column in row:
                if column == " ":
                    return False
        return True

