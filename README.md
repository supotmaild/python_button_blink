# python_button_blink 24 Jul 2015

- button_blink.py
- The first list of Python Button that can call function with parameters without any macro
- THAILAND ▌▓▐ Proud button_blink.py 1.0 (We are the first to do, Thanks Python)
- Button list in Python can't call function with parameters even though lambda:
- Example 
- Button[i]=Tkinter.Button(frame, width=4, height=1, text=str(i), command=lambda:callback(i))
- We can not use callback(i) in this sentence , We can use only callback(1)
- from this example, We can not loop for to create button in Tk.
- If you want 4 button, you need to do these
- Button[0]=Tkinter.Button(frame, width=4, height=1, text=str(0), command=lambda:callback(0))
- Button[1]=Tkinter.Button(frame, width=4, height=1, text=str(1), command=lambda:callback(1))
- Button[2]=Tkinter.Button(frame, width=4, height=1, text=str(2), command=lambda:callback(2))
- Button[3]=Tkinter.Button(frame, width=4, height=1, text=str(3), command=lambda:callback(3))
- with Python_Button_Blink
- you can do this
- Button.append(Tkinter.Button(frame,width=4, height=1, text=str(i), command=callback))
- and callback can use stop_number global variable to check all of parameters
- text=parameters[stop_number][1]	

- New version 1.2.0  b_blink.py
- 
- separate module to import
- example.py use import b_blink

- How to use
- 
- from b_blink import blink
- Button=[]
- for i in range(4):
-    	Button.append(tk.Button(frame1, width=4, height=1, text=str(i), command=redraw))
-   	Button[i].place(x=20+(i*100), y=260)
- b = blink()
- b.start(win,Button)            # win is your Tk root
- # Button is your list of Button # redraw fuction check b.bnumber() for return press button value 
