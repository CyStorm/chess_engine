import chess
from chess_game import ChessGame


class EngineBase():
    def __init__(self, game: ChessGame, side: chess.Color):
        self.game = game
        self.side = side
        self.material_weight = {
            chess.KING: 0,
            chess.QUEEN: 9,
            chess.ROOK: 5,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.PAWN: 1,
        }

    def generate_next_move(self):
        '''Uses the current board state to generate the next move
        Should overwrite in each engine class
        '''
        pass

    def play_move(self):
        if (self.game.white_to_move == self.side):
            move = self.generate_next_move()
            self.game.play_move(move)

    def get_self_material_value(self):
        '''Computes the numerical material values of all of our own peices
        '''
        total = 0
        pieces = self.game.board.piece_map()
        for piece in pieces.values():
            if (piece.color == self.side):
                total += self.material_weight[piece.piece_type]
        return total

    def get_opponent_material_value(self):
        '''Computes the numerical material values of all of opponent's peices
        '''
        total = 0
        pieces = self.game.board.piece_map()
        for piece in pieces.values():
            if (piece.color != self.side):
                total += self.material_weight[piece.piece_type]
        return total

if (__name__ == "__main__"):
    '''debug code for this file
    '''
    material_weight = {
        chess.KING: 0,
        chess.QUEEN: 9,
        chess.ROOK: 5,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.PAWN: 1,
    }
    print(material_weight[chess.KING])
    print(material_weight[chess.QUEEN])
    for piece, val in material_weight.items():
        print(piece, val)
