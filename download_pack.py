import tkinter as Tk
from tkinter.font import families
from download_yt import down_video


window = Tk.Tk()
window.title("Youtube Video Download")
#window.geometry('452x224+500+300')
#window.resizable(1, 1)

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

def clear_entry(event):
    text_var.set('')

frame = Tk.Frame(window, borderwidth = 10)


# Creating a photoimage object to use image 
photo = Tk.PhotoImage(file="images.png") 

label = Tk.Label(
    frame,
    text="Youtube Video Download\n\nPlease paste\nThe youtube address below:",
    foreground="white",  # Set the text color to white
    background="#34A2FE",  # Set the background color to black
    #width=30
    image =photo,
    compound = Tk.LEFT,
).pack(padx=5, pady=5)


text_var  = Tk.StringVar()
text_var.set('Please copy the address here')
text = Tk.Entry(frame, textvariable=text_var, width=40)
text.pack(padx=5, pady=5)

text.bind('<Button-1>', clear_entry)

frame.pack()


frame_bottom = Tk.Frame(window, borderwidth = 10)
button = Tk.Button(
    frame_bottom,
    text="Download Video!",
    # width=25,
    # height=5,
    bg="blue",
    fg="yellow",
    command = do_action
).pack(side="left",padx=5, pady=5)

button = Tk.Button(
    frame_bottom,
    text="Quit",
    # width=10,
    # height=5,
    bg="blue",
    fg="yellow",
    command = window.quit
).pack(side="left",padx=5, pady=5)


frame_bottom.pack()

window.mainloop()
