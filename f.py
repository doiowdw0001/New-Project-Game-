import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([800, 600])

f = True
while f:
    for e in pygame.event.get():
        if e.type == QUIT:
            f = False


