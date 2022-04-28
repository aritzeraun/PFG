import configparser
import urllib

from PyQt5 import QtCore, QtGui, QtWidgets

from Connecttion import IntenetConnection
from Logic import DeterminedStated
from Views import GraphicWidgetPanel, WithoutConnectionPanelWidget, LoginWidgetPanel, KeyWordsWidgetPanel, \
    ResultWidgetPanel, SearchWidgetPanel


class DockWidgetPanel(object):

    def __init__(self, Form, centralWidget, MainWindow, projectDirectory):

        self.Form = Form
        self.centralWidget = centralWidget
        self.MainWindow = MainWindow
        self.projectDirectory = projectDirectory

        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.widget = QtWidgets.QWidget(Form)
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.graphicsButton = QtWidgets.QPushButton(self.widget)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.analiseButton = QtWidgets.QPushButton(self.widget)
        self.downloadButton = QtWidgets.QPushButton(self.widget)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.fix_ip = self.configGeneral.get('IP', 'fix_ip')
        self.wireless_ip = self.configGeneral.get('IP', 'wireless_ip')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.visibleForm = QtWidgets.QWidget(self.centralWidget)
        self.controller = None
        self.setupUi(self.Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(785, 622)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(200, 600))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("background-color: rgb" + self.secondaryColor + "; border: none;")
        self.widget.setObjectName("widget")
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsButton.setMinimumSize(QtCore.QSize(0, 35))
        self.graphicsButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.graphicsButton.setFont(font)
        self.graphicsButton.setObjectName("graphicsButton")
        self.gridLayout.addWidget(self.graphicsButton, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.searchButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.searchButton.setFont(font)
        self.searchButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.searchButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")
        self.searchButton.setIconSize(QtCore.QSize(0, 0))
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(True)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 1, 0, 1, 1)
        self.analiseButton.setMinimumSize(QtCore.QSize(0, 35))
        self.analiseButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.analiseButton.setFont(font)
        self.analiseButton.setObjectName("analiseButton")
        self.gridLayout.addWidget(self.analiseButton, 3, 0, 1, 1)
        self.downloadButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.downloadButton.setFont(font)
        self.downloadButton.setObjectName("downloadButton")
        self.downloadButton.setMinimumSize(QtCore.QSize(0, 35))
        self.downloadButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.gridLayout.addWidget(self.downloadButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

        # action definition
        self.searchButton.clicked.connect(lambda: self.goToPanel(1))
        self.downloadButton.clicked.connect(lambda: self.goToPanel(2))
        self.analiseButton.clicked.connect(lambda: self.goToPanel(3))
        self.graphicsButton.clicked.connect(lambda: self.goToPanel(4))
        self.goToPanel(1)

    def goToPanel(self, actionType):

        controller = DeterminedStated.DeterminedState(self, self.projectDirectory)
        controller.stateDetermination()

        self.searchButton.setStyleSheet("background-color: rgb" + self.secondaryColor + "; border: none;")
        self.downloadButton.setStyleSheet("background-color: rgb" + self.secondaryColor + "; border: none;")
        self.analiseButton.setStyleSheet("background-color: rgb" + self.secondaryColor + "; border: none;")
        self.graphicsButton.setStyleSheet("background-color: rgb" + self.secondaryColor + "; border: none;")

        if actionType == 1:
            self.searchButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")
            if IntenetConnection.connectionToEthernet():
                ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
                if ip != self.fix_ip and ip not in self.wireless_ip:
                    LicenseView = QtWidgets.QWidget(self.centralWidget)
                    self.controller = LoginWidgetPanel.LoginWidgetPanel(LicenseView, self.centralWidget,
                                                                        self.MainWindow)
                    self.MainWindow.visibleForm.close()
                    self.MainWindow.visibleForm = LicenseView
                    self.MainWindow.gridLayout.addWidget(LicenseView)
                else:
                    SearchView = QtWidgets.QWidget(self.centralWidget)
                    self.controller = SearchWidgetPanel.SearchWidgetPanel(SearchView, None, self.centralWidget,
                                                                          self.MainWindow)
                    self.MainWindow.visibleForm.close()
                    self.MainWindow.visibleForm = SearchView
                    self.MainWindow.gridLayout.addWidget(SearchView)
            else:
                WithoutConnectionView = QtWidgets.QWidget(self.centralWidget)
                self.controller = WithoutConnectionPanelWidget.WithoutConnectionPanelWidget(WithoutConnectionView,
                                                                                            self.centralWidget,
                                                                                            self.MainWindow)
                self.MainWindow.visibleForm = WithoutConnectionView
                self.MainWindow.gridLayout.addWidget(WithoutConnectionView)
        elif actionType == 2:
            self.downloadButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")
            resultView = QtWidgets.QWidget(self.centralWidget)
            self.controller = ResultWidgetPanel.ResultWidgetPanel(resultView, self.centralWidget, self.MainWindow,
                                                                  self.projectDirectory)

            self.MainWindow.gridLayout.addWidget(self.controller.Form)
            self.MainWindow.visibleForm.close()
            self.MainWindow.visibleForm = resultView

        elif actionType == 3:
            self.analiseButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")
            keyWordView = QtWidgets.QWidget(self.centralWidget)
            self.controller = KeyWordsWidgetPanel.KeyWordsWidgetPanel(keyWordView, self.centralWidget, self.MainWindow,
                                                                      self.projectDirectory)
            self.MainWindow.gridLayout.addWidget(self.controller.Form)
            self.MainWindow.visibleForm.close()
            self.MainWindow.visibleForm = keyWordView

        elif actionType == 4:
            self.graphicsButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")

            graphicsView = QtWidgets.QWidget(self.centralWidget)
            self.controller = GraphicWidgetPanel.GraphicWidgetPanel(graphicsView, self.centralWidget, self.MainWindow,
                                                                    self.projectDirectory)
            self.MainWindow.gridLayout.addWidget(self.controller.Form)
            self.MainWindow.visibleForm.close()
            self.MainWindow.visibleForm = graphicsView

    def translateUi(self):
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        _translate = QtCore.QCoreApplication.translate
        self.graphicsButton.setText(_translate("Form", str(self.config.get('DockWidgetSection',
                                                                           'graphics_button_text')).encode('ansi')))
        self.searchButton.setText(_translate("Form", str(self.config.get('DockWidgetSection',
                                                                         'search_button_text')).encode('ansi')))
        self.analiseButton.setText(_translate("Form", str(self.config.get('DockWidgetSection',
                                                                          'analyse_button_text')).encode('ansi')))
        self.downloadButton.setText(_translate("Form", str(self.config.get('DockWidgetSection',
                                                                           'download_button_text')).encode('ansi')))
