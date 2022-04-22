from PyQt5 import QtCore, QtGui, QtWidgets
from Views import LicenseWidgetPanel, ProjectWidgetPanel, CustomiseWidgetPanel
import configparser


class WelcomeView(object):

    def __init__(self, MainWindow, init):

        self.MainWindow = MainWindow
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.optionsWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.optionsWidget)
        self.projectOptionButton = QtWidgets.QPushButton(self.optionsWidget)
        self.AppNameLabel = QtWidgets.QPushButton(self.optionsWidget)
        self.customiseOptionButton = QtWidgets.QPushButton(self.optionsWidget)
        self.licenseOptionButton = QtWidgets.QPushButton(self.optionsWidget)
        self.sectionViews = QtWidgets.QWidget(self.centralWidget)
        self.gridLayout = QtWidgets.QGridLayout(self.sectionViews)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.setupUi(MainWindow, init)

    def setupUi(self, MainWindow, init):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 889)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionsWidget.sizePolicy().hasHeightForWidth())
        self.optionsWidget.setSizePolicy(sizePolicy)
        self.optionsWidget.setMinimumSize(QtCore.QSize(250, 600))
        self.optionsWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.optionsWidget.setStyleSheet("background-color: rgb" + self.secondaryColor + "; border: none;")
        self.optionsWidget.setObjectName("optionsWidgets")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AppNameLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AppNameLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.AppNameLabel.setStyleSheet("border: none;\n"
                                        "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "    color: palette(window-text);\n"
                                        "    background: transparent;\n"
                                        "font: " + str(self.fontSize) + "pt \"" + self.font + "\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('./Resources/img/app_icon.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AppNameLabel.setIcon(icon)
        self.AppNameLabel.setIconSize(QtCore.QSize(50, 80))
        self.AppNameLabel.setDefault(False)
        self.AppNameLabel.setFlat(True)
        self.AppNameLabel.setObjectName("AppNameLabel")
        self.verticalLayout.addWidget(self.AppNameLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.projectOptionButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.projectOptionButton.setFont(font)
        self.projectOptionButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.projectOptionButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")
        self.projectOptionButton.setIconSize(QtCore.QSize(0, 0))
        self.projectOptionButton.setAutoDefault(False)
        self.projectOptionButton.setDefault(True)
        self.projectOptionButton.setFlat(False)
        self.projectOptionButton.setObjectName("projectOptionButton")
        self.verticalLayout.addWidget(self.projectOptionButton)
        self.customiseOptionButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.customiseOptionButton.setFont(font)
        self.customiseOptionButton.setObjectName("Customise")
        self.verticalLayout.addWidget(self.customiseOptionButton)
        self.licenseOptionButton.setMinimumSize(QtCore.QSize(0, 35))
        self.licenseOptionButton.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.licenseOptionButton.setFont(font)
        self.licenseOptionButton.setObjectName("licenseOptionButton")
        self.verticalLayout.addWidget(self.licenseOptionButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.optionsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionViews.sizePolicy().hasHeightForWidth())
        self.sectionViews.setSizePolicy(sizePolicy)
        self.sectionViews.setObjectName("SectionViews")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout.addWidget(self.sectionViews)
        MainWindow.setCentralWidget(self.centralWidget)

        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.projectOptionButton.clicked.connect(lambda: self.moveToWelcomeViewOptions(1))
        self.customiseOptionButton.clicked.connect(lambda: self.moveToWelcomeViewOptions(2))
        self.licenseOptionButton.clicked.connect(lambda: self.moveToWelcomeViewOptions(3))

        self.moveToWelcomeViewOptions(init)

    def moveToWelcomeViewOptions(self, chooseButtonIdentifier):
        self.projectOptionButton.setStyleSheet("border: none;")
        self.customiseOptionButton.setStyleSheet("border: none;")
        self.licenseOptionButton.setStyleSheet("border: none;")

        # go to Project View
        if chooseButtonIdentifier == 1:
            self.projectOptionButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")
            ProjectView = QtWidgets.QWidget(self.centralWidget)
            self.horizontalLayout.addWidget(ProjectView)
            projectViewController = ProjectWidgetPanel.ProjectWidgetPanel(ProjectView, self.MainWindow)
            self.sectionViews.close()
            self.sectionViews = projectViewController.Form

        # go to Customise View
        elif chooseButtonIdentifier == 2:
            self.customiseOptionButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")

            CustomiseView = QtWidgets.QWidget(self.centralWidget)
            self.horizontalLayout.addWidget(CustomiseView)
            customiseViewController = CustomiseWidgetPanel.CustomiseWidgetPanel(CustomiseView, self.centralWidget, self)
            self.sectionViews.close()
            self.sectionViews = customiseViewController.Form

        # go to License View
        elif chooseButtonIdentifier == 3:
            self.licenseOptionButton.setStyleSheet("background-color: rgb" + self.mainColor + "; border: none;")
            LicenseView = QtWidgets.QWidget(self.centralWidget)
            self.horizontalLayout.addWidget(LicenseView)
            licenseViewController = LicenseWidgetPanel.LicenseWidgetPanel(LicenseView)
            self.sectionViews.close()
            self.sectionViews = licenseViewController.Form

    def translateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.AppNameLabel.setText(_translate("MainWindow", "  SpyDocument\n"
                                                           "  v2022.1"))
        self.projectOptionButton.setText(_translate("MainWindow", self.config.get('WelcomeViewSection',
                                                                                  'projectOptionButton_text')
                                         .encode('ansi')))
        self.customiseOptionButton.setText(_translate("MainWindow", str(self.config.get('WelcomeViewSection',
                                                                                        'customiseOptionButton_text'))
                                                      .encode('ansi')))
        self.licenseOptionButton.setText(_translate("MainWindow", str(self.config.get('WelcomeViewSection',
                                                                                      'licenseOptionButton_text'))
                                                    .encode('ansi')))
