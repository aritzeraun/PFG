import time

from PyQt5.QtCore import QThread, pyqtSignal

from Rake_Analysis import rake_Analysis


class AnalyseDocuments(QThread):

    successful_Action = pyqtSignal()

    def __init__(self, dataToAnalise, downloadFilesFolder, stopPathFile, relationFilePath,
                 uniqueKeysFilePath, matrixAnalysisFile, finalDocumentPath):
        super(QThread, self).__init__()
        self.dataToAnalise = dataToAnalise
        self.downloadFilesFolder = downloadFilesFolder
        self.stopPathFile = stopPathFile
        self.relationFilePath = relationFilePath
        self.uniqueKeysFilePath = uniqueKeysFilePath
        self.matrixAnalysisFile = matrixAnalysisFile
        self.finalDocumentPath = finalDocumentPath

    def run(self):
        rake_Analysis.writeRelationCSV(self.relationFilePath, self.dataToAnalise)
        time.sleep(1)
        rake_Analysis.allAnalysis(self.relationFilePath, self.downloadFilesFolder, self.uniqueKeysFilePath,
                                  self.matrixAnalysisFile, self.finalDocumentPath, self.stopPathFile)

        self.successful_Action.emit()
