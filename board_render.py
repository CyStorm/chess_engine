import os
import pygame


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

def draw_pieces(surface: pygame.Surface, board):
    '''Draws the pieces from a given board state
    '''
    surface.blit(IMAGES["bR"], (10, 10))    # user surface.blit to draw images


# use ENUMs for mapping
def map_coord_to_index(x, y):
    '''Maps mouse click coordinates to chess squares
    '''
    col = (x // SQUARE_SIZE)
    row = (DIMENTION - (y // SQUARE_SIZE)) - 1

    square = row * 8 + col
    # print(row)
    # print(col)
    print(square)
    return square

def map_index_to_coord(index):
    '''Maps the square index to display location for piece
    '''
    row = index // 8
    col = index % 8

    x = col * SQUARE_SIZE
    y = (DIMENTION - (row + 1))
    return (x, y)

def main():

    load_images()

    pygame.init()

    logo = IMAGES["wP"]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("chad is op")

    running = True

    while running:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                print("Exited")
                running = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                map_coord_to_index(pos[0], pos[1])

        draw_board(screen)
        draw_pieces(screen, None)
        pygame.display.flip()


if (__name__ == "__main__"):
    main()
    # import chess
    # board = chess.Board()
    # print(board)
    # print(board.piece_map())
