#----------------------------
# Name: Section 4 Star
# Purpose: Work with turtle and for loops and creating functions
#
# Author: DrewV
#
# Created: 02/19/2026
#----------------------------
import turtle
"""
def greg (turt, length, points):
    for i in range(points):
        turt.forward(length)
        turt.right(180-(180/points))

drew = turtle.Turtle()
length = int(input("How long would you like the star sides to be? "))
points = int(input("How many points do you want your star to have? This only works for odd numbers. "))
greg(drew,length,points)
"""
def lady (turt, length):
    for i in range(5):
        turt.forward(length)
        turt.right(144)

werd = turtle.Turtle()
lady(werd,100)