#!/usr/bin/python3
import os

os.chdir('/home/adrian/Music/Cormac McCarthy Cesta/')
for i in os.listdir():
    if i.endswith(".jpg"):
        continue
    name1 , name2, title, num = i.split()
    new_name = f'{num.zfill(2)}-{name2}:{title}.mp3'
    print(new_name)

    os.rename(i, new_name)





"""
10-McCarthy:Cesta.mp3
Cormac McCarthy cesta 1
"""
