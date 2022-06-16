import os
import json
import calendar
from datetime import date
from pathlib import Path
from rich.tree import Tree
from rich import print
from lifemanager import timer
from lifemanager import delmakeobj 
from pyfiglet import figlet_format

#startdir in all func.  IS THIS A PROBLEM??
#have command with arguments (use argparse to implement this)
ListOfCommands = """
    - startwork
    - new
    - delete
    - lookatprojects 
    - lookatsubprojects - .json not apart of input
    - lookattasks - .json not apart of input
    """

directory = Path(__file__).parent/"config.json"  #define where config file is located
today = date.today()

def welcome_message():
    ''' displayed when LifeManager command is typed without any arguments'''
    welcome_message = figlet_format("Life Manager",font="slant",width=70)
    print(welcome_message)
    print(ListOfCommands)

def make_config():
    with open(directory,'w',encoding="utf-8") as config:
        start = {"year":today.year-1}
        json.dump(start,config)

def modify_config(attribute,value):
    with open(directory,'r+',encoding="utf-8") as config:
        configdict = json.load(config)
        if attribute not in configdict.keys():
            configdict = dict(configdict)
            configdict.update({attribute:value})
            config.seek(0)
            json.dump(configdict,config)
            config.truncate()
        else:  
            configdict[attribute] = value
            config.seek(0)
            json.dump(configdict, config, indent=4) #why null
            config.truncate()

def find_config(attribute):
    ''' use to find the value of the "year" or "startdir"(where calendar is set up) attribute in config file'''
    try:
        with open(directory,'r+',encoding="utf-8") as config:
            configdict = json.load(config)
            return configdict[attribute]
    except FileNotFoundError:
        return("config file not found. You probably deleted it by accident")      
    except Exception as e:
        print(e,"Send this to me if you are confused") 
        print("Config file most likely only contains year and not start directory because \n the question of where to install was skipped or not properly answered. Please enter path to a empty folder that exists.")
        BuildCalendar()

def BuildCalendar():
    '''makes calendar folder which will have tasks populated into it'''
    startdir= input("What directory do you want to install the calendar in?").strip()
    try:
        os.chdir(startdir)
        os.makedirs("Topics\\Calendar\\Months")
    except (FileNotFoundError,FileExistsError) as e:
        print(e)
        print(" input another directory that is empty(or create if file not found error)")
        BuildCalendar()

    else:
        leapYearStatus = calendar.isleap(today.year)
        feb = 30 if leapYearStatus == True else 29
        monthswith31days = [1, 3, 5, 7, 8, 10, 12]
        monthswith30days = [4, 6, 9, 11]
        """build the calendar"""
        for month in range(1, 13):
            os.chdir(f"{startdir}\\Topics\\Calendar\\Months")
            os.mkdir(str(month))
            os.chdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}")
            if month in monthswith31days:  # check if leap year for feb
                for day in range(1, 32):
                    os.mkdir(str(day))
            os.chdir(f"{startdir}\\Topics\\Calendar\\Months")
            if month in monthswith30days:
                os.chdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}")
                for day in range(1, 31):
                    os.mkdir(str(day))
            os.chdir(f"{startdir}\\Topics\\Calendar\\Months")
            if month == 2:
                os.chdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}")
                for day in range(1, feb):
                    os.mkdir(str(day))
            os.chdir(f"{startdir}\\Topics\\Calendar\\Months")
        modify_config("start_directory",startdir)
           
def main():
    ''' entry point for the program(this should be executed when just life-manager is given without args)'''
    welcome_message()
    if find_config("start_directory") == "not found":
        make_config()
        with open(directory, "r+",encoding="utf-8") as config:
            year_yesterday= json.load(config)
            year_yesterday = year_yesterday["year"]#careful of quotes
            if today.year != int(year_yesterday):
                modify_config("year",today.year)
                BuildCalendar()

def startwork():#change this so that tasks from any day(in same month) can be done
    startdir = find_config("start_directory")
    for_today = input("Is the task scheduled for today?(y/n)").strip(" ")
    if for_today == 'y':
        month,day = today.month,today.day
        StartTree(startdir,month,day)
        task = input("What task would you like to start?(exclude \".json\") ")
        os.chdir(f'{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}')
    elif for_today == 'n':
       month,day = input("From what month and day(number for both)?(m d)").split(" ")
       StartTree(startdir,month,day)
       task = input("What task would you like to make up(or start ahead of time)?(exclude \".json\") ")
       os.chdir(f'{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}')
    task = task+ ".json"
    taskpath = f'{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}\\{task}'
    attr = LookAtAttr(task,taskpath)
    blocked_websites = attr["blocked_websites"]
    if len(attr['duration']) == 1:
        hour = attr['duration'][0]
        timer.countdown(task,taskpath,blocked_websites,hour) #take blocked websites as well
    elif len(attr['duration']) == 2: #problem due to that
        hour,minutes = attr['duration']
        timer.countdown(task,taskpath,blocked_websites,hour,minutes)
    elif len(attr['duration'])== 3:
        hour,minutes,seconds =  attr['duration']
        timer.countdown(task,taskpath,blocked_websites,hour,minutes,seconds)

def new(startdir):
    startdir = find_config("start_directory")
    delmakeobj.CreateNew(startdir)

def delete(startdir):
    startdir = find_config("start_directory")
    u = input('Deltype and what to delete?(separate by comma)').split(",")
    deltype,todel = u
    delmakeobj.delete(startdir,deltype,todel)

def LookAtProjects(startdir):#make it so that attrs can be changed
    startdir = find_config("start_directory")
    topic = input("What Topic is it?" )#is it in
    location = f"{startdir}\\Topics\\{topic}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" not in x),allfileindir))
    print(allfileindir)
    project = input("What project do you want to look at?")
    os.chdir(location+f"\\{project}")
    objpath = f"{location}\\{project}\\{project} Description"
    print(LookAtAttr(project+" Description",objpath))

def LookAtsubProjects(startdir): #make it so that they can be changed
    startdir = find_config("start_directory")
    project,topic = input("What Project and Topic do you want to look at(project,topic)?" ).split(",")
    location = f"{startdir}\\Topics\\{topic}\\{project}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" in x),allfileindir))
    print(allfileindir)
    subproject = input("What subproject do you want to look at? ")
    for i in os.listdir(f"{startdir}\\Topics\\{topic}\\{project}"):
        if i == subproject+".json":
            subproject = subproject+".json"
            objpath = f"{startdir}\\Topics\\{topic}\\{project}\\{subproject}"
            print(LookAtAttr(subproject,objpath))

def LookAtTasks(startdir):#make it so that attrs can be changed
    startdir = find_config("start_directory") #optimize later
    fortoday = input("For today(y/n)? ").strip(" ")
    if fortoday == "y":
        day,month = today.day,today.month
        os.chdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}")
        tasklist = os.listdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}")
        print(tasklist)
        if len(tasklist) == 0:
           exit()
           
    if fortoday == "n":
        lookdaymonth = input("From what day and month?(format: \"d m\") ").split(" ")
        day,month = lookdaymonth
        os.chdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}")
        print(os.listdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}"))
        if len(tasklist) == 0:
           exit()

    get_attr = input("Would you like to get details on any of the tasks?(y/n) ")
    if get_attr.strip(" ") == "y":    
        Taskname = input("What task would you like to look at ")
        Taskname = Taskname+".json"
        objpath = f"{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}\\{Taskname}"
        print(LookAtAttr(Taskname,objpath))
    else:
        exit()
        
def LookAtAttr(objname,objpath):#working on
    if ".json" in objname: #has json in it righttttttt
        with open(objpath,'r+',encoding="utf-8") as objfile:
            attr = json.load(objfile)
            return attr
    else: #look at later plz
        with open(objpath,'r+',encoding="utf-8") as objfile:
            print(objfile.read())

def StartTree(startdir,month,day):
    '''Create Tree upon starting'''
    os.chdir(f"{startdir}\\Topics")
    ListofTopics = [i for i in os.listdir(f"{startdir}\\Topics") if i != "Calendar"]
    for topic in ListofTopics:
        os.chdir(f"{startdir}\\Topics\\{topic}")
        Topic = Tree(f"[yellow]{topic}")
        for project in os.listdir(f"{startdir}\\Topics\\{topic}"):
            Project = Topic.add(f"[red]{project}")
            #read tasks to return what proj they are in
            os.chdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}")
            tasks = os.listdir(f"{startdir}\\Topics\\Calendar\\Months\\{month}\\{day}")
            for task in tasks:
                taskfile = open(task) #just to make obj
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
               
if __name__ == "__main__":
    main()