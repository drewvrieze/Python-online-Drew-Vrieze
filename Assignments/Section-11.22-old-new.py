#----------------------------
# Name: Section 11 old to new
# Purpose: learn how to replace old code with new code
#
# Author: DrewV
#
# Created: 04/05/2026
#----------------------------

def takestring():
    string = input("What phrase would you like to edit? ")
    replace = input("What instances would you like to replace? ")
    with_what = input("What would you like to replace the instances with? ")
    return string, replace, with_what

def replacing(string, replace, with_what):
    s = string.split()
    for i in range(len(s)):
        if replace in s[i]:
            s[i] = s[i].replace(replace, with_what)
    return s

a = replacing("I love spom! Spom is my favorite food. Spom, spom, yum!", "om", "am")
print (" ".join(a))




def main():
    string, replace, with_what = takestring()
    s = replacing(string, replace, with_what)
    print(" ".join(s))

if __name__ == "__main__":
    main()
    