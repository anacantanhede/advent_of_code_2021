def main():
    bingo = BingoGame()
    with open("./input.txt", "r") as file:
        lottery = [int(x) for x in file.readline().split(",")]
        # skip empty line between lottery numbers and boards
        file.readline()

        b = []
        for line in file:
            if not (line.startswith("\n")):
                b.append(list(line.replace("\n", "").split()))
            elif line.startswith("\n") or len(b) == 5:
                bingo.add_bingo_board(BingoBoard(b))
                b = []
        # last empty line is being skipped, so force the last board to be added
        bingo.add_bingo_board(BingoBoard(b))

    for drawn_number in lottery:
        bingo.draw_number(int(drawn_number))
        if bingo.check_victory():
            print(bingo.calculate_score_last_win(int(drawn_number)))
            break


class BingoBoard:
    def __init__(self, numbers):
        self.board = []
        self.winning_board = False
        self.last_to_win = False

        for row_index, row in enumerate(numbers):
            for column_index, number in enumerate(row):
                self.board.append(
                    {
                        # number : match
                        int(number): False,
                        "row": row_index,
                        "column": column_index,
                    }
                )

    def __str__(self):
        board_str = ""
        for num in self.board:
            n, r, c = num.items()
            if c[1] == 4:
                board_str += f"{n[0]:2},{n[1]:2}\n"
            else:
                board_str += f"{n[0]:2},{n[1]:2}|"
        return board_str

    def draw_number(self, number):
        match = False
        match = [True for x in self.board if int(number) in x]
        if match:
            for num in self.board:
                if int(number) in num:
                    num[int(number)] = True

    def _check_matched_row(self):
        victory = False
        for i in range(5):
            temp = [list(x.values())[0] for x in self.board if x["row"] == i]
            victory = all(temp)
            if victory == True:
                break
        return victory

    def _check_matched_column(self):
        victory = False
        for i in range(5):
            victory = all([list(x.values())[0] for x in self.board if x["column"] == i])
            if victory:
                break
        return victory

    def check_victory(self, last_to_win_flag):
        # victory might be a row OR a column
        victory = any([self._check_matched_row(), self._check_matched_column()])
        if victory:
            self.winning_board = True
            self.last_to_win = last_to_win_flag
        return victory

    def is_winning_board(self):
        return self.winning_board

    def is_last_to_win(self):
        return self.last_to_win

    def calculate_score(self, last_drawn_number):
        unmarked_numbers = [
            int(list(x.keys())[0])
            for x in self.board
            if "False" == str(list(x.values())[0])
        ]

        return last_drawn_number * sum(unmarked_numbers)


class BingoGame:
    def __init__(self):
        self.boards = []

    def __str__(self):
        game_str = ""
        for b in self.boards:
            game_str += str(b)
            game_str += "----\n"
        return game_str

    def add_bingo_board(self, board):
        self.boards.append(board)
        return self.boards

    def draw_number(self, number):
        for board in self.boards:
            board.draw_number(int(number))

    def check_victory(self):
        # victory is only when the last board wins
        if self.num_boards_left() > 1:
            is_last_board = False
        else:
            is_last_board = True
        for board in self.boards:
            if not (board.is_winning_board()):
                board.check_victory(is_last_board)
        if self.num_boards_left() == 0:
            return True
        return False

    def calculate_score_last_win(self, last_drawn_number):
        for board in self.boards:
            if board.is_last_to_win():
                return board.calculate_score(last_drawn_number)

    def num_boards_left(self):
        boards_left = 0
        for board in self.boards:
            if not (board.is_winning_board()):
                boards_left += 1
        return boards_left


if __name__ == "__main__":
    main()
