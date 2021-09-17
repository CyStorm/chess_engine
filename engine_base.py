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

    def get_material_value_from_board(self, board, side):
        '''Get a side's material from a board, more flexiable method
        '''
        total = 0
        pieces = board.board.piece_map()
        for piece in pieces.values():
            if (piece.color == side):
                total += self.material_weight[piece.piece_type]
        return total

    def get_self_material_value(self):
        '''Computes the numerical material values of all of our own peices
        '''
        return self.get_material_value_from_board(self.game.board, self.side)

    def get_opponent_material_value(self):
        '''Computes the numerical material values of all of opponent's peices
        '''
        return self.get_material_value_from_board(self.game.board, not self.side)

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
