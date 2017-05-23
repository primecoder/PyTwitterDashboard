# Read twitter user's data (followers, following, tweets, and likes).
# Author: Ace
# Created: 2017.06.19

import urllib.request
import ssl
import re
from string import Template

twitterUrl = "http://twitter.com/"

# Twitter redirs to https. Need to handle this.
ssl._create_default_https_context = ssl._create_unverified_context

userInfoTemplateStr = """
    <div class='UserInfo'>
        <div class='Avatar'><img class='Avatar' src='${avatar}'/></div>
        <div class='Handle'>${handle}</div>
        <div class='Followers'>${followers}</div><div class="DataLabel">followers</div>
        <div class='Following'>${following}</div><div class="DataLabel">followings</div>
        <div class='Tweets'>${tweets}</div><div class="DataLabel">tweets</div>
        <div class='Likes'>${likes}</div><div class="DataLabel">likes</div>
    </div>
"""
userInfoTemplate = Template(userInfoTemplateStr)

def twitterGetUserData(twitterHandle):
    targetUrl = twitterUrl + twitterHandle
    html = urllib.request.urlopen(targetUrl).read()
    return html.decode("utf-8")

def saveToFile(fileName, data):
    with open(fileName, 'w') as f:
        f.write(data)
        f.close

def readFromFile(fileName):
    with open(fileName, 'r') as f:
        read_data = f.read()
        f.close()
        return read_data

def parseData(dataString):
    followersGrp = re.search(r"[\d,]+ Follower[s]*", dataString)
    followingGrp = re.search(r"[\d,]+ Following", dataString)
    tweetsGrp = re.search(r"[\d,]+ Tweet[s]*", dataString)
    likesGrp = re.search(r"[\d,]+ Like[s]*", dataString)
    avatarGrp = re.search(r"ProfileAvatar-image.*", dataString)
    avatarSrcGrp = re.search(r"src=.*\" ", avatarGrp.group())
    r"src=.*\" "

    followers = re.split(' ', followersGrp.group())[0]
    following = re.split(' ', followingGrp.group())[0]
    tweets =  re.split(' ', tweetsGrp.group())[0]
    likes =  re.split(' ', likesGrp.group())[0]
    avatar = re.split('=', avatarSrcGrp.group())[1].replace("\"", "")

    return {
        'followers': followers,
        'following': following,
        'tweets': tweets,
        'likes': likes,
        'avatar': avatar
        }

def formatHtml(userInfo):
    return userInfoTemplate.substitute(userInfo)
