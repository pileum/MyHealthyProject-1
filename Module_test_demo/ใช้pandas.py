import xlsxwriter
from pandas import *
data = {'Data' : [20, 30, 45, 12, 33, 9,[0]]}
data['locate'] = [0,1,2,3,4,5,'P\nA']
dataframe = DataFrame(data)   
writer= ExcelWriter('simple_data.xlsx', engine='xlsxwriter')
dataframe.to_excel(writer,sheet_name='หน้าที่1',index=False)
writer.save()