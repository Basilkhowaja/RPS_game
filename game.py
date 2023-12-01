from time import sleep
import random
import pygame
import sys

pygame.init()
pygame.mixer.init() 


#loading all game images, including match result images:

background=pygame.image.load('bg.jpg')
rock=pygame.image.load('rock.png')
paper=pygame.image.load('paper.jpg')
scissor=pygame.image.load('scissor.jpg')
lost=pygame.image.load('lost.jpg')
choose=pygame.image.load('choose.jpg')
win=pygame.image.load('win.jpg')
tie=pygame.image.load('tie.jpg')
again=pygame.image.load('again.jpg')
rr=pygame.image.load("rr.jpg")          #when user input is rock and computer choice is rock
rp=pygame.image.load("rp.jpg")          #when user input is rock and computer choice is paper
rs=pygame.image.load("rs.jpg")          #when user input is rock and computer choice is scissor
pr=pygame.image.load("pr.jpg")          #when user input is paper and computer choice is rock
pp=pygame.image.load("pp.jpg")          #when user input is paper and computer choice is paper
ps=pygame.image.load("ps.jpg")          #when user input is paper and computer choice is scissor
sr=pygame.image.load("sr.jpg")          #when user input is scissor and computer choice is rock
sp=pygame.image.load("sp.jpg")          #when user input is scissor and computer choice is paper
ss=pygame.image.load("ss.jpg")          #when user input is scissor and computer choice is scissor

#adding background music for the game
def music():
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
music()



#setting up the game background first
gameDisplay=pygame.display.set_mode((800,600))  #positioning the display screen
gameDisplay.blit(background,(0,0))
pygame.display.update()
sleep(10)   #will show bg screen for 10 seconds



#making use of function here (maing game function)

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

    #computer choice through random() built_in function, it will select through the list s.            
    s=['rock','paper','scissor']   #selecting the computer choice inside the game function so that whenever user wants to play again, the new value of C gets selected.
    computer=random.choice(s)
    
#giving conditions now on which choice to display which image, we designed these images through canva.com

    if key[pygame.K_r]==True and computer=='rock':
        gameDisplay.blit(rr,(0,0)) 
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_r]==True and computer=='paper':
        gameDisplay.blit(rp,(0,0))
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_r]==True and computer=='scissor':
        gameDisplay.blit(rs,(0,0))
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_p]==True and computer=='rock':
        gameDisplay.blit(pr,(0,0))
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_p]==True and computer=='paper':
        gameDisplay.blit(pp,(0,0))
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_p]==True and computer=='scissor':
        gameDisplay.blit(ps,(0,0))
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_s]==True and computer=='rock':
        gameDisplay.blit(sr,(0,0))
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_s]==True and computer=='paper':
        gameDisplay.blit(sp,(0,0))
        pygame.display.update()
        sleep(5)
    elif key[pygame.K_s]==True and computer=='scissor':
        gameDisplay.blit(ss,(0,0))
        pygame.display.update()
        sleep(5)
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
                if key[pygame.K_n]==True:
                    exit()

                    

game()


