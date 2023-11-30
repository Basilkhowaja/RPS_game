from time import sleep
import random
import pygame
pygame.init()


#loading all game images
background=pygame.image.load('bg.jpg')
rock=pygame.image.load('rock.png')
paper=pygame.image.load('paper.jpg')
scissor=pygame.image.load('scissor.jpg')
lost=pygame.image.load('lost.jpg')
choose=pygame.image.load('choose.jpg')
win=pygame.image.load('win.jpg')
tie=pygame.image.load('tie.jpg')
again=pygame.image.load('again.jpg')


s=['rock','paper','scissor']
#c=random.choice(s)

#user=input("enter your choice")
gameDisplay=pygame.display.set_mode((800,700))

gameDisplay.blit(background,(0,0))
pygame.display.update()
sleep(3)

c='paper'

#make use of function here

def game():
    run=True
    while run:
        gameDisplay.blit(choose,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.KEYDOWN:
                key=pygame.key.get_pressed()
                run=False
    
    if key[pygame.K_r]==True and c=='rock':
        gameDisplay.blit(tie,(0,0)) 
        pygame.display.update()
        sleep(2)

    elif key[pygame.K_r]==True and c=='paper':
        gameDisplay.blit(lost,(0,0))
        pygame.display.update()
        sleep(2)
    elif key[pygame.K_r]==True and c=='scissor':
        gameDisplay.blit(win,(0,0))
        pygame.display.update()
        sleep(2)
    elif key[pygame.K_p]==True and c=='rock':
        gameDisplay.blit(win,(0,0))
        pygame.display.update()
        sleep(2)
    elif key[pygame.K_p]==True and c=='paper':
        gameDisplay.blit(tie,(0,0))
        pygame.display.update()
        sleep(2)
    elif key[pygame.K_p]==True and c=='scissor':
        gameDisplay.blit(lost,(0,0))
        pygame.display.update()
        sleep(2)
    elif key[pygame.K_s]==True and c=='rock':
        gameDisplay.blit(lost,(0,0))
        pygame.display.update()
        sleep(2)
    elif key[pygame.K_s]==True and c=='paper':
        gameDisplay.blit(win,(0,0))
        pygame.display.update()
        sleep(2)
    elif key[pygame.K_s]==True and c=='scissor':
        gameDisplay.blit(tie,(0,0))
        pygame.display.update()
        sleep(2)
    run=True
    key=None
    while run:
        gameDisplay.blit(again,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.KEYDOWN:
                key=pygame.key.get_pressed()
                if key[pygame.K_y]==True:
                    game()
                else:
                    run=False
                    

game()


