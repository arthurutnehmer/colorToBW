#! /usr/bin/python
# Exercise No. 01
# File Name: hw12project1.py
# Programmer: Arthur Utnehmer
# Date: May. 6, 2020
#
# Problem Statement:
# 1. Modify the Dice Poker program from this chapter to include any or all of the following features:
#
# a) Splash Screen. When the program first fires up, have it print a short introductory message about the program and
# buttons for "Let's Play'' and "Exit." The main interface shouldn't appear unless the user se­ lects "Let's Play."
#
# import necessary python libraries

from guipoker import *
from graphics import *
from pokerapp import PokerApp
from button import Button
from cdieview import ColorDieView



def shortMessage():

    win = GraphWin("Dice Poker" , 400, 300)
    win.setCoords(0.0, 0.0, 400, 300)

    #Ask the user if they want to play or not.
    Text(Point(200,200) , "Welcome to Dice Poker").draw(win).setSize(20)
    letsPlayButton = Rectangle(Point(70,135), Point(130, 167))
    letsPlayButton.draw(win).setFill("green")
    NoWayButton = Rectangle(Point(270,135), Point(330, 167)).draw(win).setFill("red")
    Text(Point(100,150) , "Lets Play").draw(win)
    Text(Point(300,150) , "NO WAY").draw(win)
    letsPlay = False
    exit = False

    while(True):

        point = checkWherePressed(win)
        letsPlay = checkIfletsPlayWasClicked(point)
        exit = (checkIfNoWayWasPressed(point))

        if(exit):
            win.close()
            return False
        elif(letsPlay):
            win.close()
            return True


def checkWherePressed(win):
    clickPoint = win.getMouse()
    return clickPoint

def checkIfletsPlayWasClicked(point):
    if(70 < point.getX() < 130  and (135 < point.getY() < 167 )):
        return True
    else:
        return False

def checkIfNoWayWasPressed(point):
    if(270 < point.getX() < 330  and (135 < point.getY() < 167 )):
        return True
    else:
        return False


startGame = shortMessage()
if(startGame):
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()

