def main():
    bingo = BingoGame()
    with open("./input.txt", "r") as file:
        lottery = [int(x) for x in file.readline().split(",")]
        # skip empty line between numbers and boards
        file.readline()

        b = []
        for line in file:
            if not (line.startswith("\n")):
                b.append(list(line.replace("\n", "").split()))
            elif line.startswith("\n") or len(b) == 5:
                bb = BingoBoard(b)
                bingo.add_bingo_board(bb)
                b = []
        # last empty line is being skipped, so force the last board to be added
        bingo.add_bingo_board(BingoBoard(b))

        for drawn_number in lottery:
            bingo.draw_number(int(drawn_number))
            if bingo.check_victory():
                print("THERE IS A WINNER AFTER NUMBER: ", drawn_number)
                print(bingo.calculate_score(drawn_number))
                break


class BingoBoard:
    def __init__(self, numbers):
        self.board = []

        for row_index, row in enumerate(numbers):
            for column_index, number in enumerate(row):
                self.board.append(
                    {
                        # number / match
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

    def check_victory(self):
        # victory might be a row OR a column
        return any([self._check_matched_row(), self._check_matched_column()])

    def calculate_score(self, last_drawn_number):
        if self.check_victory():
            unmarked_numbers = [
                int(list(x.keys())[0])
                for x in self.board
                if "False" == str(list(x.values())[0])
            ]

        return last_drawn_number * sum(unmarked_numbers)


class BingoGame:
    drawn_numbers = []

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
        for board in self.boards:
            if board.check_victory():
                return True
        return False

    def calculate_score(self, last_drawn_number):
        for board in self.boards:
            if board.check_victory():
                return board.calculate_score(last_drawn_number)
        return None


if __name__ == "__main__":
    main()
