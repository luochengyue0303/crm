# -*-coding:UTF-8 -*-

from xlrd import open_workbook
from myexcel.demo import cell_value


class MyExcel():

    def __init__(self, workbook_name, sheet_name):
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name

    def __sheet(self):
        bk = open_workbook(self.workbook_name) 
        sheet = bk.sheet_by_name(self.sheet_name)
        return sheet
    #读总行数
    def total_rows(self):
        return self.__sheet().nrows
    #读总列数
    def total_columns(self):
        return self.__sheet().ncols  
        #读单元格
    def total_cell(self, row, col):
        total_value = self.__sheet().cell_value(row,col)
        return total_value
    
         #读某列值
    def col_value(self):
    
    #读某单元格
    #cell_value = sheet.cell_value(12,6) #下标从0开始
    #print(cell_value)

my = MyExcel(r'd:\emp.xls', 'empinfo')
print(my.total_rows())
print(my.total_columns())
print(my.total_cell(12,6))