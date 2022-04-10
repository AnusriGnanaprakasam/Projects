import os
import json
import typer
from shutil import rmtree 
from datetime import date

app = typer.Typer()
today = date.today()

class subProjects():
    def __init__(self,objname,start_date, end_date,topic_under,project_under):
        self.start_date = start_date
        self.end_date = end_date
        self.topic_under = topic_under
        self.project_under = project_under
        self.objname = objname 

    def __str__(self):
        description = f"name: {self.objname} \n project: {self.project_under} "
        return description


class Tasks(subProjects):
    def __init__(self, objname,start_date, end_date,topic_under, project_under,month_number,day_number, subproject_under='none'): 
        self.subproject_under = subproject_under
        self.month_number = month_number 
        self.day_number = day_number
        super().__init__(objname,start_date, end_date,topic_under,project_under)

    def __str__(self):
        description = f"name: {self.name} \n amount of time: {self.time_to_complete} \n to complete by: {self.to_complete_by} \n project: {self.project_under} \n subproject: {self.subproject_under}"
        return description


class ObjectEncoder(json.JSONEncoder):
    '''Json encoder class for projects'''

    def default(self, obj):
        if isinstance(obj,subProjects ):
            return [obj.__dict__]
        if isinstance(obj,Tasks):
            return[obj.__dict__]
        return json.JSONEncoder.default(self, obj)


def makejsonfile(objname, obj):
    with open(f"Store{objname}.json", "w+") as file:
        file.write('\n')
        json.dump(obj, file, cls=ObjectEncoder)

def delproject(type,todel):
   try:
      if type == "Topic":
         os.chdir(f"C:/DEV/Projects/Topics/{todel}")
         warning = input("Warning this will delete all project,subprojects and tasks within the directory. \n Type \"confirm\" to continue").strip(" ")
         if warning != "confirm":
            exit()
         confirmation = input("Type confirm?(y/n) ").strip(" ")
         if confirmation == "n":
            exit()
         if confirmation == 'y':
            os.chdir("C:/DEV/Projects/Topics")
            rmtree(f"C:/DEV/Projects/Topics/{todel}")
      if type == "Projects":
         os.chdir("C:/DEV/Projects/Topics")
         for topic in os.listdir():
            os.chdir(f"C:/DEV/Projects/Topics/{topic}")
            for project in os.listdir():
                if project == todel:
                  delpath = os.getcwd()
         os.chdir(delpath)
         rmtree(f"{delpath}/{todel}")
      if type == "subProject":
         os.chdir("C:/DEV/Projects/Topics")
         for topic in os.listdir():
            os.chdir(f"C:/DEV/Projects/Topics/{topic}")
            for project in os.listdir():
               os.chdir(f"C:/DEV/Projects/Topics/{topic}/{project}")
               for subproject in os.listdir():
                  if todel in subproject:
                     todel = subproject
                     delpath = os.getcwd()
         os.chdir(delpath)
         os.remove(f"{delpath}\\{todel}")
      if type == "Task":
         os.chdir("C:/DEV/Projects/Topics")
         for topic in os.listdir():
            os.chdir(f"C:/DEV/Projects/Topics/{topic}")
            for project in os.listdir():
               os.chdir(f"C:/DEV/Projects/Topics/{topic}/{project}/Months")
               for month in os.listdir():
                  os.chdir(f"C:/DEV/Projects/Topics/{topic}/{project}/Months/{month}")
                  for day in os.listdir():
                     os.chdir(f"C:/DEV/Projects/Topics/{topic}/{project}/Months/{month}/{day}")
                     for task in os.listdir():
                        if todel in task:
                           todel = task
                           delpath = os.getcwd()
         os.chdir(delpath)
         os.remove(f"{delpath}\\{todel}")
   except (FileNotFoundError,UnboundLocalError) :
      print(f"There is no {type} under the name \"{todel}\"")
   finally:
      print("Make?")
      
    

def CreateNew():
    typeof = input("Do you want to make a new Task, subProject, Project or Topic?").strip(" ")
    if typeof == "Topic":
        CreateTopic()
    if typeof == "Project":
        CreateProject()
    if typeof == "subProject":
        CreatesubProject()
    if typeof == "Task":
        CreateTask()

def CreateTopic():
    TopicName = input("What should be the name of the topic? ")
    os.chdir("C:/DEV/Projects/Topics")
    os.mkdir(f"{TopicName}")
def CreateProject():
    project_name = input("What is this project\'s name? ").strip(" ")
    to_complete_by = input("When should this project be completed by: ")
    time_to_complete = input(
        "How much time will you consistently put in this: ")
    Project_attr = {}
    Project_attr.update({"to complete by": to_complete_by, "time to complete": time_to_complete}) #replace with end date and start date
    os.chdir("C:/DEV/Projects/Topics")
    ListofTopics = os.listdir("C:/DEV/Projects/Topics")
    print(ListofTopics)
    TopicUnder = input("What topic is this project under? ").strip(" ")
    os.chdir(""f"C:/DEV/Projects/Topics/{TopicUnder}""")
    os.mkdir(f"{project_name}")
    os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}")
    # to determine subproject switches may have to happen between months sometimes
    # make text file that contains info about project
    os.chdir(""f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}""")
    with open(f"{project_name} Description", "a+") as project_description:
        project_description.write(str(Project_attr))
def CreatesubProject():
    objname = input("Enter name: ")
    end_date = input("When should this project be completed by: ")
    start_date = input("When to start: ").strip(" ")
    topic_under = input("Topic under ").strip(" ")
    project_under = input("Enter Project under:  ")
    obj = subProjects(objname,start_date, end_date,topic_under, project_under)
    os.chdir(f"C:/DEV/Projects/Topics/{topic_under}/{project_under}")
    makejsonfile(objname,obj)
def CreateTask():
    objname = input("Enter name of Task: ")
    month_number = today.month #maybe change this later...
    day_number = int(input('What day should this task be done on(please give number)'))
    start_date = input("Start time: ") #what time you should start it 
    end_date = input("End time: ")#due date
    topic_under = input("What topic is this task under")
    project_under = input("What project is this task under?")
    is_there_subproject_under = input("Is there is subproject(y/n)").strip(" ")
    if  is_there_subproject_under == 'y':
        subproject_under = input("what subproject is it under: ")
        obj = Tasks(objname,start_date, end_date,topic_under, project_under,month_number,day_number, subproject_under)
        os.chdir(f"C:/DEV/Projects/Topics/Calendar/Months/{month_number}/{day_number}")
        makejsonfile(objname, obj)
    else:
        obj = Tasks(objname,start_date, end_date,topic_under, project_under,month_number,day_number)
        os.chdir(f"C:/DEV/Projects/Topics/Calendar/Months/{month_number}/{day_number}")
        makejsonfile(objname, obj)

# obj.__setattr__("name","Beem")use this instead to change attributes

