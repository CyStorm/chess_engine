import os
import pygame

import chess_game  # replace with chess modules later

IMAGES_FOLDER = os.path.join(os.path.dirname(__file__), "images")
WIDTH = HEIGHT = 512
DIMENTION = 8
MAX_FPS = 15
SQUARE_SIZE = HEIGHT // DIMENTION

IMAGES = {}

def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wB", "wN", "wR", "wK", "wQ", "bP", "wP"]
    for piece in pieces:
        image_path = os.path.join(IMAGES_FOLDER, "{}.png".format(piece))
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(image_path), (SQUARE_SIZE, SQUARE_SIZE))

def main():

    load_images()
    # define a variable to control the main loop
    pygame.init()
    running = True
    logo = IMAGES["wP"]
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    screen = pygame.display.set_mode((240, 180))
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print("here")
                running = False

if (__name__ == "__main__"):
    main()
