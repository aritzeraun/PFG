import configparser
import errno
import os
import shutil
import threading
from os.path import exists

from PIL import Image

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Logic import GraphicCreator
from Views import DialogWidget


class GraphicWidgetPanel(object):
    def __init__(self, Form, centralWidget, MainWindow, ProjectDirectory):

        self.Form = Form
        self.centralWidget = centralWidget
        self.MainWindow = MainWindow
        self.ProjectDirectory = ProjectDirectory

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.graphicLabel = QtWidgets.QLabel(Form)
        self.widget = QtWidgets.QWidget(Form)
        self.gridLayoutTop = QtWidgets.QGridLayout(self.widget)
        self.createGraphicButton = QtWidgets.QPushButton(self.widget)
        self.typeOfGraphicCombo = QtWidgets.QComboBox(self.widget)
        self.widthSpinBox = QtWidgets.QSpinBox(self.widget)
        self.widthLabel = QtWidgets.QLabel(self.widget)
        self.heightLabel = QtWidgets.QLabel(self.widget)
        self.heightSpinBox = QtWidgets.QSpinBox(self.widget)
        self.exportButton = QtWidgets.QPushButton(self.widget)
        self.SupportLabel = QtWidgets.QLabel(self.widget)
        self.lineRight = QtWidgets.QFrame(self.widget)
        self.lineLeft = QtWidgets.QFrame(self.widget)
        self.confidenceLabel = QtWidgets.QLabel(self.widget)
        self.supportSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.confidenceSpinBox = QtWidgets.QDoubleSpinBox(self.widget)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        self.recentProjectsDoc = configparser.RawConfigParser()
        self.movie = QMovie("./Resources/img/process_running_gif.gif")

        self.GraphicsFolder = self.ProjectDirectory + '/'
        self.GraphicsFolder = self.GraphicsFolder + self.configGeneral.get('LOCATIONS', 'graphics_folder_name') + '/'
        self.graphImageName = self.GraphicsFolder + self.configGeneral.get('LOCATIONS', 'graph_graphic_name')
        self.circularImageName = self.GraphicsFolder + self.configGeneral.get('LOCATIONS', 'circular_graphic_name')
        self.keyExtractionFolder = self.ProjectDirectory + '/'
        self.keyExtractionFolder = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                     'analysis_folder_name') + '/'
        self.UniqueKeysFile = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS', 'unique_keys_file_name')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.thread = None

        self.setupUi(self.Form)

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1171, 660)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.graphicLabel.setText("")
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setObjectName("graphicLabel")
        self.gridLayout.addWidget(self.graphicLabel, 1, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 140))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 140))
        self.widget.setObjectName("widget")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTop.addItem(spacerItem1, 0, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.createGraphicButton.setFont(font)
        self.createGraphicButton.setStyleSheet("QPushButton {\n"
                                               "    border: 2px solid;\n"
                                               "     border-radius: 10px;\n"
                                               "    background-color: rgb" + self.secondaryColor + ";\n"
                                               "    padding-right: 20px;\n"
                                               "    padding-left: 20px;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: rgb" + self.mainColor + ";\n"
                                               "}")
        self.createGraphicButton.setObjectName("createGraphicButton")
        self.gridLayoutTop.addWidget(self.createGraphicButton, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTop.addItem(spacerItem2, 0, 3, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.widthSpinBox.setFont(font)
        self.widthSpinBox.setStyleSheet("")
        self.widthSpinBox.setMinimum(400)
        self.widthSpinBox.setMaximum(2000)
        self.widthSpinBox.setSingleStep(100)
        self.widthSpinBox.setProperty("value", 1000)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.gridLayoutTop.addWidget(self.widthSpinBox, 0, 5, 1, 1)
        self.typeOfGraphicCombo.setMinimumSize(QtCore.QSize(185, 0))
        self.typeOfGraphicCombo.setMaximumSize(QtCore.QSize(185, 16777215))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.typeOfGraphicCombo.setFont(font)
        self.typeOfGraphicCombo.setStyleSheet("QComboBox {\n"
                                              "    background-color: rgb" + self.secondaryColor + ";\n"
                                              "    padding-right: 20px;\n"
                                              "    padding-left: 20px;\n"
                                              "}\n"
                                              "QComboBox:hover {\n"
                                              "    background-color: rgb" + self.mainColor + ";\n"
                                              "}")
        self.typeOfGraphicCombo.setObjectName("typeOfGraphicCombo")
        self.typeOfGraphicCombo.addItem("")
        self.typeOfGraphicCombo.addItem("")
        self.gridLayoutTop.addWidget(self.typeOfGraphicCombo, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.heightLabel.setFont(font)
        self.heightLabel.setObjectName("heightLabel")
        self.gridLayoutTop.addWidget(self.heightLabel, 1, 4, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.heightSpinBox.setFont(font)
        self.heightSpinBox.setMinimum(300)
        self.heightSpinBox.setMaximum(2000)
        self.heightSpinBox.setSingleStep(100)
        self.heightSpinBox.setProperty("value", 1000)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.gridLayoutTop.addWidget(self.heightSpinBox, 1, 5, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.widthLabel.setFont(font)
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayoutTop.addWidget(self.widthLabel, 0, 4, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.SupportLabel.setFont(font)
        self.SupportLabel.setObjectName("SupportLabel")
        self.gridLayoutTop.addWidget(self.SupportLabel, 4, 4, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.lineRight.setFont(font)
        self.lineRight.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineRight.setObjectName("lineRight")
        self.gridLayoutTop.addWidget(self.lineRight, 3, 4, 1, 1)
        self.lineLeft.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineLeft.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineLeft.setObjectName("lineLeft")
        self.gridLayoutTop.addWidget(self.lineLeft, 3, 5, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.confidenceLabel.setFont(font)
        self.confidenceLabel.setObjectName("confidenceLabel")
        self.gridLayoutTop.addWidget(self.confidenceLabel, 5, 4, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.supportSpinBox.setFont(font)
        self.supportSpinBox.setSingleStep(0.05)
        self.supportSpinBox.setProperty("value", 0.1)
        self.supportSpinBox.setObjectName("supportSpinBox")
        self.gridLayoutTop.addWidget(self.supportSpinBox, 4, 5, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.confidenceSpinBox.setFont(font)
        self.confidenceSpinBox.setSingleStep(0.05)
        self.confidenceSpinBox.setProperty("value", 0.05)
        self.confidenceSpinBox.setObjectName("confidenceSpinBox")
        self.gridLayoutTop.addWidget(self.confidenceSpinBox, 5, 5, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.exportButton.setFont(font)
        self.exportButton.setStyleSheet("QPushButton {\n"
                                        "    border: 2px solid;\n"
                                        "     border-radius: 10px;\n"
                                        "    background-color: rgb" + self.secondaryColor + ";\n"
                                        "    padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb" + self.mainColor + ";\n"
                                        "}")
        self.exportButton.setObjectName("exportButton")
        self.gridLayoutTop.addWidget(self.exportButton, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        Form.setObjectName("Form")

        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.createGraphicButton.clicked.connect(lambda: self.createGraphics())
        self.typeOfGraphicCombo.currentTextChanged.connect(lambda: self.changeImageOfLabel())
        self.exportButton.clicked.connect(lambda: self.exportImageResult())

        self.initialCheck()
        self.movie.start()

    def initialCheck(self):
        if exists(self.GraphicsFolder) and exists(self.graphImageName) and exists(self.circularImageName):
            self.changeImageOfLabel()
        else:
            self.exportButton.setEnabled(False)
            self.typeOfGraphicCombo.setEnabled(False)

    def changeImageOfLabel(self):
        self.graphicLabel.clear()

        if 'ular' in self.typeOfGraphicCombo.currentText():
            pixmap_image = QtGui.QPixmap(self.circularImageName)
        else:
            pixmap_image = QtGui.QPixmap(self.graphImageName)

        pixmap_image.scaled(1600, 1000, QtCore.Qt.KeepAspectRatio)
        pixmap_image.devicePixelRatio()

        self.graphicLabel.setPixmap(pixmap_image)
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setScaledContents(True)
        self.graphicLabel.setMinimumSize(1, 1)
        self.graphicLabel.show()

    def loadViewThread(self):
        # change login view
        self.graphicLabel.clear()
        self.MainWindow.dockWidget.setEnabled(False)
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setMovie(self.movie)
        self.typeOfGraphicCombo.setEnabled(False)
        self.exportButton.setEnabled(False)
        self.widthLabel.setEnabled(False)
        self.widthSpinBox.setEnabled(False)
        self.heightLabel.setEnabled(False)
        self.heightSpinBox.setEnabled(False)
        self.createGraphicButton.setEnabled(False)
        self.MainWindow.menuBar.setEnabled(False)

    def thread_image_creation_correctly(self):
        self.graphicLabel.clear()
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setMovie(self.movie)
        self.typeOfGraphicCombo.setEnabled(True)
        self.exportButton.setEnabled(True)
        self.widthLabel.setEnabled(True)
        self.widthSpinBox.setEnabled(True)
        self.heightLabel.setEnabled(True)
        self.heightSpinBox.setEnabled(True)
        self.createGraphicButton.setEnabled(True)
        self.MainWindow.dockWidget.setEnabled(True)
        self.supportSpinBox.setEnabled(True)
        self.confidenceLabel.setEnabled(True)
        self.confidenceSpinBox.setEnabled(True)
        self.SupportLabel.setEnabled(True)
        self.MainWindow.menuBar.setEnabled(True)

        if 'ular' in self.typeOfGraphicCombo.currentText():
            pixmap_image = QtGui.QPixmap(self.circularImageName)
        else:
            pixmap_image = QtGui.QPixmap(self.graphImageName)

        self.graphicLabel.setPixmap(pixmap_image)
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setScaledContents(True)
        self.graphicLabel.devicePixelRatioFScale()
        self.graphicLabel.setMinimumSize(1, 1)
        self.graphicLabel.show()

    def createGraphics(self):

        # it saved the window format
        self.graphicLabel.clear()
        self.graphicLabel.setScaledContents(False)

        if not exists(self.GraphicsFolder):
            editState = True
            try:
                os.mkdir(self.GraphicsFolder)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        else:
            if exists(self.graphImageName) and exists(self.circularImageName):
                dialog = QtWidgets.QDialog(self.centralWidget)
                text_1 = str(self.config.get('GraphViewSection', 'dialog_widget_message_text_1'))
                text_2 = str(self.config.get('GraphViewSection', 'dialog_widget_message_text_2'))
                controller = DialogWidget.DialogWidget(dialog, text_1, text_2)
                dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                dialog.exec_()

                if controller.state:
                    editState = True
                else:
                    editState = False
                    self.initialCheck()
            else:
                editState = True

        if editState:
            loadView = threading.Thread(name="loadViewThread", target=self.loadViewThread)

            self.thread = GraphicCreator.GraphicCreatorAction(self.UniqueKeysFile, self.widthSpinBox.value(),
                                                              self.heightSpinBox.value(), self.supportSpinBox.value(),
                                                              self.confidenceSpinBox.value(), self.circularImageName,
                                                              self.graphImageName)
            self.thread.image_creation_correctly.connect(self.thread_image_creation_correctly)

            self.supportSpinBox.setEnabled(False)
            self.SupportLabel.setEnabled(False)
            self.confidenceSpinBox.setEnabled(False)
            self.confidenceLabel.setEnabled(False)

            loadView.start()
            self.thread.start()

    def exportImageResult(self):

        if 'ular' in self.typeOfGraphicCombo.currentText():
            source = self.circularImageName
        else:
            source = self.graphImageName

        if exists(self.GraphicsFolder) and exists(source):

            options = QFileDialog.Options()
            folder = QFileDialog.getSaveFileName(None, str(self.config.get('GraphViewSection', 'file_dialog_title')),
                                                 "", "JPG (*.jpg);;PNG (*.png);; PDF (*.pdf)", options=options)
            if 'JPG' in folder[1]:
                shutil.copy(source, str(folder[0]))
            elif 'PNG' in folder[1]:
                image = Image.open(source)
                image.save(str(folder[0]))
            elif 'PDF' in folder[1]:
                image_1 = Image.open(source)
                im_1 = image_1.convert('RGB')
                im_1.save(str(folder[0]))
        else:
            ErrorBox = QMessageBox()
            ErrorBox.setText(str(self.config.get('GraphViewSection', 'error_exporting_label_message')).encode('ansi'))
            ErrorBox.exec()

    def translateUi(self):
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        _translate = QtCore.QCoreApplication.translate
        self.createGraphicButton.setText(_translate("Form",
                                                    str(self.config.get('GraphViewSection',
                                                                        'create_graphics_button_text')).encode('ansi')))
        self.typeOfGraphicCombo.setItemText(0, _translate("Form",
                                                          str(self.config.get('GraphViewSection',
                                                                              'type_of_graphic_combo_bos_option_0'))
                                                          .encode('ansi')))
        self.typeOfGraphicCombo.setItemText(1, _translate("Form",
                                                          str(self.config.get('GraphViewSection',
                                                                              'type_of_graphic_combo_bos_option_1'))
                                                          .encode('ansi')))
        self.widthLabel.setText(_translate("Form", str(self.config.get('GraphViewSection',
                                                                       'width_label_text')).encode('ansi')))
        self.heightLabel.setText(_translate("Form", str(self.config.get('GraphViewSection',
                                                                        'height_label_text')).encode('ansi')))
        self.exportButton.setText(_translate("Form", str(self.config.get('GraphViewSection',
                                                                         'export_button_text')).encode('ansi')))
        self.SupportLabel.setText(_translate("Form", str(self.config.get('GraphViewSection',
                                                                         'support_label_text')).encode('ansi')))
        self.confidenceLabel.setText(_translate("Form", str(self.config.get('GraphViewSection',
                                                                            'confidence_label_text')).encode('ansi')))
