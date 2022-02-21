#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:13:08 2021

@author: rachelwildeson
OBJECTIVE:
    Click on the DARK BLUE bubble and you win the game!
    
RULES:
    If you click on anything other than the  DARK BLUE bubble,
    you will not win the game. In order to win the game,
    you must click on the DARK BLUE bubble!

CHALLENGE:
    There will be a lot of bubbles to distinguish from!

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
    
SHOW YOUR GAME TO A FRIEND:
    I showed this to my partner and he said I should try to incorporate movement and a feature that, upon
    clicking the dark blue bubble, resets the panel and shifts the bubbles to a new random location. I explained 
    the accesibility feature and he appreciated that. He also liked the variability between bubble size and mentioned
    that it takes a second for your mind to register where the correct bubble is located. 

"""
import turtle
import random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 600
h = 600
panel.setup(width=w, height=h)

# ================ VARIABLES  =========================
#colors
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

winningColor = (3, 3, 67) #midnight blue


# ================ CLASS AND FUNCTION SETUP  =========================

class Bubbles:
    ''' Creates a class for a bubble. Can change color and circle size '''
    def __init__(self, color, size):
        self.shape = turtle.Turtle(shape="circle")
        self.color = color
        self.shape.shapesize(size)
        self.shape.color(self.color)
        self.shape.up()


    def clickBubble (self,x,y):
        '''Prints statement "You Win" in the Command Line'''
        if self.color == (3,3,67):
            print("You Win!")
        
# =============  =========================

# bubble colors and sizing
bubbleOne = Bubbles(apricot,1) 
bubbleTwo = Bubbles(oldLavender,8) 
bubbleThree = Bubbles(englishLavender,5) 
bubbleFour = Bubbles(selectiveYellow,4) 
bubbleFive = Bubbles(babyBlueEyes,10) 
bubbleSix = Bubbles(pistachio,2) 
bubbleSeven = Bubbles(cottonCandy,3) 
bubbleEight = Bubbles(mediumCarminne,4) 
bubbleNine = Bubbles(tiffanyBlue,7) 
bubbleTen = Bubbles(black,9) 
bubbleEleven = Bubbles(tiffanyBlue,2)
bubbleTwelve = Bubbles(apricot, 6)
bubbleThirteen = Bubbles(englishLavender, 8)
bubbleFourteen = Bubbles(pistachio, 3)
bubbleFifteen = Bubbles(black, 2)

bubbleWinner = Bubbles(winningColor, 3) 

# ============= BUBBLE LOCATIONS  =========================
#bubble locations
bubbleOne.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleTwo.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleThree.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleFour.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleFive.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleSix.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleSeven.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleEight.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleNine.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleTen.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleEleven.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleTwelve.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleThirteen.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleFourteen.shape.goto(random.randint(-250,250), random.randint(-250,250))
bubbleFifteen.shape.goto(random.randint(-250,250), random.randint(-250,250))

#winning bubble
bubbleWinner.shape.goto(random.randint(-250,250), random.randint(-250,250))

bubbleWinner.shape.onclick(bubbleWinner.clickBubble)




panel.update()

# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup
