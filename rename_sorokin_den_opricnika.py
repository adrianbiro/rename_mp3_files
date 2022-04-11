#!/usr/bin/python3
import os

os.chdir('/home/adrian/Music/Vladimir Sorokin Den opričníka/')
for i in os.listdir():
    autor_name1, autor_name2, titul1, titul2, num = i.split()
    new_name= f'{num.zfill(2)}-{autor_name2.strip()}_{autor_name1.strip()}:{titul1.strip()}_{titul2.strip()}.mpeg'

    os.rename(i, new_name)





"""
Vladimir Sorokin Den opričníka 1
01-Sorokin_Vladimir:Den_opričníka.mpeg
"""
