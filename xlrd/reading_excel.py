# import xlrd
# path =r'C:\Users\dhamo\PycharmProjects\selenium_training\files\selenium example.xlsx'
# workbook = xlrd.open_workbook(path)
# print(workbook)
#
# worksheet=workbook.sheet_by_name('Sheet1')
# print(worksheet)
#
# rows=worksheet.get_rows()
# print(rows)
# #
# # for ele in rows:
# #     print(ele)
#
# for ele in rows:
#     print(ele[0],ele[1],ele[2])
###########################

import xlrd
# path =r'C:\Users\dhamo\PycharmProjects\selenium_training\files\selenium example.xlsx'
# workbook = xlrd.open_workbook(path)
# print(workbook)
#
# worksheet=workbook.sheet_by_name('Sheet1')
# print(worksheet)
#
# rows=worksheet.get_rows()
# print(rows)
# #
# # for ele in rows:
# #     print(ele)
#
# for ele in rows:
#     print(ele[0],ele[1],ele[2])
import xlrd
path= r'/files/username password.xlsx'

def excel_read():
    workbook=xlrd.open_workbook(path)
    worksheet=workbook.sheet_by_name('reg_data')
    rows = worksheet.get_rows()

    header = next(rows)
    reg = {}
    for ele in rows:
     reg[ele[0].value] = ele[1].value

    return reg




