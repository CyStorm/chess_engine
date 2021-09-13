import os
import pygame

import chess

from chess_game import ChessGame
from value_maps import SYMBOL_MAP
from random_move import RandomMove

# TODO use env variables and combine to value maps
IMAGES_FOLDER = os.path.join(os.path.dirname(__file__), "images")
WIDTH = HEIGHT = 512
DIMENTION = 8
MAX_FPS = 15
SQUARE_SIZE = HEIGHT // DIMENTION

IMAGES = {}

def load_images():
    '''Loads the images of pieces
    '''
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wB", "wN", "wR", "wK", "wQ", "bP", "wP"]
    for piece in pieces:
        image_path = os.path.join(IMAGES_FOLDER, "{}.png".format(piece))
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(image_path), (SQUARE_SIZE, SQUARE_SIZE))

def draw_board(surface: pygame.Surface):
    '''Draws the empty chess board with given colors
    '''
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for row in range(DIMENTION):
        for col in range(DIMENTION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(surface, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(surface: pygame.Surface, board: chess.Board):
    '''Draws the pieces from a given board state
    '''
    piece_map = board.piece_map()
    for index, piece in piece_map.items():
        x, y = map_index_to_coord(index)
        image = map_piece_to_image(piece.symbol())
        surface.blit(IMAGES[image], (x, y))    # user surface.blit to draw images

def draw_highlighted_squares(surface: pygame.Surface, board: chess.Board, held_piece_square: int):
    '''Draws the highlighted squares if in check or holding a piece
    '''
    if (held_piece_square is not None):
        for move in board.legal_moves:
            if (move.from_square == held_piece_square):
                color = pygame.Color("yellow")
                x, y = map_index_to_coord(move.to_square)
                pygame.draw.rect(surface, color, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))

    if (board.is_check()):
        # TODO handle if in check display a red square
        pass

def draw_promotion_graphic(surface: pygame.Surface):
    '''Draws the promotion graphic when pawns promote
    '''
    pass

def map_piece_to_image(piece_symbol):
    '''Maps the piece symbol to the image to be displayed
    '''
    return SYMBOL_MAP[piece_symbol]

# use ENUMs for mapping
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

def main():

    load_images()

    pygame.init()

    logo = IMAGES["wP"]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("chad is op")

    running = True

    engine = RandomMove()
    # e2 = RandomMove()
    game = ChessGame("player", engine)
    engine.side = chess.BLACK
    engine.game = game
    # e2.side = chess.WHITE
    # e2.game = game

    draw_board(screen)
    draw_pieces(screen, game.board)
    pygame.display.flip()

    while running:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                print("Exited")
                running = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                game.handle_player_mouse_event(x, y)

            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_a):
                    game.play_engine_moves()
        draw_board(screen)
        draw_highlighted_squares(screen, game.board, game.held_piece_square)
        draw_pieces(screen, game.board)
        pygame.display.flip()

if (__name__ == "__main__"):
    main()
