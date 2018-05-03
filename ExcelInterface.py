import openpyxl
from shutil import copyfile


wb = openpyxl.load_workbook(filename = './complete_schedule.xlsx')
sheet = wb['Schedule']

def initial():
    copyfile("./init_excel/complete_schedule.xlsx", "./")
    pass

initial()