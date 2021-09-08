"""
Authors: Anika Suman & Ayush Khanna
Date: 9/7/21
Class: Math 241 Scientific Computing
Professor: Ben Marlin
 
Description: Runs the second level of the Learn Mode, where parts of the digestive and lymphatic system must be dragged into the appropriate areas.
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
correctSound = pygame.mixer.Sound('audio/right.mp3')
incorrectSound = pygame.mixer.Sound('audio/wrong.mp3')
bgMusic = pygame.mixer.Sound('audio/elevatorMusic.mp3')
 
#function to load body part images
def load_image(name, xS, yS):
    fullname=os.path.join("data", name) #forms the file path
    image=pygame.image.load(fullname) #loads the image given the file path
    
    #Scales the sprite if a value greater than 0 is passed in for xS and yS
    if ((xS > 0) and (yS > 0)): 
        image = pygame.transform.scale(image, (xS, yS))
 
    return image, image.get_rect() #returning the image and the rectangle area of the image when called
 
#function to display the score
def show_score(x,y,score):
    s = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(s, (x,y))
    
screen = pygame.display.set_mode((960, 540)) #sets the window size
pygame.display.set_caption('Learn Mode - Digestive + Lymphatic System')
 
#Digestive + Lymphatic System Img Source: https://www.superstock.com/stock-photos-images/4378-716
#Background Img Source: https://img.freepik.com/free-photo/black-futuristic-stand-with-blue-neon-lights-scientific-podium_167650-1636.jpg?size=626&ext=jpg&ga=GA1.2.320087390.1627862400
background = pygame.image.load("images\learnmode2bg.png") #uploads the learn mode background
screen.blit(background, (0,0)) #projects the background at (0,0)
 
 
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
 
pC6 = pygame.image.load("images\purpleCircle.png")
pC6 = pygame.transform.scale(pC6, (8, 8))
 
pC7 = pygame.image.load("images\purpleCircle.png")
pC7 = pygame.transform.scale(pC7, (8, 8))
 
 
#loads and scales the guess button
guess = pygame.image.load("images\guessbutton.png")
guess = pygame.transform.scale(guess, (80, 28))
 
pygame.display.flip() #updates the screen
 
#loads each of the body parts that need to be dragged in, calling the user-defined load_image method
 
i1 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/anus.png", 6, 15)
i2 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/esophagus.png", 16, 82)
i3 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/kidney.png", 16, 29)
i4 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/liver.png", 32, 45)
i5 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/pancreas.png", 24, 18)
i6 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/small intestine.png", 40, 48)
i7 = load_image("C:/Anika/School/ECG/11th Grade/3 wk - MATH 241 - Scientific Computing/AnatoLearn/images/spleen.png", 14, 20)
 
#calling the Drag class and passing arguments to its constructor
anus = Drag(i1, (0, 0), 171, 220)
esophagus = Drag(i2, (0, 0), 755, 177)
kidney = Drag(i3, (0, 0), 137, 151)
liver = Drag(i4, (0, 0), 200, 145)
pancreas = Drag(i5, (0, 0), 205, 275)
smallIntestine = Drag(i6, (0, 0), 805, 197)
spleen = Drag(i7, (0, 0), 145, 280)
 
 
#uses the pygame.sprite method render plain to render the images
allsprites = pygame.sprite.RenderPlain((anus,esophagus,kidney,liver,pancreas,smallIntestine,spleen))
 
#shows the mouse
pygame.mouse.set_visible(True)
 
running = True
 
#counters for score update for each part (add points only once per part)
a1 = 0
e1 = 0
k1 = 0
l1 = 0
p1 = 0
s1 = 0
s2 = 0
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
                    exec(open("lev1comp.py").read()) #opens up homescreen when back button is clicked
            if (x > 89) and (x < 122):
                if (y > 470) and (y < 498):
                    bgMusic.stop() 
                    exec(open("main.py").read())
            
           #uses the rollover function of the Drag class to test if the mouse is over a body part
           
           #--------------------------------------------------------------anus code--------------------------------------------------------------
           
            anus.rollover()
            if anus.rect.collidepoint((485,256)) and a1 == 0: #if the rectangle area around the image collides with the respective coordinate of the goal coordinate and the counter is still 0, go through
                #if the guess button is clicked
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100 #add 100 points
                        a1 += 1 #increase counter so points cannot be added for the same part again
                        bgMusic.stop() #temporarily stops the music so the correctSound can play
                        correctSound.play() #plays correctSound
                        bgMusic.play() #plays background music again
                        
                        #https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window
                        root = Tk() #set root to the Tkinter pop-up
                        root.withdraw() #remove the root and only keep the origin pop-up message box
                        
                        #show the info on the messagebox
                        #Source: https://www.saintlukeskc.org/health-library/anatomy-anus
                        messagebox.showinfo('More Info', 'The anus is the last part of the digestive tract. It is at the end of the rectum and is where stool comes out of the body. It consists of a muscular ring (called a sphincter) that opens during a bowel movement to allow stool to pass through.')
                        
            if (anus.rect.collidepoint((485,138)) or anus.rect.collidepoint((472,187)) or anus.rect.collidepoint((504,174)) or anus.rect.collidepoint((485,190)) or anus.rect.collidepoint((482,212)) or anus.rect.collidepoint((463,176))) and a1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()
                        incorrectSound.play()
                        bgMusic.play()
                
            #--------------------------------------------------------------esophagus code--------------------------------------------------------------
        
            esophagus.rollover()
            if esophagus.rect.collidepoint((485,138)) and e1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        e1 += 1
                        bgMusic.stop()                        
                        correctSound.play()
                        bgMusic.play()                        
                        root = Tk()
                        root.withdraw()
                        #Source: https://www.webmd.com/digestive-disorders/picture-of-the-esophagus#:~:text=The%20esophagus%20is%20a%20muscular,in%20front%20of%20the%20spine. 
                        messagebox.showinfo('More Info', 'The esophagus is a muscular tube connecting the throat (pharynx) with the stomach. It is about 8 inches long, and it is lined by moist pink tissue called the mucosa. The esophagus runs behind the windpipe (trachea) and heart, and in front of the spine.')
            
            if (esophagus.rect.collidepoint((485,256)) or esophagus.rect.collidepoint((472,187)) or esophagus.rect.collidepoint((504,174)) or esophagus.rect.collidepoint((485,190)) or esophagus.rect.collidepoint((482,212)) or esophagus.rect.collidepoint((463,176))) and e1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()                        
                        incorrectSound.play()
                        bgMusic.play()                        
                        
            #--------------------------------------------------------------kidney code--------------------------------------------------------------                      
            
            kidney.rollover()
            if kidney.rect.collidepoint((472,187)) and k1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        k1 += 1
                        bgMusic.stop()                        
                        correctSound.play()
                        bgMusic.play()                        
                        root = Tk()
                        root.withdraw()
                        #Source: https://www.niddk.nih.gov/health-information/kidney-disease/kidneys-how-they-work#:~:text=The%20kidneys%20are%20two%20bean,extra%20water%20to%20make%20urine. 
                        messagebox.showinfo('More Info', 'The kidneys are two bean-shaped organs, each about the size of a fist. They are located just below the rib cage, one on each side of your spine. Healthy kidneys filter about a half cup of blood every minute, removing wastes and extra water to make urine.')
           
            if (kidney.rect.collidepoint((485,256)) or kidney.rect.collidepoint((485,138)) or kidney.rect.collidepoint((504,174)) or kidney.rect.collidepoint((485,190)) or kidney.rect.collidepoint((482,212)) or kidney.rect.collidepoint((463,176))) and k1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()                        
                        incorrectSound.play()
                        bgMusic.play()                        
                        
            #--------------------------------------------------------------liver code--------------------------------------------------------------                
            
            liver.rollover()
            if liver.rect.collidepoint((504,174)) and l1 == 0:
               if(x > 442) and (x < 518):
                   if (y > 498) and (y < 519):
                       score += 100
                       l1 += 1
                       bgMusic.stop()                       
                       correctSound.play()
                       bgMusic.play()                      
                       root = Tk()
                       root.withdraw()
                       #Source: https://columbiasurgery.org/liver/liver-and-its-functions 
                       messagebox.showinfo('More Info', 'The liver is the largest solid organ in the body. It removes toxins from the blood supply of the body, produces bile to digest fats maintains healthy blood sugar levels, regulates blood clotting, and performs hundreds of other vital functions. It is located beneath the rib cage in the right upper abdomen.')
                       
            if (liver.rect.collidepoint((485,138)) or liver.rect.collidepoint((472,187)) or liver.rect.collidepoint((485,256)) or liver.rect.collidepoint((485,190)) or liver.rect.collidepoint((482,212)) or liver.rect.collidepoint((463,176))) and l1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()                        
                        incorrectSound.play()
                        bgMusic.play()                        
            #--------------------------------------------------------------pancreas code--------------------------------------------------------------                        
            
            pancreas.rollover()
            if pancreas.rect.collidepoint((485,190)) and p1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        p1 += 1
                        bgMusic.stop()                        
                        correctSound.play()
                        bgMusic.play()                        
                        root = Tk()
                        root.withdraw()
                        #Source: https://www.medicalnewstoday.com/articles/10011 
                        messagebox.showinfo('More Info', 'The pancreas is a gland organ located in the abdomen. It is part of the digestive and endocrine system, producing the hormone insulin and secreting it into the bloodstream; insulin regulates glucose or sugar level.')
                        
            if (pancreas.rect.collidepoint((485,138)) or pancreas.rect.collidepoint((472,187)) or pancreas.rect.collidepoint((504,174)) or pancreas.rect.collidepoint((485,256)) or pancreas.rect.collidepoint((482,212)) or pancreas.rect.collidepoint((463,176))) and p1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()                        
                        incorrectSound.play()
                        bgMusic.play()                        
                           
            #--------------------------------------------------------------smallIntestine code--------------------------------------------------------------                       
            smallIntestine.rollover()
            if smallIntestine.rect.collidepoint((482,212)) and s1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        s1 += 1
                        bgMusic.stop()                        
                        correctSound.play()
                        bgMusic.play()                        
                        root = Tk()
                        root.withdraw()
                        
                        #Sources: https://www.seattlechildrens.org/clinics/transplant/intestine/how-the-small-intestine-works/#:~:text=The%20small%20intestine%2C%20or%20small,the%20nutrients%20from%20the%20food.&text=The%20duodenum%20is%20the%20first%20part%20of%20the%20small%20intestine. , https://www.chp.edu/our-services/transplant/intestine/education/about-small-large-intestines#:~:text=The%20large%20intestine%20is%20much,any%20waste%20products%20left%20over. 
                        messagebox.showinfo('More Info', 'The small intestine, or small bowel, is a hollow tube about 20 feet long that runs from the stomach to the beginning of the large intestine. The small intestine breaks down food from the stomach and absorbs much of the nutrients from the food. The large intestine, on the other hand, is responsible for the absorption of water and electrolytes.')
                        
            if (smallIntestine.rect.collidepoint((485,138)) or smallIntestine.rect.collidepoint((472,187)) or smallIntestine.rect.collidepoint((504,174)) or smallIntestine.rect.collidepoint((485,190)) or smallIntestine.rect.collidepoint((485,256)) or smallIntestine.rect.collidepoint((463,176))) and s1 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()                       
                        incorrectSound.play()
                        bgMusic.play()
                        
            #--------------------------------------------------------------spleen code--------------------------------------------------------------
            
            spleen.rollover()
            if spleen.rect.collidepoint((463,176)) and s2 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519):
                        score += 100
                        s2 += 1
                        bgMusic.stop()                        
                        correctSound.play()
                        bgMusic.play()                        
                        root = Tk()
                        root.withdraw()
                        #Source: https://my.clevelandclinic.org/health/body/21567-spleen 
                        messagebox.showinfo('More Info', 'The spleen is part of the lymphatic system (which is part of the immune system). It stores and filters blood and makes white blood cells that protect you from infection. A ruptured (torn) spleen can be fatal.')
                        
            if (spleen.rect.collidepoint((485,138)) or spleen.rect.collidepoint((472,187)) or spleen.rect.collidepoint((504,174)) or spleen.rect.collidepoint((485,190)) or spleen.rect.collidepoint((482,212)) or spleen.rect.collidepoint((485,256))) and s2 == 0:
                if(x > 442) and (x < 518):
                    if (y > 498) and (y < 519): 
                        score -= 100
                        bgMusic.stop()                        
                        incorrectSound.play()
                        bgMusic.play()                        
                        
                        
            
        #update all sprites once moved
        allsprites.update()
        
        #blits other images and draw body parts to screen        
        screen.blit(background,(0,0))
        screen.blit(pC1, (480,256))
        screen.blit(pC2, (480,138))
        screen.blit(pC3, (467,187))
        screen.blit(pC4, (502,175))
        screen.blit(pC5, (480,190))
        screen.blit(pC6, (477,212))
        screen.blit(pC7, (458,176))
        screen.blit(guess,(440, 495))
        show_score(410,10,score)
        allsprites.draw(screen)
        pygame.display.flip() #updates screen
        
        #if all body part counters equal 1 (all part scores have been added once only) launch the level completed screen
        if a1 == 1 and e1 == 1 and k1 == 1 and l1 == 1 and p1 == 1 and s1 == 1 and s2 == 1:
            bgMusic.stop() #stops music
            time.sleep(3) #wait 3 seconds to see score
            exec(open("lev2comp.py").read()) #launches next screen
 
pygame.quit() #allows to exit game
