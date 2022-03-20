import argparse
from pyfiglet import figlet_format


'''Upon starting'''
welcome_message = figlet_format("Welcome",font="doh",width=500)
display_possible_commands= figlet_format("Projects: list of commands in a tree")

parser = argparse.ArgumentParser()
parser.add_argument("start",help="it just prints Welcome")
args = parser.parse_args()
print(welcome_message)
print(display_possible_commands)

#i need to make a options thing to look at stuff



