import configparser
import errno
import os
import threading

from os import walk
from os.path import exists

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets
import Excel.ExcelFileTreatment
from Logic import DocumentClasifycator, DownloadDocuments


class ResultWidgetPanel(object):

    def __init__(self, Form, centralWidget, MainWindow, projectDirectory):

        self.MainWindow = MainWindow
        self.centralWidget = centralWidget
        self.Form = Form
        self.ProjectDirectory = projectDirectory

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.GoToAnaliseWidget = QtWidgets.QWidget(Form)
        self.GoToAnaliseGridLayout = QtWidgets.QGridLayout(self.GoToAnaliseWidget)
        self.GoToAnalisePushButton = QtWidgets.QPushButton(self.GoToAnaliseWidget)
        self.buttonsFrame = QtWidgets.QWidget(Form)
        self.buttonsFrameGridLayout = QtWidgets.QGridLayout(self.buttonsFrame)
        self.viewOptionsComboBox = QtWidgets.QComboBox(self.buttonsFrame)
        self.limit_time_box = QtWidgets.QSpinBox(self.buttonsFrame)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.downloadButton = QtWidgets.QPushButton(self.buttonsFrame)
        self.limit_label = QtWidgets.QLabel(self.buttonsFrame)
        self.gifChargingLabel = QtWidgets.QLabel(self.buttonsFrame)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.dataExtractFolder = self.ProjectDirectory + '/'
        self.dataExtractFolder = self.dataExtractFolder + self.configGeneral.get('LOCATIONS',
                                                                                 'data_extraction_folder_name') + '/'
        self.downloadedFolder = self.ProjectDirectory + '/'
        self.downloadedFolder = self.downloadedFolder + self.configGeneral.get('LOCATIONS',
                                                                               'downloaded_documents_folder_name')+'/'
        self.searchDocumentListFolder = self.ProjectDirectory + '/'
        self.searchDocumentListFolder = self.searchDocumentListFolder + self.configGeneral.get('LOCATIONS',
                                                                                 'document_list_folder_name') + '/'
        self.movie = QMovie("./Resources/img/process_running_gif.gif")
        self.filesName = []
        self.data = None
        self.dataToDownload = None
        self.dataOfDocuments = None
        self.state_select = ""
        self.getFilesName()
        self.searchTypology = 1
        self.thread = None

        self.setupUi(self.Form)

    def setupUi(self, Form):

        self.state_select = Qt.CheckState(0)

        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(767, 727)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout.setObjectName("gridLayout")
        self.GoToAnaliseWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.GoToAnaliseWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.GoToAnaliseWidget.setObjectName("GoToAnaliseWidget")
        self.GoToAnaliseGridLayout.setContentsMargins(0, 0, 0, 0)
        self.GoToAnaliseGridLayout.setSpacing(0)
        self.GoToAnaliseGridLayout.setObjectName("GoToAnaliseGridLayout")
        self.GoToAnalisePushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        font.setBold(True)
        font.setWeight(75)
        self.GoToAnalisePushButton.setFont(font)
        self.GoToAnalisePushButton.setStyleSheet("QPushButton {\n"
                                                 "    border: 2px solid;\n"
                                                 "     border-radius: 10px;\n"
                                                 "    background-color: rgb" + self.secondaryColor + ";\n"
                                                 "    padding-right: 20px;\n"
                                                 "    padding-left: 20px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb" + self.mainColor + ";\n"
                                                 "}")
        self.GoToAnalisePushButton.setObjectName("GoToAnalisePushButton")
        self.GoToAnaliseGridLayout.addWidget(self.GoToAnalisePushButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.GoToAnaliseWidget, 2, 0, 1, 1)
        self.buttonsFrame.setObjectName("buttonsFrame")
        self.buttonsFrameGridLayout.setObjectName("buttonsFrameGridLayout")
        # self.buttonsFrameGridLayout.addWidget(self.parametrizationComboBox, 0, 8, 1, 1)
        self.viewOptionsComboBox.setMinimumSize(QtCore.QSize(119, 0))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.viewOptionsComboBox.setFont(font)
        self.viewOptionsComboBox.setStyleSheet(" QComboBox {\n"
                                               "border: 1px solid;\n"
                                               "     border-radius: 10px;\n"
                                               "     background-color: rgb" + self.mainColor + ";\n"
                                               "     padding: 1px 18px 1px 3px;\n"
                                               "     min-width: 6em;\n"
                                               " }\n"
                                               " QComboBox:on { /* shift the text when the popup opens */\n"
                                               "     padding-top: 3px;\n"
                                               "     padding-left: 4px;\n"
                                               " }\n"
                                               " QComboBox::drop-down {\n"
                                               "     subcontrol-origin: padding;\n"
                                               "     subcontrol-position: top right;\n"
                                               "     width: 15px;\n"
                                               "     border-left-width: 1px;\n"
                                               "     border-left-color: darkgray;\n"
                                               "     border-left-style: solid; /* just a single line */\n"
                                               "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                               "     border-bottom-right-radius: 3px;\n"
                                               " }\n"
                                               " QComboBox::down-arrow {\n"
                                               "     image: url(descarga.png);\n"
                                               " }\n"
                                               " QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                               "     top: 1px;\n"
                                               "     left: 1px;\n"
                                               " }")
        self.viewOptionsComboBox.setObjectName("viewOptionsComboBox")
        self.viewOptionsComboBox.addItem("")
        self.viewOptionsComboBox.addItem("")
        self.viewOptionsComboBox.addItem("")
        self.buttonsFrameGridLayout.addWidget(self.viewOptionsComboBox, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        font.setBold(True)
        font.setWeight(75)
        self.limit_label.setFont(font)
        self.limit_label.setObjectName("label")
        self.buttonsFrameGridLayout.addWidget(self.limit_label, 0, 4, 1, 1)

        self.limit_time_box.setStyleSheet("QSpinBox {\n"
                                          "    border: 2px solid;\n"
                                          "     border-radius: 10px;\n"
                                          "    background-color: rgb" + self.secondaryColor + ";\n"
                                          "    padding-right: 20px;\n"
                                          "    padding-left: 20px;\n"
                                          "}\n"
                                          "QSpinBox:hover {\n"
                                          "    background-color: rgb" + self.mainColor + ";\n"
                                          "}\n"
                                          "QSpinBox::down-arrow:pressed\n"
                                          "{\n"
                                          "border : 4px solid green;\n"
                                          "}")
        self.limit_time_box.setObjectName("timeBox")
        self.buttonsFrameGridLayout.addWidget(self.limit_time_box, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsFrameGridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsFrameGridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("QPushButton {\n"
                                          "    border: 2px solid;\n"
                                          "     border-radius: 10px;\n"
                                          "    background-color: rgb" + self.secondaryColor + ";\n"
                                          "    padding-right: 20px;\n"
                                          "    padding-left: 20px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb" + self.mainColor + ";\n"
                                          "}")
        self.downloadButton.setCheckable(False)
        self.downloadButton.setAutoDefault(False)
        self.downloadButton.setDefault(False)
        self.downloadButton.setFlat(False)
        self.downloadButton.setObjectName("downloadButton")
        self.buttonsFrameGridLayout.addWidget(self.downloadButton, 0, 6, 1, 1)

        self.gridLayout.addWidget(self.buttonsFrame, 0, 0, 1, 1)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 0))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setStyleSheet("alternate-background-color: rgb(85, 170, 255);\n"
                                       " font: " + str(self.fontSize) + "pt " + self.font + ";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.gifChargingLabel.setMinimumHeight(100)

        self.gifChargingLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.gifChargingLabel.setText("")
        self.gifChargingLabel.setObjectName("gifChargingLabel")
        self.buttonsFrameGridLayout.addWidget(self.gifChargingLabel, 0, 2, 1, 1)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        # Predefine table columns width
        self.tableWidget.setColumnWidth(0, 25)
        self.tableWidget.setColumnWidth(1, 35)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(3, 235)
        self.tableWidget.setColumnWidth(4, 235)
        self.tableWidget.setColumnWidth(5, 135)
        self.tableWidget.setColumnWidth(6, 135)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 135)
        self.tableWidget.setColumnWidth(10, 135)

        self.translateUi()
        self.viewOptionsComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # actions with widgets
        self.tableWidget.horizontalHeader().sectionPressed.connect(self.changeAllItemState)
        self.tableWidget.cellClicked.connect(self.changeItemState)
        self.downloadButton.clicked.connect(lambda: self.downloadAction())
        self.viewOptionsComboBox.currentIndexChanged.connect(lambda: self.viewChanges())
        self.limit_time_box.valueChanged.connect(lambda: self.limit_time_Change())
        self.GoToAnalisePushButton.clicked.connect(lambda: self.goToKeyWordsView())

        # Predefined values
        self.GoToAnaliseWidget.setVisible(False)
        self.limit_time_box.setValue(int(5))
        self.limit_time_box.setMinimum(int(1))
        self.limit_time_box.setMaximum(25)

        self.search_data()
        self.movie.start()

        # define initial state
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        icon = QtGui.QIcon()
        self.state_select = Qt.CheckState(2)
        icon.addPixmap(QtGui.QPixmap("./Resources/img/checked_document_icon.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableWidget.setHorizontalHeaderItem(0, item)

    def goToKeyWordsView(self):
        self.MainWindow.controller.goToPanel(3)

    def limit_time_Change(self):

        actualValue = int(self.limit_time_box.value())
        msgBoxAlert = QMessageBox()
        if actualValue == 25:
            msgBoxAlert.setText(str(self.config.get('DownloadViewSection', 'alert_time_limit_too_high')))
            msgBoxAlert.exec()
        elif actualValue == 1:
            msgBoxAlert.setText(str(self.config.get('DownloadViewSection', 'alert_time_limit_too_low')))
            msgBoxAlert.exec()
        elif 1 < actualValue < 5:
            msgBoxAlert.setText(str(self.config.get('DownloadViewSection', 'alert_time_limit_recommend')))
            msgBoxAlert.exec()

    def viewChanges(self):
        self.searchTypology = int(self.viewOptionsComboBox.currentIndex())
        self.tableWidget.clearContents()
        self.search_data()

    def getFilesName(self):

        for (dir_path, dir_names, filenames) in walk(self.searchDocumentListFolder):
            file = self.searchDocumentListFolder + filenames[0]
            self.filesName.append(file)

        self.dataOfDocuments = Excel.ExcelFileTreatment.openFile(self.filesName)

    def changeAllItemState(self, index):

        number = self.tableWidget.rowCount()

        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        icon = QtGui.QIcon()

        if index == 0:

            if self.state_select == Qt.CheckState(0) or self.state_select == Qt.CheckState(1):
                self.state_select = Qt.CheckState(2)
                icon.addPixmap(QtGui.QPixmap("./Resources/img/checked_document_icon.png"), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(icon)
                self.tableWidget.setHorizontalHeaderItem(0, item)

            else:
                self.state_select = Qt.CheckState(0)
                icon.addPixmap(QtGui.QPixmap("./Resources/img/unchecked_document_icon.png"), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(icon)
                self.tableWidget.setHorizontalHeaderItem(0, item)

        for i in range(0, number):
            self.tableWidget.item(i, 0).setCheckState(self.state_select)

    def changeItemState(self, row, column):
        if column == 0:
            if self.tableWidget.item(row, column).checkState() == Qt.CheckState(0):
                self.tableWidget.item(row, column).setCheckState(Qt.CheckState(2))
            else:
                self.tableWidget.item(row, column).setCheckState(Qt.CheckState(0))

            number = self.tableWidget.rowCount()
            numberOfCoincidence = 0

            for i in range(0, number):
                if self.tableWidget.item(i, column).checkState() == Qt.CheckState(2):
                    numberOfCoincidence = numberOfCoincidence + 1

            item = QtWidgets.QTableWidgetItem()
            item.setBackground(QtGui.QColor(85, 170, 255))
            icon = QtGui.QIcon()

            if numberOfCoincidence == number:
                self.state_select = Qt.CheckState(2)
                icon.addPixmap(QtGui.QPixmap("./Resources/img/checked_document_icon.png"), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(icon)
                self.tableWidget.setHorizontalHeaderItem(0, item)

            elif number > numberOfCoincidence > 0:
                self.state_select = Qt.CheckState(1)
                icon.addPixmap(QtGui.QPixmap("./Resources/img/intermediate_document_icon.png"), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(icon)
                self.tableWidget.setHorizontalHeaderItem(0, item)
            elif numberOfCoincidence == 0:
                self.state_select = Qt.CheckState(0)
                icon.addPixmap(QtGui.QPixmap("./Resources/img/unchecked_document_icon.png"), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(icon)
                self.tableWidget.setHorizontalHeaderItem(0, item)

    def downloadAction(self):

        # View Selected options
        self.viewOptionsComboBox.setCurrentIndex(1)

        # Creates folder if not exists
        try:
            os.mkdir(self.dataExtractFolder)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        # Verifies that the document does not been downloaded previously
        filesName = []

        if exists(self.downloadedFolder):
            for (dir_path, dir_names, filenames) in walk(self.downloadedFolder):
                filesName.extend(filenames)
                break

        loadView = threading.Thread(name="loadViewThread", target=self.GUIActionChanges)
        self.thread = DownloadDocuments.DownloadDocuments(self.dataToDownload, self.tableWidget, filesName,
                                                          int(self.limit_time_box.text()), self.downloadedFolder,
                                                          self.dataExtractFolder)

        self.thread.downloaded_correctly.connect(lambda: self.downloadViewChanges())

        # If it is locate in changes provokes a error due to execute lines
        self.tableWidget.setEnabled(False)

        loadView.start()
        self.thread.start()

    def downloadViewChanges(self):
        self.gifChargingLabel.clear()
        self.downloadButton.setEnabled(True)
        self.limit_time_box.setEnabled(True)
        self.viewOptionsComboBox.setEnabled(True)
        self.MainWindow.dockWidget.setEnabled(True)
        self.GoToAnaliseWidget.setVisible(True)
        self.tableWidget.setEnabled(True)

    def GUIActionChanges(self):
        self.MainWindow.dockWidget.setEnabled(False)
        self.gifChargingLabel.clear()
        self.gifChargingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gifChargingLabel.setMovie(self.movie)
        self.downloadButton.setEnabled(False)
        self.limit_time_box.setEnabled(False)
        self.viewOptionsComboBox.setEnabled(False)
        self.GoToAnaliseWidget.setVisible(False)

    def chargeData(self):

        filesName = []

        if exists(self.downloadedFolder):
            for (dir_path, dir_names, filenames) in walk(self.downloadedFolder):
                filesName.extend(filenames)
                break
        else:
            try:
                os.mkdir(self.downloadedFolder)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        for i in range(0, self.tableWidget.rowCount() - 1):
            self.tableWidget.removeRow(i)

        if self.searchTypology == 1 or self.searchTypology == 2:
            self.data = DocumentClasifycator.selectedDocuments(self.dataOfDocuments, self.searchTypology)
            if self.searchTypology == 1:
                self.dataToDownload = self.data
        else:
            self.data = self.dataOfDocuments

        self.tableWidget.setRowCount(len(self.data))
        rowNumber = 0
        for iterator in self.data:

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(Qt.CheckState(2))
            self.tableWidget.setItem(rowNumber, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            icon = QtGui.QIcon()

            if len(filesName) > 0:
                documentName = iterator.__getitem__(2)
                documentName = str(documentName).replace('/', '_')
                documentName = str(documentName).replace('\\', '-')
                documentName = str(documentName) + str('.pdf')
                if documentName in filesName:
                    icon.addPixmap(QtGui.QPixmap("./Resources/img/correct_download_icon.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                else:
                    icon.addPixmap(QtGui.QPixmap("./Resources/img/incorrect_delete_icon.png"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            else:
                icon.addPixmap(QtGui.QPixmap("./Resources/img/incorrect_delete_icon.png"), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)

            item.setIcon(icon)
            self.tableWidget.setItem(rowNumber, 1, item)

            # Title
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(iterator.__getitem__(1))
            self.tableWidget.setItem(rowNumber, 2, item)

            # Author
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(iterator.__getitem__(0))
            self.tableWidget.setItem(rowNumber, 3, item)

            # DOI
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(iterator.__getitem__(2))
            self.tableWidget.setItem(rowNumber, 4, item)

            # Source Title
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(iterator.__getitem__(3))
            self.tableWidget.setItem(rowNumber, 5, item)

            # Publication Year
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(str(iterator.__getitem__(4)))
            item.setTextAlignment(Qt.AlignHCenter)
            self.tableWidget.setItem(rowNumber, 6, item)

            # ISSN
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignHCenter)
            item.setText(str(iterator.__getitem__(5)))
            self.tableWidget.setItem(rowNumber, 7, item)

            # EISSN
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(str(iterator.__getitem__(6)))
            item.setTextAlignment(Qt.AlignHCenter)
            self.tableWidget.setItem(rowNumber, 8, item)

            # UT
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setTextAlignment(Qt.AlignHCenter)
            item.setText(str(iterator.__getitem__(7)).replace('WOS:', ''))
            self.tableWidget.setItem(rowNumber, 9, item)

            # Research ID
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(str(iterator.__getitem__(8)))
            self.tableWidget.setItem(rowNumber, 10, item)

            rowNumber = rowNumber + 1

    def search_data(self):
        loadView = threading.Thread(name="loadViewThread", target=self.chargeData)
        loadView.start()

    def translateUi(self):
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        _translate = QtCore.QCoreApplication.translate
        self.downloadButton.setText(_translate("Form", str(self.config.get('DownloadViewSection',
                                                                           'download_button_text')).encode('ansi')))
        self.viewOptionsComboBox.setItemText(0, _translate("Form", str(self.config.get('DownloadViewSection',
                                                                                       'view_options_combobox_0'))
                                                           .encode('ansi')))
        self.viewOptionsComboBox.setItemText(1, _translate("Form", str(self.config.get('DownloadViewSection',
                                                                                       'view_options_combobox_1'))
                                                           .encode('ansi')))
        self.viewOptionsComboBox.setItemText(2, _translate("Form", str(self.config.get('DownloadViewSection',
                                                                                       'view_options_combobox_2'))
                                                           .encode('ansi')))
        self.limit_label.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'limit_label_text'))
                                            .encode('ansi')))
        self.GoToAnalisePushButton.setText(_translate("Form", str(self.config.get('DownloadViewSection',
                                                                                  'go_to_analise_button_text'))
                                                      .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_2'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_3'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_4'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_5'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_6'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_7'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_8'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_9'))
                                .encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", str(self.config.get('DownloadViewSection', 'table_header_column_10'))
                                .encode('ansi')))
