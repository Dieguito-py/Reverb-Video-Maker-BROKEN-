from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment 
import search
import shutil
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
      'outtmpl': search.ba[1]+'.%(ext)s',

}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([search.arq])

input_file = search.ba[1]+".mp3"
output_file = search.ba[1]+".wav"
sound = AudioSegment.from_mp3(input_file) 
sound.export(output_file, format="wav") 

source = r'C:\\Users\\User\\Documents\\code\\vmsv\\'+search.ba[1]+".wav"
destination = r'C:\\Users\\User\\Documents\\code\\vmsv\\dow&cov\\'+search.ba[1]+"new.wav"
shutil.move(source,destination)
os.remove('C:\\Users\\User\\Documents\\code\\vmsv\\'+search.ba[1]+'.MP3')