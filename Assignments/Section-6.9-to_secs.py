#----------------------------
# Name: Section 6 secs
# Purpose: covert hours and minutes to seconds
#
# Author: DrewV
#
# Created: 03/05/2026
#----------------------------
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

hours = 0
minutes = 0
seconds = 0
total_seconds = 0

def take_inputs():
    hours = int(input (" How many hours? "))
    minutes = int(input(" How many minutes? " ))
    seconds = int(input( "how many seconds? "))
    return hours, minutes, seconds

def to_secs(hour, minute, seconds):
    total_seconds = (hour * 3600) + (minute * 60) + seconds
    return total_seconds

hours, minutes, seconds = take_inputs()
total_seconds = to_secs(hours,minutes,seconds)
print ("The total amount of seconds in that time is " + str(total_seconds) + " seconds!")

def test_to_secs():
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

test_to_secs()
