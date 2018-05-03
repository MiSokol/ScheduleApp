import openpyxl
from shutil import copy2
import main

wb = openpyxl.load_workbook(filename = './complete_schedule.xlsx')
sheet = wb['Schedule']

currentRow = 1

def initial():
    copy2("./init_excel/complete_schedule.xlsx", "./complete_schedule.xlsx")
    pass

def addRow(task):
    sheet[str(currentRow) + 'A'] = task.name
    sheet[str(currentRow) + 'B'] = task.time
    sheet[str(currentRow) + 'C'] = task.deadline

initial()