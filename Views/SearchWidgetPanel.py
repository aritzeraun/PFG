import configparser
import errno
import os
import time

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from Logic import SearchAction
from Views import ResultWidgetPanel


class SearchWidgetPanel(object):

    def __init__(self, Form, connection, central, MainWindow):
        self.Form = Form
        self.MainWindow = MainWindow
        self.centralWidget = central
        self.projectDirectory = self.MainWindow.projectDirectory
        self.connection = connection
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfigEN.cfg')
        self.setupUi(Form)

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(943, 868)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "border: 2px solid;\n"
                                    " border-radius: 10px;\n"
                                    "    background-color: rgb(165, 134, 83);\n"
                                    "padding-right: 20px;\n"
                                    "    padding-left: 20px;\n"
                                    "}\n"
                                    "QComboBox:hover {\n"
                                    "background-color: rgb(95, 71, 10);\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid rgb(0, 0, 200);\n"
                                    "    border-radius: 10px;\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "    padding-left: 10px;\n"
                                    "    padding-right: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    border: 2px solid rgb(0, 0, 0);\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "border: 2px solid;\n"
                                        " border-radius: 10px;\n"
                                        "    background-color: rgb(165, 134, 83);\n"
                                        "padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(95, 71, 10);\n"
                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../descarga.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.pushButton.clicked.connect(lambda: self.search_data())
        self.lineEdit.returnPressed.connect(lambda: self.search_data())

        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def thread_search_correctly(self):
        DataListFolder = self.projectDirectory + '/' + 'Search_List'
        try:
            os.mkdir(DataListFolder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        for file in self.thread.filesName:
            oldDirectory = './Downloads/' + file
            newDirectory = self.projectDirectory + '/' + 'Search_List' + '/' + file
            os.replace(oldDirectory, newDirectory)

        time.sleep(2)

        resultView = QtWidgets.QWidget(self.centralWidget)
        controller = ResultWidgetPanel.ResultWidgetPanel(resultView, self.centralWidget, self.MainWindow,
                                                         self.projectDirectory)
        resultView.show()
        self.MainWindow.gridLayout.addWidget(controller.Form)
        self.Form.close()

    def thread_search_error(self):
        msgBoxLogin = QMessageBox()
        #meter configuracion
        msgBoxLogin.setText('messageBox_alert_loginError_text')
        msgBoxLogin.exec()

    def search_data(self):

        self.thread = SearchAction.SearchAction(self.connection, self.lineEdit.text())
        self.thread.search_success.connect(self.thread_search_correctly)
        self.thread.search_error.connect(self.thread_search_error)

        self.thread.start()

    def translateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", self.config.get('SearchViewSection',
                                                                            'search_topic_placeholder_text')))
        self.comboBox.setItemText(0, _translate("Form", self.config.get('SearchViewSection',
                                                                        'search_option_way_0')))
        self.comboBox.setItemText(1, _translate("Form", self.config.get('SearchViewSection',
                                                                        'search_option_way_1')))
        self.comboBox.setItemText(2, _translate("Form", self.config.get('SearchViewSection',
                                                                        'search_option_way_2')))
        self.pushButton.setText(_translate("Form", self.config.get('SearchViewSection',
                                                                   'searchButton_text')))
