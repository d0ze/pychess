from string import ascii_letters
from typing import List

from pieces import *


class Square:

    def __init__(self, position: str, starting_piece: "Piece" = None):
        column, row = position[0], int(position[1])
        self.row: int = int(row)
        self.column: str = column
        self.piece: "Piece" = starting_piece

    def __str__(self):
        return " * " if self.free else f" {str(self.piece) if self.piece.color == 'b' else str(self.piece).upper()} "

    @property
    def column_number(self) -> int:
        return ascii_letters.index(self.column) + 1

    @property
    def id(self):
        return f'{self.row}{self.column}'

    @property
    def free(self):
        return self.piece is None


class Board:
    def __init__(self, squares: List[Square]):
        self.squares = squares
        self._squares_mapping = {s.id: s for s in self.squares}

    def __str__(self):
        rows = ['  '.join(list(map(str, self.squares))[i:i + 8]) for i in [0, 8, 16, 24, 32, 40, 48, 56]]
        return '\n\n'.join(rows)

    def __getitem__(self, square: Square):
        return self._squares_mapping[square.id]


board = Board([
    Square('a8', Rook('b')), Square('b8', Knight('b')), Square('c8', Bishop('b')), Square('d8', Queen('b')),
    Square('e8', King('b')), Square('f8', Bishop('b')), Square('g8', Knight('b')), Square('h8', Rook('b')),
    Square('a7', Pawn('b')), Square('b7', Pawn('b')), Square('c7', Pawn('b')), Square('d7', Pawn('b')),
    Square('e7', Pawn('b')), Square('f7', Pawn('b')), Square('g7', Pawn('b')), Square('h7', Pawn('b')),
    Square('a6'), Square('b6'), Square('c6'), Square('d6'), Square('e6'), Square('f6'), Square('g6'), Square('h6'),
    Square('a5'), Square('b5'), Square('c5'), Square('d5'), Square('e5'), Square('f5'), Square('g5'), Square('h5'),
    Square('a4'), Square('b4'), Square('c4'), Square('d4'), Square('e4'), Square('f4'), Square('g4'), Square('h4'),
    Square('a3'), Square('b3'), Square('c3'), Square('d3'), Square('e3'), Square('f3'), Square('g3'), Square('h3'),
    Square('a2', Pawn('w')), Square('b2', Pawn('w')), Square('c2', Pawn('w')), Square('d2', Pawn('w')),
    Square('e2', Pawn('w')), Square('f2', Pawn('w')), Square('g2', Pawn('w')), Square('h2', Pawn('w')),
    Square('a1', Rook('w')), Square('b1', Knight('w')), Square('c1', Bishop('w')), Square('d1', Queen('w')),
    Square('e1', King('w')), Square('f1', Bishop('w')), Square('g1', Knight('w')), Square('h1', Rook('w')),
])
