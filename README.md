# python_button_blink 24 Jul 2015

- The first list of Python Button that can call function with parameters without any macro
- Button list in Python can't call function with parameters even though lambda:
- Example Button[i]=Tkinter.Button(frame, width=4, height=1, text=str(i), command=lambda:callback(i))
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
