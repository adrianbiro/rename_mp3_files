#!/usr/bin/python3
import os
#import mutagen
#from mutagen.mp3 import MP3
#from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3


os.chdir('/home/adrian/Music/Brabenec, Koch, Bondy, Benýšek a Moník. Poslechněte si povídky pěti osobností českého undergroundu 70. a 80. let')
for i in os.listdir():
    file_name, file_extension = os.path.splitext(i)
    #audio = mutagen.File(i)  # get info
    audio = EasyID3(i)
    #audio = ID3(i)
    #audio = MP3(i)
    print(audio.pprint())
    audio["title"] = file_name
    print(audio.pprint())
    audio.save()



