from tkinter import *
import random
import time
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image

#globale variable
fc=0
tc=0
s=0
ec=1
c=1
initial=time.time()
sec=10
inte=1
float_part=0
#---------------------------

#menu command
def one():
    global sec
    global initial
    initial=time.time()
    sec=1
def two():
    global sec
    global initial
    initial=time.time()
    sec=2
def three():
    global sec
    global initial
    initial=time.time()
    sec=3
def four():
    global sec
    global initial
    initial=time.time()
    sec=4
def five():
    global sec
    global initial
    initial=time.time()
    sec=5
def about():
    showinfo("About","This is Simple Typing Software Default Time=10 Second.")
def Dev():
    state=mb.askyesno("Developer","This Software is made by Henish,You want to get G-Mail?")
    if state:
        showinfo("Developer","My G-Mail is...\nhenish125@gmail.com")
def floattext():
    global inte
    global s
    global float_part
    inte=0
    temp=str(s)+"."+str(float_part)
    Label(root, text = temp,font = "arial 30 bold",bg=cctocn(c),fg="white").place(x=350,y=200,width=300,height=100)
def inttext():
    global inte
    global s
    Label(root, text = s,font = "arial 30 bold",bg=cctocn(c),fg="white").place(x=350,y=200,width=300,height=100)
    inte=1
#----------------------------------

#colour code to colour name
def cctocn(code):
    if code==0:
        return "blue"
    elif code==1:
        return "red"
#----------------------------

#print true count and flase count
def printf():
    global tc
    global fc
    Label(root, text = f"TRUE   = {tc}",font = "arial 30 bold").place(x=350,y=350)
    Label(root, text = f"FALSE = {fc}",font = "arial 30 bold").place(x=350,y=400)
#--------------------------------------------------------------------------------------

#sense true or flase
def tf():
    global s
    global tc
    global fc
    global ec
    global c
    global inte
    global float_part
    if inte==1:
        try:
            if s==int(textentry.get()) and ec==c:
                tc=tc+1
            else:
                fc=fc+1
        except:
            fc=fc+1
    else:
        try:
            temp=str(s)+"."+str(float_part)
            if temp==textentry.get() and ec==c:
                tc=tc+1
            else:
                fc=fc+1
        except:
            fc=fc+1
    printf()
#----------------------------------------

#next
def next():
    tf()
    global s
    global c
    global inte
    global float_part
    s=random.randint(0, 1000)
    c=random.randint(0, 1)
    if inte==0:
        float_part=random.randint(0, 100)
        temp=str(s)+"."+str(float_part)
        Label(root, text = temp,font = "arial 30 bold",bg=cctocn(c),fg="white").place(x=350,y=200,width=300,height=100)
    else:
        Label(root, text = s,font = "arial 30 bold",bg=cctocn(c),fg="white").place(x=350,y=200,width=300,height=100)
    textentry.set("")
#----------------------------

#event
def randomval(event):
    global initial
    initial=time.time()
    next()
def close():
    state=mb.askyesno("Quit","Do You Want To Close This?")
    if state:
        root.destroy()
def keypress(event):
    global ec
    if event.char=="+":
        ec=0
        Entry(root, textvariable = textentry, font = "arial 30 bold",bg="blue",fg="white",justify=CENTER).place(x=350,y=30,width = 300,height = 100)
        textentry.set("")
    elif event.char=="-":
        ec=1
        Entry(root, textvariable = textentry, font = "arial 30 bold",bg="red",fg="white",justify=CENTER).place(x=350,y=30,width = 300,height = 100)
        textentry.set("")
#---------------------------

#update
def update():
    global initial
    global sec
    current=time.time()
    if current>=initial+sec:
        initial=time.time()
        next()
    root.after(500,update)
#--------------------------------

#main loop
root = Tk()
root.title("Typing Test")
try:
    img = ImageTk.PhotoImage(Image.open("logo.ico"))
    root.iconphoto(False, img)
except:
    pass
root.geometry("1000x500")
root.maxsize(1000, 500)
root.minsize(1000, 500)
root.bind('<Return>', randomval)
root.protocol("WM_DELETE_WINDOW", close)
root.bind("<Key>", keypress)
Label(root, text = s,font = "arial 30 bold",bg="red",fg="white").place(x=350,y=200,width=300,height=100)
textentry = StringVar()
Entry(root, textvariable = textentry, font = "arial 30 bold",bg="red",fg="white",justify=CENTER).place(x=350,y=30,width = 300,height = 100)
Label(root, text = "TRUE   = 0",font = "arial 30 bold").place(x=350,y=350)
Label(root, text = "FALSE = 0",font = "arial 30 bold").place(x=350,y=400)
Label(root,text="By:- Henish B. Soliya",font = "arial 20 bold").place(x=700,y=460)
menubar=Menu(root)
timee = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ="Time", menu = timee)
timee.add_command(label="1 second",command=one)
timee.add_separator()
timee.add_command(label="2 second",command=two)
timee.add_separator()
timee.add_command(label="3 second",command=three)
timee.add_separator()
timee.add_command(label="4 second",command=four)
timee.add_separator()
timee.add_command(label="5 second",command=five)
option=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Option",menu=option)
option.add_command(label="Float",command=floattext)
option.add_command(label="Integer",command=inttext)
henish=Menu(menubar,tearoff=0)
menubar.add_cascade(label="About",menu=henish)
henish.add_command(label="About",command=about)
henish.add_command(label="Developer",command=Dev)
root.config(menu=menubar)
update()
root.mainloop()
#----------------------------------------------------------------------------------------------------------------