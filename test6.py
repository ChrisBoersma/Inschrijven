from tkinter import *
 
root = Tk()
root.title('Python Tk Examples @ pythonspot.com')

var = StringVar()

def printName(event):
	var = textbox.get()
	print(var)

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)

textbox = Entry(root, textvariable=var)
textbox.focus_set()
textbox.pack(pady=10, padx=10)
button_1.pack(pady=10, padx=10, side=BOTTOM)

root.mainloop()
