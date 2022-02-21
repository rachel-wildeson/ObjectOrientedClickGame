#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:16:54 2021

@author: rachelwildeson
Code modified from PC08

OBJECTIVE:
    Click on the DARK BLUE bubble and you win the game!
    
RULES:
    If you click on any other bubble than the  DARK BLUE bubble,
    you will lose the game. If you click on the DARK BLUE bubble, 
    the game will end as the game has been one.
CHALLENGE:
    There will are a few other bubbles on the screen. Each bubble 
    will move sporadically and quickly making them hard to catch. 
    Watch out for the distraction squares. If you click them, they will 
    get larger making the winning bubble harder to catch.
INTERACTION:
    The player must click on the correct DARK BLUE bubble in order
    to win the game!
HOW THE GAME IS TAILORED:
    I tailored the color choice to my bubbles using coolors.io. The most common type of color blindness is red/green.
    I used the "glasses" feature on coolors to create a palette that would yield easily distinguishable 
    colors for to include this group of users. I used dark blue as that was a close match between this type of 
    color blindness and non-color blind folks in terms of visibility and similarity in how the blue appears. 
    https://en.wikipedia.org/wiki/Color_blindness
    deuteranopia - red/green color blindness 
"""

import turtle
import random
# ================ VARIABLES  =========================

#colors losers
apricot = (255,205,178)
oldLavender = (109,104,117)
englishLavender = (181,131,141)
selectiveYellow = (255,186,8)
babyBlueEyes = (162,210,255)
pistachio = (144,190,109)
cottonCandy = (255,203,242)
mediumCarminne =  (164,74,63)
tiffanyBlue = (46,196,182)
black = (0,0,0)

#winning color
winningColor = (3, 3, 67) #midnight blue

# ================  SETUP FUNCTION  =========================
#setup function for the game and panel
def setup():
    global panel
    turtle.colormode(255) # accept 0-255 RGB values
    turtle.tracer(0) # turn off turtle's animation

    panel = turtle.Screen()
    w = 1200
    h = 1200
    panel.setup(width=w, height=h)

    global running
    running = True 

# ================ CLASS AND FUNCTION SETUP  =========================

class Bubbles(turtle.Turtle):
    ''' Creates a class for a bubble. Can change color and circle size '''
    def __init__(self, bubbleColor, size, x =0, y=0):
        super().__init__(shape = "circle")
        self.shapesize(size)
        self.color(bubbleColor)
        self.up()
        self.goto(x,y)
        
    def movementBubbles(self, leftAngle=10, distance =20, rightAngle=30):
        ''' Creates movement for the bubble class '''
        for i in range (2):
            self.speed(2)
            self.left(leftAngle)
            self.forward(distance)
            self.right(rightAngle)
            self.forward(distance)        
            for i in range (5):
                self.left(-leftAngle)
                self.forward(-distance)
                self.right(-rightAngle)
                self.forward(-distance)
        panel.update()
                    
    def clickBubble(self,x,y):
        ''' Winning bubble click interaction'''
        if self.color()[1] == (3,3,67):
            print("You Win!")

    def apricotClickBubble(self, x,y):
        ''' Losing bubble click interaction  '''
        if self.color()[1] == (apricot):
            print("You lost! Please restart the game!")
            global running
            running = False

    def oldLavenderClickBubble(self, x,y):
        ''' Losing bubble click interaction'''
        if self.color()[1] == (oldLavender):
            print("You lost! Please restart the game!")
            global running
            running = False            

    def englishLavenderClickBubble(self, x,y):
        ''' Losing bubble click interaction'''
        if self.color()[1] == (englishLavender):
            print("You lost! Please restart the game!")
            global running
            running = False
                
    def selectiveYellowClickBubble(self, x,y):
        ''' Losing bubble click interaction'''
        if self.color()[1] == (selectiveYellow):
            print("You lost! Please restart the game!") 
            global running
            running = False

    def babyBlueEyesClickBubble(self, x,y):
        '''Losing bubble click interaction '''
        if self.color()[1] == (babyBlueEyes):
            print("You lost! Please restart the game!")
            global running
            running = False
    
    def pistachioClickBubble(self, x,y):
        '''Losing bubble click interaction '''
        if self.color()[1] == (pistachio):
            print("You Lost! Please restart the game!")
            global running
            running = False
           
class Squares(turtle.Turtle):
    '''Creates a class for the distracting expanding squares '''
    def __init__(self, squareColor, size, x=0,y=0):
        super().__init__(shape = "square")
        self.color(squareColor)
        self.shapesize(size)
        self.up()
        self.goto(x,y)
        self.onclick(self.clickSquare)
    
    def clickSquare(self,x,y):
        '''Method for increasing shape size of square '''
        self.shapesize(10)
        panel.update()
  
# =============  =========================

class bubbleGame():
    def __init__(self):
        bubbleOne = Bubbles(apricot, 1, random.randint(-250,250), random.randint(-250,250))
        bubbleTwo = Bubbles(oldLavender, 8, random.randint(-250,250), random.randint(-250,250))
        bubbleThree = Bubbles(englishLavender, 5, random.randint(-250,250), random.randint(-250,250))
        bubbleFour = Bubbles(selectiveYellow, 4, random.randint(-250,250), random.randint(-250,250))
        bubbleFive = Bubbles(babyBlueEyes, 10, random.randint(-250,250), random.randint(-250,250))
        bubbleSix = Bubbles(pistachio, 7, random.randint(-250,250), random.randint(-250,250))
        bubbleSeven = Bubbles(oldLavender, 4, random.randint(-250,250), random.randint(-250,250))
        bubbleEight = Bubbles(englishLavender, 2, random.randint(-250,250), random.randint(-250,250))
        bubbleNine = Bubbles(selectiveYellow, 6, random.randint(-250,250), random.randint(-250,250))
        bubbleTen = Bubbles(apricot, 8, random.randint(-250,250), random.randint(-250,250))
        winnerBubble = Bubbles(winningColor,3,random.randint(-250,250), random.randint(-250,250))
   
        # distraction squares     
        firstSquare = Squares("black", 2, -200,-200)
        secondSquare = Squares("black", 2, 200,-200)
        thirdSquare = Squares("black", 2, 200,200)
        fourthSquare = Squares("black", 2, -0,-0)
        fifthSquare = Squares("black", 2, -150,200)
        
        firstSquare.onclick(firstSquare.clickSquare)
        secondSquare.onclick(secondSquare.clickSquare)
        thirdSquare.onclick(thirdSquare.clickSquare)
        fourthSquare.onclick(fourthSquare.clickSquare)
        fifthSquare.onclick(fifthSquare.clickSquare)
        
        
        winnerBubble.onclick(winnerBubble.clickBubble)
        bubbleOne.onclick(bubbleOne.apricotClickBubble)
        bubbleTwo.onclick(bubbleTwo.oldLavenderClickBubble)
        bubbleThree.onclick(bubbleThree.englishLavenderClickBubble)
        bubbleFour.onclick(bubbleFour.selectiveYellowClickBubble)
        bubbleFive.onclick(bubbleFive.babyBlueEyesClickBubble)
        bubbleSix.onclick(bubbleSix.pistachioClickBubble)
        bubbleSeven.onclick(bubbleSeven.oldLavenderClickBubble)
        bubbleEight.onclick(bubbleEight.englishLavenderClickBubble)
        bubbleNine.onclick(bubbleNine.selectiveYellowClickBubble)
        bubbleTen.onclick(bubbleTen.apricotClickBubble)
            
        # =============  =========================
        
        while running:
    
            winnerBubble.movementBubbles()
            bubbleOne.movementBubbles()
            bubbleTwo.movementBubbles()
            bubbleThree.movementBubbles()
            bubbleFour.movementBubbles()
            bubbleFive.movementBubbles()
            bubbleSix.movementBubbles()
            bubbleSeven.movementBubbles()
            bubbleEight.movementBubbles()
            bubbleNine.movementBubbles()
            bubbleTen.movementBubbles()


setup()
if __name__=='__main__':
    bubbleGame()

# ================== SETUP & ANIMATION =====================
    turtle.mainloop() # cleanup and listening for user interactions
        
""" I had my partner play the game I created and he commented that the game was fun and simple. He appreciated 
that I incorporated movement into the game and said the interactions were fun and engaging and could be expanded 
beyond these current features even further.  """