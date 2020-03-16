from typing import Optional
from string import ascii_letters

from pieces.moves import Move

from .board import board, Square, Board
from .player import Player

MAX_ROW = MAX_COLUMN = 8


class IllegalMoveException(Exception):
    pass


class Game(object):
    def __init__(self):
        self.board: Board = board
        self.current_player: Optional[Player] = None
        self.next_player: Optional[Player] = None

    def move(self, move: str):
        move = self.parse(move)
        from_ = move.from_
        to = move.to

        if not from_.piece.is_legal(move):
            raise IllegalMoveException(f'Illegal Move for {from_.piece.__class__.__name__}s')
        to.piece = from_.piece
        from_.piece = None

    def start(self):
        self.current_player = Player('w')
        self.next_player = Player('b')

    def switch_players(self):
        print(f"{self.current_player} - {self.next_player}")
        self.current_player.next()
        self.next_player.next()

    @staticmethod
    def parse(move: str) -> Move:
        try:
            from_, to = move.split('-')
        except ValueError:
            raise IllegalMoveException(f'Illegal Move format: {move}, move must be in format (from)-(to)')
        try:
            from_ = board[Square(from_)]
            to = board[Square(to)]
            if 1 > to.column_number > MAX_COLUMN or 1 > to.row > MAX_ROW:
                raise IllegalMoveException(f'Square {to} off the board')
        except KeyError:
            raise IllegalMoveException(f'Square {to} off the board')

        return Move(from_, to)

    def handle_check(self):
        print(f"====== {self.current_player} is in check")

    def handle_mate(self):
        print(f"====== {self.next_player} Wins")
