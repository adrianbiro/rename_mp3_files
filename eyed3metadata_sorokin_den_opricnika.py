#!/usr/bin/python3
import os
import eyed3
"""https://eyed3.readthedocs.io/en/latest/"""

os.chdir('/home/adrian/Music/Vladimir Sorokin Den opričníka/')
for i in os.listdir():
    file_name, file_extension = os.path.splitext(i)
    audio_file = eyed3.load(i)
#    print(audio_file.tag.title)
#    print(i)
    audio_file.tag.title = f'{file_name}'
#    print(audio_file.tag.title)
#    print("dalse")
    audio_file.tag.save()




"""
53df74699cda927ab4f99d4eee9d2bb6.mp3
09-Sorokin_Vladimir:Den_opričníka.mp3
"""
