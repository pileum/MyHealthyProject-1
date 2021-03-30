from tkinter import *
import xlsxwriter



def write_Excel():
    writesheet.write(row.get(), text.get()) 
    print(readfile.ncols)
    writefile.close()


writefile = xlsxwriter.Workbook('Write by tkinter.xlsx')
writesheet = writefile.add_worksheet() 
readsheet = readfile.sheet_by_index(0)
root = Tk()
text = StringVar()
row = StringVar()
Label(root, text='Enter your Text').grid(row=0, columnspan=2)
write = Entry(root, textvariable=text, width=20, font=16)
write.grid(row=1, columnspan=2)
Label(root, text='Enter your row').grid(row=2, column=0)
put_row = Entry(root, textvariable=row)
put_row.grid(row=2, column=1)
sub_btn = Button(root, text='Submit', font=16, command=write_Excel)
sub_btn.grid(row=3, columnspan=2)
root.mainloop()
