from turtle import *
import math

#My Variables
bob = Turtle()
name = ""
sides = 0

print("My name is bob.")

#get input
name = input("What's your name?")
sides = int(input("How many sides do you for the polygon?"))

#output
print ("Hi "+ name + ".  Look what I drew!")
print("Run the program again to draw another shape with me!")

#position
bob.setposition (0,0)

#bob.pencolor #BB8FCE  
bob.pencolor("purple")

#loop - includes movement
for i in range(sides):
    bob.forward(100)
    bob.left(360/sides)


