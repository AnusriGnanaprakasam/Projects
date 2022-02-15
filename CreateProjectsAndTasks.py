import os
import json
import argparse

class Topic:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        description = f"name: {self.name}"
        return description

class Projects(Topic):  # block and whitelist certain sites when working on certain things
    def __init__(self, name, to_complete_by, time_to_complete):
        super().__init__(name)
        self.to_complete_by = to_complete_by
        self.time_to_complete = time_to_complete

    def __str__(self):
        description = f"name: {self.name}"
        return description

class subProjects(Projects):
    def __init__(self, name, to_complete_by, time_to_complete, project_under):
        self.project_under = project_under  # what project the subproject is under
        super().__init__(name, to_complete_by, time_to_complete)

    def __str__(self):
        description = f"name: {self.name} \n project: {self.project_under} "
        return description

class Tasks(Projects):
    def __init__(self, name, to_complete_by, time_to_complete, project_under, subproject_under='none'):
        self.project_under = project_under  # what project the subproject is under
        self.subproject_under = subproject_under
        super().__init__(name, to_complete_by, time_to_complete)

    def __str__(self):
        description = f"name: {self.name} \n amount of time: {self.time_to_complete} \n to complete by: {self.to_complete_by} \n project: {self.project_under} \n subproject: {self.subproject_under}"
        return description

class ObjectEncoder(json.JSONEncoder):
    '''Json encoder class for projects'''
    def default(self, obj):
        if isinstance(obj, Topic):
            return [obj.__dict__]
        return json.JSONEncoder.default(self, obj)

def makejsonfile(objname,obj):
    with open(f"Store{objname}.json", "w+") as file:
        file.write('\n')
        json.dump(obj, file, cls=ObjectEncoder)

def Create_topics_projects_tasks(typeof):
    if typeof == "Topic":
        objname = input("Enter name: ")
        obj = Topic(objname)
        os.chdir("C:/DEV/Projects/Topic")
        makejsonfile(objname,obj)
    if typeof == "Projects":
        objname = input("Enter name: ")
        to_complete_by = input("When should this project be completed by: ")
        time_to_complete = input("How much time will you consistently put in this: ")
        obj = Projects(objname,to_complete_by,time_to_complete)
        os.chdir("C:/DEV/Projects/Projects")
        makejsonfile(objname,obj)
    if typeof == "subProjects":
        objname = input("Enter name: ")
        to_complete_by = input("When should this project be completed by: ")
        time_to_complete = input("How much time will you consistently put in this: ")
        #display projects
        project_under = input("Enter Project under:  ")
        obj = subProjects(objname, to_complete_by, time_to_complete,project_under)
        os.chdir("C:/DEV/Projects/subProjects")
        makejsonfile(objname,obj)
    if typeof == "Tasks":
        objname = input("Enter name: ")
        to_complete_by = input("When should this project be completed by: ")
        time_to_complete = input("How much time will you consistently put in this: ")
        project_under = input("")
        is_there_a_subproject = input("Is there is subproject(y/n)").strip(" ")
        if is_there_a_subproject == 'y':
            subproject_under = input("what subproject is it under: ")
            obj = Tasks(objname, to_complete_by, time_to_complete, project_under,subproject_under)
            os.chdir("C:/DEV/Projects/Tasks")
            makejsonfile(objname,obj)
        else:
            obj = Tasks(objname, to_complete_by, time_to_complete, project_under)
            os.chdir("C:/DEV/Projects/Tasks")
            makejsonfile(objname,obj)
# obj.__setattr__("name","Beem")use this instead to change attributes
"""cli"""
make = argparse.ArgumentParser(description="to make project,task,topic, etc.")
make.add_argument("type",metavar="type",type=str,help="enter your type")
args = make.parse_args()

type = args.type
Create_topics_projects_tasks(type)

