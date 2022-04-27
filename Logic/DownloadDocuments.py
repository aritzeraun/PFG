import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from Connecttion import scrihub
from Logic import RenameDownloadedFiles, ExtractDataFromPDF


class DownloadDocuments(QThread):

    downloaded_correctly = pyqtSignal()

    def __init__(self, dataToDownload, tableWidget, filesName, time_limit, downloadedFolder, dataExtractFolder):
        super(QThread, self).__init__()
        self.dataToDownload = dataToDownload
        self.tableWidget = tableWidget
        self.filesName = filesName
        self.limit_time = int(time_limit)
        self.downloadedFolder = downloadedFolder
        self.dataExtractFolder = dataExtractFolder
        self.sciHub_controller = ''

    def run(self):
        i = -1

        for iterator in self.dataToDownload:

            i = i + 1

            # If the document is not select nothing is done
            if self.tableWidget.item(i, 0).checkState() == 2:
                # Verifies that the document does not been downloaded previously
                documentName = iterator.__getitem__(2)
                documentName = str(documentName).replace('/', '_')
                documentName = str(documentName).replace('\\', '-')
                documentName = str(documentName) + str('.pdf')

                # Verifies that the document does not been downloaded previously
                if not documentName in self.filesName:

                    self.sciHub_controller = scrihub.main(iterator.__getitem__(2), './Downloads', self.limit_time)

                    if not 'err' in self.sciHub_controller:
                        RenameDownloadedFiles.RenameDownloadedFiles(iterator.__getitem__(2), './Downloads',
                                                                    self.downloadedFolder)

                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
                    icon = QtGui.QIcon()

                    if 'err' in self.sciHub_controller:
                        icon.addPixmap(QtGui.QPixmap("./Resources/img/incorrect_delete_icon.png"), QtGui.QIcon.Normal,
                                       QtGui.QIcon.Off)
                    else:
                        icon.addPixmap(QtGui.QPixmap("./Resources/img/correct_download_icon.png"), QtGui.QIcon.Normal,
                                       QtGui.QIcon.Off)

                    item.setIcon(icon)
                    self.tableWidget.setItem(i, 1, item)

        ExtractDataFromPDF.ExtractDataFromPDF(self.downloadedFolder, self.dataExtractFolder)

        self.downloaded_correctly.emit()
