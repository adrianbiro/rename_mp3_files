#!/usr/bin/python3
import os

os.chdir('/home/adrian/Music/Alexander Jakovlev Rusko plné krížov/')
for i in os.listdir():
    file_name, file_extension = os.path.splitext(i)
    num = file_name.split()[6]
    num = num[3:-1].zfill(2)
    autor_name = f"{file_name.split()[1]}_{file_name.split()[0]}"
    title = f"{file_name.split()[3]}_{file_name.split()[4]}_{file_name.split()[5]}"
    cap = ""
    for j in file_name.split()[7:]:
        if j != file_name.split()[-1]:
            cap += f'{j}_'
        else:
            cap += j
    new_name = f'{num}-{autor_name}:{title}:{cap}{file_extension}'
  
    os.rename(i, new_name)





"""
Alexander Jakovlev – Rusko plné křížů (č.1) Spoluviníci
04-Jakovlev_Alexander:Rusko_plné_křížů:Církev.mp3
07-Jakovlev_Alexander:Rusko_plné_křížů:Od_Kronštadtu_k_Novočerkassku.mp3
"""
