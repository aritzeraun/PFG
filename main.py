import configparser
import sys
from PyQt5 import QtWidgets, QtGui
from Views import WelcomeView


if __name__ == '__main__':
    configGeneral = configparser.RawConfigParser()
    configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(str(configGeneral.get('SYSTEM', 'theme_current_style')))
    app.setWindowIcon(QtGui.QIcon('./GUI/SpyDocument.png'))
    app.setApplicationVersion("v 2022.1")
    app.setApplicationDisplayName("SpyDocument")

    MainWindow = QtWidgets.QMainWindow()
    WelcomeView.WelcomeView(MainWindow, 1)
    MainWindow.show()

    sys.exit(app.exec())
