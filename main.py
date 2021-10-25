"""
This is just a file I used to test parts of the other projects such as the splitting and replacing of the calculator
equations.
"""

from datetime import datetime

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
# print(r.word_of_the_day())

now = datetime.now()
print("Time: ", now.strftime("%H:%M"), " Day: ", now.strftime("%Y-%m-%d"))
# print(time == now.strftime("%Y-%m-%d"))
print(now.strftime("%Y-%m-%d %H:%M"))

# import vlc

# importing pafy module
# import pafy

# url of the video
url = "https://www.youtube.com/watch?v=LrHN9Lwo6d4"

# # creating pafy object of the video
# video = pafy.new(url)
# best = video.getbest()
# media = vlc.MediaPlayer(best.url)
# media.play()

import webbrowser
# webbrowser.open("https://www.youtube.com/watch?v=LrHN9Lwo6d4", new=2)


import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=428
        height=360
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_513=tk.Listbox(root)
        GListBox_513["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_513["font"] = ft
        GListBox_513["fg"] = "#333333"
        GListBox_513["justify"] = "center"
        GListBox_513.place(x=10,y=20,width=115,height=320)

        GLabel_447=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_447["font"] = ft
        GLabel_447["fg"] = "#333333"
        GLabel_447["justify"] = "center"
        GLabel_447["text"] = "label"
        GLabel_447.place(x=140,y=20,width=272,height=30)

        GButton_810=tk.Button(root)
        GButton_810["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_810["font"] = ft
        GButton_810["fg"] = "#040404"
        GButton_810["justify"] = "center"
        GButton_810["text"] = "New File"
        GButton_810.place(x=150,y=320,width=70,height=25)
        GButton_810["command"] = self.GButton_810_command

        GButton_392=tk.Button(root)
        GButton_392["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_392["font"] = ft
        GButton_392["fg"] = "#000000"
        GButton_392["justify"] = "center"
        GButton_392["text"] = "Exit"
        GButton_392.place(x=340,y=320,width=70,height=25)
        GButton_392["command"] = self.GButton_392_command

    def GButton_810_command(self):
        print("command")


    def GButton_392_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()





