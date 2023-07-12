import twitterUtils
import json
import htmlTemplate
from datetime import datetime

''' This is Test list.
people = [
    "logical_101",
    "mkbhd",
    "ijustine",
    "Austin_Powers__",
    "ITCrowdSupport",
    "Harry_Styles",
    "snowden",
    "jk_rowling",
    "realDonaldTrump"
]
'''
people = [
    "icuriosity",
    "logical_101",
    "numerologician",
    "icuriosity2",
    "_APinchOfSalt",
    "mini_landscape",
    "Alpetcho7777",
    "_catherineada",
    "Austin_Powers__"
]
contents = ""
for person in people:
    print("Reading data for: " + person + " ...")
    read_data = twitterUtils.twitterGetUserData(person)
    userInfo = twitterUtils.parseData(read_data)
    userInfo["handle"] = "@" + person
    userHtml = twitterUtils.formatHtml(userInfo)
    contents = contents + userHtml

today = datetime.now()
todayStr = today.strftime("%A %d %B %Y %H:%M:%S")
html = htmlTemplate.htmlTemplate.substitute(contents=contents, timeinfo=todayStr)
twitterUtils.saveToFile('dashboard.html', html)
