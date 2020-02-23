# Youtube video download


from pytube import YouTube# misc
import sys, re

def down_video( file_address ):
    video = YouTube(file_address )
    format_list = video.streams.filter(file_extension = "mp4")  

    format_Regex = re.compile(r'"((\d)+)p"')
    mo = format_Regex.search(str(format_list[0]))

    format_resolutions = []
    for format_ in format_list:
        mo = format_Regex.search(str(format_))
        if mo:
            format_resolutions.append(int(mo.group(1)))
        else:
            format_resolutions.append(0)


    index_max = format_resolutions.index(max(format_resolutions)) 
    itag_ = format_list[ index_max ].itag
    video.streams.get_by_itag(itag_).download()