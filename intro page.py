
from tkinter import *
from PIL import ImageTk

root=Tk()
root.geometry("1590x800+0+0")
root.title("demo")
root.config(bg="#ea5455")

def lg_in():
    root.destroy()
    import register


btn_img=ImageTk.PhotoImage(file="button_sign-u.png")
title=Label(text="Welcome to Password Manager",font=("Verdana 15underline",50,"bold"),relief="groove",bg="#ea5455",fg="white")
title.place(x=0,y=150,relwidth=1)
des=Label(text="It gives you a easy access to store, generate , and manage\n your passwords for local applications and online services.",font=("helvetica",25,"italic"),bg="#ea5455",fg='white')
des.place(x=330,y=350)
sign_up_btn=Button(image=btn_img,borderwidth=0,bd=0,command=lg_in,bg="#ea5455")
sign_up_btn.place(x=650,y=550)

root.mainloop()

