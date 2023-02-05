from youtubesearchpython import VideosSearch
import input
import re

videosSearch = VideosSearch(input.musica, limit = 1)
result = videosSearch.result()
link = result["result"][0]["link"]
title = result["result"][0]["title"]
time = result["result"][0]["duration"]
arq = link 
ba = re.split("[=]",arq)
a = title+'-'+ba[1]

print ( )
print (a)
print ( )
print (title)
print (link)
print (time)