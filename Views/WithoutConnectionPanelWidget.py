import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Connecttion import IntenetConnection


class WithoutConnectionPanelWidget(object):
    def __init__(self, Form, centralWidget, MainWindow):

        self.Form = Form
        self.centralWidget = centralWidget
        self.MainWindow = MainWindow
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.optionWidget = QtWidgets.QWidget(Form)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.optionWidget)
        self.first_recommendation_label = QtWidgets.QLabel(self.optionWidget)
        self.second_recommendation_label = QtWidgets.QLabel(self.optionWidget)
        self.icon_label_1 = QtWidgets.QLabel(self.optionWidget)
        self.icon_label_2 = QtWidgets.QLabel(self.optionWidget)
        self.buttonTryAgain = QtWidgets.QPushButton(Form)
        self.main_message_label = QtWidgets.QLabel(Form)
        self.label_image = QtWidgets.QLabel(Form)
        self.try_message_label = QtWidgets.QLabel(Form)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 562)
        self.gridLayout.setObjectName("gridLayout")
        self.optionWidget.setMinimumSize(QtCore.QSize(0, 60))
        self.optionWidget.setObjectName("optionWidget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.first_recommendation_label.setFont(font)
        self.first_recommendation_label.setObjectName("first_recommendation_label")
        self.gridLayout_2.addWidget(self.first_recommendation_label, 0, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.second_recommendation_label.setFont(font)
        self.second_recommendation_label.setObjectName("second_recommendation_label")
        self.gridLayout_2.addWidget(self.second_recommendation_label, 1, 1, 1, 1)
        self.icon_label_1.setMaximumSize(QtCore.QSize(20, 20))
        self.icon_label_1.setText("")
        self.icon_label_1.setPixmap(QtGui.QPixmap('./Resources/img/without_connection_check_icon.png'))
        self.icon_label_1.setObjectName("icon_label_1")
        self.gridLayout_2.addWidget(self.icon_label_1, 0, 0, 1, 1)
        self.icon_label_2.setMaximumSize(QtCore.QSize(20, 20))
        self.icon_label_2.setText("")
        self.icon_label_2.setPixmap(QtGui.QPixmap('./Resources/img/without_connection_check_icon.png'))
        self.icon_label_2.setObjectName("icon_label_2")
        self.gridLayout_2.addWidget(self.icon_label_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.optionWidget, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.buttonTryAgain.setFont(font)
        self.buttonTryAgain.setStyleSheet("QPushButton {\n"
                                          "    border: 2px solid;\n"
                                          "    border-radius: 10px;\n"
                                          "    background-color: rgb" + self.secondaryColor + ";\n"
                                          "    padding-right: 20px;\n"
                                          "    padding-left: 20px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb" + self.mainColor + ";\n"
                                          "}")
        self.buttonTryAgain.setObjectName("buttonTryAgain")
        self.gridLayout.addWidget(self.buttonTryAgain, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 2))
        self.main_message_label.setFont(font)
        self.main_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_message_label.setObjectName("main_message_label")
        self.gridLayout.addWidget(self.main_message_label, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap('./Resources/img/without_connection_label_icon.png'))
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.try_message_label.setFont(font)
        self.try_message_label.setObjectName("try_message_label")
        self.gridLayout.addWidget(self.try_message_label, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 5, 1, 1, 1)

        self.buttonTryAgain.clicked.connect(lambda: self.verifyConnection())
        self.MainWindow.dockWidget.setEnabled(False)

        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def verifyConnection(self):
        if IntenetConnection.connectionToEthernet():

            self.MainWindow.controller.goToPanel(1)
            self.MainWindow.dockWidget.setEnabled(True)

            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(str(self.config.get('WithoutConnectionPanelSection',
                                                    'messageBox_alert_successful_connection_text')))
            msgBoxLogin.exec()
        else:
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(self.config.get('WithoutConnectionPanelSection',
                                                'messageBox_alert_without_connection_text'))
            msgBoxLogin.exec()

    def translateUi(self, Form):
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.first_recommendation_label.setText(_translate("Form", self.config.get('WithoutConnectionPanelSection',
                                                                                   'first_recommendation_label_text')
                                                           .encode('ansi')))
        self.second_recommendation_label.setText(_translate("Form", self.config.get('WithoutConnectionPanelSection',
                                                                                    'second_recommendation_label_text')
                                                            .encode('ansi')))
        self.buttonTryAgain.setText(_translate("Form", self.config.get('WithoutConnectionPanelSection',
                                                                       'button_Try_Again_text').encode('ansi')))
        self.main_message_label.setText(_translate("Form", self.config.get('WithoutConnectionPanelSection',
                                                                           'main_message_label_text').encode('ansi')))
        self.try_message_label.setText(_translate("Form",  self.config.get('WithoutConnectionPanelSection',
                                                                           'try_message_label_text').encode('ansi')))
