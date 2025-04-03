from tkinter import*
window=Tk()
window.geometry("500x500")
window.title("tkinter library")
for i in range (3):
    for j in range (3):
        rm=Frame(
            master=window,
            relief=RAISED,
            borderwidth=2
        )
        rm.grid(row=i,column=j,padx=3,pady=3)
        lbl=Label(master=rm, text=f"Row{i}\nColumn(j)")
        lbl.pack()
window.mainloop()