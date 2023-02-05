import lyricsgenius
import json
import os
import input
import shutil

genius = lyricsgenius.Genius('hL8qehK39Y25_UG3CZF9oyteBpaW-qn9C4n2vL5xKaIW5kXXyfebOti8_bsa6pgb')

genius.remove_section_headers = True
songg = genius.search_song(input.msc, input.art)

songg.save_lyrics()

source = 'C:\\Users\\User\\Documents\\code\\vmsv\\'+'letrasong.json'
destination = 'C:\\Users\\User\\Documents\\code\\vmsv\\letras\\'+'letrasong.json'
shutil.move(source,destination)

with open('C:\\Users\\User\\Documents\\code\\vmsv\\letras\\'+'letrasong.json') as f:
    json_data = json.load(f)
    
lirica = (json_data.get("lyrics"))
slug = (json_data.get("artist"))
title = (json_data.get('title'))
imgtitle = slug +' - '+title
yttitle = slug +' - '+title+' (Slowed + Reverb)'
print (yttitle)

os.remove('C:\\Users\\User\\Documents\\code\\vmsv\\letras\\'+'letrasong.json')


