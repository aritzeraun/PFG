import configparser
import urllib

from PyQt5.QtCore import QThread, pyqtSignal
from Connecttion import WebOfScience


class SearchAction(QThread):

    search_error = pyqtSignal()
    search_success = pyqtSignal()
    filesName = True

    def __init__(self, connection, text, search_err):
        super(QThread, self).__init__()
        self.connection = connection
        self.searchText = text
        self.searchError = search_err

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.fix_ip = self.configGeneral.get('IP', 'fix_ip')
        self.wireless_ip = self.configGeneral.get('IP', 'wireless_ip')

    def run(self):

        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

        if ip == self.fix_ip or ip in self.wireless_ip:
            self.connection = WebOfScience.Connections()
            self.connection.driverCreator()

        self.filesName = self.connection.dataSearch(self.searchText, self.searchError)

        if self.filesName is False:
            self.search_error.emit()
        else:
            self.search_success.emit()

