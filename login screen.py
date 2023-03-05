from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Login')
root.attributes("-fullscreen", True, "-topmost", True) 
root.resizable(False, False)
root.config(bg="#fff")
root.resizable(False, False)


# ---------Sign in Function-----------



def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        messagebox.showinfo("Success","Welcome")
        root.withdraw()
    elif username == "Username" and password == "Password":
        messagebox.showerror("Error", "Please Enter Username or Password")
    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "Invalid Username or Password")
    elif username == 'admin' and password != '1234':
        messagebox.showerror("Error", "Invalid Username or Password")
    elif username != 'admin' and password == '1234':
        messagebox.showerror("Error", "Invalid Username or Password")


# ---------Image Here----------


#img = PhotoImage(file='artix.png')
Label(root, bg='white').place(x=50, y=50)

# ------------Frame-------------

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=580, y=200)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# ------------User Functions------------


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


# ------Entry-----------
user = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ------------Password Functions------------


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    cname = code.get()
    if cname == '':
        code.insert(0, 'Password')


# -----------------------------------
code = Entry(frame, width=25, fg='black', border=0,
             bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# ----------------------------------
Button(frame, width=39, pady=7, text='Sign in',
       bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)


sign_up = Button(frame, width=6, text='Sign up', border=0,
                 bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)


root.mainloop()
