import configparser
import urllib

from PyQt5.QtCore import QThread, pyqtSignal
from Connecttion import Connection


class LoginAction(QThread):

    authentication_error = pyqtSignal()
    authentication_success = pyqtSignal()
    connection = Connection.Connections()
    loginActionSuccess = False

    def __init__(self, username, password, userTypology):
        super(QThread, self).__init__()
        self.username = username
        self.password = password
        self.userTypology = userTypology

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.fix_ip = self.configGeneral.get('IP', 'fix_ip')
        self.wireless_ip = self.configGeneral.get('IP', 'wireless_ip')

    def run(self):
        self.connection.driverCreator()
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        if ip != self.fix_ip and ip != self.wireless_ip:
            self.loginActionSuccess = self.connection.loginWebOfScience(self.username, self.password, self.userTypology)
        else:
            self.loginActionSuccess = True
        if self.loginActionSuccess is False:
            self.authentication_error.emit()
        else:
            self.authentication_success.emit()
