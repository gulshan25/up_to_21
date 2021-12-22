
'''Digital clock
Author: Shuvo Kumar Shill
'''
from tkinter import *
from tkinter import font
from datetime import datetime


def finish(*args):
    global window
    window.destroy()

def clock_time():
    time = datetime.now()
    time = time.strftime('%H:%M:%S')
    txt.set(time)
    window.after(1000,clock_time)

window = Tk()
window.title('My Digital Clock')
window.geometry('850x200')
window.configure(background='black')
# keyboard commad bind
window.bind('<Escape>',finish)


window.after(1000,clock_time)
fnt=font.Font(family='helvetica',size=120,weight='bold')
txt=StringVar()
lbl=Label(window,textvariable=txt,font=fnt,foreground='yellow',background='black')
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
window.mainloop()