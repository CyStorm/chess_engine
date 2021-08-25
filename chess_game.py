import chess

class ChessGame():
    '''The game class, storing where peices are and information about gamestate
    '''
    def __init__(self):
        self.board = chess.Board()  # main python-chess board object
        self.move_log = []
        self.white_to_move = True

    def move_piece(self, start_square, end_square, promotion=None):
        '''Moves piece from starting square to ending square
        '''
        move = chess.Move(start_square, end_square, promotion)
        if (move in self.board.legal_moves):
            self.board.push(move)
        else:
            print("Not legal")

if (__name__ == "__main__"):
    game = ChessGame()
    print(game.board)
    while (True):
        start = int(input("start "))
        end = int(input("end "))
        if (start == 99):
            break
        game.move_piece(start, end)
        print(game.board)
    pass
