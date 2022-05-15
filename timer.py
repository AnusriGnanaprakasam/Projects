import time
import sys
import json

def countdown(task,hour,min=59,sec = 59):
    '''prints amount of time in console and updates every second'''
    print("press control -c to stop timer")
    if min == 59:
       hour -= 1
    if sec == 59 and min != 59:
       min -= 1
    try:
        for hr in range(int(hour),-1,-1):
            for minutes in range(int(min), -1, -1):
                for seconds in range(int(sec),-1,-1): #works but extra 59 seconds everytime
                    if seconds in range(-1,10):
                        seconds = "0"+ str(seconds)
                    if minutes in range(-1,10):
                        minutes = "0"+ str(minutes)
                    sys.stdout.write("\r")
                    sys.stdout.write(f"{hr}:{minutes}:{seconds} ")
                    sys.stdout.flush()
                    time.sleep(1)
                sec = 59
            min = 59
        sys.stdout.write("\rComplete!  \n")
    except KeyboardInterrupt:
        ChangeAttr(task,hr,minutes,seconds)
        print("Paused. type start command again")

def ChangeAttr(objname,hr,minutes,seconds):
    if ".json" in objname:
        with open(f"{objname}",'r+') as objfile:
            attr = json.load(objfile)
            if str(0) in str(minutes):
                minutes = minutes[1]
            if str(0) in str(seconds):
                seconds = seconds[1]
            attr['duration'] = [hr,int(minutes),int(seconds)]
            objfile.seek(0) # <--- should reset file position to the beginning.
            json.dump(attr, objfile, indent=4)
            objfile.truncate() # remove remaining part.  