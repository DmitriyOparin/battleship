# -*- coding:utf-8 -*- 
import pygame
import math
import sys
import time
from random import randint

pygame.init()


width = 1400
height = 700
SIZE = (width, height)
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Морской бой')
screen = pygame.Surface((1400,700))
# info_string = pygame.Surface((width, 30))


N = 10
M = 10
pix = 60


score_font = pygame.font.SysFont(None, 24)
font = pygame.font.SysFont(None, 45)
red = (255,0,0)
green = (18,173,42)
yellow = (254,228,62)

class Platform:
    def __init__(self):
        self.fon = pygame.image.load('img/ship_fon.png')
        self.ship = pygame.image.load('img/ship.png')
        self.past = pygame.image.load('img/past.png')
        self.ship_fire = pygame.image.load('img/ship_fire.png')

def make_level(level1,level2, platform):
    x = 60
    y = 60
    for i in range(len(level1)):
        for j in range(len(level1[i])):
            if level1[i][j] == 0:
                screen.blit(platform.fon, (x,y))
            if level1[i][j] == 5:
                screen.blit(platform.ship, (x,y))  
            if level1[i][j] == 6:
                screen.blit(platform.ship_fire, (x,y))   
            if level1[i][j] == 3:
                screen.blit(platform.past, (x,y)) 
            x += 60
        y += 60
        x = 60

    x1 = 760
    y1 = 60
    for i in range(len(level2)):
        for j in range(len(level2[i])):
            if level2[i][j] == 0:
                screen.blit(platform.fon, (x1,y1))
            if level2[i][j] == 5:
                screen.blit(platform.fon, (x1,y1))  
            if level2[i][j] == 6:
                screen.blit(platform.ship_fire, (x1,y1))   
            if level2[i][j] == 3:
                screen.blit(platform.past, (x1,y1)) 
            x1 += 60
        y1 += 60
        x1 = 760


def shot_comp():
    a = randint(0, len(level_player)-1)
    b = randint(0, len(level_player[0])-1)
    if level_player[b][a] == 5:
        level_player[b][a] = 6
        message("В Вас попали", red)
        # make_level(level_player, level_comp, pl)
        pygame.display.update()
        control(b,a)
        shot_comp()
    elif level_player[b][a] == 0:
        message("Комрьютер промахнулся", yellow)
        level_player[b][a] = 3
        shot_player()   

   
def shot_player():
    (mouseA, mouseB) = pygame.mouse.get_pos()
    a = int(mouseA/pix)-13
    b = int(mouseB/pix)-1
    if level_comp[b][a] == 5:
        level_comp[b][a] = 6
        message("Вы попали в корабль! Стреляйте еще раз", green)
        # make_level(level_player, level_comp, pl)
        pygame.display.update()
        control(b,a)
        shot_player()
    elif level_comp[b][a] == 0:
        message("Мимо", yellow)
        level_comp[b][a] = 3
        shot_comp()    

def control(b,a):
    for i in range(N):
        for j in range(M):
            if level_comp[b][a] == 6:
                try:
                    if level_comp[b+1][a] != 5 and level_comp[b-1][a] != 5 and level_comp[b][a+1] != 5 and level_comp[b][a-1] != 5:
                        pass
                except IndexError:
                    pass
                finally:
                    message("Вы затопили корабль", green)   
            if level_player[b][a] == 6:
                try:
                    if level_player[b+1][a] != 5 and level_player[b-1][a] != 5 and level_player[b][a+1] != 5 and level_player[b][a-1] != 5:
                        pass    
                except IndexError:
                    pass
                finally:
                    message("Ваш корабль затопили", red)   




def message(message, color):
    screen_text = font.render(message, True, color)
    window.blit(screen_text, [width/2, height/2])
    pygame.display.update()
    

level_player = [
    [0,0,0,0,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,5,0,0],
    [5,0,0,0,0,0,0,5,0,0],
    [5,0,0,5,0,0,0,0,0,0],
    [5,0,0,0,0,0,5,5,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [5,0,0,0,5,5,5,0,0,5],
    [0,0,0,0,0,0,0,0,0,0],
    [0,5,5,5,0,0,0,0,5,0],
    [0,0,0,0,0,0,0,0,5,0]]

level_comp = [
    [5,5,5,5,0,0,0,0,5,0],
    [0,0,0,0,0,5,0,0,5,0],
    [0,0,5,0,0,0,0,0,0,0],
    [0,0,5,0,0,0,0,5,5,0],
    [0,0,5,0,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,5,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [5,5,5,0,0,5,0,0,0,0],
    [0,0,0,0,0,5,0,0,0,5]] 

pl = Platform()



done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                shot_player() 


        
    screen.fill((240,255,255))
    # info_string.fill((45,80,40))
  
    
    make_level(level_player, level_comp, pl)

 
    window.blit(screen, (0,0))
    # window.blit(info_string, (0,0))

    pygame.display.flip()