'''log info in sql database using sql api
https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
get some meaningful data out of it
'''

import json
from json import JSONEncoder


class Projects: #block and whitelist certain sites when working on certain things
    def __init__(self, name, to_complete_by, time_to_complete):
        self.name = name
        self.to_complete_by = to_complete_by
        self.time_to_complete = time_to_complete

    def __str__(self):
        description = f"name: {self.name}"
        return description
    def changeName(self,tochangeto):
        self.name = tochangeto
        return print(self)
    def change_to_complete_by(self,tochangeto):
        self.to_complete_by = tochangeto
        return print(tochangeto)
    def change_time_to_complete(self,tochangeto):
        self.time_to_complete = tochangeto
        return print(tochangeto)

class subProjects(Projects):
    def __init__(self,name,to_complete_by,time_to_complete,project_under):
        self.project_under = project_under # what project the subproject is under
        super().__init__(name,to_complete_by,time_to_complete)
    def __str__(self):
        description = f"name: {self.name} \n project: {self.project_under} "
        return description


    def changeName(self,tochangeto):
        self.name = tochangeto
        return print(self)
    def change_to_complete_by(self,tochangeto):
        self.to_complete_by = tochangeto
        return print(tochangeto)
    def change_time_to_complete(self,tochangeto):
        self.time_to_complete = tochangeto
        return print(tochangeto)
    def change_project_under(self,tochangeto):
        self.project_under = tochangeto
        return print(tochangeto)
class Tasks(Projects):
    def __init__(self,name,to_complete_by,time_to_complete,project_under,subproject_under = 'none'):
        self.project_under = project_under # what project the subproject is under
        self.subproject_under = subproject_under
        super().__init__(name,to_complete_by,time_to_complete)
    def __str__(self):
        description = f"name: {self.name} \n amount of time: {self.time_to_complete} \n to complete by: {self.to_complete_by} \n project: {self.project_under} \n subproject: {self.subproject_under}"
        return description
    def changeName(self,tochangeto):
        self.name = tochangeto
        return print(self)
    def change_to_complete_by(self,tochangeto):
        self.to_complete_by = tochangeto
        return print(tochangeto)
    def change_time_to_complete(self,tochangeto):
        self.time_to_complete = tochangeto
        return print(tochangeto)
    def change_project_under(self,tochangeto):
        self.project_under = tochangeto
        return print(tochangeto)
    def change_subproject_under(self,tochangeto):
        self.subproject_under = tochangeto
        return print(tochangeto)

x = Projects("Proto","Feb 4", 1)

