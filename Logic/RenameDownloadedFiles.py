import os
from os import walk


def RenameDownloadedFiles(DOI, DirectoryToSearch, FinalDirectory):

    oldDirectory = ''

    for (dir_path, dir_names, filenames) in walk(DirectoryToSearch):
        oldDirectory = DirectoryToSearch + '/' + filenames[0]

    DOI = str(DOI).replace('/', '_')
    DOI = str(DOI).replace('\\', '-')
    DOI = str(DOI) + str('.pdf')
    newDirectory = FinalDirectory + '/' + DOI
    os.replace(oldDirectory, newDirectory)
