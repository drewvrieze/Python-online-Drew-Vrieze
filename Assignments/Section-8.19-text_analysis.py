#----------------------------
# Name: Section 8 text analysis
# Purpose: take text and print how much words and letter e
#
# Author: DrewV
#
# Created: 03/23/2026
#----------------------------




punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
def remove_punctuation(s):
    minus_punctuation = ""
    for letter in s:
        if letter not in punctuation:
            minus_punctuation += letter
    return minus_punctuation

def word_count(modified_text):
    modified_text = modified_text.split()
    word_count = len(modified_text)
    return word_count

def e(modified_text):
    modified_text = modified_text.split()
    e_count = 0
    for c in modified_text:
        count = 0
        for letter in c:
            if letter == "e" or letter == "E":
                count = 1
        if count == 1:
            e_count += 1
        count = 0
    return e_count

text = "A well-structured paragraph serves as a foundational building block of writing, focusing on a single, " \
"cohesive idea or topic. It typically begins with a topic sentence that introduces the main point, followed by " \
"supporting sentences that provide details, evidence, or analysis to reinforce that idea. A concluding sentence " \
"brings the thought to a close, often summarizing the main point or bridging to the next paragraph. While length " \
"can vary, a standard paragraph is often roughly four to seven sentences long, providing enough space to develop a " \
"thought without becoming confusing."




def main():
    # text = input("please enter a text you would like to analyze: ")
    modified_text = remove_punctuation(text)
    count = word_count(modified_text)
    count_e = e(modified_text)
    print(f'Your text contains {count} words, of which {count_e} ({round(((count_e/count)*100),1)}%) contain an "e"')

if __name__ == "__main__":
    main()
