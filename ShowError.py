from tkinter import messagebox
from datetime import datetime
import csv

now = datetime.today()
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
            c = 0
            for i in d_login:
                if user == i['ชื่อผู้ใช้'] and password == i['รหัสผ่าน']:
                    c += 1
                    return True
            if c == 0:
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
