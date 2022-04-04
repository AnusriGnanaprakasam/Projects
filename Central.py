import argparse
import typer
import CreateAndDeleteItems
from pyfiglet import figlet_format

app = typer.Typer()

@app.command()
def LookAtTasksForToday():
    pass 
@app.command()
def New():
    CreateAndDeleteItems.CreateNew()
#look at tasks for today  -one command
#make new task - another command



if __name__ == '__main__':
    welcome_message = figlet_format("Welcome",font="doh",width=500)
    display_possible_commands= figlet_format("Projects: list of commands in a tree")
    print(welcome_message)
    print(display_possible_commands)
    app()