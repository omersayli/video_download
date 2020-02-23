import tkinter as Tk
from tkinter.font import families
from  download_yt import down_video
from tkinter import messagebox
# Let's create the Tkinter window
window = Tk.Tk()
window.title("Youtube Video Download")
# Then, you will define the size of the window in width(312) and height(324) using the 'geometry' method
window.geometry('312x224+500+300')

def do_action():
    youtube_address = text_var.get()
    try:
        #messagebox.showinfo('Do''Downloading video..')
        text_var.set('Downloading..')
        down_video( youtube_address )
        text_var.set('Downloaded')
    except: # Exception as e:
        #text_var.set(str(e))
        text_var.set('Error in download')

    

label = Tk.Label(
    text="Youtube Video Download\n\nPlease paste\nThe youtube address below:",
    foreground="white",  # Set the text color to white
    background="#34A2FE",  # Set the background color to black
    width=30
).pack(pady=10)

text_var  = Tk.StringVar()
text = Tk.Entry(textvariable=text_var, width=30).pack(pady=10)

button = Tk.Button(
    text="Download Video!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command = do_action
).pack(pady=10)

button = Tk.Button(
    text="Quit",
    width=10,
    height=5,
    bg="blue",
    fg="yellow",
    command = window.quit
).pack()

window.mainloop()
