# -*-coding:UTF-8 -*-
from xlrd import open_workbook
from pymysql import Connect


bk = open_workbook(r'd:\测试计划参与学员表.xls')
sheet = bk.sheet_by_name('学生信息') 

empinfo = []
for i in range(5, 8):
    empinfo.append(sheet.row_values(i, 4))
    
conn = Connect(host='192.168.1.4', user='root', password="root", database='cms', port=3306)
cursor = conn.cursor()

for i in range(len(empinfo)):
    cursor.execute("insert into _cai_student_cai(s_id, s_name, s_birth, s_sex) values (%d,'%s','%s','%s')" % (int(empinfo[i][0]), empinfo[i][1], empinfo[i][2], empinfo[i][3]))
    conn.commit()
    
cursor.close()
conn.close()
