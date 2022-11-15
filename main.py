"""
ITS 1801 F22 HW-09 
The program below does not run
Go to Blackboard and follow the instructions include in HW-09's the grading rubric to fix it
and change its functionality

"""

import turtle

# Global variables and objects
sideOfSquare = 
casper = turtle.Turtle()

# Function definitions
def square(turtleName, x,y):
  turtleName.penup()
  turtleName.goto(x,y)
  turtleName.pendown()
  turtleName.forward(sideOfSquare)
  turtleName.left(90)
  turtleName.forward(sideOfSquare)
  turtleName.left(90)
  turtleName.forward(sideOfSquare)
  turtleName.left(90)
  turtleName.forward(sideOfSquare)
  turtleName.left(90)

# Instructions for user
print ("Enter (x,y) coordinates to draw a square with a length of " + str(sideOfSquare) +"pixels")
print ("(x,y) specifiy the bottom left corner of the square")
print ("Your x and y coordinates should be between -150 and 150 pixels from the origin.")

# Ask for user input
xPositionStr = input("Enter the x coordinate for the bottom left vertex:")
yPositionStr = input("Enter the y coordinate for the bottom left vertex:")

xPosInt = int()
yPosInt = int()

if (xPosInt<) or (>150) or (yPosInt<) or (yPosInt>150):
  print("One of your coordinates is out of bounds, not drawing anything...")
else:
  print("Drawing a square at x = " + str() + " and y = " + str(yPositionStr))
  square(casper,#Parameter1,#Parameter2)





