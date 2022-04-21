import subprocess
from os import walk


def ExtractDataFromPDF(DirectoryToSearch, FinalDirectory):

    allFiles = []

    for (dir_path, dir_names, filenames) in walk(DirectoryToSearch):
        allFiles.extend(filenames)

    for fileName in allFiles:
        fileDirectory = DirectoryToSearch + '/' + fileName
        documentToSave = FinalDirectory + '/' + str(fileName).replace('.pdf', '.txt')
        subprocess.call(['java', '-jar', './PDF_Extraction/PDF_Data_Extraction.jar', fileDirectory, documentToSave])
