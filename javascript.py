import json
import console
import date
import time
import requests
from datetime import datetime
def getDateandtime:
 times = []
 for rt in risetimes:
   time = datetime.fromtimestamp(rt)
   times.append(time)
   return time
