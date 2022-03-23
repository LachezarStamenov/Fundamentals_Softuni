# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there. It`s
# different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you
# are
# the best, so go ahead, learn the rules and win!
# On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden
# word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a
# match,
# and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"

import re

pattern = r"(@|\#)(?P<first_word>[a-zA-z]{3,})\1\1(?P<second_word>[a-zA-z]{3,})\1"
mirror_words = []
mirror_words_counter = 0
input_line = input()
match_count = 0
matches = re.finditer(pattern, input_line)
for match in matches:
    first_word = match.group('first_word')
    second_word = match.group('second_word')
    match_count += 1
    if first_word == second_word[::-1]:
        mirror_words_counter += 1
        mirror_words.append(f"{first_word} <=> {second_word}")


if match_count == 0:
    print("No word pairs found!")
else:
    print(f"{match_count} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(*mirror_words, sep=', ')