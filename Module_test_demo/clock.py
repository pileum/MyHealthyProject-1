
from tkinter import * 
from datetime import datetime 
from tkinter import ttk 
from tkinter import messagebox
def loop_time():
    print(list_time)
    time_real = datetime.now()
    if time_real.strftime("%H:%M") in list_time:
        messagebox.showinfo('test','จับเวลา')
        list_time.remove(time_real.strftime("%H:%M"))
    time_now['text'] = time_real.strftime("%H:%M:%S")
    root.after(1000,loop_time)
root= Tk() 
root.geometry('500x300')
time_now = Label(root,font='consolas 25')
time_now.grid(row=0,columnspan=2) 
hour = ttk.Combobox(root,values=[f'0{i}'if i<10  else i for i in range(0,24) ],font='consolas 10 ',state='readonly')
minute = ttk.Combobox(root,values=[f'0{i}' if i<10 else i for i in range(0,60)],font='consolas 10 ',state='readonly') 
Button(root,text='mark',font='consolas 10 ',command= lambda : list_time.append(f"{hour.get()}:{minute.get()}")).grid(row=2,columnspan=2)
hour.grid(row=1,column=0)
minute.grid(row=1,column=1)
list_time = [] 
root.after(1000,loop_time)
root.mainloop()