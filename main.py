"""
Authors: Anika Suman & Ayush Khanna
Date: 9/7/21
Class: Math 241 Scientific Computing
Professor: Ben Marlin

Description: Root file that projects the homescreen, adds functionality to the buttons, and launches the learn and practice modes.
"""

#imports pygame, the module we use to launch and display our game
import pygame

#initializes the pygame workspace
pygame.init()

#sets the screen size to 960 x 540 pixels
screen = pygame.display.set_mode((960, 540))

#sets the caption of the window
pygame.display.set_caption('AnatoLearn')

#loads up the background music
#Source: https://www.youtube.com/watch?v=jj0ChLVTpaA
bgMusic = pygame.mixer.Sound('audio/elevatorMusic.mp3')

#loads the main homescreen page and projects it
background = pygame.image.load("images\homescreen.png")
screen.blit(background, (0,0))
pygame.display.flip() #updates background

#running the program until something makes it stop            
running = True
sC = 0 #sound count to make sure only one stream of music is playing at once
while running:
    #plays the background music
    if sC == 0:    
        bgMusic.play()
        sC += 1
      
    for event in pygame.event.get():
        #if the user quits the game, it stops running
        if event.type == pygame.QUIT:
            running = False
        
        #if the coordinates of the mouse-click match those of the first or second button, launch the respective mode
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if(x > 102) and (x < 452):
                if (y > 333) and (y < 398):
                    bgMusic.stop() #stop the music
                    exec(open("lev1intro.py").read()) #launch the Learn Mode Level 1 Intro page
            if(x > 508) and (x < 858):
                if (y > 333) and (y < 398):
                    bgMusic.stop()
                    exec(open("pMLevel1Intro.py").read()) #launch the Practice Mode Level 1 Intro page
        
pygame.quit() #allows to exit game







