from tkinter import*
window=Tk()
window.geometry("500x500")
window.title("tkinter library")
L1=Label(text="enter name:",fg="white",bg="black")
L1.place(x=50,y=50)
L2=Label(text="enter email:",fg="white",bg="black")
L2.place(x=50,y=80)

e1=Entry()
e2=Entry()
e1.place(x=140,y=50)
e2.place(x=140,y=80)

window.mainloop()