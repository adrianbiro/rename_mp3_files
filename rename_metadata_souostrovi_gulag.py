#!/usr/bin/python3
import os
from mutagen.easyid3 import EasyID3

os.chdir('/home/adrian/Music/Alexander Solženicyn/Alexandr Solženicyn - Souostroví Gulag/')
for i in os.listdir():
    if i.endswith(".jpg"):
        continue
    file_name, file_extension = os.path.splitext(i)
    num = "".join(file_name.split()[:1])
    num = num.replace(".", "")
    title = "_".join(file_name.split()[1:])

    new_name = f'{num}-{title}{file_extension}'

    os.rename(i, new_name)

    audio = EasyID3(i)  # edit metadata
    audio["title"] = file_name
    audio.save()

"""
052. Souostroví Gulag.mp3
243-Souostroví_Gulag.mp3
"""
