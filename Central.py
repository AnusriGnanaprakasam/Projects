import os
import pathlib
import json
from datetime import date
import typer
import CreateAndDeleteItems
from pyfiglet import figlet_format
from rich.tree import Tree
from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text


startdir = "C:/DEV/Projects/Topics"
today = date.today()
app = typer.Typer()

#make a startup overview function that gives an overview at a certain time of what tasks in what proj and subproj need to be done
welcome_message = figlet_format("Welcome",font="doh",width=500)
display_possible_commands= figlet_format("Projects: list of commands in a tree")
print(welcome_message)

@app.command()
def startwork():
    tree = Tree(Tree(f":open_file_folder: [link file://{startdir}]{startdir}",guide_style="bold bright_blue",))
    walk_directory(pathlib.Path(startdir), tree)
    print(tree)
    #make it print tree function with rich from the module
@app.command()
def New():
    CreateAndDeleteItems.CreateNew()
@app.command()
def LookAtProjects():#make it so that attrs can be changed
    topic = input("What Topic do you want to look at?" )
    location = f"C:\DEV\Projects\Topics\{topic}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" not in x),allfileindir))
    print(allfileindir)
    project = input("What project do you want to look at?")
    os.chdir(location+f"\{project}")
    LookAtAttr(project+" Description")
@app.command()
def LookAtsubProjects(): #make it so that they can be changed
    project,topic = input("What Project and Topic do you want to look at(project,topic)?" ).split(",")
    location = f"C:\DEV\Projects\Topics\{topic}\{project}"
    os.chdir(location)
    allfileindir = os.listdir(location)
    allfileindir = list(filter(lambda x:(".json" in x),allfileindir))
    print(allfileindir)
    subproject = input("What subproject do you want to look at? ")
    for i in os.listdir(f"C:\DEV\Projects\Topics\{topic}\{project}"):
        if i == "Store"+subproject+".json":
            subproject = "Store"+subproject+".json"
            LookAtAttr(subproject)
@app.command()
def LookAtTasks():#make it so that attrs can be changed
    fortoday = input("For today(y/n)? ").strip(" ")
    if fortoday == "y":
        day,month = today.day,today.month
        os.chdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}')
        print(os.listdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}'))
        get_attr = input("Would you like to get details on the task?(y/n) ")
        if get_attr.strip(" ") == "y":
            Taskname = input("What task would you like to look at")
            Taskname = "Store"+Taskname+".json"
            LookAtAttr(Taskname)
        
    if fortoday == "n":
        lookdaymonth = input("From what day and month?(format: \"d m\") ").split(" ")
        day,month = lookdaymonth
        os.chdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}')
        print(os.listdir(f'C:\DEV\Projects\Topics\Calendar\Months\{month}\{day}'))
        get_attr = input("Would you like to get details on the task?(y/n) ")
        if get_attr.strip(" ") == "y":
            Taskname = input("What task would you like to look at")
            Taskname = "Store"+Taskname+".json"
            LookAtAttr(Taskname)
        
def LookAtAttr(objname):
    if ".json" in objname:
        with open(f"{objname}",'r+') as objfile:
            attr = json.load(objfile)
            print(attr)
    else:
        with open(f"{objname}",'r+') as objfile:
            print(objfile.read())

def walk_directory(directory: pathlib.Path, tree: Tree) -> None:
    """Recursively build a Tree with directory contents. cred: https://github.com/Textualize/rich""" 
    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    for path in paths:
        # Remove hidden files
        if path.name.startswith("1"):
           break
        if path.name.startswith("2"):
           break
        if path.name.startswith("3"):
           break
        if path.is_dir():
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
                style=style,
                guide_style=style,
            )
            walk_directory(path, branch)
        else:
            text_filename = Text(path.name, "green")
            text_filename.highlight_regex(r"\..*$", "bold red")
            text_filename.stylize(f"link file://{path}")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            icon = "🐍 " if path.suffix == ".py" else "📄 "
            tree.add(Text(icon) + text_filename)


#look at tasks for today  -one command
#make new task - another command

if __name__ == '__main__':
    #print(display_possible_commands)
    app()