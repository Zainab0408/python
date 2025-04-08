from tkinter import*
from tkinter import messagebox

window=Tk()
window.geometry("500x500")
def msg():
    messagebox.showinfo("are you sure to leave?")
btn=Button(text="Click me",command=msg)
btn.pack()
def msg2():
    messagebox.askyesno("do you want to save this image?")
btn=Button(text="Click me",command=msg2)
btn.pack()
def msg3():
    messagebox.showwarning("Do you want to delete this work?")
btn=Button(text="Click me",command=msg3)
btn.pack()
window.mainloop()
