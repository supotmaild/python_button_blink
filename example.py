'''example.py'''
from b_blink import blink
import sys
if sys.version_info[0] < 3:
	import Tkinter as tk
	from Tkinter import BOTH,ALL
else:
	import tkinter as tk
	from tkinter import BOTH,ALL
global tk,win,canvas,BOTH,ALL
global blink,b,parameters
parameters=[['Button 0','Cat'],\
			['Button 1','Dog'],\
			['Button 2','Hippo'],\
			['Button 3','Giraffe']]

def redraw():
	canvas.delete(ALL)
	txt=str(b.bnumber())
	ptxt=parameters[b.bnumber()][1]
	canvas.create_text(100,100, text=txt, font='Arial 76')	
	canvas.create_text(100,150, text=ptxt, font='Arial 16')	

win=tk.Tk()
frame1 = tk.Frame(
	master = win,
	width = 600,
	height = 300,
	bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
canvas = tk.Canvas(frame1, width=600, height=300)
canvas.place(in_=frame1,x=0,y=0, width=600, height=300)
Button=[]
for i in range(4):
	Button.append(tk.Button(frame1, width=4, height=1, text=str(i), command=redraw))
	Button[i].place(x=20+(i*100), y=260)
b=blink()
b.start(win,Button)
redraw()
win.mainloop()
