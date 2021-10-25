"""
This is a significant project as it will test your knowledge on the various concepts of Python. You need to build an app
 that anyone uses to explore the files in their system. You can also add features like searching and copy-paste.
 Tkinter is a commendable choice for this project as it makes the development of GUI applications fast and easy.

To create the Python File Explorer using Tkinter, you have to import the filedialog module from Tkinter. This module is
designed for opening files and directories and saving them.

I also want to try add a feature to make it cross platform so that when getting the base directories to search for files
you can run this script on either Mac or Windows.

Idea from: https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/#20_Random_Password_Generator
"""

import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
from os import walk, path

mypath = "/Users/matthew/DNEG"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

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

        lstDirectories=tk.Listbox(root)
        lstDirectories["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lstDirectories["font"] = ft
        lstDirectories["fg"] = "#333333"
        lstDirectories["justify"] = "center"
        lstDirectories.place(x=10,y=20,width=115,height=320)

        lblPath=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lblPath["font"] = ft
        lblPath["fg"] = "#333333"
        lblPath["justify"] = "center"
        lblPath["text"] = "label"
        lblPath.place(x=140,y=20,width=272,height=30)

        btnNew=tk.Button(root)
        btnNew["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        btnNew["font"] = ft
        btnNew["fg"] = "#040404"
        btnNew["justify"] = "center"
        btnNew["text"] = "New File"
        btnNew.place(x=150,y=320,width=70,height=25)
        btnNew["command"] = self.btnNew_command

        btnExit=tk.Button(root)
        btnExit["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        btnExit["font"] = ft
        btnExit["fg"] = "#000000"
        btnExit["justify"] = "center"
        btnExit["text"] = "Exit"
        btnExit.place(x=340,y=320,width=70,height=25)
        btnExit["command"] = self.btnExit_command

    def btnNew_command(self):
        print("command")


    def btnExit_command(self):
        root.destroy()

if __name__ == "__main__":
    file = filedialog.askopenfilenames(initialdir=path.dirname(__file__))
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# print(f)
#
# file = open(f[1])
# for lines in file.readlines():
#     print(lines)

