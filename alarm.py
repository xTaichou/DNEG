"""
This application is for an alarm clock but everytime the alarm is triggered it will look up a rondom  Youtube link from
a file and play it.

Please note that I do my coding on a Mac and it opens fine in a safari tab.

Left to do:
Checks on the day and time supplied
"""
import random
from datetime import datetime
import webbrowser


def getLink():
    """
    This will select a random link for the given file and then will open it in a new tab in your browser
    :return: N/A
    """
    lines = open('y-links.txt', 'r').read().splitlines()
    myline = random.choice(lines)
    webbrowser.open(myline, new=2)

def alarmClock(day, time):
    """
    This function will wait until the time is met for the alarm and then trigger the next function to play the youtube
    video
    :param day: whether it is today or another day
    :param time: time for the alarm
    :return: N/A
    """
    now = datetime.now()
    while time != now.strftime("%Y-%m-%d %H:%M"):
        now = datetime.now()
        continue
    getLink()

print("The application will play a random youtube link when the alarm clock time set is triggered. You can either enter"
      "a time for today or you can set it for a specific day. \nYou will first be asked to confirm for today or a specifc"
      " day. Just enter today or day to choose and then enter the day and time or just time.\nThe acceptable formats are"
      " as follows:\n24 hour format: 13:24 or 03:15.\nDay format: 2021-10-20 15:00\n")

day = input("Today or a specific day? ")
time = input("What time do you want to set the alarm? ")

alarmClock(day, time)





