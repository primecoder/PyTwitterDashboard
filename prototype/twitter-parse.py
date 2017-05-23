# Parse twitter data from file.
# This can be executed as often as you like.
import re

infile = "output.html"

# Getting data from file.
with open(infile, 'r') as f:
    read_data = f.read()
    f.close()

followersGrp = re.search(r"[\d,]+ Followers", read_data)
followingGrp = re.search(r"[\d,]+ Following", read_data)
tweetsGrp = re.search(r"[\d,]+ Tweets", read_data)
likesGrp = re.search(r"[\d,]+ Like[s]*", read_data)
avatarGrp = re.search(r"ProfileAvatar-image.*", read_data)
avatarSrcGrp = re.search(r"src=.*\" ", avatarGrp.group())

followers = re.split(' ', followersGrp.group())[0]
following = re.split(' ', followingGrp.group())[0]
tweets =  re.split(' ', tweetsGrp.group())[0]
likes =  re.split(' ', likesGrp.group())[0]
#avatar = re.split('=', avatarSrcGrp.group())[1].replace("\"", "")

print("Followers: " + followers)
print("Following: " + following)
print("Tweets: " + tweets)
print("Likes: " + likes)
print("Avatar group: " + avatarSrcGrp.group())
#print("Avatar: " + avatar)

