#!/usr/bin/python3
import os
#import mutagen
#from mutagen.mp3 import MP3
#from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3


os.chdir('/home/adrian/Music/Vladimir Sorokin Den opričníka/')
for i in os.listdir():
    file_name, file_extension = os.path.splitext(i)
    #audio = mutagen.File(i)  # get info
    audio = EasyID3(i)
    #audio = ID3(i)
    #audio = MP3(i)
    audio["title"] = file_name
    print(audio.pprint())
    audio.save()



"""
53df74699cda927ab4f99d4eee9d2bb6.mp3
title=Sorokin_Vladimir:Den_opričníka
"""
