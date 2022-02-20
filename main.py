import sys
from PyQt5 import QtWidgets
from Views import LoginView


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    MainWindow = QtWidgets.QMainWindow()
    GUI = LoginView.Ui_MainWindow()
    GUI.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec())
