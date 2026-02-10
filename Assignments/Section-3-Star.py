#----------------------------
# Name: Section 3 Star
# Purpose: Work with turtle and for loops
#
# Author: DrewV
#
# Created: 02/09/2026
#----------------------------
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
#set up the turtle and get it to the correct position
drew = turtle.Turtle()
drew.speed(10)
drew.color("blue")
drew.shape("turtle")
drew.penup()
drew.stamp()
drew.forward(105)
#start the clock orientation
for i in range(12):
    drew.pendown()
    drew.forward(10)
    drew.penup()
    drew.forward(20)
    drew.stamp()
    drew.backward(15)
    drew.right(120)
    drew.forward(60)
    drew.left(90)
drew.hideturtle()
wn.mainloop()

