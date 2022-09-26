import random
import pygame
from pygame.locals import *
pygame.init()
#Edit screen side
s = pygame.RESIZABLE
screen = pygame.display.set_mode([800, 600],s)

#Name caption
pygame.display.set_caption("Stupid game")
#icon game
logo = pygame.image.load('D:\c\img\starbucks_corporation_logo.png')
pygame.display.set_icon(logo)
#background spaceship
bg = pygame.image.load(r'D:\c\bg\768px-Milky_way.png')
player = pygame.image.load('D:\c\img\spaceship\Starbucks-Cup.png')

enemy = []
bix = []
biy = []
cbix = []
cbiy = []
num_of_bi = 10

for i in range (num_of_bi):
    enemy.append(pygame.image.load(r'D:\c\img\Enemy\3306571.png'))
    bix.append(random.randint(0, 740))
    biy.append(random.randint(0, 250))
    cbix.append(random.randint(-1, 1))
    cbiy.append(1)

def bi(x, y, i):
    screen.blit(enemy[i], (x, y))



#transform scale
player = pygame.transform.scale(player,(100,100))
#loop screen and end loop (Exit the program)
t = True
while t:
    for e in pygame.event.get():
        if e.type == QUIT:
            t = False
#

    screen.blit(bg,(0, 0))
    screen.blit(player,(380, 520))
    pygame.display.flip()

for i in range (num_of_bi):
    bix[i] += cbix[i]
    biy[i] += cbiy[i]
    if biy[i] >= 600:
       biy[i] = 0
       bix[i] = random.randint(0 ,740)
       bi(bix[i], biy[i], i)
       pygame.display.update()



