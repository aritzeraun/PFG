from PyQt5.QtCore import QThread, pyqtSignal


class SearchAction(QThread):

    search_error = pyqtSignal()
    search_success = pyqtSignal()
    filesName = True

    def __init__(self, connection, text):
        super(QThread, self).__init__()
        self.connection = connection
        self.searchText = text

    def run(self):

        self.filesName = self.connection.dataSearch(self.searchText)

        if self.filesName is False:
            self.search_error.emit()
        else:
            self.search_success.emit()

