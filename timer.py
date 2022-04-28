import time
import sys,os

def countdown(hour,min,sec):
    '''prints amount of time in console and updates every second'''
    for hr in range(hour,0,-1):
        for minutes in range(min, 0, -1):
            for seconds in range(sec,0,-1):
                if seconds in range(0,10):
                    seconds = "0"+ str(seconds)
                if minutes in range(0,10):
                    minutes = "0"+ str(minutes)
                sys.stdout.write("\r")
                os.system("cls")
                sys.stdout.write(f"{hr}:{minutes}:{seconds}")
                sys.stdout.flush()
                time.sleep(1)

    sys.stdout.write("\rComplete!  \n")

