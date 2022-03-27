#make delete function that deletes takes the type of thing to be deleted(task,topic,etc.) and
import os
import argparse
from shutil import rmtree 

def delproject(type,todel):
   try:
      if type == "Topic":
         os.chdir(f"C:/DEV/Projects/Topics/{todel}")
         nameofTopic = str(todel)
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

"""cli"""
delete = argparse.ArgumentParser(description="to make project,task,topic, etc.")
delete.add_argument("type",metavar="type",type=str,help="enter your type")
delete.add_argument("todel",metavar="todel",type=str,help="enter file to delete")
args = delete.parse_args()

type = args.type
todel = args.todel
delproject(type,todel)
#maybe have something to display trees before deleting and having more exit points
