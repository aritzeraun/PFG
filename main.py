import sys
import urllib.request

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from Connecttion import Connection


class main(QMainWindow):

    username = ""
    password = ""
    connection = Connection.Connections()
    userTipology = 0

    def __init__(self):
        super().__init__()
        uic.loadUi("./GUI/front.ui", self)
        self.AccessButton.clicked.connect(self.login_Action)

        self.progressBar.setVisible(False)
        self.passwordField.returnPressed.connect(self.login_Action)

    def login_Action(self):
        self.username = self.usernameField.text()
        self.password = self.passwordField.text()
        self.progressBar.setVisible(True)
        self.requestSenderThread()

    def requestSenderThread(self):

        if self.username_domain() is True:
            self.connection = Connection.Connections()
            self.connection.driverCreator()

            if not urllib.request.urlopen('https://ident.me').read().decode('utf8') == "193.146.227.236":
                self.connection.loginWebOfScience(self.username, self.password, self.userTipology)

            # uic.loadUi("./GUI/buscador.ui", self)
            self.connection.dataSearch("web scraping")
        else:
            self.messageLabel.setText("El dominio de de correo introducido no es valido para la Universidad de Deusto."
                                      + " Por favor, introduzca un correo válido para dicha organización o pongase en"
                                      + " contacto con el administrador para solicitar un nombre de usuario válido. "
                                      + "Los  dominios acceptados son @deusto.es y @opendeusto.es")

    def username_domain(self):

        self.username.replace(" ", "")

        if "@opendeusto.es" in self.username:
            self.username = self.username.replace("@opendeusto.es", "")
            self.userTipology = 1
            return True
        if "@deusto.es" in self.username:
            self.username = self.username.replace("@deusto.es", "")
            self.userTipology = 2
            return True
        else:
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    GUI = main()
    GUI.show()
    sys.exit(app.exec())
