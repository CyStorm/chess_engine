import os
import pygame

import chess

from chess_game import ChessGame
from value_maps import map_coord_to_index, map_index_to_coord, map_piece_to_image, DIMENTION, SCREEN_PIXEL_SIZE, SQUARE_SIZE, IMAGES_FOLDER
from random_move import RandomMove


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

def initial_setup():
    '''Runs when the program first starts, loads images and initializes pygame
    '''
    load_images()
    pygame.init()
    logo = IMAGES["wP"]
    screen = pygame.display.set_mode((SCREEN_PIXEL_SIZE, SCREEN_PIXEL_SIZE))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("chad is op")
    return screen

def update_display(screen, game):
    '''Updates the display screen with game info
    '''
    draw_board(screen)
    draw_highlighted_squares(screen, game.board, game.held_piece_square)
    draw_pieces(screen, game.board)
    pygame.display.flip()

def run_pygame_display(game):
    '''Single function to have the pygame display function for visually displaying the game
    calls all the setup as well
    '''
    screen = initial_setup()
    running = True
    update_display(screen, game)
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
        update_display(screen, game)


if (__name__ == "__main__"):
    '''Debug code for this file
    '''
    engine = RandomMove(None, None)
    e2 = RandomMove(None, None)
    game = ChessGame(e2, engine)
    engine.side = chess.BLACK
    engine.game = game
    e2.side = chess.WHITE
    e2.game = game
    run_pygame_display(game)
