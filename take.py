from tkinter import *
from PIL import Image,ImageTk #importing libs


def face():
    window2 = Toplevel()
    window2.title("this is how you look beautiful")
    windows.geometry("600x330")
    bg =  Image.open("photo/16440777.jpg")
    img = ImageTk.PhotoImage(bg)
    bgimage = Label(window2,image = img)
    bgimage.pack()
    window2.mainloop()
#creating window
windows = Tk()
windows.geometry("500x500")
windows.title("amazing")

btn = Button(windows,text = "click to see your face",width = 20,height = 5,command = face)
btn.place(relx = 0.4,rely = 0.3)

windows.mainloop()