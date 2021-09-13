import chess

from value_maps import PROMOTION_SQUARES, map_coord_to_index

class ChessGame():
    '''The game class, storing where peices are and information about gamestate
    '''
    def __init__(self, white, black):
        self.board = chess.Board()  # main python-chess board object
        self.move_log = []
        self.white_to_move = self.board.turn
        self.white = white
        self.black = black
        self.held_piece_square = None

    def move_piece(self, start_square, end_square, promotion=None):
        '''Moves piece from starting square to ending square
        '''
        move = chess.Move(start_square, end_square, promotion)
        self.play_move(move)

    def play_move(self, move, legal_check=True):
        '''plays move, with a legal check, because illegal moves can be played
        '''
        if (move in self.board.legal_moves and legal_check):
            self.board.push(move)
            self.white_to_move = self.board.turn
            return True
        else:
            return False

    def handle_player_mouse_event(self, x, y):
        '''Handlings the mouse button down event from pygame
        in case of player interaction
        '''
        clicked_square = map_coord_to_index(x, y)
        piece_map = self.board.piece_map()

        if (clicked_square in piece_map.keys()):
            piece = piece_map[clicked_square]
            # TODO need to check player sides compared to engine
        else:
            piece = None

        if (self.held_piece_square is not None):
            # holding a prievous piece no matter if there is a piece or not do the move
            promotion = None
            # TODO need to handle promotion, Currently promotion Auto Queens
            held_piece = piece_map[self.held_piece_square].symbol()
            if (held_piece == "P" or held_piece == "p"):
                if (clicked_square in PROMOTION_SQUARES[held_piece]):
                    promotion = chess.PieceType(5)      # Queen is 5 from documentation

            success = self.move_piece(self.held_piece_square, clicked_square, promotion)

            if (not success and piece is not None):
                self.held_piece_square = clicked_square
            else:
                self.held_piece_square = None

        elif (not self.held_piece_square and piece is not None):
            # case of not holding any piece, and picks up this piece
            self.held_piece_square = clicked_square

    def play_engine_moves(self):
        if (self.white_to_move and not (self.white == "player")):
            self.white.play_move()
        elif (not self.white_to_move and not (self.black == "player")):
            self.black.play_move()

if (__name__ == "__main__"):
    game = ChessGame("player", "player")
    print(game.board)
    print(game.board.piece_map())
    while (True):
        start = int(input("start "))
        end = int(input("end "))
        if (start == 99):
            break
        game.move_piece(start, end)
        print(game.board)
    pass
