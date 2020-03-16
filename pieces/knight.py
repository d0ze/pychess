from .piece import Piece

from .moves import Move


class Knight(Piece):
    def __str__(self):
        return "n"

    def is_legal(self, move: Move):
        return abs(move.row_delta) == 2 and abs(move.column_delta) == 1
