import configparser
import os
import shutil
import threading
from os.path import exists

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox

from Views import DialogWidget
from Logic import FindKeyWords, AnalyseDocuments


class KeyWordsWidgetPanel(object):

    def __init__(self, Form, centralWidget, MainWindow, ProjectDirectory):

        self.Form = Form
        self.centralWidget = centralWidget
        self.MainWindow = MainWindow
        self.ProjectDirectory = ProjectDirectory

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.widget = QtWidgets.QWidget(Form)
        self.generalGridLayout = QtWidgets.QGridLayout(self.widget)
        self.labelWidget = QtWidgets.QWidget(self.widget)
        self.labelWidgetLayout = QtWidgets.QGridLayout(self.labelWidget)
        self.gifChargingLabel = QtWidgets.QLabel(self.labelWidget)
        self.buttonsWidget = QtWidgets.QWidget(self.widget)
        self.buttonsWidgetLayout = QtWidgets.QGridLayout(self.buttonsWidget)
        self.findKeysButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.addKeyButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.analiseButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.createGraphicsButton = QtWidgets.QPushButton(self.buttonsWidget)
        self.widgetParametrization = QtWidgets.QWidget(self.widget)
        self.gridLayoutParametrization = QtWidgets.QGridLayout(self.widgetParametrization)
        self.min_char_length_SpinBox = QtWidgets.QSpinBox(self.widgetParametrization)
        self.min_keyword_frequency_SpinBox = QtWidgets.QSpinBox(self.widgetParametrization)
        self.min_phrase_freq_adj_SpinBox = QtWidgets.QSpinBox(self.widgetParametrization)
        self.min_char_length_label = QtWidgets.QLabel(self.widgetParametrization)
        self.min_phrase_freq_adj_label = QtWidgets.QLabel(self.widgetParametrization)
        self.min_keyword_frequency_label = QtWidgets.QLabel(self.widgetParametrization)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        self.recentProjectsDoc = configparser.RawConfigParser()

        self.keyExtractionFolder = self.ProjectDirectory + '/'
        self.keyExtractionFolder = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                     'analysis_folder_name') + '/'
        self.downloadFilesFolder = self.ProjectDirectory + '/'
        self.downloadFilesFolder = self.downloadFilesFolder + self.configGeneral.get('LOCATIONS',
                                                                                     'data_extraction_folder_name')+'/'
        self.keyListFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS', 'key_list_file_name')
        self.stopPathFile = self.configGeneral.get('LOCATIONS', 'stop_file_relative_path')
        self.relationFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS', 'key_relation_file_name')
        self.uniqueKeysFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                    'unique_keys_file_name')
        self.matrixAnalysisFile = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                    'matrix_analysis_file_name')
        self.finalDocumentPath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                   'normalised_matrix_file_name')
         # GRAPHICS_FOLDER
        self.GraphicsFolder = self.ProjectDirectory + '/'
        self.GraphicsFolder = self.GraphicsFolder + self.configGeneral.get('LOCATIONS', 'graphics_folder_name') + '/'

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')
        self.colorOfItem = str(self.mainColor).replace('(', '')
        self.colorOfItem = self.colorOfItem.replace(')', '')
        self.colorOfItem = self.colorOfItem.replace(' ', '') + ','
        self.colorOfItem = self.colorOfItem.split(',')

        self.state = 0
        self.thread = None
        self.movie = QMovie("./Resources/img/process_running_gif.gif")

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
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("alternate-background-color: rgb(85, 170, 255);\n"
                                       " font: " + str(self.fontSize) + "pt " + self.font + ";")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.setColumnWidth(0, 35)
        self.tableWidget.setColumnWidth(1, 435)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.generalGridLayout.setObjectName("generalGridLayout")
        self.labelWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.labelWidget.setObjectName("labelWidget")
        self.labelWidgetLayout.setObjectName("labelWidgetLayout")
        self.gifChargingLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.gifChargingLabel.setText("")
        self.gifChargingLabel.setObjectName("gifChargingLabel")
        self.labelWidgetLayout.addWidget(self.gifChargingLabel, 0, 0, 1, 1)
        self.generalGridLayout.addWidget(self.labelWidget, 1, 2, 1, 1)
        spacerItemRight = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generalGridLayout.addItem(spacerItemRight, 1, 3, 1, 1)
        self.buttonsWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.buttonsWidget.setObjectName("buttonsWidget")
        self.buttonsWidgetLayout.setObjectName("buttonsWidgetLayout")
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.findKeysButton.setFont(font)
        self.findKeysButton.setStyleSheet("QPushButton {\n"
                                          "    border: 2px solid;\n"
                                          "     border-radius: 10px;\n"
                                          "    background-color: rgb" + self.secondaryColor + ";\n"
                                          "    padding-right: 20px;\n"
                                          "    padding-left: 20px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb" + self.mainColor + ";\n"
                                          "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bitmap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.findKeysButton.setIcon(icon)
        self.findKeysButton.setObjectName("findKeysButton")
        self.buttonsWidgetLayout.addWidget(self.findKeysButton, 0, 0, 1, 1)
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.addKeyButton.setFont(font)
        self.addKeyButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addKeyButton.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid;\n"
                                        "     border-radius: 10px;\n"
                                        "    background-color: rgb" + self.secondaryColor + ";\n"
                                        "    padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb" + self.mainColor + ";\n"
                                        "}")
        self.addKeyButton.setIcon(icon)
        self.addKeyButton.setObjectName("addKeyButton")
        self.buttonsWidgetLayout.addWidget(self.addKeyButton, 2, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.analiseButton.setFont(font)
        self.analiseButton.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid;\n"
                                         "     border-radius: 10px;\n"
                                         "    background-color: rgb" + self.secondaryColor + ";\n"
                                         "    padding-right: 20px;\n"
                                         "    padding-left: 20px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb" + self.mainColor + ";\n"
                                         "}")
        self.analiseButton.setIcon(icon)
        self.analiseButton.setCheckable(False)
        self.analiseButton.setChecked(False)
        self.analiseButton.setObjectName("analiseButton")
        self.buttonsWidgetLayout.addWidget(self.analiseButton, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.createGraphicsButton.setFont(font)
        self.createGraphicsButton.setStyleSheet("QPushButton {\n"
                                                "    border: 2px solid;\n"
                                                "     border-radius: 10px;\n"
                                                "    background-color: rgb" + self.secondaryColor + ";\n"
                                                "    padding-right: 20px;\n"
                                                "    padding-left: 20px;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb" + self.mainColor + ";\n"
                                                "}")
        self.createGraphicsButton.setIcon(icon)
        self.createGraphicsButton.setObjectName("createGraphicsButton")
        self.buttonsWidgetLayout.addWidget(self.createGraphicsButton, 3, 0, 1, 1)
        self.generalGridLayout.addWidget(self.buttonsWidget, 1, 4, 1, 1)
        self.widgetParametrization.setObjectName("widgetParametrization")
        self.gridLayoutParametrization.setObjectName("gridLayoutParametrization")
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.min_keyword_frequency_label.setFont(font)
        self.min_char_length_SpinBox.setMinimum(1)
        self.min_char_length_SpinBox.setProperty("value", 3)
        self.min_char_length_SpinBox.setObjectName("spinBox")
        self.min_char_length_SpinBox.setFont(font)
        self.gridLayoutParametrization.addWidget(self.min_char_length_SpinBox, 0, 1, 1, 1)
        self.min_phrase_freq_adj_SpinBox.setMinimum(1)
        self.min_phrase_freq_adj_SpinBox.setProperty("value", 8)
        self.min_phrase_freq_adj_SpinBox.setFont(font)
        self.min_phrase_freq_adj_SpinBox.setObjectName("min_phrase_freq_adj_SpinBox")
        self.gridLayoutParametrization.addWidget(self.min_phrase_freq_adj_SpinBox, 1, 1, 1, 1)
        self.min_keyword_frequency_SpinBox.setMinimum(1)
        self.min_keyword_frequency_SpinBox.setProperty("value", 6)
        self.min_keyword_frequency_SpinBox.setFont(font)
        self.min_keyword_frequency_SpinBox.setObjectName("min_keyword_frequency_SpinBox")
        self.gridLayoutParametrization.addWidget(self.min_keyword_frequency_SpinBox, 2, 1, 1, 1)
        self.min_char_length_label.setObjectName("min_char_length_label")
        self.min_char_length_label.setFont(font)
        self.gridLayoutParametrization.addWidget(self.min_char_length_label, 0, 0, 1, 1)
        self.min_phrase_freq_adj_label.setObjectName("min_keyword_frequency_label")
        self.min_phrase_freq_adj_label.setText("")
        self.min_phrase_freq_adj_label.setFont(font)
        self.gridLayoutParametrization.addWidget(self.min_phrase_freq_adj_label, 1, 0, 1, 1)
        self.min_keyword_frequency_label.setObjectName("min_phrase_freq_adj_label")
        self.min_keyword_frequency_label.setText("")
        self.gridLayoutParametrization.addWidget(self.min_keyword_frequency_label, 2, 0, 1, 1)
        self.generalGridLayout.addWidget(self.widgetParametrization, 1, 0, 1, 1)
        spacerItemLeft = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generalGridLayout.addItem(spacerItemLeft, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.findKeysButton.clicked.connect(lambda: self.findKeyWords(1))
        self.addKeyButton.clicked.connect(lambda: self.addNewKey())
        self.analiseButton.clicked.connect(lambda: self.makeAnalise())
        self.createGraphicsButton.clicked.connect(lambda: self.goToGraphicWidgetPanel())
        self.tableWidget.cellChanged.connect(self.changeItemState)
        self.tableWidget.cellClicked.connect(self.deleteItem)

        self.initialStateDefined()
        self.movie.start()

    def initialStateDefined(self):
        if exists(self.keyExtractionFolder):
            if exists(self.keyListFilePath) and exists(self.relationFilePath) and exists(self.uniqueKeysFilePath):
                self.findKeyWords(3)
            else:
                if exists(self.keyListFilePath):
                    self.findKeyWords(2)
                    self.createGraphicsButton.setEnabled(False)
                else:
                    self.addKeyButton.setEnabled(False)
                    self.analiseButton.setEnabled(False)
                    self.createGraphicsButton.setEnabled(False)
        else:
            self.addKeyButton.setEnabled(False)
            self.analiseButton.setEnabled(False)
            self.createGraphicsButton.setEnabled(False)

    def goToGraphicWidgetPanel(self):
        self.MainWindow.controller.goToPanel(4)

    def deleteItem(self, row, column):
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
                if row % 2:
                    self.tableWidget.item(row, column).setBackground(QtGui.QColor(85, 170, 255))
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

    def makeAnalise(self):
        allTableWithData = True
        dataToAnalise = []
        changeState = True

        for row in range(0, self.tableWidget.rowCount() - 1):

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
                msgBoxLogin.setText('Error: concepto vacio en la tabla. Linea: ' + str(int(row + 1)))
                msgBoxLogin.exec()
                break

        if allTableWithData:
            for row in range(0, self.tableWidget.rowCount() - 1):
                relation = [self.tableWidget.item(row, 1).text(), self.tableWidget.item(row, 2).text()]
                dataToAnalise.append(relation)

            if exists(self.keyExtractionFolder):
                if exists(self.keyListFilePath) and exists(self.relationFilePath) and exists(
                        self.uniqueKeysFilePath):
                    dialog = QtWidgets.QDialog(self.centralWidget)
                    text_1 = str(self.config.get('KeyWordsViewSection', 'dialog_widget_message_text_1'))
                    text_2 = str(self.config.get('KeyWordsViewSection', 'dialog_widget_message_text_2'))
                    controller = DialogWidget.DialogWidget(dialog, text_1, text_2)
                    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                    dialog.exec_()

                    if controller.state:
                        if exists(self.GraphicsFolder):
                            shutil.rmtree(self.GraphicsFolder)
                    else:
                        changeState = False
            else:
                os.mkdir(self.keyExtractionFolder)

            if changeState:
                loadView = threading.Thread(name="loadViewThread", target=self.GUIActionChanges(False))

                self.thread = AnalyseDocuments.AnalyseDocuments(dataToAnalise, self.downloadFilesFolder,
                                                                self.stopPathFile, self.relationFilePath,
                                                                self.uniqueKeysFilePath,
                                                                self.matrixAnalysisFile, self.finalDocumentPath,
                                                                self.min_char_length_SpinBox.value(),
                                                                self.min_phrase_freq_adj_SpinBox.value(),
                                                                self.min_keyword_frequency_SpinBox.value())
                self.thread.successful_Action.connect(lambda: self.allCorrect())
                self.tableWidget.setEnabled(False)
                loadView.start()
                self.thread.start()

    def allCorrect(self):
        self.findKeysButton.setEnabled(True)
        self.addKeyButton.setEnabled(True)
        self.analiseButton.setEnabled(True)
        self.createGraphicsButton.setEnabled(True)
        self.min_keyword_frequency_label.setEnabled(True)
        self.min_phrase_freq_adj_SpinBox.setEnabled(True)
        self.min_phrase_freq_adj_label.setEnabled(True)
        self.min_keyword_frequency_SpinBox.setEnabled(True)
        self.min_char_length_label.setEnabled(True)
        self.min_char_length_SpinBox.setEnabled(True)
        self.MainWindow.dockWidget.setEnabled(True)
        self.tableWidget.setEnabled(True)
        self.MainWindow.menuBar.setEnabled(True)
        self.gifChargingLabel.clear()

    def findKeyWords(self, typology):

        changeState = True
        self.state = 0
        data = ''

        if typology == 1:
            if exists(self.keyListFilePath):
                dialog = QtWidgets.QDialog(self.centralWidget)
                text_1 = str(self.config.get('KeyWordsViewSection', 'dialog_widget_message_text_1'))
                text_2 = str(self.config.get('KeyWordsViewSection', 'dialog_widget_message_text_2'))
                controller = DialogWidget.DialogWidget(dialog, text_1, text_2)
                dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                dialog.exec_()

                if controller.state:
                    if exists(self.GraphicsFolder):
                        shutil.rmtree(self.GraphicsFolder)
                else:
                    changeState = False
            if changeState:
                if not exists(self.keyExtractionFolder):
                    os.mkdir(self.keyExtractionFolder)

        if changeState:

            loadView = threading.Thread(name="loadViewThread", target=self.GUIActionChanges(True))

            self.thread = FindKeyWords.FindKeyWords(typology, data, self.downloadFilesFolder, self.keyListFilePath,
                                                    self.stopPathFile, self.relationFilePath,
                                                    self.min_char_length_SpinBox.value(),
                                                    self.min_phrase_freq_adj_SpinBox.value(),
                                                    self.min_keyword_frequency_SpinBox.value())
            self.thread.successful_Action.connect(
                lambda: self.successful_Action(changeState, self.thread.data, typology))
            loadView.start()
            self.thread.start()

    def GUIActionChanges(self, typology):
        self.gifChargingLabel.clear()
        self.gifChargingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gifChargingLabel.setMovie(self.movie)
        if typology:
            self.tableWidget.clearContents()
        self.findKeysButton.setEnabled(False)
        self.analiseButton.setEnabled(False)
        self.addKeyButton.setEnabled(False)
        self.min_keyword_frequency_label.setEnabled(False)
        self.min_phrase_freq_adj_SpinBox.setEnabled(False)
        self.min_phrase_freq_adj_label.setEnabled(False)
        self.min_keyword_frequency_SpinBox.setEnabled(False)
        self.min_char_length_label.setEnabled(False)
        self.min_char_length_SpinBox.setEnabled(False)
        self.MainWindow.menuBar.setEnabled(False)
        self.createGraphicsButton.setEnabled(False)
        self.translateUi()

        # set dockWidget enable
        self.MainWindow.dockWidget.setEnabled(False)

    def successful_Action(self, changeState, data, typology):

        if changeState:
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
                item.setText('')
                item.setBackground(QtGui.QColor(255, 255, 255))
                self.tableWidget.setItem(rowNumber, 0, item)

                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)

                if typology != 3:
                    item.setText(str(iterator))
                else:
                    item.setText(str(iterator))

                self.tableWidget.setItem(rowNumber, 1, item)

                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)

                if typology == 3:
                    item.setText(str(data.get(iterator)))

                self.tableWidget.setItem(rowNumber, 2, item)

                rowNumber = rowNumber + 1
            self.state = 1
            self.addKeyButton.setEnabled(True)
            self.analiseButton.setEnabled(True)
            self.gifChargingLabel.clear()
            self.findKeysButton.setEnabled(True)
            self.min_keyword_frequency_label.setEnabled(True)
            self.min_phrase_freq_adj_SpinBox.setEnabled(True)
            self.min_phrase_freq_adj_label.setEnabled(True)
            self.min_keyword_frequency_SpinBox.setEnabled(True)
            self.min_char_length_label.setEnabled(True)
            self.min_char_length_SpinBox.setEnabled(True)
            self.MainWindow.dockWidget.setEnabled(True)

            if typology == 3:
                self.createGraphicsButton.setEnabled(True)

    def translateUi(self):
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                            'table_header_title_1')).encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                            'table_header_title_2')).encode('ansi')))
        self.findKeysButton.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                                           'find_keywords_button_text'))
                                               .encode('ansi')))
        self.findKeysButton.setShortcut(_translate("Form", "Ctrl+F"))
        self.analiseButton.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                                          'analise_button_text')).encode('ansi')))
        self.analiseButton.setShortcut(_translate("Form", "Ctrl+A"))
        self.addKeyButton.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                                         'add_key_button_text')).encode('ansi')))
        self.addKeyButton.setShortcut(_translate("Form", "Ctrl+K"))
        self.createGraphicsButton.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                                                 'go_to_graphic_button_text'))
                                                     .encode('ansi')))
        self.min_phrase_freq_adj_label.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                                     'minimum_phrase_frequency_adj_label_text'))
                                                          .encode('ansi')))
        self.min_keyword_frequency_label.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                                               'minimum_keyword_frequency_label_text'))
                                                            .encode('ansi')))
        self.min_char_length_label.setText(_translate("Form", str(self.config.get('KeyWordsViewSection',
                                                                                  'minimum_keyword_length_label_text'))
                                           .encode('ansi')))
