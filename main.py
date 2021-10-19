"""
This is just a file I used to test parts of the other projects such as the splitting and replacing of the calculator
equations.
"""

import random
import urllib.request
from random_word import RandomWords
import yaml
import requests


def retNumbers(equat, ope, op):
    num = []
    num1 = ""
    num2 = ""
    if op == "n":
        for x in equat[equat.find(ope) - 1::-1]:
            try:
                num1 += str(int(x))
            except:
                break
        num.append(int(num1[::-1]))

        for x in equat[equat.find(ope) + 1:]:
            try:
                num2 += str(int(x))
            except:
                break
        num.append(int(num2))
    else:
        pos1 = 0
        pos2 = 0
        for x in equat[equat.find(ope) - 1::-1]:
            try:
                num1 += str(int(x))
                pos1 -= 1
            except:
                break
        num.append(pos1)

        for x in equat[equat.find(ope) + 1:]:
            try:
                num2 += str(int(x))
                pos2 += 1
            except:
                break
        num.append(pos2)
    return num
equ = "22+233/33"



#print(equ[equ.find("+") + retNumbers(equ, "+", "p")[0]: equ.find("+") + retNumbers(equ, "+", "p")[1]+1])
print(random.randrange(8,20))

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()



r = RandomWords()

# Return a single random word
print(r.get_random_word())
# Return list of Random words
r.get_random_words()
# Return Word of the day
print(r.word_of_the_day())