from .piece import Piece

from .moves import Move


class Bishop(Piece):
    def __str__(self):
        return "b"

    def is_legal(self, move: Move):
        return move.is_diagonal()
