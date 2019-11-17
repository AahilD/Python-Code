from SimpleGraphics import *

###Sky
background("light sky blue")
def sky():

    #Sun
    setOutline("gold")
    setFill("gold")
    ellipse(650, -100, 250, 250)

    #Cloud
    setOutline("black")
    setFill("white")
    blob(50, 225,
         125, 150,
         200, 225)

    blob(600, 300,
         725, 250,
         850, 300)

    blob(75, 100,
         110, 50,
         145, 50,
         175, 75,
         205, 50,
         240, 50,
         275, 75,
         310, 50,
         345, 50,
         380, 100,
         345, 150,
         310, 150,
         275, 125,
         240, 150,
         205, 150,
         175, 125,
         145, 150,
         110, 150)

sky()

###Grass
def grass():
    setOutline("chartreuse2")
    setFill("chartreuse4")
    rect(0, 400, 800, 600)

    #setOutline("black")
    #line(150, 525, 160, 510,
         #160, 510, 170, 525,)

grass()

###Builds The House
def house():
    setOutline("black")

    #Chimney
    setFill("Black")
    rect(500, 110, 50, 100)

    #House
    setFill("brown4")
    rect(200, 250, 400, 250)

    #Roof
    setFill("salmon4")
    blob(150, 250, 150, 250,
         400, 75, 400, 75,
         650, 250, 650, 250,)

    #Door
    setFill("dimgrey")
    rect(225, 350, 100, 150)

    setFill("black")
    ellipse(310, 425, 10, 10)

    #Windows
    setFill("lightgray")
    rect(450, 325, 50, 50)
    rect(450, 375, 50, 50)
    rect(500, 325, 50, 50)
    rect(500, 375, 50, 50)

    #Round Window
    setFill("lightgray")
    ellipse(364, 150, 75, 75)
    line(364, 186, 440, 186)
    line(400, 150, 400, 225)

house()

###Text
def name():
    setFont("Comic Sans", "15", "bold")
    text(700, 575, "Aahil Dawoodani")

name()
#####