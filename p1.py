import pygame, sys

pygame.init()

WIDTH=600
HEIGHT=600
red=(255,255,0)

screen= pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE')
screen.fill(red)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pygame.display.update()