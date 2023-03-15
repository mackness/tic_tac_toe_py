from enum import Enum


class TicTacToe:
    class Player(Enum):
        X = 0
        O = 1

    EMPTY_CELL = " "

    game_state = {
        "board": [
            [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
            [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
            [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        ],
        "has_winner": False,
        "current_player": Player.X,
    }

    def get_state(self, field):
        return self.game_state.get(field)

    def set_state(self, field, value):
        self.game_state[field] = value

    def parse_and_validate_input(self, move):
        result = move.split(",")
        row_index = int(result[0])
        col_index = int(result[1])
        max_index = len(self.get_state("board")) - 1
        min_index = 0
        if len(result) > 2:
            raise ValueError("Input must have a max length of 2")
        elif (
            row_index > max_index
            or row_index < min_index
            or col_index > max_index
            or col_index < min_index
        ):
            raise ValueError(
                "Input move is out of bounds please enter a value between 0 and 2 inclusive"
            )
        return [row_index, col_index]

    def print_board(self):
        for row in self.get_state("board"):
            print(row)

    def update_board(self, move):
        for row_index, row in enumerate(self.get_state("board")):
            for cell_index, _ in enumerate(row):
                if move[0] == row_index and move[1] == cell_index:
                    self.get_state("board")[row_index][
                        cell_index
                    ] = self.get_current_player()
                else:
                    pass

    def get_current_player(self):
        return self.get_state("current_player").name.lower()

    def toggle_player(self):
        if self.get_state("current_player") == self.Player.X:
            self.set_state("current_player", self.Player.O)
        else:
            self.set_state("current_player", self.Player.X)

    def check_winner(self):
        def check_horizontal():
            for row in self.get_state("board"):
                if self.list_cardinality_check(row):
                    return True

        def check_vertical():
            val_map = {0: [], 1: [], 2: []}
            for row_index, row in enumerate(self.get_state("board")):
                for col_index, _ in enumerate(row):
                    val_map.get(col_index).append(
                        self.get_state("board")[row_index][col_index]
                    )

            for key in val_map:
                if self.list_cardinality_check(val_map[key]):
                    return True
                else:
                    pass

            return False

        def check_diagonal():
            val_reuslt = []
            for row_index, row in enumerate(self.get_state("board")):
                for col_index, _ in enumerate(row):
                    if col_index == row_index:
                        val_reuslt.append(self.get_state("board")[row_index][col_index])

            return self.list_cardinality_check(val_reuslt)

        def check_reverse_diagonal():
            val_reuslt = []
            for row_index, row in enumerate(self.get_state("board")):
                for col_index, _ in enumerate(row):
                    if col_index == (row_index - (len(row) - 1)):
                        val_reuslt.append(self.get_state("board")[row_index][col_index])

            return self.list_cardinality_check(val_reuslt)

        return (
            check_horizontal()
            or check_vertical()
            or check_diagonal()
            or check_reverse_diagonal()
        )

    # check cardinality of a list ignoring EMPTY
    def list_cardinality_check(self, input_list):
        return len(set(input_list)) == 1 and set(input_list).pop() != self.EMPTY_CELL

    def start(self):
        self.print_board()

        while self.game_state.get("has_winner") == False:
            move = self.parse_and_validate_input(
                input(f"Enter your move player {self.get_current_player()}: ")
            )

            self.update_board(move)
            self.toggle_player()
            self.print_board()

            if self.check_winner():
                self.set_state("has_winner", True)

        self.toggle_player()
        print(f"Congrats player {self.get_current_player()} you win!")


TicTacToe().start()
