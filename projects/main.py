
import os 
import json
import calendar
from datetime import date
from pyfiglet import figlet_format
from pathlib import Path
import cli

'''entry point: updates stuff whenever needed'''
#year initially will always be set to last year when intially installed so that calendar is formed
today = date.today()
directory = Path(__file__).parent/"config.json" #to find json file(need to look into why this is required)
def main():
    #have the startup message here\
    welcome_message()
    if find_config("start_directory") == "not found":
        make_config()
        with open(directory, "r+") as config:
            year_yesterday= json.load(config)
            year_yesterday = year_yesterday["year"]#careful of quotes
            if today.year != int(year_yesterday):
                modify_config("year",today.year)
                BuildCalendar()
    ListOfCommands = """
    - startwork
    - new
    - delete
    - lookatprojects 
    - lookatsubprojects - .json not apart of input
    - lookattasks - .json not apart of input
    """
    path = find_config("start_directory")
    get_command = input(ListOfCommands+"\n Please type one of these commands.If not, exit with \"no\" ").strip()# if not exit with (n)
    if get_command == "no":
        exit()
    if get_command == "startwork":
        cli.startwork(path)
    if get_command == "new":
        cli.new(path)
    if get_command == "delete":
        cli.delete(path)
    if get_command == "lookattasks":
        cli.LookAtTasks(path)
    if get_command == "lookatprojects":
        cli.LookAtProjects(path)
    if get_command == "lookatsubprojects":
        cli.LookAtsubProjects(path)
    
       

def modify_config(attribute,value):
    with open(directory,'r+') as config:
        configdict = json.load(config)
        if attribute not in configdict.keys():#find way to update dictionary(hmm)
            configdict = dict(configdict)
            configdict.update({attribute:value})
            config.seek(0)
            json.dump(configdict,config)#this value is null?
            config.truncate()
        else:  #this part is fine
            configdict[attribute] = value
            config.seek(0)
            json.dump(configdict, config, indent=4) #why null
            config.truncate() 

def find_config(attribute):
    try:
        directory = Path(__file__).parent/"config.json" 
        with open(directory,'r+') as config: #may want to revise this one...
            configdict = json.load(config)
            return configdict[attribute]
    except FileNotFoundError:
        return("not found")
    except:
        print("something must be wrong internally.")
             

def BuildCalendar():
    '''makes calendar folder which will have tasks populated into it'''
    startdir= input("What directory do you want to install the calendar in?").strip()
    try:
        #if error, del prev calander and replace with new one
        os.chdir(startdir) #dir not found and file not empty
        os.makedirs("Topics/Calendar/Months")
    except (FileNotFoundError,FileExistsError) as e:
        print(e)
        print("you should most likely input another directory(or create if file not found error)")
        BuildCalendar()

    else:
        leapYearStatus = calendar.isleap(today.year)
        feb = 30 if leapYearStatus == True else 29
        monthswith31days = [1, 3, 5, 7, 8, 10, 12]
        monthswith30days = [4, 6, 9, 11]
        """build the calendar"""
        for month in range(1, 13):
            os.chdir(f"{startdir}/Topics/Calendar/Months")
            os.mkdir(str(month))
            os.chdir(f"{startdir}/Topics/Calendar/Months/{month}")
            if month in monthswith31days:  # check if leap year for feb
                for day in range(1, 32):
                    os.mkdir(str(day))
            os.chdir(f"{startdir}/Topics/Calendar/Months")
            if month in monthswith30days:
                os.chdir(f"{startdir}/Topics/Calendar/Months/{month}")
                for day in range(1, 31):
                    os.mkdir(str(day))
            os.chdir(f"{startdir}/Topics/Calendar/Months")
            if month == 2:
                os.chdir(f"{startdir}/Topics/Calendar/Months/{month}")
                for day in range(1, feb):
                    os.mkdir(str(day))
            os.chdir(f"{startdir}/Topics/Calendar/Months")
        modify_config("start_directory",startdir)


def welcome_message():
    welcome_message = figlet_format("ello :)",font="doh",width=500)
    print(welcome_message)

def make_config(): #make the actual file
    with open(directory,'w') as config:
        start = {"year":today.year-1}
        json.dump(start,config)
 
