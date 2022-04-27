import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class NewProjectDialog(object):
    def __init__(self, Dialog, typology):
        self.typology = typology

        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        if self.typology != 1:
            self.folderInputLine = QtWidgets.QLineEdit(Dialog)
            self.directoryAccessButton = QtWidgets.QPushButton(Dialog)
        if self.typology <= 1:
            self.projectNameInputLine = QtWidgets.QLineEdit(Dialog)
        self.widget = QtWidgets.QWidget(Dialog)
        self.errorMessageLabel = QtWidgets.QLabel(Dialog)
        self.specificationMessageLabel = QtWidgets.QLabel(Dialog)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.createPushButton = QtWidgets.QPushButton(self.widget)
        self.cancelPushButton = QtWidgets.QPushButton(self.widget)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.folder = None
        self.newProjectName = None
        self.newProjectLocation = None
        self.newProjectNameValidated = None
        self.creationState = None
        self.dialog = None
        self.setupUi(Dialog)

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        if self.typology == 0:
            Dialog.resize(550, 205)
        else:
            Dialog.resize(550, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(550, 205))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")

        if self.typology != 1:
            self.folderInputLine.setMinimumSize(QtCore.QSize(400, 0))
            font = QtGui.QFont()
            font.setFamily(self.font)
            font.setBold(False)
            font.setWeight(50)
            self.folderInputLine.setFont(font)
            self.folderInputLine.setStyleSheet("QLineEdit {\n"
                                               "    border: 2px solid rgb" + self.secondaryColor + ";\n"
                                               "    border-radius: 10px;\n"
                                               "    background-color: rgb(255, 255, 255);\n"
                                               "    padding-left: 10px;\n"
                                               "    padding-right: 10px;\n"
                                               "}\n"
                                               "QLineEdit:hover {\n"
                                               "    border: 2px solid rgb" + self.mainColor + ";\n"
                                               "}")
            self.folderInputLine.setReadOnly(True)
            self.folderInputLine.setClearButtonEnabled(False)
            self.folderInputLine.setObjectName("lineEdit_2")
            self.gridLayout.addWidget(self.folderInputLine, 2, 0, 1, 1)

            self.directoryAccessButton.setStyleSheet("QPushButton{\n"
                                                     "    border: 0px solid;\n"
                                                     "    border-radius: 2px;\n"
                                                     "    background-color: rgb" + self.secondaryColor + ";\n"
                                                     "    padding-right:0px;\n"
                                                     "    padding-left: 0px;\n"
                                                     "}")
            self.directoryAccessButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('./Resources/img/folder_open_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.directoryAccessButton.setIcon(icon)
            self.directoryAccessButton.setObjectName("directoryAccessButton")
            self.gridLayout.addWidget(self.directoryAccessButton, 2, 1, 1, 1)

        if self.typology <= 1:
            font = QtGui.QFont()
            font.setFamily(self.font)
            self.projectNameInputLine.setFont(font)
            self.projectNameInputLine.setStyleSheet("QLineEdit {\n"
                                                    "    border: 2px solid rgb" + self.secondaryColor + ";\n"
                                                    "    border-radius: 10px;\n"
                                                    "    background-color: rgb(255, 255, 255);\n"
                                                    "    padding-left: 10px;\n"
                                                    "    padding-right: 10px;\n"
                                                    "}\n"
                                                    "QLineEdit:hover {\n"
                                                    "    border: 2px solid rgb" + self.mainColor + ";\n"
                                                    "}")
            self.projectNameInputLine.setObjectName("locationInput")
            self.gridLayout.addWidget(self.projectNameInputLine, 1, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.createPushButton.setMinimumSize(QtCore.QSize(150, 25))
        self.createPushButton.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.createPushButton.setFont(font)
        self.createPushButton.setStyleSheet("QPushButton {\n"
                                            "    border: 2px solid rgb" + self.secondaryColor + ";\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: rgb" + self.secondaryColor + ";\n"
                                            "    padding-left: 10px;\n"
                                            "    padding-right: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    border: 2px solid rgb" + self.mainColor + ";\n"
                                            "    background-color: rgb" + self.mainColor + ";\n"
                                            "}")
        self.createPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.createPushButton)
        self.cancelPushButton.setMinimumSize(QtCore.QSize(150, 25))
        self.cancelPushButton.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setStyleSheet("QPushButton {\n"
                                            "    border: 2px solid rgb" + self.secondaryColor + ";\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "    padding-left: 10px;\n"
                                            "    padding-right: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    border: 2px solid rgb" + self.mainColor + ";\n"
                                            "}")
        self.cancelPushButton.setObjectName("createPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.widget, 5, 0, 2, 1)
        self.errorMessageLabel.setText("")
        self.errorMessageLabel.setObjectName("errorMessageLabel")
        self.errorMessageLabel.setStyleSheet("color: rgb(255, 0, 0);")
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.createPushButton.setFont(font)
        self.errorMessageLabel.setFont(font)
        self.gridLayout.addWidget(self.errorMessageLabel, 3, 0, 1, 1)
        self.specificationMessageLabel.setText("")
        self.specificationMessageLabel.setObjectName("specificationMessageLabel")
        self.specificationMessageLabel.setStyleSheet("color: rgb(255, 0, 0);")
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.specificationMessageLabel.setFont(font)
        self.gridLayout.addWidget(self.specificationMessageLabel, 4, 0, 1, 1)

        self.translateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.createPushButton.clicked.connect(lambda: self.createNewProject())
        self.cancelPushButton.clicked.connect(lambda: self.cancelNewProject())

        if self.typology != 1:
            self.directoryAccessButton.clicked.connect(lambda: self.openNewProjectDirectory())
        if self.typology <= 1:
            self.projectNameInputLine.textChanged.connect(lambda: self.projectNameVerifier())

    def projectNameVerifier(self):

        notAcceptedCharacters = ['\\', '/', ';', ':', '<', '>', '*', '?', '¿', '¡', '!', '"', '+', ',', '=', '|', 'º',
                                 'ª', '@', '·', '#', '$', '~', '€', '%', '&', '¬', '{', '}', '[', ']', '´', '`', '¨']
        _translate = QtCore.QCoreApplication.translate

        if any(ext in self.projectNameInputLine.text() for ext in notAcceptedCharacters):
            self.errorMessageLabel.setText(_translate("Dialog", str(self.config.get('NewProjectDialogSection',
                                                                                    'noValidCharacter_error_message'))
                                                      .encode('ansi')))

            self.specificationMessageLabel.setText('\\/;:<>¿?¡!*+"=,|ºª@·#$~%&¬{}[]^`´¨€')
            self.newProjectNameValidated = False
        else:
            self.newProjectNameValidated = True
            self.errorMessageLabel.setText('')
            self.specificationMessageLabel.setText('')

    def createNewProject(self):
        _translate = QtCore.QCoreApplication.translate
        if self.typology == 0:
            if self.folderInputLine.text() != '' and self.projectNameInputLine.text() != '' \
                    and self.newProjectNameValidated:
                self.errorMessageLabel.setText('')
                self.newProjectName = self.projectNameInputLine.text()
                self.newProjectLocation = self.folderInputLine.text()
                self.creationState = True
                self.dialog.close()
        elif self.typology == 1:
            if self.projectNameInputLine.text() != ''and self.newProjectNameValidated:
                self.errorMessageLabel.setText('')
                self.newProjectName = self.projectNameInputLine.text()
                self.creationState = True
                self.dialog.close()
        elif self.typology == 2:
            if self.folderInputLine.text() != '':
                self.errorMessageLabel.setText('')
                self.newProjectLocation = self.folderInputLine.text()
                self.creationState = True
                self.dialog.close()

        if self.typology <= 1:
            if self.projectNameInputLine.text() == '':
                self.errorMessageLabel.setText(_translate("Dialog",
                                                          str(self.config.get('NewProjectDialogSection',
                                                                              'projectNameInput_empty_error_message'))
                                                          .encode('ansi')))

        if self.typology != 1:
            if self.folderInputLine.text() == '':
                self.errorMessageLabel.setText(_translate("Dialog",
                                                          str(self.config.get('NewProjectDialogSection',
                                                                              'folderInput_empty_error_message'))
                                               .encode('ansi')))

    def cancelNewProject(self):
        self.creationState = False
        self.dialog.close()

    def openNewProjectDirectory(self):
        folder = str(QFileDialog.getExistingDirectory(None, str(self.config.get('NewProjectDialogSection',
                                                                                'newProject_fileDialog_title_text'))))
        self.folder = folder
        self.folderInputLine.setText(str(folder))

    def translateUi(self, Dialog):
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        _translate = QtCore.QCoreApplication.translate
        if self.typology == 0:
            Dialog.setWindowTitle(_translate("Dialog", str(self.config.get('NewProjectDialogSection',
                                                                           'window_title_0_text')).encode('ansi')))
        elif self.typology == 1:
            Dialog.setWindowTitle(_translate("Dialog", str(self.config.get('NewProjectDialogSection',
                                                                           'window_title_1_text')).encode('ansi')))
        elif self.typology == 2:
            Dialog.setWindowTitle(_translate("Dialog", str(self.config.get('NewProjectDialogSection',
                                                                           'window_title_2_text')).encode('ansi')))
        if self.typology != 1:
            self.folderInputLine.setPlaceholderText(
                _translate("Dialog", str(self.config.get('NewProjectDialogSection',
                                                         'location_inputLine_placeholder_text'))
                           .encode('ansi')))

        if self.typology <= 1:
            self.projectNameInputLine.setPlaceholderText(
                _translate("Dialog", str(self.config.get('NewProjectDialogSection', 'name_inputLine_placeholder_text'))
                           .encode('ansi')))

        if self.typology == 0:
            self.createPushButton.setText(_translate("Dialog",  str(self.config.get('NewProjectDialogSection',
                                                                                    'createButton_text'))
                                                     .encode('ansi')))
        elif self.typology >= 1:
            self.createPushButton.setText(_translate("Dialog",  str(self.config.get('NewProjectDialogSection',
                                                                                    'changeButton_text'))
                                                     .encode('ansi')))

        self.cancelPushButton.setText(_translate("Dialog", str(self.config.get('NewProjectDialogSection',
                                                                               'cancelButton_text'))
                                                 .encode('ansi')))
