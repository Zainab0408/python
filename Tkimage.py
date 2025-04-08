from tkinter import*
from PIL import Image,ImageTk
window=Tk()
window.geometry("500x500")
img=Image.open('moon.jpg')
imge=ImageTk.PhotoImage(img)
lbl=Label(image=imge)
lbl.pack()
window.mainloop()