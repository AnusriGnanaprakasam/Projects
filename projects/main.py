
import os 
import json
import calendar
from datetime import date
from pyfiglet import figlet_format
from pathlib import Path

'''entry point: updates stuff whenever needed'''
#year initially will always be set to last year when intially installed so that calendar is formed
today = date.today()
directory = Path(__file__).parent/"config.json" #to find json file(need to look into why this is required)
def main():
    #have the startup message here
    with open(directory, "r+") as config:
        year_yesterday= json.load(config)
        year_yesterday = year_yesterday["year"]#be careful of the quotes
        if today.year != int(year_yesterday):
            modify_config("year",today.year)
            BuildCalendar()
            
     
    print("use command  \'projects --help\' to look at commands \n And make sure to run this again after a new year :)")

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
    directory = Path(__file__).parent/"config.json" 
    with open(directory,'r+') as config: #may want to revise this one...
        configdict = json.load(config)
        return configdict[attribute]         

def BuildCalendar():
    '''makes calendar folder which will have tasks populated into it'''
    startdir= input("What directory do you want to install the calendar in?").strip()
    os.chdir(startdir)
    os.makedirs("Topics/Calendar/Months")
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
    
if __name__ == '__main__':
    welcome_message()
    make_config()
    main()