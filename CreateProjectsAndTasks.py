import os
import json
import typer
import calendar
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


@app.command()
def simpfunction():
    print("I make everything else work")#eventually make main function that calls  individual functions that each specialize in making task,project,tocpic,subproject 


@app.command()
def CreateNew():
    typeof = input("Do you want to make a new Task, subProject, Project,and Topic? ").strip(" ")
    if typeof == "Topic":
        TopicName = input("What should be the name of the topic? ")
        os.chdir("C:/DEV/Projects/Topics")
        os.mkdir(f"{TopicName}")
    if typeof == "Project":
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
        os.makedirs(f"{project_name}/Months")
        os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}")
        os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}/Months")
        # get current year to see if leap year
        leapYearStatus = calendar.isleap(today.year)
        feb = 30 if leapYearStatus == True else 29
        monthswith31days = [1, 3, 5, 7, 8, 10, 12]
        monthswith30days = [4, 6, 9, 11]
        # to determine subproject switches may have to happen between months sometimes
        for i in range(1, 13):
            os.mkdir(str(i))
            os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}/Months/{i}")
            if i in monthswith31days:  # check if leap year for feb
                for e in range(1, 32):
                    os.mkdir(str(e))
            os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}/Months")
            if i in monthswith30days:
                os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}/Months/{i}")
                for e in range(1, 31):
                    os.mkdir(str(e))
            os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}/Months")
            if i == 2:
                os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}/Months/{i}")
                for e in range(1, feb):
                    os.mkdir(str(e))
            os.chdir(f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}/Months")
        # make text file that contains info about project
        os.chdir(""f"C:/DEV/Projects/Topics/{TopicUnder}/{project_name}""")
        with open(f"{project_name} Description", "a+") as project_description:
            project_description.write(str(Project_attr))

    if typeof == "subProjects":
        objname = input("Enter name: ")
        end_date = input("When should this project be completed by: ")
        start_date = input("When to start: ").strip(" ")
        topic_under = input("Topic under ").strip(" ")
        project_under = input("Enter Project under:  ")
        obj = subProjects(objname,start_date, end_date,topic_under, project_under)
        os.chdir(f"C:/DEV/Projects/Topics/{topic_under}/{project_under}")
        makejsonfile(objname,obj)
    if typeof == "Task":
        #have vars for what day and month it should be under
        objname = input("Enter name of Task: ")
        month_number = today.month #maybe change this later...
        day_number = int(input('What day should this task be done on'))
        start_date = input("Start time: ") #what time you should start it 
        end_date = input("End time: ")#due date
        topic_under = input("What topic is this task under")
        project_under = input("What project is this task under?")
        is_there_subproject_under = input("Is there is subproject(y/n)").strip(" ")
        if  is_there_subproject_under == 'y':
            subproject_under = input("what subproject is it under: ")
            obj = Tasks(objname,start_date, end_date,topic_under, project_under,month_number,day_number, subproject_under)
            os.chdir(f"C:/DEV/Projects/Topics/{topic_under}/{project_under}/Months/{month_number}/{day_number}")
            makejsonfile(objname, obj)
        else:
            obj = Tasks(objname,start_date, end_date,topic_under, project_under,month_number,day_number)
            os.chdir(f"C:/DEV/Projects/Topics/{topic_under}/{project_under}/Months/{month_number}/{day_number}")
            makejsonfile(objname, obj)


# obj.__setattr__("name","Beem")use this instead to change attributes
"""cli"""
if __name__ == "__main__":
    app()
