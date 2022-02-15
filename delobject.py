#make delete function that deletes takes the type of thing to be deleted(task,topic,etc.) and
import os
import argparse
from CreateProjectsAndTasks import Create_topics_projects_tasks

def mylife(type,todel):
   try:
      os.chdir(f"C:/DEV/Projects/{type}")
      f = open(f"Store{todel}.json",'r+')
      lines = f.readlines()
      nameofTopic = str(todel)
      for i in lines:
         if nameofTopic in i:
            print(i)
            nameofTopic = i
      lines.remove(nameofTopic)
      f.truncate(0)
      for i in lines:
         f.write(i)
      f.close()
   except FileNotFoundError :
      print(f"There is no {type} under the name \"{todel}\"")
   finally:
      print("make?")

"""cli"""
delete = argparse.ArgumentParser(description="to make project,task,topic, etc.")
delete.add_argument("type",metavar="type",type=str,help="enter your type")
delete.add_argument("todel",metavar="todel",type=str,help="enter file to delete")
args = delete.parse_args()

type = args.type
todel = args.todel
mylife(type,todel)

