from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="gray")
root.resizable(False, False)

img = PhotoImage(file="login_bg.png")

###############---------------------------------------------------------

def signin():
    username = user.get()
    password = code.get()

    conn = sqlite3.connect("m1.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rw(name TEXT,m TEXT)''')
    
    cursor.execute("SELECT * FROM rw WHERE name=? AND m=?", (username, password))
    rows = cursor.fetchall()
    
    if len(rows) > 0:
        root.destroy()
    

    else:
        messagebox.showerror("Invalid", "Invalid Username and/or Password")

    cursor.close()
    conn.close()

def signup():
    username = user.get()
    password = code.get()

    if username and password:
        conn = sqlite3.connect("m1.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rw(name TEXT,m TEXT)''')

        cursor.execute("SELECT * FROM rw WHERE name=?", (username,))
        rows = cursor.fetchall()
        
        if len(rows) == 0:
            cursor.execute("INSERT INTO rw (name, m) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Sign-up successful!")
            
            user.delete(0, 'end')
            code.delete(0, 'end')
        else:
            messagebox.showerror("Invalid", "Username already exists. Please log in.")
        
        cursor.close()
        conn.close()
    else:
        messagebox.showerror("Invalid", "Please enter both username and password")

###############---------------------------------------------------------

# Adjust x, y coordinates and width, height of the image
image_label = Label(root, image=img, bg="white")
image_label.place(x=40, y=60, width=400, height=300)  # Adjust width and height as needed

frame = Frame(root, width=320, height=380, bg="gainsboro")
frame.place(x=544, y=60)

heading = Label(frame, text="Sign in", fg="Black", bg="white", font=("Algerian", 23, "bold"))
heading.place(x=100, y=5)

##################----------------------------------------------------------

def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username:')

user = Entry(frame, width=25, fg="black", bg="white", border=2, font=("Times new roman", 11, "bold"))
user.place(x=30, y=80)
user.insert(0, "Username:")
user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)

##################----------------------------------------------------------

def on_enter_code(e):
    code.delete(0, 'end')

def on_leave_code(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password:')

code = Entry(frame, width=25, fg="black", bg="white", border=2, font=("Times new roman", 11, "bold"), show='*')
code.place(x=30, y=150)
code.insert(0, "Password:")
code.bind('<FocusIn>', on_enter_code)
code.bind('<FocusOut>', on_leave_code)

Button(frame, width=29, pady=7, text='Log in', bg='#57a1f8', font=('Times New Roman', 10, 'bold'), fg='white', border=0, command=signin).place(x=30, y=200)

label = Label(frame, text="Don't have an account? ", fg='black', bg='white', font=('Times New Roman', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='#57a1f8', font=('Times New Roman', 8, 'bold'), cursor='hand2', fg='white', command=signup)
sign_up.place(x=215, y=270)

##################----------------------------------------------------------

root.mainloop()
