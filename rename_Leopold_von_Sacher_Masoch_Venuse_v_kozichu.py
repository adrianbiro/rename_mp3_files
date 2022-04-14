#!/usr/bin/python3
import os

os.chdir('/home/adrian/Music/ Leopold von Sacher Masoch Venuse v kozichu/')
for i in os.listdir():
    if i.endswith(".jpg"):
        continue
    file_name, file_extension = os.path.splitext(i)
    list_name = file_name.split()
    num = list_name[-1].zfill(2)
    author = "_".join(list_name[0:4])
    title = "_".join(list_name[4:-1])
    new_name = f'{num}-{author}:{title}.mp3'
    print(new_name)

    os.rename(i, new_name)





"""
01-Leopold_von_Sacher_Masoch:Venuse_v_kozichu.mp3
Leopold von Sacher Masoch Venuse v kozichu 1
"""
