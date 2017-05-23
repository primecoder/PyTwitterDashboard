# Read Twitter data and save to a file.
# Be careful, not to read this to often as this may appear as DOS attack.
#
import urllib.request
import ssl

twitterUrl = "http://twitter.com/"
targetUser = "snowden"

targetUrl = twitterUrl + targetUser

# Twitter redirs to https. Need to handle this.
ssl._create_default_https_context = ssl._create_unverified_context

print("Reading {0} ...".format(targetUrl))
html = urllib.request.urlopen(targetUrl).read()

print("Saving data to file ...")
f = open("output.html", "wb")
f.write(html)
f.close()

print("Done")
