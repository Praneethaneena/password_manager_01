from tkinter import *
from tkinter import messagebox
import mysql.connector


root=Tk()
root.geometry("1590x800+0+0")
root.title("demo")
root.config(bg="#ea5455")
img_reg=PhoyoImage(file="images/button_sign_up.png")
frame1=Frame(bg="white",bd=0)
frame1.place(x=550,y=30,width=500,height=740)

lbl_sign_up=Label(text="SIGN UP",font("times new roman",30,"bold"),bg="white",fg="black")
lbl_sign_up.place(x=690,y=70)
username=Label(text="enter your email",font=("helvetica",15),bg="white")
username.place(x=600,y=200)
user_mail=Entry(text="hell",font=("helvetica",15),bg="white",relief="ridge",borderwidth=1)
user_mail.place(x=600,y=260,width=300)
user_mail.focus()
paswd=Label(text="New Password",font=("helvetica",15),bg="white")
paswd.place(x=600,y=330)
new_pswd=Entry(font=("helvetica",15),show="*",relief="ridge",borderwidth=1)
new_pswd.place(x=600,y=380,width=300)
cfrm_paswd=Label(text="confirm password",font=("helvetica",15),bh="white")
cfrm_paswd.place(x=600,y=440,height=35)
cnfrm_pswd=Entry(font=("helvetica",15),show="*",relief="ridge",borderwidth=1)
cnfrm_pswd.place(x=600,y=490,width=300)



def regs():
    if new_pswd.get()=="" or cnfrm_pswd.get()=="" or user_mail.get()=="" :
        messagebox.showerror("Error","All Fields are required")
    elif new_pswd.get()!=cnfrm_pswd.get():
        messagebox.showerror("Error","Password and confirm password doen't match")
    else:
        try:
            db=mysql.connector.connect(host='localhost',user='root',passwd='root',database="password_manager")
            cur=db.cursor()
            cur.execute("Insert into useraccounts(mail_id,password)values(%s, %s)",(user_mail.get(),new_pswd.get()))
            db.commit()
            db.close()
            root.destroy()
            import log_in
        except EXCEPTION as e:
            messagebox.showerror("Error",f "Error Due to {e}")

    frame1=Frame(bg="white",bd=0)
    frame1.place(x=550,y=30,width=500,height=740)

    btn_login=PhotoImage(file="images/button_log-in.png")
    title=Label(text="Login In",bg="white",font=("Californian FB",35,"bold"))
    title.place(x=710,y=80)

    label=Label(text="username",compound=LEFT,font=("helvetica",18),bg="white")
    label.place(x=600,y=200)

    email_txt=Entry(text="hell",font=("helvetica",18),bg="white",relief="sunken",bd=1)
    email_txt.place(x=600,y=260,width=300)
    email_txt.focus()

    pass_lbl=Label(text="Password",font=("helvetica",18),bg="white")
    pass_lbl.place(x=600,y=320)
    paswd_txt=Entry(font=("helvetica",15),show="*",relief="sunken",bd=1)
    paswd_txt.place(x=600,y=380,width=300)
    sign_in=Button(image=btn_login,bd=0,bg="white",command=login)
    sign_in.place(x=610,y=500)

    root.mainloop()

    
             
