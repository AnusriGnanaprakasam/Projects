import os
import json
from datetime import date
import typer
import CreateAndDeleteItems
from pyfiglet import figlet_format

startdir = "C:/DEV/Projects/Topics"
today = date.today()
app = typer.Typer()

#make a startup overview function that gives an overview at a certain time of what tasks in what proj and subproj need to be done

@app.command()
def LookAtProjects():
    pass
@app.command()
def LookAtsubProjects():
    project,topic = input("What Project and Topic do you want to look at(project,topic)?" ).split(",")
    location = f"C:\DEV\Projects\Topics\{topic}\{project}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" in x),allfileindir))
    print(allfileindir)
    subproject = input("What subproject do you want to look at? ")
    for i in os.listdir(f"C:\DEV\Projects\Topics\{topic}\{project}"):
        if i == "Store"+subproject+".json":
            subproject = "Store"+subproject+".json"
            LookAtAttr(subproject)

@app.command()
def LookAtTasks():
    fortoday = input("For today(y/n)? ").strip(" ")
    if fortoday == "y":
        day,month = today.day,today.month
        os.chdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}')
        print(os.listdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}'))
        get_attr = input("Would you like to get details on the task?(y/n) ")
        if get_attr.strip(" ") == "y":
            Taskname = input("What task would you like to look at")
            Taskname = "Store"+Taskname+".json"
            LookAtAttr(Taskname)
        
    if fortoday == "n":
        lookdaymonth = input("From what day and month?(format: \"d m\") ").split(" ")
        day,month = lookdaymonth
        os.chdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}')
        print(os.listdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}'))
        get_attr = input("Would you like to get details on the task?(y/n) ")
        if get_attr.strip(" ") == "y":
            Taskname = input("What task would you like to look at")
            Taskname = "Store"+Taskname+".json"
            LookAtAttr(Taskname)
        
def LookAtAttr(objname):
    with open(f"{objname}",'r+') as objfile:
        attr = json.load(objfile)
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