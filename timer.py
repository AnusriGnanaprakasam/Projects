import time
import sys
import json

def countdown(task,hour,min,sec = 59):
    '''prints amount of time in console and updates every second'''
    #one min more than the actual value is always added
    print("press control -c to stop timer")
    try:
        for hr in range(int(hour),-1,-1):
            for minutes in range(int(min), -1, -1):
                for seconds in range(int(sec),0,-1):
                    if seconds in range(-1,10):
                        seconds = "0"+ str(seconds)
                    if minutes in range(-1,10):
                        minutes = "0"+ str(minutes)
                    sys.stdout.write("\r")
                    sys.stdout.write(f"{hr}:{minutes}:{seconds} ")
                    sys.stdout.flush()
                    time.sleep(1)
            min = 59
        sys.stdout.write("\rComplete!  \n")
    except KeyboardInterrupt:
        ChangeAttr(task,hr,minutes,seconds)
        print("Pause. type start command again")

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