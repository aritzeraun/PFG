from PyQt5 import QtCore, QtGui, QtWidgets


class NewProjectDialog(object):
    def __init__(self,  Dialog):
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.directoryAccessButton = QtWidgets.QPushButton(Dialog)
        self.locationInput = QtWidgets.QLineEdit(Dialog)
        self.widget = QtWidgets.QWidget(Dialog)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.cancelPushButton = QtWidgets.QPushButton(self.widget)
        self.createPushButton = QtWidgets.QPushButton(self.widget)

        self.setupUi(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(475, 162)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(475, 162))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "    border: 2px solid rgb(59, 91, 134);\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    padding-left: 10px;\n"
                                      "    padding-right: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "    border: 2px solid rgb(32, 111, 209);\n"
                                      "}")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.directoryAccessButton.setStyleSheet("QPushButton{\n"
                                                 "    border: 0px solid;\n"
                                                 "    border-radius: 2px;\n"
                                                 "    background-color: rgb(59, 91, 134);\n"
                                                 "    padding-right:0px;\n"
                                                 "    padding-left: 0px;\n"
                                                 "}")
        self.directoryAccessButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/descarga.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.directoryAccessButton.setIcon(icon)
        self.directoryAccessButton.setObjectName("directoryAccessButton")
        self.gridLayout.addWidget(self.directoryAccessButton, 2, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.locationInput.setFont(font)
        self.locationInput.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(59, 91, 134);\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    padding-left: 10px;\n"
                                         "    padding-right: 10px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(32, 111, 209);\n"
                                         "}")
        self.locationInput.setObjectName("locationInput")
        self.gridLayout.addWidget(self.locationInput, 1, 0, 1, 1)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancelPushButton.setMinimumSize(QtCore.QSize(150, 25))
        self.cancelPushButton.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(9)
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setStyleSheet("QPushButton {\n"
                                            "    border: 2px solid rgb(59, 91, 134);\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: rgb(59, 91, 134);\n"
                                            "    padding-left: 10px;\n"
                                            "    padding-right: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    border: 2px solid rgb(32, 111, 209);\n"
                                            "    background-color: rgb(32, 111, 209);\n"
                                            "}")
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.createPushButton.setMinimumSize(QtCore.QSize(150, 25))
        self.createPushButton.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(9)
        self.createPushButton.setFont(font)
        self.createPushButton.setStyleSheet("QPushButton {\n"
                                            "    border: 2px solid rgb(59, 91, 134);\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "    padding-left: 10px;\n"
                                            "    padding-right: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    border: 2px solid rgb(32, 111, 209);\n"
                                            "}")
        self.createPushButton.setObjectName("createPushButton")
        self.horizontalLayout.addWidget(self.createPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.widget, 4, 0, 2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Location"))
        self.locationInput.setPlaceholderText(_translate("Dialog", "Name of new project.."))
        self.cancelPushButton.setText(_translate("Dialog", "Create"))
        self.createPushButton.setText(_translate("Dialog", "Cancel"))
