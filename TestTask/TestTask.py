import requests
import datetime
from xml.dom import minidom
#import pandas as pd
import xlsxwriter
import smtplib

#Импорт собственных модулей
import sendler
import num_to_str

#Получаем текущую дату
date = datetime.date.today()
year = date.year
month = date.month
day = date.day

try:            #Отправляем запрос на сайт moex.com по паре USD/RUB
    response = requests.get(f"""https://moex.com/export/derivatives/currency-rate.aspx?
                        language=en&currency=USD_RUB&moment_start={year}-{month}-01&moment_end={year}-{month}-{day}""")
    sts_code = response.status_code
    response.encoding = 'utf-8'
except:
    print("Не удалось соединиться с сайтом")

try:            #Отправляем запрос на сайт moex.com по паре EUR/RUB
    response_eur = requests.get(f"""https://moex.com/export/derivatives/currency-rate.aspx?
                        language=en&currency=EUR_RUB&moment_start={year}-{month}-01&moment_end={year}-{month}-{day}""")
    sts_code_eur = response_eur.status_code
    response_eur.encoding = 'utf-8'
except:
    print("Не удалось соединиться с сайтом")

f = open('usd_rub.xml', 'w')        #Создаем файл usd_rub.xml и записываем туда полученный ответ с сайта в формате xml

if sts_code == 200:
    f.write(response.text)

f.close()

f_eur = open('eur_rub.xml', 'w')    #Создаем файл eur_rub.xml и записываем туда полученный ответ с сайта в формате xml

if sts_code_eur == 200:
    f_eur.write(response_eur.text)
f_eur.close()

mydoc = minidom.parse('usd_rub.xml')        #Работа с долларом вытаскиваем необходимые элементы с xml файла
items = mydoc.getElementsByTagName('rate')
values = []
moments = []
changes = []
for i in range(1,len(items)+1):
    values.append(items[i-1].attributes['value'].value)
    moments.append(items[i-1].attributes['moment'].value)
    if i == 1:
        changes.append(0)
    else:
        changes.append(float(values[i-1])-float(values[i-2]))

mydoc_eur = minidom.parse('eur_rub.xml')        #Работа с евро вытаскиваем необходимые элементы с xml файла
items_eur = mydoc_eur.getElementsByTagName('rate')
values_eur = []
moments_eur = []
changes_eur = []
for i in range(1,len(items_eur)+1):
    values_eur.append(items_eur[i-1].attributes['value'].value)
    moments_eur.append(items_eur[i-1].attributes['moment'].value)
    if i == 1:
        changes_eur.append(0)
    else:
        changes_eur.append(float(values_eur[i-1])-float(values_eur[i-2]))

eur_usd = []
print(len(values_eur))
for i in range(1, len(values_eur)+1):
    eur_usd.append(float(values_eur[i-1])/float(values[i-1]))

workbook = xlsxwriter.Workbook('usd_rub.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold':1})
money_format_usd = workbook.add_format({'num_format': '$#,##0.00'})
money_format_eur = workbook.add_format({'num_format': '€#,##0.00'})

len_A1 = [len('Дата доллара')]      #Расчет максимальной длины ячейки A1 для ширины ячейки
for i in range(1,len(moments)+1):
    len_A1.append(len(str(moments[i-1])))

max_len_A1 = max(len_A1)

len_B1 = [len('Курс доллара')]      #Расчет максимальной длины ячейки B1 для ширины ячейки
for i in range(1,len(values)+1):
    len_B1.append(len(str(values[i-1])))

max_len_B1 = max(len_B1)

len_C1 = [len('Изменение доллара')]     #Расчет максимальной длины ячейки C1 для ширины ячейки
for i in range(1,len(changes)+1):
    len_C1.append(len(str(changes[i-1])))

max_len_C1 = max(len_C1)

len_D1 = [len('Дата евро')]     #Расчет максимальной длины ячейки D1 для ширины ячейки
for i in range(1,len(moments_eur)+1):
    len_D1.append(len(str(moments_eur[i-1])))

max_len_D1 = max(len_D1)

len_E1 = [len('Курс евро')]     #Расчет максимальной длины ячейки E1 для ширины ячейки
for i in range(1,len(values_eur)+1):
    len_E1.append(len(str(values_eur[i-1])))

max_len_E1 = max(len_E1)

len_F1 = [len('Изменение евро')]        #Расчет максимальной длины ячейки F1 для ширины ячейки
for i in range(1,len(changes_eur)+1):
    len_F1.append(len(str(changes_eur[i-1])))

max_len_F1 = max(len_F1)

len_G1 = [len('EUR/USD')]       #Расчет максимальной длины ячейки G1 для ширины ячейки
for i in range(1,len(eur_usd)+1):
    len_G1.append(len(str(eur_usd[i-1])))

max_len_G1 = max(len_G1)

worksheet.set_column(0,0,int(max_len_A1))   #Установка ширины колонны
worksheet.set_column(0,1,int(max_len_B1))
worksheet.set_column(0,2,int(max_len_C1))
worksheet.set_column(0,3,int(max_len_D1))
worksheet.set_column(0,4,int(max_len_E1))
worksheet.set_column(0,5,int(max_len_F1))
worksheet.set_column(0,6,int(max_len_G1))

worksheet.write('A1','Дата доллара',bold)       #Запись данных в строки excel
worksheet.write('B1','Курс доллара',bold)
worksheet.write('C1','Изменение доллара',bold)
worksheet.write('D1','Дата евро',bold)                
worksheet.write('E1','Курс евро',bold)
worksheet.write('F1','Изменение евро',bold)
worksheet.write('G1','EUR/USD',bold)

row = 1
col = 0
for i in moments:
    worksheet.write_string(row, col, str(i))
    row+=1
row = 1
col = 1
for i in values:
    worksheet.write_number(row, col, float(i), money_format_usd)
    row+=1
row = 1
col = 2
for i in changes:
    worksheet.write_number(row, col, i)
    row+=1
row = 1
col = 3
for i in moments_eur:
    worksheet.write_string(row, col, str(i))
    row+=1
row = 1
col = 4
for i in values_eur:
    worksheet.write_number(row, col, float(i), money_format_eur)
    row+=1
row = 1
col = 5
for i in changes_eur:
    worksheet.write_number(row, col, i)
    row+=1
row = 1
col = 6
for i in eur_usd:
    worksheet.write_number(row, col, i)
    row+=1

workbook.close()

len_excel = len(items)+1

#Формируем сообщение для отправки на почту
len_num = num_to_str.int_to_word(len_excel)
msg = f'В excel файле {len_num.to_word()} строки'

addr_to   = "zagreev.marat@gmail.com"
files = ['usd_rub.xlsx'] 
sendler.send_email(addr_to, "Тема сообщения", msg, files)
