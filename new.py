from tkinter import*
root=Tk()
root.title('denomination counter')
root.configure(bg='lavender')
root.geometry('650x400')

label=Label(text="enter total amount")
entry=Entry()
lbl=Label(text="here are number of notes for each denomination")

l1= Label(text="2000", bg='Light grey')
l2= Label(text="500", bg='Light grey')
l3= Label(text="100", bg='Light grey')

t1=Entry()
t2=Entry()
t3=Entry()

def calculator():
    try:
        global amount
        amount=int(entry.get())
        note2000 = amount // 2000
        amount %=2000
        note500 = amount // 500
        amount %=500
        note100 = amount // 100
        amount %=100

        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)

        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    except ValueError:
        print("error","please enter a valid number")

btn=Button(text='Calculate', command=calculator, bg='beige', fg='black')

label.place(x=230,y=50)
entry.place(x=200,y=80)
btn.place(x=240,y=120)
lbl.place(x=140,y=170)

l1.place(x=180,y=200)
l2.place(x=180,y=230)
l3.place(x=180,y=260)

t1.place(x=270,y=200)
t2.place(x=270,y=230)
t3.place(x=270,y=260)



root.mainloop()
