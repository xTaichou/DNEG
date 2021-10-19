import random
import json
from random_word import RandomWords
import yaml
import requests


def substitue(word):
    word = word.replace("o", "0")
    word = word.replace("a", "@")
    word = word.replace("i", "!")
    word = word.replace("e", "3")

    return word

def randPass(length):
    r = RandomWords()
    # Return a single random word
    word = r.get_random_word()
    word = addNumbers(word, length)
    return word

def addNumbers(word, length):
    words = word.split(" ")
    password = ""

    if len(words) == 1:
        if len(word) < length:
            word = substitue(word) + str(random.randrange(0, 10000000000000000))[:length - len(word)]
        password = word
    else:
        if len(word) < length:
            for x in words:
                x = substitue(x) + str(random.randrange(0, 10000000000000000))[:int((length / len(words) - len(x)))]
                password += x + " "
        else:
            for x in words:
                password += substitue(x) + " "

    return password

def generatePassword(word, length):
    words = word.split(" ")
    password = ""

    if length == 0:
        length = random.randrange(8, 20)

    if word == "":
        password = randPass(length)
    else:
        password = addNumbers(word, length)

    return password


print("The program will generate a random password based of the following criteria:\nIf you leave the word/phrase empty"
      " it will generate a random password of the specified length. If you leave the length empty it will generate a "
      "length between 8-20.\nIf it is a phrase it must be separated by spaces.\n"
      "    If the phrase is longer than the length then it will not be shortened.\n\nBy default it will "
      "use special characters and randomly make some characters uppercase. To leave selection blank just press enter\n")
words = input("Enter a word or phrase (leave blank for random): ")

while True:
    pLength = input("Length of password: ")
    if pLength == "":
        pLength = 0
        break

    try:
        pLength = int(pLength)
        if pLength > 20:
            answer = input("Are you sure? (y/n)")
            if answer.lower() == "y":
                break
        else:
            break
        continue
    except:
        print("Please enter a number")

print("Password: ", generatePassword(words, pLength))

