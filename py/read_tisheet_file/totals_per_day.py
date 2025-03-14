import json
import sys
from dateutil.parser import isoparse, parse
from datetime import datetime, timedelta, timezone
from tabulate import tabulate

TI_SHEET_LOCATION = "/home/elia/.ti-sheet"

tz = timezone.utc

# open file
with open(TI_SHEET_LOCATION) as file:
    data = json.load(file)["work"]

# format for printing
def getDateString(d):
    return f'{d:%d/%m/%y at %H:%M}'

def cleanData(data):
    for x in data:
        x["start"] = isoparse(x["start"])
        if "end" not in x:
            x["end"] = datetime.now(tz=tz)
        else:
            x["end"] = isoparse(x["end"])
    
    return data

def getTotalMinutes(data, startoflog, endoflog=0):
    # endoflog is an optional parameter, if unspecified will default to "right now" (see few lines down for where it is assigned)

    # get current datetime; ?
    now = datetime.now(tz=tz)
    if (endoflog == 0): endoflog = now # default assignment for optional here, because we need it to be equal to now

    # for storing amount of time spent on each activity
    timedata = {}

    # loop through every item in ti_sheet,
    for x in data:
        xstart = x["start"]
        xend = x["end"]
        
        # if before or after this period of time, skip
        if (xstart < startoflog): continue 
        elif (xend > endoflog): continue

        # calculate difference as total minutes
        difference = (xend - xstart)
        difference = int(difference / timedelta(minutes=1))

        # save total time(s) into dictionary
        if x["name"] not in timedata: timedata[x["name"]] = 0
        timedata[x["name"]] += difference

    # return
    return timedata

def printCalendarFormat(data, startoflog, endoflog=0):
    # get current datetime; ?
    now = datetime.now(tz=tz)
    if (endoflog == 0): endoflog = now # default assignment for optional here, because we need it to be equal to now

    # generate each hour; we will loop through this
    timeslots = [startoflog + timedelta(hours=i) for i in range((endoflog - startoflog).seconds // 3600 + 1)]

    # header!
    header = ["Time", "Activities"]

    # gen table rowsmissing
    table = []
    for t in timeslots:
        t_end = t + timedelta(hours=1) # t2 = t + an hour
        row = [t.strftime("%H:%M")] # time label in time column
        events = [event["name"] for event in data if event["start"] < t_end and t < event["end"]]
        
        if events:
            row.append(", ".join(events))
        else:
            row.append("")

        table.append(row)
    
    # print table
    print(tabulate(table, headers=header, tablefmt="plain"))


now = datetime.now(tz=tz)
# start of current day
startofday = datetime(now.year, now.month, now.day, tzinfo=now.tzinfo)
# start of current week (todo does this work if the week starts last month?)
startofweek = datetime(now.year, now.month, now.day - now.weekday(), tzinfo=now.tzinfo)

# clean data! specifically, fill in missing "end" datapoints with current datetime
data = cleanData(data)

# parse args
target = 0 # overwrite this below
DAILYTARGETHOURS = 4
if (len(sys.argv) == 2):
    # if one argument given, assume text direction given
    if sys.argv[1] == "day": # today 
        target = DAILYTARGETHOURS * 60 # 4.5 hours
        start = startofday
        print(f"Reading events today (from {getDateString(startofday)} to right now)")
    elif sys.argv[1] == "week": # this week
        weekday = (now - startofweek).days+1
        if weekday > 5: weekday = 5
        print(weekday)
        target = DAILYTARGETHOURS * 60 * weekday # 4.5 hours multiplied by amount of days in week 
        start = startofweek
        print(f"Reading events this week (from {getDateString(startofweek)} to right now)")
    activity = getTotalMinutes(data, start)
    printCalendarFormat(data, start)
elif (len(sys.argv) == 3): 
    # if two arguments given, assume they are given dates 
    start = (parse(sys.argv[1], dayfirst=True)).replace(tzinfo=tz)
    end = (parse(sys.argv[2], dayfirst=True)).replace(tzinfo=tz)

    print(f"Reading events from given dates : {getDateString(startofweek)} to {getDateString(startofday)}\n")

    activity = getTotalMinutes(data, start, end)
else:
    print(f"Dates not given, reading events today (from {getDateString(startofday)} to right now)")
    target = DAILYTARGETHOURS * 60
    activity = getTotalMinutes(data, startofday)

print() # empty line

# json print as amount of minutes
#print(timedata)

# calendar thing!
printCalendarFormat(data, startofday)

# pretty print
print()
totalmins = 0
for x in activity:
    hours = int(activity[x] / 60)
    minutes = activity[x] % 60
    totalmins += activity[x]
    print(f"{x} : {hours} hour{'' if hours == 1 else 's'} and {minutes} minutes")
hours = int(totalmins/60)
minutes = totalmins % 60
print(f"\nTotal : {hours} hour{'' if hours == 1 else 's'} and {minutes} minutes")

# relative to target
if target != 0:
    print(f"Target : {target/60} hours")
    print(f"{round((totalmins / target)*100)}% of target")
