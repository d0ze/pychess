from .piece import Piece

from .moves import Move


class Rook(Piece):
    def __str__(self):
        return "r"

    def is_legal(self, move: Move):
        return move.is_forward() or move.is_backward()
