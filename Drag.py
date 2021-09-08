# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:20:18 2021

@author: anika
"""
import os, pygame
from pygame.locals import*

class Drag(pygame.sprite.Sprite):
    
    def __init__(self,image,initpos, x, y):
        #super().init()
        pygame.sprite.Sprite.__init__(self)
        #self.pos = initpos
        #self.image = pygame.Surface((375, 225))
        self.image, self.rect=image
        self.rect.midtop = (x,y)
        self.button=(0,0,0)#mouse buttons not pressed
        self.selected = 0
        self.mouseover=False
        self.focused=False
        #print ("init chrom at "),self.pos

   
    def rollover(self):
        """Test if the mouse fly over a body part
       self.mouseover==True if mouse flying over the part,
       False if not"""
        mpos=pygame.mouse.get_pos()#mouseposition
        #test if mouse roll over the sprite
        if self.rect.collidepoint(mpos):
            self.mouseover=True
        else:
            self.mouseover=False
        
    def update(self):
        self.button = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()
        self.selected=self.rect.collidepoint(mpos)
        #the mouse flies over a part
        if (self.mouseover):
            if self.button==(1,0,0):  
                pos = pygame.mouse.get_pos()
                self.rect.midtop = pos
