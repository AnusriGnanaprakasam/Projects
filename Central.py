import os
import json
from datetime import date
import typer
import CreateAndDeleteItems
from pyfiglet import figlet_format

startdir = "C:/DEV/Projects/Topics"
today = date.today()
app = typer.Typer()

''' I may be removing this function after but i just want to show how it would be like to set everything up in a directory'''

@app.command()
def LookAtTasks():
    fortoday = input("For today(y/n)? ").strip(" ")
    if fortoday == "y":
        day,month = today.day,today.month
        os.chdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}')
        print(os.listdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}'))
        get_attr = input("Would you like to get details on the task?(y/n) ")
        if get_attr.strip(" ") == "y":
            LookAtTaskAttr()
        
    if fortoday == "n":
        lookdaymonth = input("From what day and month?(format: \"d m\") ").split(" ")
        day,month = lookdaymonth
        os.chdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}')
        print(os.listdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}'))
        get_attr = input("Would you like to get details on the task?(y/n) ")
        if get_attr.strip(" ") == "y":
            LookAtTaskAttr()
        
def LookAtTaskAttr():
    Taskname = input("What task would you like to look at")
    Taskname = "Store"+Taskname+".json"
    with open(f"{Taskname}",'r+') as taskfile:
        attr = json.load(taskfile)
        print(attr)

@app.command()
def New():
    CreateAndDeleteItems.CreateNew()
#look at tasks for today  -one command
#make new task - another command



if __name__ == '__main__':
    welcome_message = figlet_format("Welcome",font="doh",width=500)
    display_possible_commands= figlet_format("Projects: list of commands in a tree")
    print(welcome_message)
    #print(display_possible_commands)
    app()