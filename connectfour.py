from board import Board

PLAYER_CHARS = "X", "O"

class ConnectFour:
    def __init__(self, rows: int=6, columns: int=7):
        self.board = Board(rows, columns)
        self.game_over = False
        self.game_draw = False
        self.max_turns = rows * columns
        self.turns  = 0
        self.player = 0

    def __repr__(self):
        return self.board.__repr__()

    def _get_move(self) -> int:
        return int(input(f"\nPlayer {self.player+1}: Enter move column\n"))
    
    def _swap_player(self) -> None:
        self.player = 1 - self.player

    def _set_draw(self) -> None:
        if self.turns >= self.max_turns:
            self.game_over = self.game_draw = True

    def _make_move(self, column: int) -> None:
        self.game_over = self.board.make_move(column, PLAYER_CHARS[self.player])
        self.turns += 1

        self._set_draw()
        if not self.game_over:
            self._swap_player()
    
    def _make_turn(self) -> None:
        move_column = self._get_move()

        if self.board.can_move(move_column):
            self._make_move(move_column)
        else:
            print("Invalid move!\n")

    def _process_turns(self) -> None:
        print(self.board)

        while not self.game_over:
            self._make_turn()
            print(self.board)

    def _output_result(self):
        if self.game_draw:
            print(f"The game was drawn in {self.max_turns} turns!")
        else:
            print(f"\nPlayer {self.player+1} won in {self.turns} turns!")

    def start(self):
        self._process_turns()
        self._output_result()



if __name__ == "__main__":
    game = ConnectFour()
    game.start()