

Hello! It is 3 am right now so there are probably going to be typos in this. Anyways, this document should explain what this package does. Please read all of it if you can.

 General Description and Explanation:

The LifeManager package(This name is not that good so please tell me if you have any suggestions for an alternative) can manage that amount of time people spend on certain things throughout the year. There are four catagories(going from largest to smallest): topic,project,subproject,task. Topics should be broad subject or skill(i.e. Typing). 


Modules explained:

main.py:

This is the module that the app is always run from(entry-point)

config.json:

Contains information about where calander is installed and the current year.

blocker.py:

This module contains functions that modify the host file. The host file is unessential and can be deleted with no harm to the system. Despite this, the host file is set to read-only by default. To change this, you can run the command : "icacls hosts /grant everyone:(f) /t /c". You should run this command from an account with administrator privileges on Windows 10 (for Windows 7 you can only run it from the administrator account itself). This command will enable program to run from anywhere without errors. If the command does not work, just go to the directory : C:\Windows\System32\drivers\etc and you will find the hosts file. Edit the properties from there. 

delmakeobj.py:

Classes to define project and tasks attributes. These objects are later turned into json files for storage. There are also functions to delete them in this module.

timer.py:

This is the module that creates a timer. The timer can be paused because the countdown process can be interrupted if a person presses control c while in the cmd. So if there is a "Keyboard Interrupt" error, the attribute "duration" of the task is modified . This means the timer can be continued from where it left off because the pause function modifies the attribute "duration" that the task contains.

cli.py:

This module is kind of a middleman. I may change the way I orgainize the package later but this file is important because it does contain important functions.

requirements.txt:

text file that contains all the requirements needed to run this pacakge
use command:  pip install -r requirements.txt

setup.py:

I need this file in order to package for distribution
