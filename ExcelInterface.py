import openpyxl
from shutil import copy2
import main

def initial():
    global wb, sheet, currentRow
    try:
        wb._archive.close()
    except:
        pass
    copy2("./init_excel/complete_schedule.xlsx", "./complete_schedule.xlsx")
    wb = openpyxl.load_workbook(filename='./complete_schedule.xlsx')
    sheet = wb['Schedule']
    currentRow = 2

def addRow(task):
    global currentRow
    sheet['A' + str(currentRow)] = task.name
    sheet['B' + str(currentRow)] = task.time
    sheet['C' + str(currentRow)] = task.deadline
    currentRow+=1
    wb.save("./complete_schedule.xlsx")


wb = openpyxl.load_workbook(filename = './complete_schedule.xlsx')
sheet = wb['Schedule']
currentRow = 2