import matplotlib.pyplot as plt
import numpy as np
import json
from dateutil.parser import isoparse, parse
from datetime import datetime, timedelta, timezone
from itertools import accumulate

TI_SHEET_LOCATION = "/home/elia/.ti-sheet"

with open(TI_SHEET_LOCATION) as file:
    data = json.load(file)["work"]

def cleanData(data):
    for x in data:
        x["start"] = isoparse(x["start"])
        if "end" not in x:
            x["end"] = datetime.now(tz=timezone.utc)
        else:
            x["end"] = isoparse(x["end"])
    
    return data

cleanData(data)

# function from totals_per_day.py
def getTotalMinutes(data, startoflog, endoflog=0):
    # endoflog is an optional parameter, if unspecified will default to "right now" (see few lines down for where it is assigned)

    # get current datetime; ?
    now = datetime.now(tz=timezone.utc)
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

# what do you want to exclude?
excluded = ["comp1054", "comp1056"]

# get all keys
keys = list({d["name"] for d in data if d["name"] not in excluded})
#print(keys)

# define start
# use this if you have a particular idea:
#start = datetime(2025,2,3, tzinfo=timezone.utc) 
# use this if you want to just use the date of the first recorded thing:
start = data[0]["start"]
start = datetime(start.year, start.month, start.day, tzinfo=timezone.utc)
start = start - timedelta(days=start.weekday())

# get data
# generate each week
end = datetime.now(tz=timezone.utc) # end
timeslots = [start + timedelta(weeks=i) for i in range((int((end - start).total_seconds()) // 604800)+1)]
# loop through keys, adding to array
y = {k: [] for k in keys}
for start in timeslots:
    d = getTotalMinutes(data, start, start+timedelta(weeks=1))
    for k in keys:
        # if k is in y, append it; else, append 0
        if k in d.keys():
            y[k].append(d[k] / 60)
        else:
            y[k].append(0)

# Convert to numpy arrays
for n in y:
    y[n] = np.array(y[n])

# plot as line chart
weeknums = [str(w.isocalendar()[1]) for w in timeslots]
#for n in y:
#    plt.plot(weeknums, y[n])

# plot A: stackplot
sortedkeys = sorted(y.keys())
# A1: per week
y_vals = [y[n] for n in sortedkeys]
# A2: accumulated
#y_vals = [y[n].cumsum().tolist() for n in sortedkeys]
plt.stackplot(weeknums, y_vals)

# plot B/C: stacked bar chart or stacked line chart
#bottom = np.empty(len(weeknums))
#sortedkeys = sorted(y.keys())
#for n in sortedkeys:
    # B
    #plt.bar(weeknums, y[n], bottom=bottom)
    # C
    #plt.plot(weeknums, y[n]+bottom)
    # both B and C
    #bottom = np.add(bottom, y[n])

# show plot
plt.xlabel("Week numbers")
plt.ylabel("Hours")
plt.legend(sortedkeys)
plt.title("Amount of time on modules per week")
plt.show()