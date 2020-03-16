class Player(object):
    def __init__(self, color):
        self.color = color

    def next(self):
        self.color = ('w' if self.color == 'b' else 'b')

    def __str__(self):
        return 'White Player' if self.color == 'w' else "Black player"
