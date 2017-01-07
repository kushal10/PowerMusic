import os
import requests
import urllib2
import sys
import codecs
query = sys.argv[2]
name = query.replace("+","")
os.system('youtube-dl -o "'+name+'.mp3" --extract-audio --prefer-ffmpeg --audio-format mp3 ytsearch:'+query+'')
if(len(sys.argv) == 3):
  if(sys.argv[1] == "play"):
    os.system("mplayer "+name+".mp3")
