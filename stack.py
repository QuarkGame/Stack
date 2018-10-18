import pygame
from pygame.locals import *
import logging
import math
import random

logging.basicConfig(filename="debug.log", level=logging.DEBUG)

pygame.init()

display_width = 1000
display_height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_RED = (255, 20, 0)
BRIGHT_GREEN = (0, 255, 0)
GREY = (77, 79, 74)
BROWN = (102, 74, 50)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (153, 204, 255)
LIGHT_BROWN = (74, 52, 38)
LIGHT_YELLOW = (255, 255, 153)
DARK_ORANGE = (204, 102, 0)
LIGHT_ORANGE = (255, 153, 51)



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('STACK')

clock = pygame.time.Clock()

class Block:

    width = 200
    height = 50
    family = []

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        Block.family.append(self)

    def show(self):
        pygame.draw.rect(gameDisplay, self.color,
                        (self.x, self.y, Block.width, Block.height))

    def check(self):
        if 


def game_loop():

    block_init_x = int(display_width / 2 - block_width / 2)

    while True:
        gameDisplay.fill(LIGHT_BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    quitgame()
