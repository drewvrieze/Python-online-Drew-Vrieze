#----------------------------
# Name: Section 13 reversefile
# Purpose: learn how to open and use files 
#
# Author: DrewV
#
# Created: 04/12/2026
#----------------------------
# I thought this was funny so i kept it
"""
def reverselines(file):
    old = open(file, "r")
    new = open(file + ".reversed", "w")
    while True:
        buf = old.readline()
        if len(buf) == 0:
            break
        new.write(old[::-1])


    old.close()
    new.close()

reverselines("sup")
"""
def reverselines(file):
    old = open(file, "r")
    new = open(file + ".reversed", "w")
    buf = old.readlines()
    for line in reversed(buf):
            new.write(line)

    old.close()
    new.close()

reverselines("sup")
