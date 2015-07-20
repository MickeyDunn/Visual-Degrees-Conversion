import os
from random import shuffle
from glob import glob
import Tkinter
from Tkinter import *
from PIL import Image, ImageTk



root = Tk()
root.wm_title("VACS")

# Top Label

StimSelect = Label(root, text="Select Parameters", padx=5, pady=10)
StimSelect.grid(columnspan=8)

# Spatial Frequency Parameters

SpatialF = Label(root, text="Spatial Frequency", width=20)
SpatialF.grid(row=1)

FreqFrom = Label(root, text="from", width=6, justify=RIGHT, padx=5)
FreqFrom.grid(row=1, column=1)

FromSel = Spinbox(root, from_=0, to=10, width=5)
FromSel.grid(row=1, column=2)

FreqTo = Label(root, text="to", width=6, justify=RIGHT, padx=5)
FreqTo.grid(row=1, column=3)

ToSel = Spinbox(root, from_=0, to=10, width=5)
ToSel.grid(row=1, column=4)

FreqSteps = Label(root, text="in steps of", width=8, justify=RIGHT, padx=5)
FreqSteps.grid(row=1, column=5)

StepsSel = Spinbox(root, from_=0, to=300, width=5)
StepsSel.grid(row=1, column=6)

# Contrast Parameters

Cont = Label(root, text="Contrast", width=20, pady=15)
Cont.grid(row=2)

ContFrom = Label(root, text="from", width=6, justify=RIGHT, padx=5)
ContFrom.grid(row=2, column=1)

CFromSel = Spinbox(root, from_=0, to=10, width=5)
CFromSel.grid(row=2, column=2)

ContTo = Label(root, text="to", width=6, justify=RIGHT, padx=5)
ContTo.grid(row=2, column=3)

CToSel = Spinbox(root, from_=0, to=10, width=5)
CToSel.grid(row=2, column=4)

ContSteps = Label(root, text="in steps of", width=8, justify=RIGHT, padx=5)
ContSteps.grid(row=2, column=5)

CStepsSel = Spinbox(root, from_=0, to=100, width=5)
CStepsSel.grid(row=2, column=6)

# Go Button

def newwin():
    top = Toplevel()
    top.wm_title("Directory")
    Dir = Label(top, text="Stimuli Filepath", padx=5, pady=10)
    Dir.grid(row=1,column=0)
    Field = Entry(top)
    Field.grid(row=1, column=1)
    Ok = Button(top, text="OK", width=10, command=top.destroy)
    Ok.grid(row=2, columnspan=2)

Start = Button(root, text="Find Stimuli", width=15, command=newwin, pady=5)
Start.grid(row=3, columnspan=8)

# Stimuli Preview

preview = LabelFrame(root, text="Preview", height=500, width=500, padx=5, pady=5)

preview.grid(row=7, columnspan=8)

stim_filename = "image.png"

PIL_image = Image.open(stim_filename)

width = 500
height = 500

PIL_image_small = PIL_image.resize((width,height), Image.ANTIALIAS)

img = ImageTk.PhotoImage(PIL_image_small)
in_frame = Label(preview, image = img)
in_frame.pack()

files = glob(r"C:\Users\Mickey\Desktop\VisualAngle\sample images\*.png")
stim_list = []

for f in files:
    stimulus = Image.open(f)
    image_small = stimulus.resize((width,height), Image.ANTIALIAS)
    stim_list.append(image_small)


def next_image():
    shuffle(stim_list)
    print stim_list[0]
    img = ImageTk.PhotoImage(stim_list[0])
    in_frame.configure(image = img)
    in_frame.image = img
    in_frame.pack()


next_button = Button(root, text="Next", padx=15, pady=5, command=next_image)
next_button.grid(row=8, column=2)


root.mainloop()

