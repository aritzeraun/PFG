import os
#RECORDAR QUE AL PINCIPIO SE QUISO UTILIZAR OPENPYXL PERO ESTE NO ESA HABILITADO PARA LOS XML
import pandas as pd


class ExcelFileTreatment:

    def openFile(self, nombreArchivo):
        ROOT_DIR = os.path.abspath(os.curdir)
        ROOT_DIR = ROOT_DIR + '\Downloads\ '.replace(' ', '') + nombreArchivo
        group = pd.ExcelFile(ROOT_DIR)
        sheetX = group.parse(0)  # 2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

        articleTitle = sheetX['Article Title']
        DOI = sheetX['DOI']

        a = -1
        array = []
        for i in DOI:
            a = a + 1
            if not'nan' in str(i):
                element = [articleTitle[a], str(i)]
                array.append(element)
        # print(i.__getitem__(1))

        return array