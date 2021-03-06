import time
import sys
import json
from pathlib import Path
from lifemanager import delmakeobj
from lifemanager import blocker

def find_config(attribute): #have main import from here?
    try:
        directory = Path(__file__).parent/"config.json" 
        with open(directory,'r+') as config:
            configdict = json.load(config)
            return configdict[attribute]
    except FileNotFoundError:
        return("file does not exit ")
    except Exception as e:
        print("e")
        

def countdown(task,taskpath,blocked_websites,hour,min=59,sec = 59):#reads attribute and calls the a func from block web file for specific task
    '''prints amount of time left and updates every second. Task deleted when done'''
    blocker.block(blocked_websites)
    print("press control -C to pause timer")
    if min == 59:
       hour -= 1
    if sec == 59 and min != 59:
       min -= 1
    try:
        for hr in range(int(hour),-1,-1):
            for minutes in range(int(min), -1, -1):
                for seconds in range(int(sec),-1,-1): #works but -1 seconds everytime
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
        sys.stdout.write("\r:)\n")
    except KeyboardInterrupt:
        Pause(taskpath,hr,minutes,seconds)
        print("Paused. type start command again")
    else:
        delmakeobj.delete(find_config("start_directory"),"Task",task)
        
def Pause(taskpath,hr,minutes,seconds):
    '''lets the timer start from where it left off by modifying json attribute: duration'''
    blocker.clear()
    if ".json" in taskpath:
        with open(f"{taskpath}",'r+') as objfile:
            attr = json.load(objfile)
            if str(0) in str(minutes):
                minutes = minutes[1]
            if str(0) in str(seconds):
                seconds = seconds[1]
            attr['duration'] = [hr,int(minutes),int(seconds)]
            objfile.seek(0) # <--- should reset file position to the beginning.
            json.dump(attr, objfile, indent=4)
            objfile.truncate() # remove remaining part.  