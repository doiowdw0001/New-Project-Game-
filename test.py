import random
import pygame
from pygame.locals import *
pygame.init()

f = pygame.RESIZABLE
s = pygame.display.set_mode([800, 600], f)
img = pygame.image.load(r"D:\c\bg\768px-Milky_way.png")
me = pygame.image.load(r"D:\c\img\spaceship\3306571.png")
me = pygame.transform.scale(me, (100, 100))
s.blit(img, (0, 0))
s.blit(me, (380, 520))
pygame.display.flip()


t = True
while t:
    for m in pygame.event.get():
        if m.type == QUIT:
            t = False


