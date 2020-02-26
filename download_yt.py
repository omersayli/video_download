# Youtube video download


from pytube import YouTube# misc
import sys, re


def select_media(format_list, video):
    import tkinter as Tk
    window = Tk.Tk()
    Lb1 = Tk.Listbox(window)
    Lb1.config(width=150, height=len(format_list)+2)
    for item in format_list:
        Lb1.insert(Tk.END, item)
    Lb1.pack(padx=2, pady=2)

    def select_button():
        selected = Lb1.curselection()
        #print(selected)
        #print(format_list[ selected[0] ])
        #print(index_max)
        global index_max
        index_max = selected[0]
        itag_ = format_list[ index_max ].itag
        try:
            video.streams.get_by_itag(itag_).download()
        finally:
            window.quit()
            window.destroy()

    doStuffBtn = Tk.Button(window, text='Select type', command=select_button)
    doStuffBtn.pack()
    window.mainloop()


def down_video( file_address ):
    video = YouTube(file_address )
    format_list = video.streams.filter(file_extension = "mp4")  
    index_max = 0
    select_media(format_list, video)

    # index_max = format_resolutions.index(max(format_resolutions)) 
"""     itag_ = format_list[ index_max ].itag
    video.streams.get_by_itag(itag_).download()
     """