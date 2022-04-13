#!/usr/bin/python3
import os

os.chdir('/home/adrian/Music/Brabenec, Koch, Bondy, Benýšek a Moník. Poslechněte si povídky pěti osobností českého undergroundu 70. a 80. let/')
for i in os.listdir():
    if i.endswith(".jpg"):
        continue
    title = i.replace(" ", "_")
    new_name = f'{title}.mp3'
    print(new_name)

    os.rename(i, new_name)




