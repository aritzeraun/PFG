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

    def run(self):
        self.connection.driverCreator()
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        if  ip != "193.146.227.236" and ip != "193.146.227.237":
            self.loginActionSuccess = self.connection.loginWebOfScience(self.username, self.password, self.userTypology)
        else:
            self.loginActionSuccess = True
        if self.loginActionSuccess is False:
            self.authentication_error.emit()
        else:
            self.authentication_success.emit()
