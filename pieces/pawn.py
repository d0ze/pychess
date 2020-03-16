from .piece import Piece

from .moves import Move


class Pawn(Piece):
    def __str__(self):
        return "p"

    def is_legal(self, move: Move):
        return abs(move.row_delta) == 1 and \
               self._is_forward(move) or \
               ((move.is_up_left() or move.is_up_right()) and not move.to.free)

    def _is_forward(self, move):
        return move.is_forward() if self.color == 'w' else move.is_backward()
