"""
VERSION 0.3 APRIL 2018
"""

import urllib2
import json

url = 'https://player.vimeo.com/video/266084213/config'

response = urllib2.urlopen(url)
webContent = response.read()
webContent = json.loads(webContent)

available_videos=webContent.get("request").get("files").get("progressive")

print "Available videos are:"
i = 1
for video in available_videos:
    print "[" + str(i) + "] " + str(video.get("width")) + "x" + str(video.get("height")) + " - " + str(video.get("quality")) + " " + str(video.get("fps")) + "fps (" + video.get("mime") + ")"
    i+=1
print "Choose the option to download: "
pass