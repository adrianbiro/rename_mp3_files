#!/usr/bin/python3

import fnmatch
import os

Path = os.getcwd()
pattern = '*.mp3'

"""Check where are .mp3 files store recursively from the current working directory."""
dirs_with_mp3 = []
for root, dirs, files in os.walk(Path):
    for filename in fnmatch.filter(files, pattern):
        #dirs_with_mp3.append(os.path.join(root, filename))
        if (root not in dirs_with_mp3):
            dirs_with_mp3.append(root)
"""Print locations out."""
for i in dirs_with_mp3:
    print(i)
