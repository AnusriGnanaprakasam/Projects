import typer
import os 
import calendar
from datetime import date
today = date.today()
startdir = "C:/DEV/Projects/Topics"
app = typer.Typer()


@app.command()
def BuildCalendar():
    #makes calendar folder which will have tasks populated into it
    os.chdir(startdir)
    os.makedirs("Calendar/Months")
    leapYearStatus = calendar.isleap(today.year)
    feb = 30 if leapYearStatus == True else 29
    monthswith31days = [1, 3, 5, 7, 8, 10, 12]
    monthswith30days = [4, 6, 9, 11]
    """build the calendar"""
    for i in range(1, 13):
        os.chdir(f"{startdir}/Calendar/Months")
        os.mkdir(str(i))
        os.chdir(f"{startdir}/Calendar/Months/{i}")
        if i in monthswith31days:  # check if leap year for feb
            for e in range(1, 32):
                os.mkdir(str(e))
        os.chdir(f"{startdir}/Calendar/Months")
        if i in monthswith30days:
            os.chdir(f"{startdir}/Calendar/Months/{i}")
            for e in range(1, 31):
                os.mkdir(str(e))
        os.chdir(f"{startdir}/Calendar/Months")
        if i == 2:
            os.chdir(f"{startdir}/Calendar/Months/{i}")
            for e in range(1, feb):
                os.mkdir(str(e))
        os.chdir(f"{startdir}/Calendar/Months")

if __name__ == '__main__':
    app()