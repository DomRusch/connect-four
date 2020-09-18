from itertools import groupby

MIN_SIZE = 4
EMPTY_ELEMENT = "."

class BoardTooSmall(Exception):
    """Raised when the board created is too small."""


class Board:
    def __init__(self, rows: int, columns: int):
        self.rows, self.cols = rows, columns
        self._check_size()
        
        self.board = [[EMPTY_ELEMENT] * self.cols for _ in range(self.rows)]

    def __repr__(self):
        return "\n".join(" ".join(elem for elem in row) for row in self.board)

    def _check_size(self):
        if self.rows < MIN_SIZE or self.cols < MIN_SIZE:
            raise BoardTooSmall(f"Board must have at least {MIN_SIZE} rows or columns.")

    def _in_bounds(self, pos: (int, int)) -> bool:
        row, col = pos
        return 0 <= row < self.rows and self._valid_column(col)
    
    def _is_empty(self, row: int, col: int) -> bool:
        return self.board[row][col] == EMPTY_ELEMENT

    def _get_diag(self, row: int, col: int, direction: int) -> [(int, int)]:
        return [(row+(i*direction), col+i) for i in range(-MIN_SIZE, MIN_SIZE+1)]

    def _get_row(self, row: int, col: int) -> [(int, int)]:
        return [(r, col) for r in range(row-MIN_SIZE, row+MIN_SIZE)]

    def _get_col(self, row: int, col: int) -> [(int, int)]:
        return [(row, c) for c in range(col-MIN_SIZE, col+MIN_SIZE)]

    def _check_win(self, row: int, col: int) -> bool:
        return any(map(self._has_win, 
                       [self._get_row(row, col),
                        self._get_col(row, col),
                        self._get_diag(row, col, 1),
                        self._get_diag(row, col, -1)]))
    
    def _has_win(self, positions: [(int, int)]) -> bool:
        in_bounds = filter(self._in_bounds, positions)

        for elem, group in groupby(self.board[r][c] for r, c in in_bounds):
            if elem != EMPTY_ELEMENT and len(list(group)) >= MIN_SIZE:
                return True

        return False

    def _valid_column(self, col: int) -> bool:
        return 0 <= col < self.cols
    
    def can_move(self, col: int) -> bool:
        return self._valid_column(col) and self._is_empty(0, col)

    def make_move(self, col: int, elem: str) -> bool:
        for row in range(self.rows-1, -1, -1):
            if self._is_empty(row, col):
                self.board[row][col] = elem
                return self._check_win(row, col)
        
        return False


if __name__ == "__main__":
    board = Board(4, 5)
    board.make_move(1, "X")
    print(board)