import dateutil.parser
from datetime import datetime, timedelta
import os
import sys
import json
from pprint import pprint

PATH = 'labels/'
DIF = 5

if sys.argv[1] == 'now':
    datestring = "2018-05-05T{0}:{1}:{2}.908Z".format(
        datetime.now().hour,
        datetime.now().minute,
        datetime.now().second)

# print(datestring)

# print(datestring)
camDate = dateutil.parser.parse(datestring) - timedelta(hours=3)
# camDate = datetime.now()

labels = []

for filename in os.listdir(PATH):
    if filename.endswith(".json"):
        with open(PATH + filename) as file:
            data = json.load(file)
        startDate = dateutil.parser.parse(data['startTime'])
        if (camDate + timedelta(minutes=DIF)) >= startDate >= (camDate - timedelta(minutes=DIF)):
            labels = data["slides"]
            break

# pprint(labels)
result = []
for l in labels:
    time = dateutil.parser.parse(l['time'])
    result.append([(time - startDate).seconds * 1000, l['num']])

print(result)