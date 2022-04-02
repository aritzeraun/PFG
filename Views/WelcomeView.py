from PyQt5 import QtCore, QtGui, QtWidgets
from Views import LicenseWidgetPanel, ProjectWidgetPanel, CustomiseWidgetPanel
import configparser


class WelcomeView(object):

    def __init__(self, MainWindow):

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
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
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
        self.optionsWidget.setStyleSheet("background-color: rgb(59, 91, 134); border: none;")
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
                                        "font: 8pt \"Cascadia Mono\";")
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
        font.setFamily("Cascadia Mono")
        font.setPointSize(9)
        self.projectOptionButton.setFont(font)
        self.projectOptionButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.projectOptionButton.setStyleSheet("background-color: rgb(32, 111, 209); border: none;")
        self.projectOptionButton.setIconSize(QtCore.QSize(0, 0))
        self.projectOptionButton.setAutoDefault(False)
        self.projectOptionButton.setDefault(True)
        self.projectOptionButton.setFlat(False)
        self.projectOptionButton.setObjectName("projectOptionButton")
        self.verticalLayout.addWidget(self.projectOptionButton)
        self.customiseOptionButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(9)
        self.customiseOptionButton.setFont(font)
        self.customiseOptionButton.setObjectName("Customise")
        self.verticalLayout.addWidget(self.customiseOptionButton)
        self.licenseOptionButton.setMinimumSize(QtCore.QSize(0, 35))
        self.licenseOptionButton.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(9)
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
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1216, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.translateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.projectOptionButton.clicked.connect(lambda: self.moveToWelcomeViewOptions(1))
        self.customiseOptionButton.clicked.connect(lambda: self.moveToWelcomeViewOptions(2))
        self.licenseOptionButton.clicked.connect(lambda: self.moveToWelcomeViewOptions(3))

        ProjectView = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayout.addWidget(ProjectView)
        projectViewController = ProjectWidgetPanel.ProjectWidgetPanel(ProjectView)
        self.sectionViews.close()
        self.sectionViews = projectViewController.Form

    def moveToWelcomeViewOptions(self, chooseButtonIdentifier):
        self.projectOptionButton.setStyleSheet("border: none;")
        self.customiseOptionButton.setStyleSheet("border: none;")
        self.licenseOptionButton.setStyleSheet("border: none;")

        if chooseButtonIdentifier == 1:
            self.projectOptionButton.setStyleSheet("background-color: rgb(32, 111, 209); border: none;")
            ProjectView = QtWidgets.QWidget(self.centralWidget)
            self.horizontalLayout.addWidget(ProjectView)
            projectViewController = ProjectWidgetPanel.ProjectWidgetPanel(ProjectView)
            self.sectionViews.close()
            self.sectionViews = projectViewController.Form

        elif chooseButtonIdentifier == 2:
            self.customiseOptionButton.setStyleSheet("background-color: rgb(32, 111, 209); border: none;")

            CustomiseView = QtWidgets.QWidget(self.centralWidget)
            self.horizontalLayout.addWidget(CustomiseView)
            customiseViewController = CustomiseWidgetPanel.CustomiseWidgetPanel(CustomiseView)
            self.sectionViews.close()
            self.sectionViews = customiseViewController.Form

        elif chooseButtonIdentifier == 3:
            self.licenseOptionButton.setStyleSheet("background-color: rgb(32, 111, 209); border: none;")
            LicenseView = QtWidgets.QWidget(self.centralWidget)
            self.horizontalLayout.addWidget(LicenseView)
            licenseViewController = LicenseWidgetPanel.Ui_Form(LicenseView)
            self.sectionViews.close()
            self.sectionViews = licenseViewController.Form

    def translateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
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
