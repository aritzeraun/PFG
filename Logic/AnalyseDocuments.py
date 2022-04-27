import time

from PyQt5.QtCore import QThread, pyqtSignal

from Rake_Analysis import rake_Analysis


class AnalyseDocuments(QThread):

    successful_Action = pyqtSignal()

    def __init__(self, dataToAnalise, downloadFilesFolder, stopPathFile, relationFilePath,
                 uniqueKeysFilePath, matrixAnalysisFile, finalDocumentPath, min_char_length, min_phrase_freq_adj,
                 min_keyword_frequency):
        super(QThread, self).__init__()
        self.dataToAnalise = dataToAnalise
        self.downloadFilesFolder = downloadFilesFolder
        self.stopPathFile = stopPathFile
        self.relationFilePath = relationFilePath
        self.uniqueKeysFilePath = uniqueKeysFilePath
        self.matrixAnalysisFile = matrixAnalysisFile
        self.finalDocumentPath = finalDocumentPath
        self.min_char_length = min_char_length
        self.min_phrase_freq_adj = min_phrase_freq_adj
        self.min_keyword_frequency = min_keyword_frequency

    def run(self):
        rake_Analysis.writeRelationCSV(self.relationFilePath, self.dataToAnalise)
        time.sleep(1)
        rake_Analysis.allAnalysis(self.relationFilePath, self.downloadFilesFolder, self.uniqueKeysFilePath,
                                  self.stopPathFile,  self.min_char_length, self.min_phrase_freq_adj,
                                  self.min_keyword_frequency)

        self.successful_Action.emit()
