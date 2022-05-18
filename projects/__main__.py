
import os 
import calendar
from datetime import date
from pyfiglet import figlet_format

'''entry point'''
#to run package as executable program: python -m packagename
today = date.today()

def main():
    #have the startup message here
    with open("re_calendar.txt", "r") as re_calendar:
        year_yesterday= re_calendar.read()
        year_yesterday = year_yesterday.strip()
    if today.year != int(year_yesterday):
        with open('re_calendar.txt','w+') as re_calendar:
            re_calendar.write(str(today.year))
        BuildCalendar()
         
    print("use command \'python ./cli.py --help\' to look at commands")

def BuildCalendar():
    #makes calendar folder which will have tasks populated into it
    startdir = input("What directory do you want to install the calendar in?").strip()
    os.chdir(startdir)
    os.makedirs("Calendar/Months")
    leapYearStatus = calendar.isleap(today.year)
    feb = 30 if leapYearStatus == True else 29
    monthswith31days = [1, 3, 5, 7, 8, 10, 12]
    monthswith30days = [4, 6, 9, 11]
    """build the calendar"""
    for month in range(1, 13):
        os.chdir(f"{startdir}/Calendar/Months")
        os.mkdir(str(month))
        os.chdir(f"{startdir}/Calendar/Months/{month}")
        if month in monthswith31days:  # check if leap year for feb
            for day in range(1, 32):
                os.mkdir(str(day))
        os.chdir(f"{startdir}/Calendar/Months")
        if month in monthswith30days:
            os.chdir(f"{startdir}/Calendar/Months/{month}")
            for day in range(1, 31):
                os.mkdir(str(day))
        os.chdir(f"{startdir}/Calendar/Months")
        if month == 2:
            os.chdir(f"{startdir}/Calendar/Months/{month}")
            for day in range(1, feb):
                os.mkdir(str(day))
        os.chdir(f"{startdir}/Calendar/Months")

if __name__ == '__main__':
    welcome_message = figlet_format("Beem :)",font="doh",width=500)
    display_possible_commands= figlet_format("Projects: list of commands in a tree")
    print(welcome_message)

    if "re_calendar.txt" not in os.listdir():
        with open("re_calendar.txt",'w') as re_calendar:
            re_calendar.write(str(today.year))
    main()