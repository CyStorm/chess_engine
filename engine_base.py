import chess
from chess_game import ChessGame


class EngineBase():
    def __init__(self, game: ChessGame, side: chess.Color):
        self.game = game
        self.side = side

    def generate_next_move(self):
        '''Uses the current board state to generate the next move
        Should overwrite in each engine class
        '''
        pass

    def play_move(self):
        if (self.game.white_to_move == self.side):
            move = self.generate_next_move()
            self.game.play_move(move)
