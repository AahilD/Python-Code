
import tkinter as Tk
from graphics import *

x = 700
y = 500


def main():
    #Creates Screen
    win = GraphWin("Test Window",x, y)
    win.setBackground(color_rgb(211, 211, 211))

    #Creates Title
    header = Rectangle(Point(x-25, 25), Point(25, y/2))
    header.setFill(color_rgb(100, 100, 100))
    header.draw(win)

    Label= (win, text = "Hello World!").pack()






    win.getMouse()
    win.close()



main()