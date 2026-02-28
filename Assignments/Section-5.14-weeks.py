#----------------------------
# Name: Section 5 Weeks
# Purpose: get a number and print what day of the week it is
#
# Author: DrewV
#
# Created: 02/28/2026
#----------------------------



def week (day):
    if day == 0:
        print ("It is Sunday!")
    elif day == 1:
        print ("It is Monday!")
    elif day == 2:
        print( "It is Tuesday!")
    elif day == 3:
        print ("It is Wednesday!")
    elif day == 4:
        print ("It is Thursday!")
    elif day == 5:
        print ("It is Friday!")
    elif day == 6:
        print ("It is Saturday!")
    else:
        print ("really? Try again. (0-6)")
        day = int (input ("What day of the week is it? (0-6) "))
        week(day)

day = int (input ("What day of the week is it? (0-6) "))

week(day)