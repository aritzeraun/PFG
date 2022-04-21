import configparser
import shutil
import threading

from PIL import Image

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QFileDialog
from Logic import GraphicCreator


class GraphicWidgetPanel(object):
    def __init__(self, Form, centralWidget, MainWindow, ProjectDirectory):

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.graphicLabel = QtWidgets.QLabel(Form)
        self.widget = QtWidgets.QWidget(Form)
        self.gridLayoutTop = QtWidgets.QGridLayout(self.widget)
        self.createGraphicButton = QtWidgets.QPushButton(self.widget)
        self.typeOfGraphicCombo = QtWidgets.QComboBox(self.widget)
        self.widgetTop = QtWidgets.QWidget(Form)
        self.gridLayoutSecond = QtWidgets.QGridLayout(self.widgetTop)
        self.widthSpinBox = QtWidgets.QSpinBox(self.widget)
        self.widthLabel = QtWidgets.QLabel(self.widget)
        self.heightLabel = QtWidgets.QLabel(self.widget)
        self.heightSpinBox = QtWidgets.QSpinBox(self.widget)
        self.exportButton = QtWidgets.QPushButton(self.widgetTop)
        self.Form = Form
        self.centralWidget = centralWidget
        self.MainWindow = MainWindow
        self.ProjectDirectory = ProjectDirectory

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
        self.matrixAnalysisFile = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                    'matrix_analysis_file_name')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.thread = None

        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(929, 590)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout.setObjectName("gridLayout")
        self.graphicLabel.setText("")
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setObjectName("graphicLabel")
        self.gridLayout.addWidget(self.graphicLabel, 2, 0, 1, 1)
        self.widget.setMinimumSize(QtCore.QSize(0, 80))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget.setObjectName("widget")
        self.gridLayoutTop.setObjectName("gridLayoutTop")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTop.addItem(spacerItem, 0, 1, 1, 1)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTop.addItem(spacerItem1, 0, 3, 1, 1)
        self.typeOfGraphicCombo.setMinimumSize(QtCore.QSize(130, 0))
        self.typeOfGraphicCombo.setMaximumSize(QtCore.QSize(165, 16777215))
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
        self.widthSpinBox.setFont(font)
        self.widthSpinBox.setStyleSheet("")
        self.widthSpinBox.setMinimum(400)
        self.widthSpinBox.setMaximum(2000)
        self.widthSpinBox.setSingleStep(100)
        self.widthSpinBox.setProperty("value", 1000)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.gridLayoutTop.addWidget(self.widthSpinBox, 0, 5, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.widthLabel.setFont(font)
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayoutTop.addWidget(self.widthLabel, 0, 4, 1, 1)
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
        self.heightSpinBox.setMaximum(1600)
        self.heightSpinBox.setSingleStep(100)
        self.heightSpinBox.setProperty("value", 1600)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.gridLayoutTop.addWidget(self.heightSpinBox, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widgetTop.setMinimumSize(QtCore.QSize(0, 50))
        self.widgetTop.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widgetTop.setObjectName("widgetTop")
        self.gridLayoutSecond.setObjectName("gridLayoutSecond")
        spacerItem2 = QtWidgets.QSpacerItem(782, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutSecond.addItem(spacerItem2, 0, 0, 1, 1)
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
        self.gridLayoutSecond.addWidget(self.exportButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widgetTop, 1, 0, 1, 1)

        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.createGraphicButton.clicked.connect(lambda: self.createGraphics())

        self.exportButton.setEnabled(False)
        self.typeOfGraphicCombo.setEnabled(False)
        self.movie.start()

    def loadViewThread(self):
        # change login view
        self.graphicLabel.clear()
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setMovie(self.movie)
        self.typeOfGraphicCombo.setEnabled(False)
        self.exportButton.setEnabled(False)
        self.widthSpinBox.setEnabled(False)
        self.heightLabel.setEnabled(False)
        self.createGraphicButton.setEnabled(False)

    def thread_image_creation_correctly(self):
        self.graphicLabel.clear()
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setMovie(self.movie)
        self.typeOfGraphicCombo.setEnabled(True)
        self.exportButton.setEnabled(True)
        self.widthSpinBox.setEnabled(True)
        self.heightLabel.setEnabled(True)
        self.createGraphicButton.setEnabled(True)

        pixmap_image = ''

        if 'Graph' in self.typeOfGraphicCombo.currentText():
            pixmap_image = QtGui.QPixmap(self.graphImageName)
        elif 'Circular' in self.typeOfGraphicCombo.currentText():
            pixmap_image = QtGui.QPixmap(self.graphImageName)

        self.graphicLabel.setPixmap(pixmap_image)
        self.graphicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicLabel.setScaledContents(True)
        self.graphicLabel.setMinimumSize(1, 1)
        self.graphicLabel.show()

    def createGraphics(self):

        loadView = threading.Thread(name="loadViewThread", target=self.loadViewThread)

        self.thread = GraphicCreator.GraphicCreatorAction(self.matrixAnalysisFile, self.widthSpinBox.value(),
                                                          self.heightSpinBox.value(), self.circularImageName,
                                                          self.graphImageName)
        self.thread.image_creation_correctly.connect(self.thread_image_creation_correctly)

        loadView.start()
        self.thread.start()

    def exportProject(self):
        options = QFileDialog.Options()
        folder = str(QFileDialog.getSaveFileName(None, "Select graphic export location", "",
                                                 "JPG (*.jpg);;PNG (*.png);; PDF (*.pdf)", options=options))

        if 'JPG' in folder[1]:
            shutil.copy("src", str(folder[0]))
        elif 'PNG' in folder[1]:
            image = Image.open(r'path where the JPG is stored\file name.jpg')
            image.save(str(folder[0]))
        elif 'PDF' in folder[1]:
            image_1 = Image.open(r'C:\Users\Ron\Desktop\Test\view_1.jpg')
            im_1 = image_1.convert('RGB')
            im_1.save(str(folder[0]))

    def translateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.createGraphicButton.setText(_translate("Form", "Create Graphic"))
        self.typeOfGraphicCombo.setItemText(0, _translate("Form", "Graph graphic"))
        self.typeOfGraphicCombo.setItemText(1, _translate("Form", "Circular graphic"))
        self.widthLabel.setText(_translate("Form", "Width: "))
        self.heightLabel.setText(_translate("Form", "Height:"))
        self.exportButton.setText(_translate("Form", "Export"))
