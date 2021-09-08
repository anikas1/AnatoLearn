"""
Authors: Anika Suman & Ayush Khanna
Date: 9/7/21
Class: Math 241 Scientific Computing
Professor: Ben Marlin
"""

import pygame

#initializes the pygame workspace
pygame.init()

#sets the screen size to 960 x 540 pixels
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption('Practice Mode')
successSound = pygame.mixer.Sound('audio/success.mp3')
font = pygame.font.SysFont('bahnschrift', 25)

#loads the main homescreen page
background = pygame.image.load("images\plevel2comp.png")
screen.blit(background, (0,0))
pygame.display.flip() #updates background

#running the program until something makes it stop            
running = True
sC = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if sC == 0:
            pygame.mixer.Sound.play(successSound)
            sC += 1
        pygame.mixer.music.stop()
    
        #if mouse button is down in the return to main screen button area, return to the homescreen
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (x > 184) and (x < 448):
                if (y > 281) and (y < 348):
                    exec(open("main.py").read())
        
pygame.quit() #allows to exit game