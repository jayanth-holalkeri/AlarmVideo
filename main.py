import random
from datetime import datetime
import webbrowser as bw
import os




def play_video(video):
    bw.open(video)


def random_lines(fname):
    lines = open(fname).read().splitlines()
    selected_video = random.choice(lines)
    # print(lines)
    # print(y)
    play_video(selected_video)


def check(t):
    if len(t) != 11:
        return ("invalid format")
    else:
        if int(t[0:2]) > 12:
            return "invalid hour"
        elif int(t[3:5]) > 59:
            return "invalid minute"
        elif int(t[6:8]) > 59:
            return "invalid second"
        else:
            return True


while True:
    x = input("enter the time in HH:MM:SS AM/PM format : ")

    new = check(x)
    if new:
        print(f"video will be played at {x}")
        break
    else:
        print(new)

alarm_period = x[9:]
alarm_min = x[3:5]
alarm_sec = x[6:8]
alarm_hour = x[0:2]

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Video will now play")
                    random_lines('links.txt')
                    break
