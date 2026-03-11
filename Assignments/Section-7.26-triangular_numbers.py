#----------------------------
# Name: Section 7 tirangular numbers
# Purpose: covert hours and minutes to seconds
#
# Author: DrewV
#
# Created: 03/11/2026
#----------------------------

def triangle_numbers(a):
    number = 0
    triangle = 0
    for b in range(a):
        number = number +1
        
        triangle = triangle + number
        
        print(f"{number}\t{triangle}")

a = int(input("How many triangular calculations do you want? "))
triangle_numbers(a)


