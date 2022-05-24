import os
import json
from datetime import datetime,date,timedelta
from shutil import rmtree


today = date.today()


class subProjects():
    def __init__(self,objname,topic_under,project_under,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.topic_under = topic_under
        self.project_under = project_under
        self.objname = objname 

    def __str__(self):
        description = f"name: {self.objname} \n project: {self.project_under} "
        return description


class Tasks():
    def __init__(self, objname,topic_under, project_under,month_number,day_number,duration,blocked_websites,subproject_under='none'): 
        self.subproject_under = subproject_under
        self.month_number = month_number 
        self.day_number = day_number
        self.duration = duration
        self.objname = objname
        self.topic_under = topic_under
        self.project_under = project_under
        self.blocked_websites = blocked_websites

    def __str__(self):
        description = f"name: {self.name} \n amount of time: {self.time_to_complete} \n to complete by: {self.to_complete_by} \n project: {self.project_under} \n subproject: {self.subproject_under}"
        return description



def delete(startdir,type,todel):#make it so that spaces can be taken
    try:
        if "topic" == type.lower() : #be careful with "or"
            print('tf')
            os.chdir(f"{startdir}/Topics/{todel}")
            warning = input("Warning this will delete all project,subprojects and tasks within the directory. \n Type \"confirm\" to continue ").strip(" ")
            if warning != "confirm":
                exit()
            else:
                os.chdir(f"{startdir}/Topics")
                os.removedirs(f"{startdir}/Topics/{todel}")
        if "project" == type.lower():
            os.chdir(f"{startdir}/Topics")
            for topic in os.listdir():
                os.chdir(f"{startdir}/Topics/{topic}")
            for project in os.listdir():
                if project == todel:
                    rmtree(f"{startdir}/Topics/{topic}/{todel}")
        if "subproject" == type.lower(): 
            os.chdir(f"{startdir}/Topics")
            for topic in os.listdir():
                os.chdir(f"{startdir}/Topics/{topic}")
            for project in os.listdir():
                os.chdir(f"{startdir}/Topics/{topic}/{project}")
                for subproject in os.listdir():
                    if todel in subproject:
                        os.remove(f"{startdir}/Topics/{topic}/{project}/{subproject}")
        if "task" ==  type.lower():
            os.chdir(f"{startdir}/Topics/Calendar/Months")
            for month in os.listdir(f"{startdir}/Topics/Calendar/Months"):
                os.chdir(f"{startdir}/Topics/Calendar/Months/{month}")
                for day in os.listdir(f"{startdir}/Topics/Calendar/Months/{month}"):
                    os.chdir(f"{startdir}/Topics/Calendar/Months/{month}/{day}")
                    tasklist = os.listdir(f"{startdir}/Topics/Calendar/Months/{month}/{day}")             
                    for task in tasklist:
                        if todel in task:
                            os.remove(f"{startdir}/Topics/Calendar/Months/{month}/{day}/{task}")

    except(FileNotFoundError,UnboundLocalError) as e: #add thing for win5 error
        print(e)
        print(f"There is no {type} under the name \"{todel}\"")
        print("Make?")
      
    

class ObjectEncoder(json.JSONEncoder):
    '''Json encoder class for projects'''

    def default(self, obj):
        if isinstance(obj,subProjects ):
            return obj.__dict__
        if isinstance(obj,Tasks):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


def makejsonfile(objname, obj):
    with open(f"{objname}.json", "w+") as file:
        file.write('\n')
        json.dump(obj, file, cls=ObjectEncoder)

def LookAtAttr(objname): #need to sort everything out pls helps
    if ".json" in objname:
        with open(f"{objname}",'r+') as objfile:
            attr = json.load(objfile)
            return attr
    else:
        with open(f"{objname}",'r+') as objfile:
            print(objfile.read())

def CreateNew(startdir):#startdir argument
    typeof = input("Do you want to make a new Task, subProject, Project or Topic?").strip(" ")
    if typeof.lower() == "task":
        CreateTask(startdir)
    if typeof.lower() == "project":
        CreateProject(startdir)
    if typeof.lower() == "subproject":
        CreatesubProject(startdir)
    if typeof.lower() == "topic":
        CreateTopic(startdir)
    else:
        exit()

def CreateTopic(startdir):
    TopicName = input("What should be the name of the topic? ").strip()
    os.chdir(f"{startdir}/Topics")
    os.mkdir(TopicName)
def CreateProject(startdir):
    project_name = input("What is this project\'s name? ").strip(" ")
    to_complete_by = input("When should this project be completed by?  ")
    time_to_complete = input("How long should be spent on it each day?  ")
    blocked_websites = input("(can be blank) What websites should be unavailable when completing tasks?(in format \"www.website.com\" with a comma between each) ").split(",")
    Project_attr = {"to complete by": to_complete_by,"time to complete": time_to_complete,"blocked_websites":blocked_websites}
    os.chdir(f"{startdir}/Topics")
    ListofTopics = os.listdir(f"{startdir}/Topics")
    print(list(filter(lambda x: x != "Calendar",ListofTopics)))
    TopicUnder = input("What topic should this project be under? ").strip(" ")
    os.chdir(""f"{startdir}/Topics/{TopicUnder}""")
    os.mkdir(project_name)
    os.chdir(f"{startdir}/Topics/{TopicUnder}/{project_name}")
    with open(f"{project_name} Description", "a+") as project_description:
        project_description.write(str(Project_attr))
def CreatesubProject(startdir): 
    objname = input("Enter name of subProject: ").strip()
    fortheweek = input("Will the subproject continue for the week(7 days from whatever day is now)?(y/n)").strip(" ")
    if fortheweek == 'y':
        topic_under = input("What topic is it under? ").strip(" ")
        project_under = input("What project is it under?  ").strip(" ")
        start_date = datetime(today.year,today.month,today.day)
        end_date = start_date + timedelta(days = 7)
        obj = subProjects(objname,topic_under, project_under,str(start_date),str(end_date))
        os.chdir(f"{startdir}/Topics/{topic_under}/{project_under}")
        makejsonfile(objname,obj)

    if fortheweek == 'n':
        monthstart,daystart = list(map(int,input("When to start(m d): ").split(" ")))
        monthend,dayend = list(map(int,input("When to end(m d): ").split(" ")))
        start_date = datetime(today.year,monthstart,daystart)
        end_date = datetime(today.year,monthend,dayend)
        topic_under = input("What topic is it under? ").strip(" ")
        project_under = input("What project is it under? ")
        obj = subProjects(objname,topic_under, project_under,start_date,end_date)
        os.chdir(f"{startdir}/Topics/{topic_under}/{project_under}")
        makejsonfile(objname,obj)

def CreateTask(startdir):
    objname = input("Enter name of Task: ")
    month_number = today.month #maybe change this later...
    day_number = int(input('What day should this task be done on(please input number)? '))
    duration = list(map(int,input("How long do you want to spend on this(hr min)?  ").split(" ")))
    topic_under = input("What topic should this task be under? ")
    project_under = input("What project should this task be under? ")
    blocked_websites = input("(can be blank) What websites should be unavailable when completing this specific task (will inherit websites from project task is under)? \n In format \"www.website.com\" with a comma between each)  ").split(",")
    
    is_there_subproject_under = input("Is there is subproject(y/n)? ").strip(" ")
    if  is_there_subproject_under == 'y':
        subproject_under = input("What subproject is it under? ")
        obj = Tasks(objname,topic_under,project_under,month_number,day_number,duration,blocked_websites,subproject_under)
        os.chdir(f"{startdir}/Topics/Calendar/Months/{month_number}/{day_number}")
        makejsonfile(objname, obj)
    else:
        obj = Tasks(objname,topic_under,project_under,month_number,day_number,duration,blocked_websites)
        os.chdir(f"{startdir}/Topics/Calendar/Months/{month_number}/{day_number}")
        makejsonfile(objname, obj)

# obj.__setattr__("name","Beem")use this instead to change attributes

