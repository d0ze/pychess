from game.game import Game, IllegalMoveException
from pieces.moves import Move


class PyChess(object):

    @staticmethod
    def new_game():
        return Game()

    @staticmethod
    def start():
        game = PyChess.new_game()
        game.start()
        print("====== Starting new game")
        while True:
            try:
                print(game.board)
                game.handle_mate()
                game.handle_check()
                move = input(f"====== {game.current_player}'s move\n")
                game.move(move)
            except IllegalMoveException as e:
                print(e)
            else:
                game.switch_players()


if __name__ == '__main__':
    PyChess.start()
