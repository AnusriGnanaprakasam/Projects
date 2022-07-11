###############################################################################################

 General Description and Explanation:

The LifeManager package(This name is not that good so please tell me if you have any suggestions for an alternative) can manage that amount of time people spend on certain things throughout the year. There are four catagories(going from largest to smallest): topic,project,subproject,task. Topics should be broad subject or skill(i.e. Typing). Each of the others listed after Topic should be more specific and be completed in a specific time frame like a month or week depending on however you would like to think about it. Tasks are subsets of (in this order specific to broadest) subprojects(if you think this level of subcategorization is needed),Projects, and Topics. 

everything is done. just need to test all the functions.

Some potential issues: 

 When uninstalling using pip, the config file is not uninstalled with the rest of the package. This means that the location where the task calendar was installed is still recorded. If you want to reinstall everything (like it was never installed before), you will have to go to  [python installation location]\lib\site-packages\lifemanager\config.json and delete it yourself.(i really need to fix this later)
 ---not an issue with the executable that i sent

Did not put an 'r' infront of directories. That is because i do not want the directories to be treated as raw strings. I escaped them instead. 

need to put list of commands as a part of the argparse help thing 

SOME OTHER STUFF THAT I WILL FIND LATER:

- should display projects and subprojects when asked for making new task or subproject (new function )
- put the main.py file in the directory outside the "lifemanager" uses form works fine

Modules explained:

main.py:

This is the module that the app is always run from(entry-point). Basically the command line interface.

config.json:

Contains information about where calander is installed and the current year.

blocker.py: #Please read

This module contains functions that modify the host file. The host file is unessential and can be deleted with no harm to the system. The host file is set to read-only by default. To change this, you can run the command : "icacls hosts /grant everyone:(f) /t /c". You should run this command from an account with administrator privileges on Windows 10 (for Windows 7 you can only run it from the administrator account itself). This command will enable program to run from anywhere without errors. If the command does not work, just go to the directory : C:\Windows\System32\drivers\etc and you will find the hosts file. Edit the properties from there. 

delmakeobj.py:

Classes to define project and tasks attributes. These objects are later turned into json files for storage. There are also functions to delete them in this module.

timer.py:

This is the module that creates a timer. The timer can be paused because the countdown process is interrupted if a person presses control c while in the cmd. So if there is a "Keyboard Interrupt" error(you press ctrl c), the attribute "duration" of the task is modified . This means the timer can be continued from where it left off because the pause function modifies the attribute "duration" that the task contains to the time remaining.

setup.py:

For package distribution ^-^

setup.cfg:

Also for package distribution. Sets entry points and contains requirements and some other important stuff. 

pyproject.toml:

For package distribution
specifies how project is built

To change:
- make it so that all the questions are in cli(then given to function that it calls)
