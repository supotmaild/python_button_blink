'''Button Blink        ▌▓▐'''
'''======================='''
'''Thailand Proud'''
'''          version 1.0.0'''
'''The World first list'''
'''   of Tkinter button'''
'''that can call function'''
'''with many of parameters'''
'''======================='''
''' Copyright (c) Jul 2015'''
''' Supot Sawangpiriyakij'''
''' all right reserve'''
import sys
if sys.version_info[0] < 3:
	import Tkinter as tk
	from Tkinter import BOTH,ALL
else:
	import tkinter as tk
	from tkinter import BOTH,ALL
from PIL import Image,ImageDraw,ImageFont
import ImageTk
global tk,win,canvas,BOTH,ALL
global Button,button_number,blink,button_blink,Label
global motion,motion_pass,bind,stop_number
global parameters
'''These all Buttons are in the list'''
Button=[]
parameters=[['Button 0','Cat'],\
			['Button 1','Dog'],\
			['Button 2','Hippo'],\
			['Button 3','Giraffe']]

def redraw():
	global stop_number
	canvas.delete(ALL)
	canvas.create_text(100,100,text=str(stop_number),font='Arial 76')	
	canvas.create_text(100,150,text=parameters[stop_number][1],font='Arial 16')	

def motion(event):
	global Label,stop_number
	Label.place_forget()
	Label=tk.Label(canvas,text='Button#'+str(button_number)+' :x '+str(event.x)+', y '+str(event.y))
	Label.place(x=400,y=260)
	stop_number=button_number

def motion_pass(event):
	pass

def button_blink():
	global canvas,blink,Button,button_number,bind
	bind.bind('<Motion>',motion_pass)
	button_number=button_number+1
	if button_number==len(Button):
		button_number=0
	Button[button_number].bind('<Motion>',motion)
	bind=Button[button_number]
	blink=win.after(10,button_blink)

def on_closing():
    global win,blink
    win.after_cancel(blink)    
    win.destroy()

win=tk.Tk()
frame1 = tk.Frame(
	master = win,
	width = 600,
	height = 300,
	bg = '#808000'
)
button_number=0
stop_number=0
frame1.pack(fill='both', expand='yes')
canvas = tk.Canvas(frame1, width=600, height=300)
canvas.place(in_=frame1,x=0,y=0,width=600,height=300)
Label=tk.Label(canvas,text='Button#  :x , y')
Label.place(x=400,y=260)
for i in range(4):
	Button.append(tk.Button(canvas,width=4, height=1, text=str(i), command=redraw))
	Button[i].place(x=20+(i*100), y=260)
canvas.bind('<Motion>',motion)
bind=canvas
redraw()
blink=win.after(10,button_blink)
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()
