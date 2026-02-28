#----------------------------
# Name: Section 5 Turtle Chart
# Purpose: Work with turtle and create a different colored chart
#
# Author: DrewV
#
# Created: 02/28/2026
#----------------------------
import turtle
def draw_bar(t, height):
    
    if height < 100:
        t.color("skyblue", "green")
    elif 100 <= height <= 200:
        t.color("skyblue", "yellow")
    else:
        t.color("skyblue", "red")
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write('  ' + str(height))
    t.right(90)
    t.forward(40)         
    t.right(90)
    t.forward(height)    
    t.left(90)
    t.end_fill()
    t.up()
    t.forward(10)
    t.down()

drew = turtle.Turtle()
"""
drew.color("skyblue","red")
drew.color("skyblue","yellow")
drew.color("skyblue","green")
"""
data = [48, 117, 200, 240, 160, 260, 220]

screen = turtle.Screen()
screen.bgcolor("salmon")



for value in data:
    draw_bar(drew, value)