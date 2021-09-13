from enum import Enum

WIDTH = HEIGHT = 512
DIMENTION = 8
MAX_FPS = 15
SQUARE_SIZE = HEIGHT // DIMENTION
class letter_column(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

SYMBOL_MAP = {
    # lower case is black
    "p": "bP",
    "k": "bK",
    "q": "bQ",
    "r": "bR",
    "n": "bN",
    "b": "bB",
    # Upper case is white
    "P": "wP",
    "K": "wK",
    "Q": "wQ",
    "R": "wR",
    "N": "wN",
    "B": "wB"
}

PROMOTION_SQUARES = {
    "p": [0, 1, 2, 3, 4, 5, 6, 7],      # black pawn promotion squares
    "P": [56, 57, 58, 59, 60, 61, 62, 63],      # white pawn promotion squares
}


def map_coord_to_index(x, y):
    '''Maps mouse click coordinates to chess squares
    '''
    col = (x // SQUARE_SIZE)
    row = (DIMENTION - (y // SQUARE_SIZE)) - 1

    square = row * 8 + col
    return square

def map_index_to_coord(index):
    '''Maps the square index to display location for piece
    '''
    row = index // 8
    col = index % 8

    x = col * SQUARE_SIZE
    y = (DIMENTION - (row + 1)) * SQUARE_SIZE
    return x, y


# # old board
# self.board = [
#             ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
#             ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
#             ["--", "--", "--", "--", "--", "--", "--", "--"],
#             ["--", "--", "--", "--", "--", "--", "--", "--"],
#             ["--", "--", "--", "--", "--", "--", "--", "--"],
#             ["--", "--", "--", "--", "--", "--", "--", "--"],
#             ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
#             ["bR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
#         ]
