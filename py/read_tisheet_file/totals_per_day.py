import json
from dateutil.parser import isoparse
from datetime import datetime, timedelta, timezone

with open("/home/elia/.ti-sheet", "r") as file:
    data = json.load(file)["work"]

now = datetime.now(tz=timezone.utc)
today = datetime(now.year, now.month, now.day, tzinfo=now.tzinfo)

timedata = {}

for x in data:
    start = isoparse(x["start"])
    if "end" not in x:
        print(f"{x['name']} : currently ongoing") 
        continue
    end = isoparse(x["end"])
    if (start < today): continue # before this day
    # todo check for end of day
    difference = end - start
    #print(f"{x['name']} : {difference}")

    if x["name"] not in timedata: timedata[x["name"]] = timedelta(days=0)
    timedata[x["name"]] += difference

for x in timedata:
    print(f"{x} : {timedata[x]}")
