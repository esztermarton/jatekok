import numpy as np


class ComputerPlayer:
    def __init__(self, my_mark, their_mark, strength):
        self.my_mark = my_mark
        self.their_mark = their_mark
        self.strength = strength
        self.memory_high_d = []
        self.memory_low_d = []
        self.memory_high_a = []
        self.memory_low_a = []

    def make_move(self, game_in):
        if self.strength == 1:
            move_row, move_column = ComputerPlayer.make_random_move(game_in.board)
        elif self.strength == 2:
            move_row, move_column = self.make_almost_random_move(game_in)
        else:
            move_row, move_column = "", ""
        return move_row, move_column

    def make_almost_random_move(self, game):
        if game.current_column == "":
            print(int(game.rows / 2), int(game.columns / 2 + 1))
            return int(game.rows / 2), int(game.columns / 2 + 1)
        else:
            self.check_for_obvious(game)
            print("High priority def:\n" + str(self.memory_high_d) + "\nLow priority def:\n" + str(self.memory_low_d))
            print("High priority off:\n" + str(self.memory_high_d) + "\nLow priority off:\n" + str(self.memory_low_d))
            if len(self.memory_high_d) > 0:
                self.my_last_move = self.memory_high_d[np.random.choice(len(self.memory_high_d))]
                self.memory_high_d = [x for x in self.memory_high_d if x != self.my_last_move]
                return self.my_last_move[0], self.my_last_move[1]
            elif len(self.memory_high_a) > 0:
                self.my_last_move = self.memory_high_a[np.random.choice(len(self.memory_high_a))]
                self.memory_high_a = [x for x in self.memory_high_a if x != self.my_last_move]
                return self.my_last_move[0], self.my_last_move[1]
            elif len(self.memory_low_a) > 0:
                self.my_last_move = self.memory_low_a[np.random.choice(len(self.memory_low_a))]
                self.memory_low_a = [x for x in self.memory_low_a if x != self.my_last_move]
                return self.my_last_move[0], self.my_last_move[1]
            elif len(self.memory_low_d) > 0:
                self.my_last_move = self.memory_low_d[np.random.choice(len(self.memory_low_d))]
                self.memory_low_d = [x for x in self.memory_low_d if x != self.my_last_move]
                return self.my_last_move[0], self.my_last_move[1]
            else:
                return ComputerPlayer.make_random_move(game.board)

    @staticmethod
    def make_random_move(board_in):
        random_row = np.random.randint(0, len(board_in) - 1)
        random_col = np.random.randint(1, len(board_in[0]))
        # print("This is your move: %s%s, from coordinates %d%d" % (
        #     board_in[len(board_in) - 1][random_col], board_in[random_row][0], random_row, random_col))

        while not ComputerPlayer.empty(random_row, random_col, board_in):
            # print("This is not an empty spot unfortunately.")
            random_row = np.random.randint(0, len(board_in) - 1)
            random_col = np.random.randint(1, len(board_in[0]))
            # print_board(board_in)
            # print("This is your move: %s%s, from coordinates %d%d" % (
            #     board_in[len(board_in) - 1][random_col], board_in[random_row][0], random_row, random_col))
        print("Computer's move: %s%s" % (board_in[len(board_in) - 1][random_col], board_in[random_row][0]))
        return random_row, random_col

    @staticmethod
    def empty(row_in, column_in, board_in):
        if board_in[row_in][column_in] == " ":
            return True

    def check_for_obvious(self, game):
        mark = self.their_mark
        directions = [0, 1, 1, 0, -1, 1, 1, 1]
        for i in range(0, 8, 2):
            next_step_low, next_step_high = game.check_in_line(directions[i], directions[i + 1], mark)

            if len(next_step_high) != 0:
                for those in next_step_high:
                    self.memory_high_d.append(those)
            elif len(next_step_low) != 0:
                for those in next_step_low:
                    self.memory_low_d.append(those)
            else:
                print("error with check_in_row")

        mark = self.my_mark

        for mine in game.move_history[self.my_mark]:
            for i in range(0, 8, 2):
                next_step_low, next_step_high = game.check_in_line(directions[i], directions[i + 1], mark, mine[0],
                                                                   mine[1])

                if len(next_step_high) != 0:
                    for those in next_step_high:
                        self.memory_high_a.append(those)
                elif len(next_step_low) != 0:
                    for those in next_step_low:
                        self.memory_low_a.append(those)
                else:
                    print("error with check_in_row")
