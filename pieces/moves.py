from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.board import Square


class Move(object):
    def __init__(self, from_, to):
        self.from_: Square = from_
        self.to: Square = to

    @property
    def row_delta(self) -> int:
        return self.to.row - self.from_.row

    @property
    def column_delta(self):
        return self.to.column_number - self.from_.column_number

    def is_forward(self) -> bool:
        return self.row_delta > 0 and self.column_delta == 0

    def is_backward(self) -> bool:
        return self.row_delta < 0 and self.column_delta == 0

    def is_diagonal(self) -> bool:
        return self.is_up_right() or self.is_up_left() or self.is_down_left() or self.is_down_right()

    def is_up_right(self) -> bool:
        return self.row_delta > 0 and self.column_delta > 0

    def is_up_left(self) -> bool:
        return self.row_delta > 0 > self.column_delta

    def is_down_right(self) -> bool:
        return self.row_delta < 0 < self.column_delta

    def is_down_left(self) -> bool:
        return self.row_delta < 0 and self.column_delta < 0
