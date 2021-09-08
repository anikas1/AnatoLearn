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

#loads the main homescreen page
background = pygame.image.load("images\plevel1intro.png")
screen.blit(background, (0,0))
pygame.display.flip() #updates background

#running the program until something makes it stop            
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
        
    #if mouse button is down, open the first level of practice mode
    if event.type == pygame.MOUSEBUTTONDOWN:
        exec(open("practiceMode.py").read())
        
pygame.quit() #allows to exit game