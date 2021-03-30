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


def nofication_show(all_time, root, list_time):
    all_time.sort(reverse=True)
    a = len(all_time) - 1
    if a < 0:
        return
    else:
        print(all_time, ':', all_time[a])
        time_set = datetime.strptime(all_time[a], "%H:%M")
        now_time = datetime.strptime(
            f'{now.strftime("%H")}:{now.strftime("%M")}', '%H:%M')
        result_second_set = time_set.minute * 60 + time_set.hour * 3600
        result_second_now = now_time.minute * 60 + now_time.hour * 3600
        diff_time = (result_second_set - result_second_now) * 1000
        root.after(diff_time, lambda: eat_med(list_time))
        nofication_show(all_time[:a], root, list_time)
