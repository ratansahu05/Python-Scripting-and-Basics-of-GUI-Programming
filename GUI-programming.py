import tkinter

#tkinter test
#tkinter._test()

from tkinter import Tk
from tkinter import ttk
from tkinter import *

root = Tk()
root.title("Basic GUI program")

'''
ttk.Button(root, text = "Hello Friend").grid()
root.mainloop()
'''
'''
frame = Frame(root)
labelText = StringVar()

label = Label(frame, textvariable = labelText)
button = Button(frame, text = "Hey, I'm button, click me")

labelText.set("Hey! How you doin' ?")

label.pack()
button.pack()
frame.pack()
root.mainloop()
'''

'''
frame = Frame(root)
Label(frame, text = "hey!").pack()
Button(frame, text = "B1").pack(side = LEFT, fill = Y)
Button(frame, text = "B2").pack(side = RIGHT, fill = X)
Button(frame, text = "B3").pack(side = LEFT, fill = Y)
Button(frame, text = "B4").pack(side = RIGHT, fill = X)

frame.pack()
root.mainloop()
'''

Label(root, text = "Name").grid(row=0,column=0, sticky = N)
Entry(root, width=50).grid(row=0,column=1)

Button(root, text= "Submit").grid(row=0,column=5)

Label(root, text="Profile: ").grid(row=1,column=0, sticky = N)
Radiobutton(root, text = "SDE", value = 1).grid(row=1,column=1, sticky = N)
Radiobutton(root, text = "Web Dev", value = 2).grid(row=1,column=2, sticky = N)
Radiobutton(root, text = "ML", value = 3).grid(row=1,column=3, sticky = N)
Radiobutton(root, text = "Data Science", value = 4).grid(row=1,column=4, sticky = N)
Radiobutton(root, text = "Big Data", value = 5).grid(row=1,column=5, sticky = N)

Label(root, text="Courses: ").grid(row=2,column=0, sticky = N)
Checkbutton(root, text = "PYTHON").grid(row=3,column=1, sticky = N)
Checkbutton(root, text = "C++").grid(row=3,column=2, sticky = N)
Checkbutton(root, text = "C").grid(row=3,column=3, sticky = N)
Checkbutton(root, text = "SQL").grid(row=3,column=4, sticky = N)

root.mainloop()



