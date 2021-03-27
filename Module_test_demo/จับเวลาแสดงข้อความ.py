from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


def show_time():
    time_set = f'{hour.get()}:{minutes.get()}'
    distime['text'] = time_set
    today = datetime.now()
    now = '{}:{}'.format(today.strftime('%H'), today.strftime('%M'))
    today_second = datetime.strptime(now, '%H:%M')
    totals_today_seconds = today_second.minute * 60 + today_second.hour * 3600
    set_time_second = datetime.strptime(time_set, '%H:%M')
    totals_set_time_seconds = set_time_second.minute * 60 + set_time_second.hour * 3600
    wave_time = (totals_set_time_seconds - totals_today_seconds) * 1000
    root.after(wave_time, lambda: messagebox.showinfo('เตือน', message.get()))


root = Tk()
message = StringVar()
Label(root, text='ตั้งเวลาแสดงข้อความ', font=15).grid(row=0, columnspan=3)
Label(root, text='ใส่ข้อความ', font=15).grid(row=1, columnspan=2)
Entry(root, width=20, textvariable=message, font=15).grid(row=2, columnspan=3)
Label(root, text='เวลา', font=15).grid(row=3, column=0)
hour = ttk.Combobox(root, values=list(range(1, 25)),
                    state='readonly', font=15, width=4)
hour.grid(row=3, column=1)
minutes = ttk.Combobox(root, values=list(range(1, 61)),
                       state='readonly', font=15, width=4)
minutes.grid(row=3, column=2)
Button(root, text='Submit', font=15,
       command=show_time).grid(row=4, columnspan=3)
distime = Label(root, font=15)
distime.grid(row=5, columnspan=3)
root.mainloop()
