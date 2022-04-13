#!/usr/bin/python3
import os

os.chdir('/home/adrian/Music/Cornelius Ryan Poslední bitva/')
for i in os.listdir():
    if i.endswith(".jpg"):
        continue
    file_name, file_extension = os.path.splitext(i)
    list_name = file_name.split()
    num = "".join(file_name.split()[4]).zfill(2)
    file_name = "_".join(file_name.split()[2:-1])
    new_name = f'{num}-{file_name}{file_extension}'

    os.rename(i, new_name)





"""
Cornelius Ryan Poslední bitva 3.mp3
01-Poslední_bitva.mp3
"""
