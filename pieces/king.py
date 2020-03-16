from .piece import Piece

from .moves import Move


class King(Piece):
    def __str__(self):
        return "k"

    def is_legal(self, move: Move):
        return 0 <= abs(move.row_delta) <= 1 and 0 <= abs(move.column_delta) <= 1
