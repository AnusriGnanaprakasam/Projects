
import os
import json
from datetime import date
import delmakeobj
from rich.tree import Tree
from rich import print
from timer import countdown


#next task : remove hardcoding
today = date.today()
 #modify to take startdir  as an argument
#make a startup overview function that gives an overview at a certain time of what tasks in what proj and subproj need to be done

def startwork(startdir):#change this so that tasks from any day(in same month) can be done
    for_today = input("Is the task scheduled for today?(y/n)").strip(" ") 
    if for_today == 'y':
        month,day = today.month,today.day
        StartTree(startdir,month,day)
        task = input("What task would you like to start?(exclude \".json\") ")
        os.chdir(f'{startdir}\Topics\Calendar\Months\{month}\{day}')
    elif for_today == 'n':
       month,day = input("From what month and day(number for both)?(m d)").split(" ")
       StartTree(startdir,month,day)
       task = input("What task would you like to make up(or start ahead of time)?(exclude \".json\") ")
       os.chdir(f'{startdir}\Topics\Calendar\Months\{month}\{day}')
    task = task+ ".json" 
    taskpath = f'{startdir}\Topics\Calendar\Months\{month}\{day}\{task}'
    attr = LookAtAttr(task,taskpath)
    blocked_websites = attr["blocked_websites"]
    if len(attr['duration']) == 1:
        hour = attr['duration'][0]
        countdown(taskpath,blocked_websites,hour) #take blocked websites as well
    elif len(attr['duration']) == 2: #problem due to that
        hour,minutes = attr['duration']
        countdown(taskpath,blocked_websites,hour,minutes)
    elif len(attr['duration'])== 3:
        hour,minutes,seconds =  attr['duration']
        countdown(taskpath,blocked_websites,hour,minutes,seconds)

def new(startdir):
    delmakeobj.CreateNew(startdir)

def delete(startdir):
    u = input('Deltype and what to delete?(separate by comma)').split(",")
    deltype,todel = u
    delmakeobj.delete(startdir,deltype,todel)

def LookAtProjects(startdir):#make it so that attrs can be changed
    topic = input("What Topic is it?" )#is it in
    location = f"{startdir}\Topics\{topic}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" not in x),allfileindir))
    print(allfileindir)
    project = input("What project do you want to look at?")
    os.chdir(location+f"\{project}")
    objpath = f"{location}\{project}\{project} Description"
    print(LookAtAttr(project+" Description",objpath))

def LookAtsubProjects(startdir): #make it so that they can be changed
    project,topic = input("What Project and Topic do you want to look at(project,topic)?" ).split(",")
    location = f"{startdir}\Topics\{topic}\{project}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" in x),allfileindir))
    print(allfileindir)
    subproject = input("What subproject do you want to look at? ")
    for i in os.listdir(f"{startdir}\Topics\{topic}\{project}"):
        if i == subproject+".json":
            subproject = subproject+".json"
            objpath = f"{startdir}\Topics\{topic}\{project}\{subproject}"
            print(LookAtAttr(subproject,objpath))

def LookAtTasks(startdir):#make it so that attrs can be changed
    fortoday = input("For today(y/n)? ").strip(" ")
    if fortoday == "y":
        day,month = today.day,today.month
        os.chdir(f"{startdir}\Topics\Calendar\Months\{month}\{day}")
        tasklist = os.listdir(f"{startdir}\Topics\Calendar\Months\{month}\{day}")
        print(tasklist)
        if len(tasklist) == 0:
           exit()
           
    if fortoday == "n":
        lookdaymonth = input("From what day and month?(format: \"d m\") ").split(" ")
        day,month = lookdaymonth
        os.chdir(f"{startdir}\Topics\Calendar\Months\{month}\{day}")
        print(os.listdir(f"{startdir}\Topics\Calendar\Months\{month}\{day}"))
        if len(tasklist) == 0:
           exit()

    get_attr = input("Would you like to get details on any of the tasks?(y/n) ")
    if get_attr.strip(" ") == "y":    
        Taskname = input("What task would you like to look at ")
        Taskname = Taskname+".json"
        objpath = f"{startdir}\Topics\Calendar\Months\{month}\{day}\{Taskname}"
        print(LookAtAttr(Taskname,objpath))
    else:
        exit()
        
def LookAtAttr(objname,objpath):#working on
    if ".json" in objname: #has json in it righttttttt
        with open(objpath,'r+') as objfile:
            attr = json.load(objfile)
            return attr
    else: #look at later plz
        with open(objpath,'r+') as objfile:
            print(objfile.read())
def ChangeAttr(objname,hour,min): #maybe look at resolving this and the one from the timer file
    if ".json" in objname:
        with open(f"{objname}",'r+') as objfile:
            attr = json.load(objfile)
            attr["duaration"] = [hour,min]

def StartTree(startdir,month,day):
    '''Create Tree upon starting'''
    os.chdir(f"{startdir}/Topics")
    ListofTopics = [i for i in os.listdir(f"{startdir}/Topics") if i != "Calendar"]
    for topic in ListofTopics:
        os.chdir(f"{startdir}/Topics/{topic}")
        Topic = Tree(f"[yellow]{topic}")
        for project in os.listdir(f"{startdir}/Topics/{topic}"):
            Project = Topic.add(f"[red]{project}")
            #read tasks to return what proj they are in
            os.chdir(f"{startdir}\Topics\Calendar\Months\{month}\{day}")
            tasks = os.listdir(f"{startdir}\Topics\Calendar\Months\{month}\{day}")
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
