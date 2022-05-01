import time
import sys

global run 
run = True
def changewhile():
    run = False
#desired_window_name = "Stopwatch" #Whatever the name of your window should be
def countdown(hour,min,sec = 59):
    '''prints amount of time in console and updates every second'''
    for hr in range(hour,-1,-1):
        for minutes in range(min, -1, -1):
            for seconds in range(sec,0,-1):
                if seconds in range(-1,10):
                    seconds = "0"+ str(seconds)
                if minutes in range(-1,10):
                    minutes = "0"+ str(minutes)
                sys.stdout.write("\r")
                sys.stdout.write(f"{hr}:{minutes}:{seconds}")
                sys.stdout.flush()
                time.sleep(1)
        min = 59
    sys.stdout.write("\rComplete!  \n")


