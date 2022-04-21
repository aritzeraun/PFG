import configparser
import os
import time
from os.path import exists

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Rake_Analysis import rake_Analysis
from Views import GraphicWidgetPanel


class KeyWordsWidgetPanel(object):

    def __init__(self, Form, centralWidget, MainWindow, ProjectDirectory):
        self.Form = Form
        self.centralWidget = centralWidget
        self.MainWindow = MainWindow
        self.ProjectDirectory = ProjectDirectory

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        self.recentProjectsDoc = configparser.RawConfigParser()

        self.keyExtractionFolder = self.ProjectDirectory + '/'
        self.keyExtractionFolder = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                     'analysis_folder_name') + '/'
        self.downloadedFilesFolder = self.ProjectDirectory + '/' + self.configGeneral.get('LOCATIONS',
                                                                               'downloaded_files_folder_name')+'/'
        self.keyListFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS', 'key_list_file_name')
        self.stopPathFile = self.configGeneral.get('LOCATIONS', 'stop_file_relative_path')
        self.relationFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS', 'key_relation_file_name')
        self.uniqueKeysFilePath = self.keyExtractionFolder+self.configGeneral.get('LOCATIONS', 'unique_keys_file_name')
        self.matrixAnalysisFile = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                    'matrix_analysis_file_name')
        self.finalDocumentPath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                   'normalised_matrix_file_name')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')
        self.colorOfItem = str(self.mainColor).replace('(', '')
        self.colorOfItem = self.colorOfItem.replace(')', '')
        self.colorOfItem = self.colorOfItem.replace(' ', '') + ','
        self.colorOfItem = self.colorOfItem.split(',')
        self.state = 0

        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(882, 782)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.tableWidget.setFont(font)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.downloadButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.downloadButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bitmap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon)
        self.downloadButton.setObjectName("downloadButton")
        self.gridLayout_2.addWidget(self.downloadButton, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.pushButton.setFont(font)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(False)

        self.downloadButton.clicked.connect(lambda: self.findKeyWords())
        self.pushButton_2.clicked.connect(lambda: self.addNewKey())
        self.pushButton.clicked.connect(lambda: self.makeAnalise())
        self.pushButton_3.clicked.connect(lambda: self.goToGraphicWidgetPanel())
        self.tableWidget.cellChanged.connect(self.changeItemState)
        self.tableWidget.cellClicked.connect(self.deleteItem)

    def goToGraphicWidgetPanel(self):
        graphicsView = QtWidgets.QWidget(self.centralWidget)
        controller = GraphicWidgetPanel.GraphicWidgetPanel(graphicsView, self.centralWidget, self.MainWindow,
                                                           self.ProjectDirectory)
        self.MainWindow.gridLayout.addWidget(controller.Form)
        graphicsView.show()
        self.Form.close()

    def deleteItem(self,  row, column):
        column = int(column)
        if column == 0:
            self.tableWidget.removeRow(row)

    def changeItemState(self, row, column):
        text = self.tableWidget.item(row, column).text()
        text.replace(' ', '')
        if self.state != 0:
            if text == '':
                self.tableWidget.item(row, column).setBackground(QtGui.QColor(int(self.colorOfItem[0]),
                                                                              int(self.colorOfItem[1]),
                                                                              int(self.colorOfItem[2])))
            else:
                self.tableWidget.item(row, column).setBackground(QtGui.QColor(255, 255, 255))

    def addNewKey(self):

        self.tableWidget.insertRow(0)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
        icon = QtGui.QIcon()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        icon.addPixmap(QtGui.QPixmap("./Resources/img/incorrect_delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(int(self.colorOfItem[0]), int(self.colorOfItem[1]), int(self.colorOfItem[2])))
        item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(int(self.colorOfItem[0]), int(self.colorOfItem[1]), int(self.colorOfItem[2])))
        item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)

    def chargeData(self):
        if exists(self.keyExtractionFolder):
            print(11)

    def makeAnalise(self):
        allTableWithData = True
        dataToAnalise = []

        for row in range(0, self.tableWidget.rowCount()-1):

            key = self.tableWidget.item(row, 1).text()
            key = key.replace(' ', '')

            selfKey = self.tableWidget.item(row, 2).text()
            selfKey = selfKey.replace(' ', '')

            if key == '' or selfKey == '':
                allTableWithData = False
                if key == '':
                    self.tableWidget.item(row, 1).setBackground(QtGui.QColor(int(self.colorOfItem[0]),
                                                                             int(self.colorOfItem[1]),
                                                                             int(self.colorOfItem[2])))
                elif selfKey == '':
                    self.tableWidget.item(row, 1).setBackground(QtGui.QColor(int(self.colorOfItem[0]),
                                                                             int(self.colorOfItem[1]),

                                                                             int(self.colorOfItem[2])))
                msgBoxLogin = QMessageBox()
                msgBoxLogin.setText('error: at line ' + str(int(row + 1)) + ' of the table.')
                msgBoxLogin.exec()
                break

        if allTableWithData:
            for row in range(0, self.tableWidget.rowCount()-1):
                relation = [self.tableWidget.item(row, 1).text(), self.tableWidget.item(row, 2).text()]
                dataToAnalise.append(relation)

            if not exists(self.keyExtractionFolder):
                os.mkdir(self.keyExtractionFolder)

            rake_Analysis.writeRelationCSV(self.relationFilePath, dataToAnalise)
            time.sleep(1)
            rake_Analysis.allAnalysis(self.relationFilePath, self.downloadedFilesFolder, self.uniqueKeysFilePath,
                                      self.matrixAnalysisFile, self.finalDocumentPath, self.stopPathFile)

            self.pushButton_3.setEnabled(True)

    def findKeyWords(self):

        self.state = 0

        if not exists(self.keyExtractionFolder):
            os.mkdir(self.keyExtractionFolder)

        data = rake_Analysis.writeListKey(self.downloadedFilesFolder, self.keyListFilePath, self.stopPathFile)

        self.tableWidget.setRowCount(len(data))

        rowNumber = 0
        for iterator in data:

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
            icon = QtGui.QIcon()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            icon.addPixmap(QtGui.QPixmap("./Resources/img/incorrect_delete_icon.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setBackground(QtGui.QColor(255, 255, 255))
            self.tableWidget.setItem(rowNumber, 0, item)

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setText(str(iterator))
            self.tableWidget.setItem(rowNumber, 1, item)

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(rowNumber, 2, item)

            rowNumber = rowNumber + 1
        self.state = 1
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(True)

    def translateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "KeyWord"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Self kew"))
        self.downloadButton.setText(_translate("Form", "Find KeyWord"))
        self.downloadButton.setShortcut(_translate("Form", "Ctrl+F"))
        self.pushButton.setText(_translate("Form", "Analise"))
        self.pushButton.setShortcut(_translate("Form", "Ctrl+A"))
        self.pushButton_2.setText(_translate("Form", "Add KeyWord"))
        self.pushButton_2.setShortcut(_translate("Form", "Ctrl+K"))
        self.pushButton_3.setText(_translate("Form", "Create Graphics"))
