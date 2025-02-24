import matplotlib.pyplot as plt
import numpy as np
import json
from dateutil.parser import isoparse, parse
from datetime import datetime, timedelta, timezone

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

# get all keys
keys = list({d["name"] for d in data if "name" in d})
print(keys)

# define start
# use this if you have a particular idea:
#start = datetime(2025,2,3, tzinfo=timezone.utc) 
# use this if you want to just use the first recorded thing:
start = data[0]["start"]
print(start)
start = start - timedelta(days=start.weekday())
print(start)

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

print(timeslots)
print(y)

# plot as line chart
weeknums = [str(w.isocalendar()[1]) for w in timeslots]
#for n in y:
#    plt.plot(weeknums, y[n])

# plot as stacked bar chart
bottom = np.empty(len(weeknums))
for n in y:
    print(f"{n}: {y[n]}")
    plt.bar(weeknums, y[n])
    bottom = np.add(bottom, y[n])

# data 
plt.xlabel("Week numbers")
plt.ylabel("Hours")
plt.legend(keys)
plt.title("Amount of time on modules per week")
plt.show()

# todo:
# bar chart option?
# or just make it a bar chart?