import configparser

from PyQt5 import QtCore, QtGui, QtWidgets


class DialogWidget(object):

    def __init__(self, Dialog, text_1, text_2):

        self.Dialog = Dialog
        self.text_1 = text_1
        self.text_2 = text_2

        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.label = QtWidgets.QLabel(Dialog)
        self.buttonsWidget = QtWidgets.QWidget(Dialog)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.buttonsWidget)
        self.acceptButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.cancelButton = QtWidgets.QPushButton(self.buttonsWidget)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        self.recentProjectsDoc = configparser.RawConfigParser()

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.state = False

        self.setupUi(self.Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 111)
        Dialog.setMinimumSize(QtCore.QSize(500, 111))
        Dialog.setMaximumSize(QtCore.QSize(500, 111))
        self.gridLayout.setObjectName("gridLayout")
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonsWidget.setObjectName("widget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.acceptButton.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid;\n"
                                        "     border-radius: 10px;\n"
                                        "    background-color: rgb" + self.secondaryColor + ";\n"
                                        "    padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb" + self.mainColor + ";\n"
                                        "}")
        self.acceptButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.acceptButton, 0, 1, 1, 1)
        self.cancelButton.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid;\n"
                                        "     border-radius: 10px;\n"
                                        "    background-color: rgb" + self.secondaryColor + ";\n"
                                        "    padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb" + self.mainColor + ";\n"
                                        "}")
        self.cancelButton.setObjectName("CancelButton")
        self.gridLayout_2.addWidget(self.cancelButton, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.buttonsWidget, 1, 0, 1, 1)

        self.translateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.acceptButton.clicked.connect(lambda: self.setEstateOfTheQuestion(0))
        self.cancelButton.clicked.connect(lambda: self.setEstateOfTheQuestion(1))

    def setEstateOfTheQuestion(self, typeOfButton):

        if typeOfButton == 0:
            self.state = True
        elif typeOfButton == 1:
            self.state = False

        self.Dialog.close()

    def translateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", str(self.config.get('DialogWidgetSection',
                                                                       'dialog_widget_title')).encode('ansi')))
        self.label.setText(_translate("Dialog", str(self.text_1 + "\n" + self.text_2)))
        self.acceptButton.setText(_translate("Dialog", str(self.config.get('DialogWidgetSection',
                                                                           'accept_button_text')).encode('ansi')))
        self.cancelButton.setText(_translate("Dialog", str(self.config.get('DialogWidgetSection',
                                                                           'cancel_button_text')).encode('ansi')))
