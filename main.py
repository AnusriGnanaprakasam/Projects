
import os
import json
from datetime import date
import typer
import CreateAndDeleteItems
from pyfiglet import figlet_format
from rich.tree import Tree
from rich import print
from timer import countdown

startdir = "C:/DEV/Projects/Topics"
today = date.today()
app = typer.Typer()

#make a startup overview function that gives an overview at a certain time of what tasks in what proj and subproj need to be done
welcome_message = figlet_format("Welcome",font="doh",width=500)
display_possible_commands= figlet_format("Projects: list of commands in a tree")
print(welcome_message)

@app.command()
def startwork():
    StartTree()
    task = input("What task would you like to start?(without store and json label)")
    task = "Store"+task+".json"
    os.chdir(f'C:\DEV\Projects\Topics\Calendar\Months\{today.month}\{today.day}')
    attr = LookAtAttr(task)
    
    if len(attr['duration']) == 1:
        hour = attr['duration'][0]
        countdown(task,hour)
    if len(attr['duration']) == 2: #problem due to that
        hour,minutes = attr['duration']
        countdown(task,hour,minutes)
    if len(attr['duration'])== 3:
        hour,minutes,seconds =  attr['duration']
        countdown(task,hour,minutes,seconds)
@app.command()
def new():
    CreateAndDeleteItems.CreateNew()
@app.command()
def delete():
    u = input('Deltype and what to delete?').split(" ")
    deltype,todel = u
    CreateAndDeleteItems.delproject(deltype,todel)
@app.command()
def LookAtProjects():#make it so that attrs can be changed
    topic = input("What Topic do you want to look at?" )
    location = f"C:\DEV\Projects\Topics\{topic}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" not in x),allfileindir))
    print(allfileindir)
    project = input("What project do you want to look at?")
    os.chdir(location+f"\{project}")
    LookAtAttr(project+" Description")
@app.command()
def LookAtsubProjects(): #make it so that they can be changed
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
            print(LookAtAttr(subproject))
@app.command()
def LookAtTasks():#make it so that attrs can be changed
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
    if ".json" in objname:
        with open(f"{objname}",'r+') as objfile:
            attr = json.load(objfile)
            return attr
    else:
        with open(f"{objname}",'r+') as objfile:
            print(objfile.read())
def ChangeAttr(objname,hour,min):
    if ".json" in objname:
        with open(f"{objname}",'r+') as objfile:
            attr = json.load(objfile)
            attr["duaration"] = [hour,min]

def StartTree():
    '''Create Tree upon starting'''
    os.chdir("C:/DEV/Projects/Topics")
    ListofTopics = [i for i in os.listdir("C:/DEV/Projects/Topics") if i != "Calendar"]
    for topic in ListofTopics:
        os.chdir(f"C:/DEV/Projects/Topics/{topic}")
        Topic = Tree(f"[yellow]{topic}")
        for project in os.listdir(f"C:/DEV/Projects/Topics/{topic}"):
            Project = Topic.add(f"[red]{project}")
            #read tasks to return what proj they are in
            os.chdir(f"C:\DEV\Projects\Topics\Calendar\Months\{today.month}\{today.day}")
            tasks = os.listdir(f"C:\DEV\Projects\Topics\Calendar\Months\{today.month}\{today.day}")
            for task in tasks:
                taskfile = open(task) #was open before
                attrs = json.load(taskfile)
                if attrs["project_under"] == str(project):
                    duration = attrs["duration"]
                    if len(duration) == 1:
                        duration.append(0)
                    if int(duration[1]) in range(0,10):
                        duration[1] = f"0{duration[1]}"
                        duration = f"{duration[0]}:{duration[1]}:00"
                        subproject = attrs["subproject_under"]
                    else:
                        duration = f"{duration[0]}:{duration[1]}:00"
                    if attrs["subproject_under"] != "none":  
                        task = Project.add(f"{task} {duration} {subproject}")#changing from "Task" to "task" somehow worked??
                    else:
                        task = Project.add(f"{task} {duration}")               
    print(Topic)
               
#look at tasks for today  -one command
#make new task - another command

if __name__ == '__main__':
    #print(display_possible_commands)
    app()