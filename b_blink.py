#    b_blink.py
#    Button Blink for import
#    =======================
#    Version 1.2.0 Supot Sawangpiriyakij
#    Copyright Jul 2015
#    Redistribution and use in source and binary forms, with or without
#    modification, are permitted provided that the following conditions are met:
#        * Redistributions of source code must retain the above copyright
#          notice, this list of conditions and the following disclaimer.
#        * Redistributions in binary form must reproduce the above copyright
#          notice, this list of conditions and the following disclaimer in the
#          documentation and/or other materials provided with the distribution.
#        * Neither the name of the organization nor the names of its contributors 
#          may be used to endorse or promote products derived from this software 
#          without specific prior written permission.
#
#    See <http://www.opensource.org/licenses/bsd-license>

class blink:
	global blink_win,blink_Button,stop_number,button_number,bind,blink

	def start(self,b_win,b_Button):
		global blink_win,blink_Button,stop_number,button_number,bind,blink

		def _blink():
			global blink_win,blink,blink_Button,button_number,bind

			def motion(event):
				global stop_number
				stop_number=button_number

			def motion_pass(event):
				pass

			try:
				bind.bind('<Motion>',motion_pass)
			except: pass
			button_number=button_number+1
			if button_number==len(blink_Button):
				button_number=0
			blink_Button[button_number].bind('<Motion>',motion)
			bind=blink_Button[button_number]
			blink=blink_win.after(10,_blink)

		def on_closing():
			global blink
			blink_win.after_cancel(blink)    
			blink_win.destroy()

		blink_win=b_win
		blink_Button=b_Button
		blink=blink_win.after(100,_blink)
		blink_win.protocol("WM_DELETE_WINDOW", on_closing)


	def bnumber(self):
		return stop_number

	button_number=0
	stop_number=0
