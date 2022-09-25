import pygame
from pygame.locals import *
pygame.init()
#กำหนดภาพ
f = pygame.RESIZABLE | DROPFILE | HWSURFACE
screen = pygame.display.set_mode([800, 600],f)

#ใส่ชื่อเกม
pygame.display.set_caption("Stupid game")
#icon game
logo = pygame.image.load('D:\c\img\starbucks_corporation_logo.png')
pygame.display.set_icon(logo)
#background and spaceship
bg = pygame.image.load(r'D:\c\bg\768px-Milky_way.png')
player = pygame.image.load('D:\c\img\spaceship\Starbucks-Cup.png')
#transform scale
player = pygame.transform.scale(player,(100,100))
t = True
while t:
    for e in pygame.event.get():
        if e.type == QUIT:
            t = False

    screen.blit(bg,(0, 0))
    screen.blit(player,(380, 520))
    pygame.display.flip()

