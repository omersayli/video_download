# Youtube video download program
# example usage: 
# python3 video_download.py https://youtu.be/oFrizuxKXeE
# Inspired by https://towardsdatascience.com/the-easiest-way-to-download-youtube-videos-using-python-2640958318ab

from pytube import YouTube# misc
import sys, re

""" import os
import shutil
import math
import datetime# plots
import matplotlib.pyplot as plt
# %matplotlib inline# image operation
import cv2
print(sys.argv[0], sys.argv[1] ) """

print("Example usage")
print('python3 video_download.py https://youtu.be/oFrizuxKXeE')
print(f'Downloading {sys.argv[1]}')
video = YouTube( sys.argv[1] )
format_list = video.streams.filter(file_extension = "mp4")  

format_Regex = re.compile(r'"((\d)+)p"')
mo = format_Regex.search(str(format_list[0]))

format_resolutions = []
for format_ in format_list:
    mo = format_Regex.search(str(format_))
    if mo:
        format_resolutions.append(int(mo.group(1)))

index_max = format_resolutions.index(max(format_resolutions)) 
itag_ = format_list[ index_max ].itag
video.streams.get_by_itag(18).download()