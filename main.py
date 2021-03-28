from abc import ABC, abstractmethod
from tkinter import *
from ShowError import *
from datetime import datetime


def Sign_up():
    sign_page = SignUp()
    sign_page.run


def on_click(e):
    global index
    if e.widget['text'] == 'Back':
        all_page[index].pack_forget()
        index -= 1
        all_page[index].pack()
    elif e.widget['text'] == 'Sign up':
        Sign_up()


def command_on_click():
    global index
    get_user = list(LoginPage._Page1__check_user.keys())[0]
    get_password = LoginPage._Page1__check_user[get_user]
    if CheckLogin(get_user, get_password) is True:
        stamp_login(get_user, get_password)
        all_page[index].pack_forget()
        index += 1
        all_page[index].pack()


class BasePage(ABC):
    def __init__(self, window):
        self.Frame = Frame(window)

    @property
    def run(self):
        self.widget()
        return self.Frame

    @abstractmethod
    def widget(self):
        pass


class Page1(BasePage):
    def __init__(self, window):
        super().__init__(window)
        self.Frame = Frame(window, background='thistle1',
                           height=500, width=600)
        self.__user_login = dict()
        self.Label = {'Heathy Project': {'pos': (145, 57), 'size': (293, 30)},
                      'ชื่อผู้ใช้:': {'pos': (146, 111), 'size': (66, 24)},
                      'รหัสผ่าน:': {'pos': (146, 196), 'size': (94, 24)}
                      }
        self.Entry = {'ชื่อผู้ใช้': {'pos': (168, 148), 'size': (270, 25), 'var': StringVar()},
                      'รหัสผ่าน': {'pos': (168, 239), 'size': (270, 25), 'var': StringVar()}
                      }
        self.Entry_user = Entry(self.Frame, fg='red', font='consolas 14',
                                width=20, textvariable=self.Entry['ชื่อผู้ใช้']['var'])
        self.Entry_password = Entry(self.Frame, fg='red', font='consolas 14',
                                    width=20, show='*', textvariable=self.Entry['รหัสผ่าน']['var'])
        self.Login = Button(self.Frame, text='Login',
                            font='Helvetica 10', command=command_on_click)
        self.Sign_up = Button(self.Frame, text='Sign up', font='Helvetica 10')

    def widget(self):
        self.Sign_up.bind('<Button-1>', on_click)
        self.Login.place(width=101, height=45, x=150, y=297)
        self.Sign_up.place(width=101, height=45, x=337, y=297)
        for label in self.Label:
            Label(self.Frame, text=label, font='Helvetica 14', bg='thistle1').place(
                x=self.Label[label]['pos'][0],
                y=self.Label[label]['pos'][1],
                width=self.Label[label]['size'][0],
                height=self.Label[label]['size'][1])
        for text, entry in [('ชื่อผู้ใช้', self.Entry_user), ('รหัสผ่าน', self.Entry_password)]:
            entry.place(
                x=self.Entry[text]['pos'][0],
                y=self.Entry[text]['pos'][1],
                width=self.Entry[text]['size'][0],
                height=self.Entry[text]['size'][1])

    @property
    def __check_user(self):
        user_login = self.Entry['ชื่อผู้ใช้']['var'].get()
        password_login = self.Entry['รหัสผ่าน']['var'].get()
        self.__user_login[user_login] = password_login
        return {user_login: password_login}


class Page2(BasePage):
    def __init__(self, window):
        super().__init__(window)
        self.Frame = Frame(window, height=500, width=600)
        self.sub_frame = Frame(self.Frame, height=420, width=378)
        self.Label = {'ดัชนีมวลกาย': {'pos': (26, 25), 'size': (134, 37), 'font': 'Helvetica 18'},
                      'น้ำหนัก': {'pos': (27, 83), 'size': (73, 34), 'font': 'Helvetica 16'},
                      'ส่วนสูง': {'pos': (27, 168), 'size': (67, 34), 'font': 'Helvetica 16'},
                      'BMI:': {'pos': (27, 307), 'size': (63, 34), 'font': 'Helvetica 16'},
                      }
        self.Entry = {'weightvar': {'pos': (33, 126), 'size': (130, 39), 'var': StringVar()},
                      'heightvar': {'pos': (33, 211), 'size': (130, 39), 'var': StringVar()}
                      }
        self.sub_title = Label(self.sub_frame, text='การแจ้งเตือนยา', font=15)
        self.add_time = Button(
            self.sub_frame, text='เพิ่มเวลาแจ้งเตือน', font=15)
            self.sub_frame, text='เพิ่มเวลาแจ้งเตือน', font=15, command=self.func_add_time)
        self.list_time = Listbox(self.sub_frame, height=10, width=40, font=15)
        self.bmi_result = Label(self.Frame, bg='white', font='20')
        self.submit_btn = Button(self.Frame, text='SUBMIT', font='18')
        self.back_btn = Button(self.Frame, text='Back', font='18')

    def widget(self):
        for label in self.Label:
            Label(self.Frame, text=label, font=self.Label[label]['font']).place(
                x=self.Label[label]['pos'][0],
                y=self.Label[label]['pos'][1],
                width=self.Label[label]['size'][0],
                height=self.Label[label]['size'][1])
        for entry in self.Entry:
            Entry(self.Frame, textvariable=self.Entry[entry]['var'], fg='red', font='Helvetica 20', width=20).place(
                x=self.Entry[entry]['pos'][0],
                y=self.Entry[entry]['pos'][1],
                width=self.Entry[entry]['size'][0],
                height=self.Entry[entry]['size'][1])
        self.bmi_result.place(width=130, height=39, x=33, y=348)
        self.submit_btn.place(x=33, y=258, width=102, height=40)
        self.submit_btn.bind('<Button-1>', self.bmi)
        self.back_btn.place(x=33, y=400, width=91, height=40)
        self.back_btn.bind('<Button-1>', on_click)
        self.widget_subframe()

    def bmi(self, *args):
        weight = float(self.Entry['weightvar']['var'].get()) if float(
            self.Entry['weightvar']['var'].get()) % 100 != 0 else int(self.Entry['weightvar']['var'].get())
        height = float(self.Entry['heightvar']['var'].get()) if float(
            self.Entry['heightvar']['var'].get()) % 100 != 0 else int(self.Entry['heightvar']['var'].get())
        self.bmi_result['text'] = format(weight/((height/100)**2), '.2f')

    def widget_subframe(self):
        self.sub_title.grid(row=0, columnspan=2)
        self.sub_frame.place(x=189, y=20)
        self.list_time.grid(row=1, columnspan=2)
        self.add_time.grid(row=2, column=0, sticky='w')
    # def func_add_time(self):
        

    def func_add_time(self):
        pop_time = Toplevel(height=356, width=536)
        sub_label = {'การแจ้งเตือนยา': {'pos': (175, 9), 'size': (171, 31), 'font': 18},
                     'โรคประจำตัว': {'pos': (24, 58), 'size': (110, 34), 'font': 16},
                     'เวลาทานยา': {'pos': (319, 58), 'size': (118, 29), 'font': 16},
                     'ชื่อยา': {'pos': (25, 138), 'size': (61, 29), 'font': 16},
                     'ปริมาณยาที่ทาน': {'pos': (24, 230), 'size': (159, 29), 'font': 16},
                     'mg': {'pos': (192, 268), 'size': (53, 29), 'font': 16}}
        sub_entry = {'โรค': {'pos': (30, 90), 'size': (205, 35), 'var': StringVar()},
                     'ชื่อยา': {'pos': (29, 170), 'size': (285, 35), 'var': StringVar()},
                     'ปริมานยา': {'pos': (30, 262), 'size': (156, 35), 'var': IntVar()}
                     }
        sub_submit_btn = Button(pop_time, text='SUBMIT',
                                command=lambda: pop_time.destroy())
        sub_submit_btn.place(x=324, y=252, width=171, height=45)
        for label in sub_label:
            Label(pop_time, text=label, font='Helvetica {}'.format(sub_label[label]['font'])).place(
                x=sub_label[label]['pos'][0],
                y=sub_label[label]['pos'][1],
                width=sub_label[label]['size'][0],
                height=sub_label[label]['size'][1])
        for entry in sub_entry:
            Entry(pop_time, textvariable=sub_entry[entry]['var'], fg='red', font='Helvetica 14', width=20).place(
                x=sub_entry[entry]['pos'][0],
                y=sub_entry[entry]['pos'][1],
                width=sub_entry[entry]['size'][0],
                height=sub_entry[entry]['size'][1])


class SignUp(BasePage):
    def __init__(self):
        self.Frame = Toplevel(background='thistle1', height=500, width=600)
        self.Label = {
            'สร้างบัญชี': {'pos': (241, 75), 'font': 'Helvetica 18', 'size': (103, 29)},
            'ชื่อ': {'pos': (124, 117), 'size': (32, 25), 'font': 'Helvetica 15'},
            'นามสกุล': {'pos': (309, 117), 'size': (72, 25), 'font': 'Helvetica 15'},
            'ชื่อผู้ใช้': {'pos': (124, 192), 'size': (62, 25), 'font': 'Helvetica 15'},
            'รหัสผ่าน': {'pos': (124, 265), 'size': (73, 25), 'font': 'Helvetica 15'},
            'ยืนยันรหัสผ่าน': {'pos': (309, 265), 'size': (119, 25), 'font': 'Helvetica 15'}
        }
        self.Entry = {
            'Name': {'pos': (129, 144), 'size': (147, 30), 'var': StringVar()},
            'Last Name': {'pos': (314, 144), 'size': (147, 30), 'var': StringVar()},
            'User Name': {'pos': (129, 220), 'size': (230, 30), 'var': StringVar()},
            'Password': {'pos': (129, 293), 'size': (147, 30), 'var': StringVar()},
            'Confirm': {'pos': (314, 293), 'size': (147, 30), 'var': StringVar()}
        }
        self.Accept = Button(self.Frame, text='Accept',
                             font='15', command=self.Backup)
        self.Back = Button(self.Frame, text='Back', font='15',
                           command=lambda: self.Frame.destroy())

    def widget(self):
        self.Accept.place(x=129, y=336, width=103, height=35)
        self.Back.place(x=358, y=336, width=103, height=35)
        for label in self.Label:
            Label(self.Frame, text=label, font=self.Label[label]['font'], bg='thistle1').place(
                x=self.Label[label]['pos'][0],
                y=self.Label[label]['pos'][1],
                width=self.Label[label]['size'][0],
                height=self.Label[label]['size'][1])
        for entry in self.Entry:
            Entry(self.Frame, textvariable=self.Entry[entry]['var'], fg='red',
                  font='13').place(
                x=self.Entry[entry]['pos'][0],
                y=self.Entry[entry]['pos'][1],
                width=self.Entry[entry]['size'][0],
                height=self.Entry[entry]['size'][1])

    def Backup(self):
        user = self.Entry['User Name']['var'].get()
        password = self.Entry['Password']['var'].get()
        confirm = self.Entry['Confirm']['var'].get()
        name = self.Entry['Name']['var'].get()
        last_name = self.Entry['Last Name']['var'].get()
        LessUserOrPassword(user, password, confirm)
        sn_upData(name, last_name, user, password)
        self.Frame.destroy()


root = Tk()
root.title(f'เม่าแบก {datetime.today().strftime("%d/%m/%y")}')
root.minsize(600, 500)
root.maxsize(600, 500)
LoginPage = Page1(root)
PutInfoPage = Page2(root)
index = 0
all_page = [LoginPage.run, PutInfoPage.run]
all_page[index].pack()
root.mainloop()
