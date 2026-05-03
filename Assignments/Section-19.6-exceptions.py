#----------------------------
# Name: Section 19 exceptions
# Purpose: learn how to handle exceptionsq
#
# Author: DrewV
#
# Created: 05/03/2026
#----------------------------

def readposint():
    number = input("Please enter a positive integer, ")
    try:
        number = int(number)
        if number <= 0:
            print(f"{number} is not a positive integer")
            leave = input("Enter y to try again: ")
            if leave == "y":
                readposint()
        else:
            print(f"{number} is a positive integer")
            leave = input("Enter y to try again: ")
            if leave == "y":
                readposint()

    except:
        print(f"{number} is not an integer")
        leave = input("Enter y to try again: ")
        if leave == "y":
            readposint()

readposint()