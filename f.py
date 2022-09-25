import pygame
from pygame.locals import *
pygame.init()
#กำหนดภาพ
f = pygame.OPENGL | RESIZABLE
screen = pygame.display.set_mode([800, 600],f)

t = True
while t:
    for e in pygame.event.get():
        if e.type == QUIT:
            t = False


