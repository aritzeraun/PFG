# RECORDAR QUE AL PINCIPIO SE QUISO UTILIZAR OPENPYXL PERO ESTE NO ESA HABILITADO PARA LOS XML
import pandas as pd


def openFile(files):

    data = []

    for ROOT_DIR in files:

        group = pd.ExcelFile(ROOT_DIR)
        sheetX = group.parse(0)  # 2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

        author = sheetX['Authors']
        articleTitle = sheetX['Article Title']
        DOI = sheetX['DOI']
        sourceTitle = sheetX['Source Title']
        publicationYear = sheetX['Publication Year']
        issn = sheetX['ISSN']
        eissn = sheetX['eISSN']
        ut = sheetX['UT (Unique ID)']
        researcherID = sheetX['Researcher Ids']

        a = -1

        for title in articleTitle:
            a = a + 1
            element = [author[a], title, str(DOI[a]), sourceTitle[a], publicationYear[a], issn[a], eissn[a], ut[a],
                       researcherID[a]]
            data.append(element)

    return data
