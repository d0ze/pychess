from abc import ABCMeta, abstractmethod

from .moves import Move


class Piece(metaclass=ABCMeta):
    def __init__(self, color: str):
        self.color: str = color

    @abstractmethod
    def is_legal(self, move: Move):
        raise NotImplemented('Pieces must implement this method')
