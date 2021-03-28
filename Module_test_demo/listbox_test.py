from tkinter import *
from tkinter import ttk
from datetime import datetime


def enter_text():
    myList.delete(int(cb_index.get())-1)
    myList.insert(int(cb_index.get())-1, insert_text.get())


root = Tk()
root.geometry('400x300')
insert_text = StringVar()
in_en = Entry(root, textvariable=insert_text, width=30)
in_en.grid(row=0, column=2, sticky='n')
cb_index = ttk.Combobox(root, values=list(range(1, 26)))
cb_index.grid(row=1, column=2, sticky='n')
insert_btn = Button(root, text='insert')
insert_btn.grid(row=2, column=2)
myList = Listbox(root, width=20, height=10)
myList.grid(row=0, column=0)
scrollbar = Scrollbar(root, command=myList.yview)
myList['yscrollcommand'] = scrollbar.set
for i in range(1, 26):
    myList.insert(END, f'Line :  {i}  | {i}') 
    myList.insert(END,'')
scrollbar.grid(row=0, column=1, sticky='ns')
btn = Button(root, text='click', command=lambda: print(
    myList.get(myList.curselection()[0]))) 
insert_btn['command'] = enter_text
btn.grid(row=1, columnspan=2)
root.mainloop()
