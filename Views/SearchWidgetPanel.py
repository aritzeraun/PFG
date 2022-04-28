import configparser
import errno
import os
import threading
import time

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox

from Logic import SearchAction


class SearchWidgetPanel(object):

    def __init__(self, Form, connection, central, MainWindow):

        self.Form = Form
        self.MainWindow = MainWindow
        self.centralWidget = central
        self.ProjectDirectory = self.MainWindow.projectDirectory
        self.connection = connection

        self.gridLayoutTwo = QtWidgets.QGridLayout(Form)
        self.widget = QtWidgets.QWidget(Form)
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.searchLineEdit = QtWidgets.QLineEdit(self.widget)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.processLabel = QtWidgets.QLabel(self.widget)

        self.movie = QMovie("./Resources/img/process_running_gif.gif")
        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.searchDocumentListFolder = self.ProjectDirectory + '/'
        self.searchDocumentListFolder = self.searchDocumentListFolder + self.configGeneral.get('LOCATIONS',
                                                                                 'document_list_folder_name') + '/'

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.thread = None
        self.searchError = False

        self.setupUi(Form)

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1317, 868)
        self.gridLayoutTwo.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutTwo.setObjectName("gridLayoutTwo")
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.searchLineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.searchLineEdit.setStyleSheet("QLineEdit {\n"
                                          "    border: 2px solid rgb" + self.secondaryColor + ";\n"
                                          "    border-radius: 10px;\n"
                                          "    padding-left: 10px;\n"
                                          "    padding-right: 10px;\n"
                                          "}\n"
                                          "QLineEdit:hover {\n"
                                          "    border: 2px solid rgb" + self.mainColor + ";\n"
                                          "}")
        self.searchLineEdit.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.searchLineEdit.setFont(font)
        self.gridLayout.addWidget(self.searchLineEdit, 1, 1, 1, 1)
        self.searchButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.searchButton.setStyleSheet("QPushButton {\n"
                                        "border: 2px solid;\n"
                                        " border-radius: 10px;\n"
                                        "background-color: rgb" + self.secondaryColor + ";\n"
                                        "padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb" + self. mainColor + ";\n"
                                        "}")
        self.searchButton.setObjectName("searchButton")
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.searchButton.setFont(font)
        self.gridLayout.addWidget(self.searchButton, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.processLabel.setText("")
        self.processLabel.setObjectName("processLabel")
        self.gridLayout.addWidget(self.processLabel, 2, 1, 1, 1)
        self.gridLayoutTwo.addWidget(self.widget, 0, 0, 1, 1)
        self.processLabel.setMinimumHeight(100)
        self.searchButton.clicked.connect(lambda: self.search_data())
        self.searchLineEdit.returnPressed.connect(lambda: self.search_data())

        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.movie.start()

    def thread_search_correctly(self):
        try:
            os.mkdir(self.searchDocumentListFolder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        fileNames = []

        for (dir_path, dir_names, filenames) in os.walk('./Downloads/'):
            fileNames.extend(filenames)
            break

        for file in fileNames:
            oldDirectory = './Downloads/' + file
            newDirectory = self.searchDocumentListFolder + file
            os.replace(oldDirectory, newDirectory)

        time.sleep(1)
        self.MainWindow.dockWidget.setEnabled(True)
        self.MainWindow.controller.goToPanel(2)

    def thread_search_error(self):
        self.processLabel.clear()
        self.searchLineEdit.setEnabled(True)
        self.searchButton.setEnabled(True)
        self.searchError = True
        msgBoxLogin = QMessageBox()
        msgBoxLogin.setText(str(self.config.get('SearchViewSection', 'error_alert_text')))
        msgBoxLogin.exec()

    def loadViewThread(self):
        # change login view
        self.processLabel.clear()
        self.processLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.processLabel.setMovie(self.movie)
        self.searchLineEdit.setEnabled(False)
        self.searchButton.setEnabled(False)
        time.sleep(0.5)
        self.MainWindow.dockWidget.setEnabled(False)

    def search_data(self):
        loadView = threading.Thread(name="loadViewThread", target=self.loadViewThread)
        self.thread = SearchAction.SearchAction(self.connection, self.searchLineEdit.text(), self.searchError)
        self.thread.search_success.connect(lambda: self.thread_search_correctly())
        self.thread.search_error.connect(lambda: self.thread_search_error())

        loadView.start()
        self.thread.start()

    def translateUi(self, Form):
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchLineEdit.setPlaceholderText(_translate("Form", self.config.get('SearchViewSection',
                                                                                  'search_topic_placeholder_text')))
        self.searchButton.setText(_translate("Form", self.config.get('SearchViewSection', 'search_button_text')))
