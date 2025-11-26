from openpyxl import Workbook

excel_workbook =Workbook()
worksheet = excel_workbook.active
worksheet.title='personal_info'

worksheet['A1']='NAME'
worksheet['B1']='PLACE'
worksheet['C1']='PHONE_NU'


data_list =[
    ['SASI','MAD','12365'],
    ['ASD','KJI','2563']

]

for row in data_list:
    worksheet.append(row)
excel_workbook.save(r'C:\Users\dhamo\PycharmProjects\selenium_training\screen s\excel.png')