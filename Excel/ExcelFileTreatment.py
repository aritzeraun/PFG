import os
#RECORDAR QUE AL PINCIPIO SE QUISO UTILIZAR OPENPYXL PERO ESTE NO ESA HABILITADO PARA LOS XML
import pandas as pd
import xlrd
from lxml import etree as et
import openpyxl as load_workbook
from openpyxl.chart import BarChart, Reference


class ExcelFileTreatment:

    def openFile(self, nombreArchivo):
        ROOT_DIR = os.path.abspath(os.curdir)
        ROOT_DIR = ROOT_DIR + '\Downloads\ '.replace(' ', '') + nombreArchivo
        group = pd.ExcelFile(ROOT_DIR)
        sheetX = group.parse(0)  # 2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

        var1 = sheetX['Article Title']

        print(var1[999])

