#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
from __future__ import unicode_literals
import youtube_dl 
import os
import sys

os.system("clear && clear && clear")
# simple logo
logo = 'PYTUBE'
# menu
menu = '''\033[0m
    {1}--Video Download
    {2}--Audio Download
    {3}--Audio PlayList Download
    {99}-Exit
 '''

print logo
print menu

# quit function
def quit():
    conn = raw_input('Continue [Y/n] -> ')
    if conn[0].upper() == 'N':
        exit()
    else:
        os.system("clear")
        print logo
        print menu
        select()

# select function
def select():
    try:
        choice = input("PyTube~# ")
        if choice == 1:
            os.system("clear")
            print """
 __     __  __        __
/  |   /  |/  |      /  |
$$ |   $$ |$$/   ____$$ |  ______    ______
$$ |   $$ |/  | /    $$ | /      \  /      \
$$  \ /$$/ $$ |/$$$$$$$ |/$$$$$$  |/$$$$$$  |
 $$  /$$/  $$ |$$ |  $$ |$$    $$ |$$ |  $$ |
  $$ $$/   $$ |$$ \__$$ |$$$$$$$$/ $$ \__$$ |
   $$$/    $$ |$$    $$ |$$       |$$    $$/
    $/     $$/  $$$$$$$/  $$$$$$$/  $$$$$$/
PUT URL EX: https://www.youtube.com/watch?v=83RUhxsfLWs
"""
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
            print("")
            quit()
        elif choice == 2:
            os.system("clear")
            print """
  /$$$$$$                  /$$ /$$
 /$$__  $$                | $$|__/
| $$  \ $$ /$$   /$$  /$$$$$$$ /$$  /$$$$$$
| $$$$$$$$| $$  | $$ /$$__  $$| $$ /$$__  $$
| $$__  $$| $$  | $$| $$  | $$| $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$
| $$  | $$|  $$$$$$/|  $$$$$$$| $$|  $$$$$$/
|__/  |__/ \______/  \_______/|__/ \______/
PUT URL EX: https://www.youtube.com/watch?v=83RUhxsfLWs
"""
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
            quit()
        elif choice == 3:
            os.system("clear")
            print("""
 /$$$$$$$  /$$                     /$$ /$$             /$$
| $$__  $$| $$                    | $$|__/            | $$
| $$  \ $$| $$  /$$$$$$  /$$   /$$| $$ /$$  /$$$$$$$ /$$$$$$
| $$$$$$$/| $$ |____  $$| $$  | $$| $$| $$ /$$_____/|_  $$_/
| $$____/ | $$  /$$$$$$$| $$  | $$| $$| $$|  $$$$$$   | $$
| $$      | $$ /$$__  $$| $$  | $$| $$| $$ \____  $$  | $$ /$$
| $$      | $$|  $$$$$$$|  $$$$$$$| $$| $$ /$$$$$$$/  |  $$$$/
|__/      |__/ \_______/ \____  $$|__/|__/|_______/    \___/
                         /$$  | $$
                        |  $$$$$$/
                         \______/
EX: https://www.youtube.com/watch?v=lp-EO5I60KA&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj
""")
            d3 = raw_input('playlist URL: ')
            os.system("clear")
            os.system("youtube-dl -cit --extract-audio --audio-format mp3 " + d3)
            print("")
            quit()
    except(KeyboardInterrupt):
        print ""


select()

            