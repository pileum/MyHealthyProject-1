import csv  
user = input()
password = input()
with open("SignUp_Date.csv",mode='r',newline='',encoding='utf8') as f: 
    d_login = csv.DictReader(f) 
    for i in list(d_login):
        if user == i['ชื่อผู้ใช้'] and password  == i['รหัสผ่าน']:
            print(True)
            