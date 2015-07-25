'''Button Exec'''
'''======================='''
'''          version 1.0.0'''
'''exec list of Tk buttons'''
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
global tk,win,canvas,BOTH,ALL
global Button,redraw
global parameters
'''These all Buttons are in the list'''
Button=[]
parameters=[['Button 0','Cat'],\
			['Button 1','Dog'],\
			['Button 2','Hippo'],\
			['Button 3','Giraffe']]

def redraw(num):
	global stop_number
	canvas.delete(ALL)
	canvas.create_text(100,100,text=str(num),font='Arial 76')	
	canvas.create_text(100,150,text=parameters[num][1],font='Arial 16')	

win=tk.Tk()
frame1 = tk.Frame(
	master = win,
	width = 600,
	height = 300,
	bg = '#808000'
)
Button=[]
frame1.pack(fill='both', expand='yes')
canvas = tk.Canvas(frame1, width=600, height=300)
canvas.place(in_=frame1,x=0,y=0,width=600,height=300)
for i in range(4):
	Button.append('')
	exec('Button[i]=tk.Button(canvas,width=4, height=1, text=str(i), command=lambda:redraw('+str(i)+'))')
	Button[i].place(x=20+(i*100), y=260)
redraw(0)
win.mainloop()
