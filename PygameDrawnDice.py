#! /usr/bin/env python
import pygame
from random import randint

def dice(dots):

    dot1 = dot2 = dot3 = dot4 = dot5 = dot6 = [0,0]

    if dots == 1:
       dot1 = [140,180]

    if dots == 2:
       dot1 = [120,180]
       dot2 = [160,180]

    if dots == 3:
       dot1 = [120,160]
       dot2 = [140,180]
       dot3 = [160,200]

    if dots == 4:
       dot1 = [120,160]
       dot2 = [120,200]
       dot3 = [160,160]
       dot4 = [160,200]

    if dots == 5:
       dot1 = [120,160]
       dot2 = [120,200]
       dot3 = [160,160]
       dot4 = [160,200]
       dot5 = [140,180]

    if dots == 6:
       dot1 = [120,156]
       dot2 = [120,180]
       dot3 = [120,204]
       dot4 = [160,156]
       dot5 = [160,180]
       dot6 = [160,204]

    return dot1, dot2, dot3, dot4, dot5, dot6 

screen = pygame.display.set_mode((400, 400))
pygame.event.set_blocked(pygame.MOUSEMOTION)
#pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

running = 1
reroll = 1
black = (0,0,0)
white = (255,255,255)

while running:

    screen.fill(black)
    pygame.draw.rect(screen, white, (100,140,80,80), 4)
    pygame.draw.rect(screen, white, (240,140,80,80), 4)

    if reroll: 
        d1 = randint(1,6)
        d2 = randint(1,6)
        reroll = 0

    dot = dice(d1)
    for each in dot:
        x,y = each
        if x > 0:
            pygame.draw.circle(screen, white, (x,y), 8, 8)

    dot = dice(d2)
    for each in dot:
        x,y = each
        if x > 0:
            x = x + 140
            pygame.draw.circle(screen, white, (x,y), 8, 8)

    pygame.time.wait(100)
    pygame.display.flip()

    pygame.event.clear()
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        running = 0
    if event.type  == pygame.KEYDOWN:
        if event.key > 20:
            reroll = 1

