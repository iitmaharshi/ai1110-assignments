import numpy as np
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment
read = pd.read_excel("raw_data.xlsx","Sheet1")
data = np.array(read)
values = list(data[0])
a = values.count(0)
b = values.count(1)
c = values.count(2)
d = values.count(3)
e = values.count(4)
f = values.count(5)
g = values.count(6)
h = values.count(7)
i = values.count(8)
j = values.count(9)

digits = [0,1,2,3,4,5,6,7,8,9]
frequencies = [a,b,c,d,e,f,g,h,i,j]
maximum = max(a,b,c,d,e,f,g,h,i,j)
minimum =  min(a,b,c,d,e,f,g,h,i,j)
dictionary = {a:0,b:1,c:2,d:3,e:4,f:5,g:6,h:7,i:8,j:9}
print(f'The Most occuring digit : {dictionary[maximum]}')
print(f'The least occuring digit : {dictionary[minimum]}')
write = pd.DataFrame({"Digits":digits,"Frequency\n":frequencies})
write.to_excel("frequency.xlsx",index=False)

wb=openpyxl.load_workbook("frequency.xlsx")
ws=wb['Sheet1']
ws['A12']='Total'
ws['B12']=50
ws.column_dimensions['B'].width = 15
ws.row_dimensions[1].height = 30
ws['B1'].alignment = Alignment(wrap_text=True)

wb.save("frequency.xlsx")
wb.close()