# -*-coding:UTF-8 -*-
from xlrd import open_workbook
from xlwt.Workbook import Workbook
bk=open_workbook(r'd:\emp.xls')
sheet = bk.sheet_by_name('empinfo')
print(sheet.nrows)

cell_value = sheet.cell_value(12,6)
print(cell_value)

row_values = sheet.row_values(6,4)
print(row_values)

col_values = sheet.row_values(5,5)
print(col_values)

row_values = sheet.row_values(6,4)
print(row_values)
row_values = sheet.row_values(7,4)
print(row_values)
row_values = sheet.row_values(8,4)
print(row_values)
row_values = sheet.row_values(9,4)
print(row_values)
row_values = sheet.row_values(10,4)
print(row_values)
row_values = sheet.row_values(11,4)
print(row_values)
row_values = sheet.row_values(12,4)
print(row_values)
row_values = sheet.row_values(13,4)
print(row_values)


wb = Workbook(UTF-8)
sheet = bw.add_sheet('测试计划书')



