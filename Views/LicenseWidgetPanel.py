import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream


class LicenseWidgetPanel(object):

    def __init__(self, Form):
        self.Form = Form
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.downWidget = QtWidgets.QWidget(Form)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.downWidget)
        self.copyrightLabel = QtWidgets.QLabel(self.downWidget)
        self.logoWidget = QtWidgets.QWidget(Form)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.logoWidget)
        self.logoLabel = QtWidgets.QLabel(self.logoWidget)
        self.nameLabel = QtWidgets.QLabel(self.logoWidget)
        self.licenseTextEditor = QtWidgets.QTextEdit(Form)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))

        self.setupUi(Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1234, 790)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout.setContentsMargins(25, -1, 25, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.downWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.downWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.downWidget.setObjectName("downWidget")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.copyrightLabel.setMinimumSize(QtCore.QSize(200, 20))
        self.copyrightLabel.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.copyrightLabel.setFont(font)
        self.copyrightLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.gridLayout_2.addWidget(self.copyrightLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.downWidget, 5, 0, 1, 1)
        self.logoWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.logoWidget.setObjectName("logoWidget")
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 4, 1, 1)
        self.logoLabel.setMinimumSize(QtCore.QSize(80, 80))
        self.logoLabel.setMaximumSize(QtCore.QSize(80, 80))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap('./Resources/img/app_icon.ico'))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")
        self.gridLayout_3.addWidget(self.logoLabel, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(self.fontSize)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout_3.addWidget(self.nameLabel, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.logoWidget, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.licenseTextEditor.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.licenseTextEditor.setObjectName("licenseTextEditor")
        self.gridLayout.addWidget(self.licenseTextEditor, 2, 0, 1, 1)

        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def translateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.copyrightLabel.setText(_translate("Form", "© 2022 Aritz Erauncetamurgil Barcina"))
        self.nameLabel.setText(_translate("Form", "SpyDocument \n v2022.1"))
        htmlFile = QFile('./Languages/License_' + self.configGeneral.get('SYSTEM', 'language_code') + '.html')
        htmlFile.open(QFile.ReadOnly | QFile.Text)
        self.licenseTextEditor.setHtml(QTextStream(htmlFile).readAll())
        htmlFile.close()
