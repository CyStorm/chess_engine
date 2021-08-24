from enum import Enum

class index_to_coord(Enum):
    pass

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
