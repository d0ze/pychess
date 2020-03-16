from .piece import Piece

from .moves import Move


class Queen(Piece):
    def __str__(self):
        return "q"

    def is_legal(self, move: Move):
        return move.is_diagonal() or move.is_forward() or move.is_backward()
