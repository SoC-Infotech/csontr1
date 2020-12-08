#import 2 libtaries to our game
import pygame
import random

#initilize the pygame (game look. game scene)
pygame.init()

#declear some variables/constants
winHeight = 480
winWidth = 700
GREEN = (0,255,0)

#create window game
win = pygame.display.set_mode((winWidth, winHeight))

#Main program
#crate game loop to keep the window visable
inPlay = True
while inPlay:
    win.fill(GREEN) #Make background colour green
    pygame.display.update()
    pygame.time.delay(100)


#quit the pygamepygame.quit()
