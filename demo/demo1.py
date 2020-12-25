# -*-coding:UTF-8 -*-

from xlwt.Formatting import Borders, Font, Alignment, Pattern, Protection
from xlwt.Style import XFStyle
from xlwt.Workbook import Workbook

wb = Workbook('utf-8')
sheet = wb.add_sheet('测试报告')
title = ['编号', '姓名', '职业', '上级', '入职日期']

title_style = XFStyle()
border = Borders()
border.left = border.THIN
border.right = border.THIN
border.top = border.THIN
border.bottom = border.THIN

font = Font()
font.bold = True
