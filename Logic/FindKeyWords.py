
from PyQt5.QtCore import QThread, pyqtSignal

from Rake_Analysis import rake_Analysis


class FindKeyWords(QThread):

    successful_Action = pyqtSignal()

    def __init__(self, typology, data, downloadFilesFolder, keyListFilePath, stopPathFile, relationFilePath,
                 min_char_length, min_phrase_freq_adj, min_keyword_frequency):
        super(QThread, self).__init__()
        self.typology = typology
        self.data = data
        self.downloadFilesFolder = downloadFilesFolder
        self.keyListFilePath = keyListFilePath
        self.stopPathFile = stopPathFile
        self.relationFilePath = relationFilePath
        self.min_char_length = min_char_length
        self.min_phrase_freq_adj = min_phrase_freq_adj
        self.min_keyword_frequency = min_keyword_frequency

    def run(self):
        if self.typology == 1:
            self.data = rake_Analysis.writeListKey(self.downloadFilesFolder, self.keyListFilePath, self.stopPathFile,
                                                   self.min_char_length, self.min_phrase_freq_adj,
                                                   self.min_keyword_frequency)
        elif self.typology == 2:
            self.data = rake_Analysis.readKeysListFile(self.keyListFilePath)
        else:
            self.data = rake_Analysis.readCSVFile(self.relationFilePath)

        self.successful_Action.emit()
