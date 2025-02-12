import json
from dateutil.parser import isoparse
from datetime import datetime, timedelta, timezone

TI_SHEET_LOCATION = "/home/elia/.ti-sheet"

# format for printing
def getDateString(d):
    return f'{d:%d/%m/%y at %H:%M}'

def getTotalMinutes(startoflog, endoflog=0):
    # endoflog is an optional parameter, if unspecified will default to "right now" (see few lines down for where it is assigned)

    # open file
    with open(TI_SHEET_LOCATION) as file:
        data = json.load(file)["work"]

    # get current datetime; ?
    now = datetime.now(tz=timezone.utc)
    if (endoflog == 0): endoflog = now # default assignment for optional here, because we need it to be equal to now

    # for storing amount of time spent on each activity
    timedata = {}

    # loop through every item in ti_sheet,
    for x in data:
        xstart = isoparse(x["start"])

        if "end" not in x: # if no end to activity, it is current 
            xend = now # so that it can count towards totals
        else: 
            xend = isoparse(x["end"])
        
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

now = datetime.now(tz=timezone.utc)
# start of current day
startofday = datetime(now.year, now.month, now.day, tzinfo=now.tzinfo)
# start of current week (todo does this work if the week starts last month?)
startofweek = datetime(now.year, now.month, now.day - now.weekday(), tzinfo=now.tzinfo)

# log dates used
print(f"Reading events from : {getDateString(startofweek)} to {getDateString(startofday)}\n")
activity = getTotalMinutes(startofweek, startofday)

# json print as amount of minutes
#print(timedata)

# pretty print
totalmins = 0
for x in activity:
    hours = int(activity[x] / 60)
    minutes = activity[x] % 60
    totalmins += activity[x]
    print(f"{x} : {hours} hour{'' if hours == 1 else 's'} and {minutes} minutes")
hours = int(totalmins/60)
minutes = totalmins % 60
print(f"\nTotal : {hours} hour{'' if hours == 1 else 's'} and {minutes} minutes")
