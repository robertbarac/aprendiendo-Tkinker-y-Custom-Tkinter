from tkinter import Tk, Button, messagebox

def helloCallBack():
    messagebox.showinfo("Hello Python", "Hello World")

top = Tk()

B = Button(top, text="Hello", command=helloCallBack)
B.pack()

top.mainloop()