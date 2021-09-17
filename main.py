import chess

from board_render import run_pygame_display
from chess_game import ChessGame
from random_move import RandomMove


def main():
    engine = RandomMove(None, None)
    e2 = RandomMove(None, None)
    game = ChessGame(e2, engine)
    engine.side = chess.BLACK
    engine.game = game
    e2.side = chess.WHITE
    e2.game = game
    run_pygame_display(game)


if (__name__ == "__main__"):
    main()
