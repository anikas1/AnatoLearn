# AnatoLearn

REQUIRED MODULES
----------------------------------------
pygame is the primary module we use for our program, and is the only module that needs to be installed


INSTALLATION
----------------------------------------
If using Anaconda, entering 
	pip install pygame
installs the pygame module to the Anaconda environment.


DESCRIPTION OF EACH FILE
----------------------------------------
main.py
Root file that projects the homescreen, adds functionality to the buttons, and launches the learn and practice modes.

Drag.py
Defines functions to allow an image to be draggable by the user, later imported to all levels and modes of play.

lev1intro.py
Projects the intro page and rules for the first level of the Learn Mode.

learnMode.py
Runs the first level of the Learn Mode, where parts of the skeletal system must be dragged into the appropriate areas.

lev1comp.py
Projects the level completed page, and displays the correct finished image for the first level of the Learn Mode. Provides the transition screen to Level 2.

learnMode2.py
Runs the second level of the Learn Mode, where parts of the digestive and lymphatic system must be dragged into the appropriate areas.

lev2comp.py
Projects the level completed page, and displays the correct finished image for the second level of the Learn Mode. Provides the transition screen to return to the home page.

pMLevel1Intro.py
Projects the intro page and rules for the first level of the Practice Mode.

practiceMode.py
Runs the first level of the Practice Mode, where the wisdom teeth must be properly removed from their place.

wrongTeethCoordinates.py
Creates an array of the coordinates of the wrong teeth (not the wisdom teeth) to be imported and used for score deduction in practiceMode.py.

pMLevel1Comp.py
Projects the level completed page, and displays the correct finished image for the first level of the Practice Mode.

pMLevel2Intro.py 
Projects the intro page and rules for the second level of the Practice Mode.

practiceMode2.py
Runs the second level of the Practice Mode, where the gallbladder must be properly removed from its place.

wrongGBCoor.py
Creates an array of the coordinates of the wrong body parts (not the gallbladder) to be imported and used for score deduction in practiceMode2.py.

pMLevel2Comp.py
Projects the level completed page, and displays the correct finished image for the second level of the Practice Mode. Provides the transition screen to return to the home page.


TROUBLESHOOTING
----------------------------------------
The main error that may come up when trying to run all the code is that the path names will need to be switched as they are specific to the path directories of the authors in the current state of the game.
