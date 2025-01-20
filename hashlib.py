from tkinter import *
import json
import hashlib
with open('database.json', 'r') as database:
    users = json.load(database)
lbl=False
def sign_in():
    global lbl3
    global lbl
    if lbl:
        lbl3.destroy()
    login = ent1.get()
    hash_login = hashlib.sha256(login.encode()).hexdigest()
    password = ent2.get()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    for user in users:
        if user['hash_login'] == hash_login:
            if user['hash_password'] == hash_password:
                lbl3 = Label(text="Вы успешно авторизованы")
            else:
                lbl3 = Label(text="Неверный пароль")
            break
    else:
        lbl3 = Label(text="Данного пользователя не существует")
    lbl3.place(x=10, y=80)
def sign_up():
    global lbl3
    global lbl
    if lbl:
        lbl3.destroy()
    login = ent1.get()
    hash_login = hashlib.sha256(login.encode()).hexdigest()
    password = ent2.get()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    new_user = {}
    new_user['hash_login'] = hash_login
    new_user['hash_password'] = hash_password
    for user in users:
        if new_user == user:
            lbl3 = Label(text="Пользователь уже существует")
            break
    else:
        users.append(new_user)
        with open('database.json', 'w') as database:
            json.dump(users, database, indent=4)
        lbl3 = Label(text="Вы успешно зарегистрированы")
    lbl3.place(x=10, y=80)
    lbl=True
root = Tk()
root.title("Вход")
root.geometry("250x200")
lbl1 = Label(root, text='Логин:')
lbl1.place(x=10, y=10)
lbl2 = Label(root, text='Пароль:')
lbl2.place(x=10, y=30)
ent1 = Entry()
ent1.place(x=60, y=10)
ent2 = Entry()
ent2.place(x=60, y=30)
bt1 = Button(root, text='Войти', command=sign_in)
bt1.place(x=10, y=50)
bt2 = Button(root, text='Зарегистрироваться', command=sign_up)
bt2.place(x=60, y=50)
root.mainloop()

