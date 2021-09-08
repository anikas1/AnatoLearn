"""
Authors: Anika Suman & Ayush Khanna
Date: 9/7/21
Class: Math 241 Scientific Computing
Professor: Ben Marlin

Description: Runs the first level of the Learn Mode, where parts of the skeletal system must be dragged into the appropriate areas.
"""

#import statements to fetch modules
import os, pygame
from pygame.locals import*
from Drag import *
from tkinter import *
import time

pygame.init() #initializes pygame

score = 0 #declares and initializes a score variable
font = pygame.font.SysFont('bahnschrift', 25) #sets the font (family & size) for the score display

#loads all music & audio for the game
#Source: https://mixkit.co/free-sound-effects/
correctSound = pygame.mixer.Sound('audio/right.mp3')
incorrectSound = pygame.mixer.Sound('audio/wrong.mp3')
#Source: https://www.youtube.com/watch?v=jj0ChLVTpaA
bgMusic = pygame.mixer.Sound('audio/elevatorMusic.mp3')


#function to load body part images
def load_image(name, xS, yS):
    fullname=os.path.join("data", name) #forms the file path
    image=pygame.image.load(fullname) #loads the image given the file path
    
    #scales the sprite if a value greater than 0 is passed in for xS and yS
    if ((xS > 0) and (yS > 0)): 
        image = pygame.transform.scale(image, (xS, yS))

    return image, image.get_rect() #returns the image and the rectangle area of the image when called

#function to display the score
def show_score(x,y,score):
    s = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(s, (x,y))
    
screen = pygame.display.set_mode((960, 540)) #sets the window size
pygame.display.set_caption('Learn Mode - Skeletal System') #sets the window caption

#Skeletal System Img Source: https://www.gettyimages.com/detail/photo/joint-pain-blue-human-anatomy-body-and-skeleton-3d-royalty-free-image/688724536
#Background Img Source: https://img.freepik.com/free-photo/black-futuristic-stand-with-blue-neon-lights-scientific-podium_167650-1636.jpg?size=626&ext=jpg&ga=GA1.2.320087390.1627862400
background2 = pygame.image.load("images\learnmode1bg.png") #uploads the learn mode background
screen.blit(background2, (0,0)) #projects the background at (0,0)

#loads the purple circles -- only for stylistic purposes to indicate to the user viable spots for part placement
pC1 = pygame.image.load("images\purpleCircle.png")
pC1 = pygame.transform.scale(pC1, (8, 8))

pC2 = pygame.image.load("images\purpleCircle.png")
pC2 = pygame.transform.scale(pC2, (8, 8))

pC3 = pygame.image.load("images\purpleCircle.png")
pC3 = pygame.transform.scale(pC3, (8, 8))

pC4 = pygame.image.load("images\purpleCircle.png")
pC4 = pygame.transform.scale(pC4, (8, 8))

pC5 = pygame.image.load("images\purpleCircle.png")
pC5 = pygame.transform.scale(pC5, (8, 8))


#loads and scales the guess button
guess = pygame.image.load("images\guessbutton.png")
guess = pygame.transform.scale(guess, (80, 28))

pygame.display.flip() #updates the screen

#loads each of the body parts that need to be dragged in, calling the user-defined load_image method
i1 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/Femur.png", 0, 0)
i2 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/Radius.png", 0, 0)
i3 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/pelvis.png", 57, 44)
i4 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/Fibula.png", 0, 0)
i5 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/Humerus.png", 0, 0)

#calling the Drag class and passing arguments to its constructor
femur = Drag(i1, (0, 0), 753, 175)
radius = Drag(i2, (0, 0), 148, 228)
pelvis = Drag(i3, (0, 0), 175, 150)
fibula = Drag(i4, (0, 0), 818, 177)
humerus = Drag(i5, (0, 0), 205, 217)

#uses the pygame.sprite method RenderPlain to render the body part images
allsprites = pygame.sprite.RenderPlain((femur,radius,pelvis,fibula,humerus))

#shows the mouse
pygame.mouse.set_visible(True)


running = True

#counters for score update for each part (add points only once per part)
f1 = 0
r1 = 0
p1 = 0
f2 = 0
h1 = 0
sC = 0 #sound count to make sure only one stream of music is playing at once

#running the program until something makes it stop
while running: #while the game is running, perform action                        
    #plays the background music    
    if sC == 0:    
        bgMusic.play()
        sC += 1
        
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
                    exec(open("lev1intro.py").read())
            if (x > 89) and (x < 122):
                if (y > 470) and (y < 498):
                    bgMusic.stop() 
                    exec(open("main.py").read())
            
            #uses the rollover function of the Drag class to test if the mouse is over a body part
            
            #--------------------------------------------------------------femur code--------------------------------------------------------------
            femur.rollover()
            if femur.rect.collidepoint((492,278)) and f1 == 0: #if the rectangle area around the image collides with the respective coordinate of the goal coordinate and the counter is still 0, go through
                #if the guess button is clicked    
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100 #add 100 points
                        f1 += 1 #increase counter so points cannot be added for the same part again
                        bgMusic.stop() #temporarily stops the music so the correctSound can play
                        correctSound.play() #plays correctSound
                        bgMusic.play() #plays background music again
                        
                        #https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window
                        root = Tk() #set root to the Tkinter pop-up
                        root.withdraw() #remove the root and only keep the origin pop-up message box
                        
                        #show the info on the messagebox
                        #Source: https://teachmeanatomy.info/lower-limb/bones/femur/#:~:text=The%20femur%20is%20the%20only,%3B%20proximal%2C%20shaft%20and%20distal. 
                        messagebox.showinfo('More Info', 'The femur is the only bone in the thigh and the longest bone in the body. The main function of the femur is weight bearing and stability of walking.')
                        
            #if the femur collides with a wrong goal coordinate, go through
            if femur.rect.collidepoint((409,235)) or femur.rect.collidepoint((462,232)) or femur.rect.collidepoint((449,374)) or femur.rect.collidepoint((508,168)):
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100 #decrease score by 100
                        bgMusic.stop() #stop background music
                        incorrectSound.play() #play the incorrectSound
                        bgMusic.play() #play the background music again   
                
            #--------------------------------------------------------------radius code--------------------------------------------------------------
            radius.rollover()
            if radius.rect.collidepoint((409,235)) and r1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        r1 += 1
                        bgMusic.stop()
                        correctSound.play()
                        bgMusic.play()
                        root = Tk()
                        root.withdraw()
                        #Source: https://www.britannica.com/science/radius-bone
                        messagebox.showinfo('More Info', 'The radius is the outer of the two bones of the forearm when viewed with the palm facing forward. All land vertebrates have this bone. In humans, it is shorter than the other bone of the forearm, the ulna.')
            
            if radius.rect.collidepoint((492,278)) or radius.rect.collidepoint((462,232)) or radius.rect.collidepoint((449,374)) or radius.rect.collidepoint((508,168)):
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()
                        incorrectSound.play()
                        bgMusic.play()
                        
            #--------------------------------------------------------------pelvis code--------------------------------------------------------------                       
            pelvis.rollover()
            if pelvis.rect.collidepoint((462,232)) and p1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        p1 += 1
                        bgMusic.stop()
                        correctSound.play()
                        bgMusic.play()
                        root = Tk()
                        root.withdraw()
                        
                        #Source: https://www.britannica.com/science/pelvis
                        messagebox.showinfo('More Info', 'The pelvis, also called the bony pelvis or pelvic girdle, is a basin-shaped complex of bones that connects the trunk and the legs, supports and balances the trunk, and contains and supports the intestines, the urinary bladder, and the internal sex organs.')
           
            if pelvis.rect.collidepoint((409,235)) or pelvis.rect.collidepoint((492,278)) or pelvis.rect.collidepoint((449,374)) or pelvis.rect.collidepoint((508,168)):
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()
                        incorrectSound.play()
                        bgMusic.play()
                        
            #--------------------------------------------------------------fibula code--------------------------------------------------------------                
            fibula.rollover()
            if fibula.rect.collidepoint((449,374)) and f2 == 0:
               if(x > 442) and (x < 518):
                   if (y > 498) and (y < 519):
                       score += 100
                       f2 += 1
                       bgMusic.stop()
                       correctSound.play()
                       bgMusic.play()
                       root = Tk()
                       root.withdraw()
                       
                       #Source: https://www.innerbody.com/image_skelfov/skel27_new.html 
                       messagebox.showinfo('More Info', 'The fibula is the long, thin and lateral bone of the lower leg. It runs parallel to the tibia, or shin bone, and plays a significant role in stabilizing the ankle and supporting the muscles of the lower leg.')
                       
            if fibula.rect.collidepoint((409,235)) or fibula.rect.collidepoint((462,232)) or fibula.rect.collidepoint((492,278)) or fibula.rect.collidepoint((508,168)):
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()
                        incorrectSound.play()
                        bgMusic.play()
                        
            #--------------------------------------------------------------humerus code--------------------------------------------------------------                        
            humerus.rollover()
            if humerus.rect.collidepoint((508,168)) and h1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        h1 += 1
                        bgMusic.stop()
                        correctSound.play()
                        bgMusic.play()
                        root = Tk()
                        root.withdraw()
                        
                        #Source: https://www.healthline.com/health/humerus-bone
                        messagebox.showinfo('More Info', 'The humerus is the bone in your upper arm. It is located between your elbow and your shoulder, and is the longest bone in the arm. The humerus serves as an attachment to 13 muscles which contribute to the movements of the hand and elbow, and therefore the function of the upper limb.')
                        
            if humerus.rect.collidepoint((409,235)) or humerus.rect.collidepoint((462,232)) or humerus.rect.collidepoint((449,374)) or humerus.rect.collidepoint((492,278)):
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()
                        incorrectSound.play()
                        bgMusic.play()                        
                        
        #updates all sprites once moved
        allsprites.update()
        
        #blits other images and draw body parts to screen
        screen.blit(background2,(0,0))
        screen.blit(pC1, (460, 232))
        screen.blit(pC2, (404, 235))
        screen.blit(pC3, (505, 168))
        screen.blit(pC4, (489, 278))
        screen.blit(pC5, (442, 374))
        screen.blit(guess,(440, 495))
        show_score(410,10,score)
        allsprites.draw(screen)
        pygame.display.flip() #updates screen
        
        #if all body part counters equal 1 (all part scores have been added once only) launch the level completed screen
        if f1 == 1 and r1 == 1 and p1 == 1 and f2 == 1 and h1 == 1:
            bgMusic.stop() #stops music
            time.sleep(3) #waits 3 seconds to see score
            exec(open("lev1comp.py").read()) #launches next screen

pygame.quit() #allows to exit game
         