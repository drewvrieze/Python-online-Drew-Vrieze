#----------------------------
# Name: Section 20 alicefile
# Purpose: work with and manipulate files
#
# Author: DrewV
#
# Created: 04/19/2026
#----------------------------
alice = open("alice_words.txt", "r")
alice_words = alice.read().split()

alice_words = [word.strip(".,!?;:\"'()1234567890*\\[]’‘”“-—").lower() for word in alice_words]
alice_words = [word for word in alice_words if word != ""]

count = {}
for word in alice_words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
count = list(count.items())
count.sort()
#print(count)
    
#FORMAT
print(f"Word{"":<26} Count")
print("=" * 36)
for word in count[:100]:
    print(f"{word[0]:<30} {word[1]}")

# I could not figure out how to get rid of the symbols that are conecting words
# in the middle which got counted weird such as alice)-"and but i tried my best