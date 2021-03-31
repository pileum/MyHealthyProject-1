import csv
import os
from datetime import datetime
from tkinter import messagebox
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
now = datetime.now()
now_day = now.strftime("%d/%m/%Y")
now_hours = now.strftime("%H:%M:%S")


def LessUserOrPassword(user, password, confirm):
    if len(user) < 8 or len(password) < 8 or len(confirm) < 8:
        messagebox.showerror(
            'Error', 'The user or password should be at least 8 characters.')
    elif (confirm != password) and (len(password) != 0 or len(confirm) != 0):
        messagebox.showerror('Error', 'Please enter the same password.')
    else:
        return True


def CheckLogin(user, password):
    try:
        with open("SignUp_Date.csv", mode='r', newline='', encoding='utf8') as f:
            d_login = csv.DictReader(f, fieldnames=[
                'ชื่อ', 'นามสกุล', 'ชื่อผู้ใช้', 'รหัสผ่าน', 'เวลา', 'วัน/เดือน/ปี'])
            for i in d_login:
                user = str(user).replace(' ', '')
                password = str(password).replace(' ', '')
                if user == i['ชื่อผู้ใช้'] and password == i['รหัสผ่าน']:
                    return True
            raise Exception('User or Password not in Data login')
    except:
        messagebox.showerror('Error', 'Invalid user or password')


def sn_upData(name, last_name, user, password):
    if name == '' or last_name == '':
        messagebox.showerror('Error', 'Please enter all information.')
    else:
        with open('SignUp_Date.csv', mode='a', newline='', encoding='utf8') as sign_file:
            sign_file = csv.writer(sign_file)
            sign_file.writerow(
                [name, last_name, user, password, now_hours, now_day])


def stamp_login(user, password):
    with open("recordlogin.csv", mode='a', newline='', encoding='utf8') as f:
        record_csv = csv.writer(f)
        record_csv.writerow([user, password, now_day, now_hours])


def eat_med(list_time):
    messagebox.showinfo('เตือน', 'กินยาได้แล้ว')
    list_time.delete(0)


def nofication(**var):
    time_real = datetime.now()
    print(time_real)
    var['text_time']['text'] = time_real.strftime("%H:%M:%S")
    if time_real.strftime("%H:%M") in var['sort_clock']:
        messagebox.showinfo('เตือน', 'กินยาได้แล้ว')
        var['list_time'].delete(0)
        var['sort_clock'].pop(0)
    var['root'].after(1000, lambda: noficattion(text_time=var['text_time'],
                      root=var['root'], list_time=var['list_time'], sort_clock=var['sort_clock']))
