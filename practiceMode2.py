"""
Authors: Anika Suman & Ayush Khanna
Date: 9/7/21
Class: Math 241 Scientific Computing
Professor: Ben Marlin

Description: Runs the second level of the Practice Mode, where the gallbladder must be properly removed from its place.
"""

#import statements to fetch modules
import os, pygame
from Drag import *
from wrongGBCoor import *
import time

pygame.init() #initializes pygame
font = pygame.font.SysFont('bahnschrift', 25) #sets the font (family & size) for the score display

#loads all music & audio for the game
correctSound = pygame.mixer.Sound('audio/right.mp3')
incorrectSound = pygame.mixer.Sound('audio/wrong.mp3')
bgMusic = pygame.mixer.Sound('audio/elevatorMusic.mp3')

clock = pygame.time.Clock() #creates a new Clock object that can be used to track an amount of time 
#sets unit variables for time
minutes = 0
seconds = 0
milliseconds = 0

#function to load body part images
def load_image(name, xS, yS):
    fullname=os.path.join("data", name) #forms the file path
    image=pygame.image.load(fullname) #loads the image given the file path
    
    #Scaling the sprite if a value greater than 0 is passed in for xS and yS
    if ((xS > 0) and (yS > 0)): 
        image = pygame.transform.scale(image, (xS, yS))

    return image, image.get_rect() #returning the image and the rectangle area of the image when called

def show_score(x,y,score):
    s = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(s, (x,y))
    
screen = pygame.display.set_mode((960, 540)) #sets the window size
pygame.display.set_caption('Practice Mode - Gallbladder Removal') #sets the window caption


background = pygame.image.load("images\practicemode1bg.png") #uploads the learn mode background
screen.blit(background, (0,0)) #projects the background at (0,0_)
body = pygame.image.load("images/gBbody.png")

#Guess Button Source: Self made on canva.com
guess = pygame.image.load("images\guessbutton.png")
guess = pygame.transform.scale(guess, (80, 28))

pygame.display.flip() #updates the screen

#loads each of the body parts that need to be dragged in
i1 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/gallbladder.png", 0, 0)

#calling the Ichrom class and passing arguments to its constructor
gallbladder = Drag(i1, (0, 0), 474, 251)

#uses the pygame.sprite method render plain to render the images
allsprites = pygame.sprite.RenderPlain(gallbladder)

#shows the mouse
pygame.mouse.set_visible(True)

running = True
#counters for score update for each part (add points only once per part)
gb = 0
score = 0
start = time.time() #take in the time before game starts
timesec = [] #seconds array
sC = 0 #sound count to make sure only one stream of music is playing at once

#running the program until something makes it stop
while running: #while the game is running, perform action
    #plays the background music    
    if sC == 0:    
        bgMusic.play()
        sC += 1

    #if milliseconds is over 1000, add 1 second & remove 1000 milliseconds    
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000

    #if seconds is over 60, add 1 minute & remove 60 seconds
    if seconds > 60:
        minutes += 1
        seconds -= 60

    milliseconds += clock.tick_busy_loop(60) #computes how many milliseconds have passed since the previous call with a framerate of 60
    timelabel = font.render("{}:{}".format(minutes, seconds), True, (0,0,0)) #display time
    
    
    sec = int(time.time() - start) #seconds between start time and present time
     #for every 10 seconds and if the value is not already in the array and is not 0
    if (sec % 10 == 0) and (sec not in timesec) and (sec != 0):
        score -= 10 #decrease score by 10
        timesec.append(sec) #add to timesec array so the same value is not checked again

        
    for event in pygame.event.get():
        #if the user quits the game, it stops running
        if event.type == pygame.QUIT:
            running = False
            
            
        #checks if mouse button is down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            #if the coordinates of the mouse-click match those of the back or home button, launch the respective screen
            if(x > 36) and (x < 75):
                if (y > 469) and (y < 505):
                    bgMusic.stop() 
                    exec(open("pMLevel2Intro.py").read()) #opens up homescreen when back button is clicked
            if (x > 89) and (x < 122):
                if (y > 470) and (y < 498):
                    bgMusic.stop() 
                    exec(open("main.py").read())
                    
            #if the clicked coordinate is in the array of coordinates that are incorrect, decrease score by 100                    
            if (x,y) in pieces:
                    score -= 100
                    bgMusic.stop()                        
                    incorrectSound.play()
                    bgMusic.play()
                    
            #uses the rollover function of the Drag class to Test if the mouse fly over a body part
            
            gallbladder.rollover()
            x1 = gallbladder.rect.x #x pos of tooth
            y1 = gallbladder.rect.y #y pos of tooth
            #if the tooth is dragged inside one of the boxes, add 200 points, and the counter is still 0            
            if(((x1 > 152) and (x1 < 240)) or ((x1 > 718) and (x1 < 807))) and gb == 0:
                if (y1 > 108) and (y1 < 284):
                    if(x > 442) and (x < 518):
                        if (y > 498) and (y < 519):
                            score += 500
                            bgMusic.stop() #stop bg music
                            correctSound.play() #play correctSound
                            bgMusic.play() #play bg music
                            gb += 1
            
            
        #update all sprites once moved
        allsprites.update()
        
        #blits other images and draw body parts to screen        
        screen.blit(background,(0,0))
        screen.blit(body, (350, 67))
        screen.blit(guess,(440, 495))
        screen.blit(timelabel,(154, 75))
        show_score(435,455,score)
        allsprites.draw(screen) #draws the teeth to the screen
        pygame.display.flip() #updates screen
 
        #if all part counters equal 1 (all part scores have been added once only) launch the level completed screen
        if gb == 1:
            bgMusic.stop() #stops music
            time.sleep(3) #wait 3 seconds to see score
            exec(open("pMLevel2Comp.py").read()) #launches next screen
    

pygame.quit() #allows to exit game
              