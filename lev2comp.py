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
pygame.display.set_caption('Learn Mode')
successSound = pygame.mixer.Sound('audio/success.mp3')

#loads the main homescreen page
background = pygame.image.load("images\lev2comp.png")
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
        pygame.mixer.music.set_volume(50)
        pygame.mixer.Sound.play(successSound)
        sC += 1
    pygame.mixer.music.stop()
    
    #if mouse button is down, open the homescreen     
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if (x > 210) and (x < 489):
            if (y > 272) and (y < 337):
                exec(open("main.py").read())
        
pygame.quit() #allows to exit game