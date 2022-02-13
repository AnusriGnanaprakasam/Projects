import argparse

from CreateProjectsAndTasks import Create_topics_projects_tasks

parser = argparse.ArgumentParser(description="cli for projects")
parser.add_argument("type",metavar="type",type=str,help="enter your type")
args = parser.parse_args()

type = args.type
Create_topics_projects_tasks(type)

