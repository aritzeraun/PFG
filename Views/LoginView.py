import threading
import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox
from Logic import DomainLogic, LoginAction, ConfigWriter
from Views import SearchView


class Ui_MainWindow:

    def __init__(self):
        self.GUI = SearchView.Ui_Form()
        self.movie = QMovie("./GUI/process.gif")
        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Languages/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.msgBoxDomain = QMessageBox()
        self.username = ""
        self.password = ""

    def setupUi(self, MainWindow):
        # open language configuration file
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('LANGUAGE', 'code') + '.cfg')
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowModality(QtCore.Qt.NonModal)
        self.MainWindow.resize(1064, 792)
        self.MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        self.MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./GUI/SpyDocument.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.MainWindow.setIconSize(QtCore.QSize(60, 60))
        self.MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.MainWindow.setDocumentMode(False)
        self.MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks |
                                  QtWidgets.QMainWindow.AnimatedDocks | QtWidgets.QMainWindow.ForceTabbedDocks |
                                  QtWidgets.QMainWindow.GroupedDragging | QtWidgets.QMainWindow.VerticalTabs)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(200, 200))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget.setBaseSize(QtCore.QSize(250, 25))
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget {\n"
                                  "qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255))\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 3)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(400, 40))
        self.widget_2.setMaximumSize(QtCore.QSize(400, 40))
        self.widget_2.setObjectName("widget_2")
        self.accessButton = QtWidgets.QPushButton(self.widget_2)
        self.accessButton.setGeometry(QtCore.QRect(130, 10, 111, 28))
        self.accessButton.setAutoFillBackground(False)
        self.accessButton.setStyleSheet("QPushButton {\n"
                                        "border: 2px solid;\n"
                                        " \n"
                                        " border-radius: 10px;\n"
                                        "    background-color: rgb(165, 134, 83);\n"
                                        "padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(95, 71, 10);\n"
                                        "}")
        self.accessButton.setObjectName("accessButton")
        self.gridLayout_2.addWidget(self.widget_2, 8, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setMinimumSize(QtCore.QSize(200, 0))
        self.checkBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 7, 1, 1, 1, QtCore.Qt.AlignRight)
        self.loadBox = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadBox.sizePolicy().hasHeightForWidth())
        self.loadBox.setSizePolicy(sizePolicy)
        self.loadBox.setMinimumSize(QtCore.QSize(400, 100))
        self.loadBox.setMaximumSize(QtCore.QSize(400, 100))
        self.loadBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loadBox.setText("")
        self.loadBox.setAlignment(QtCore.Qt.AlignCenter)
        self.loadBox.setWordWrap(True)
        self.loadBox.setOpenExternalLinks(True)
        self.loadBox.setObjectName("loadBox")
        self.gridLayout_2.addWidget(self.loadBox, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        icon1 = QtGui.QIcon('./GUI/language_english_icon.png')

        self.comboBox.addItem(icon1, '')
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('./GUI/language_spanish_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./GUI/language_basque_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, '')
        self.gridLayout_2.addWidget(self.comboBox, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 10, 1, 1, 1)
        self.passwordField = QtWidgets.QLineEdit(self.widget)
        self.passwordField.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordField.sizePolicy().hasHeightForWidth())
        self.passwordField.setSizePolicy(sizePolicy)
        self.passwordField.setMinimumSize(QtCore.QSize(400, 25))
        self.passwordField.setMaximumSize(QtCore.QSize(400, 25))
        self.passwordField.setSizeIncrement(QtCore.QSize(400, 0))
        self.passwordField.setBaseSize(QtCore.QSize(400, 25))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.passwordField.setFont(font)
        self.passwordField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passwordField.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(0, 0, 200);\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    padding-left: 10px;\n"
                                         "    padding-right: 10px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(0, 0, 0);\n"
                                         "}")
        self.passwordField.setText("")
        self.passwordField.setFrame(True)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.passwordField.setDragEnabled(False)
        self.passwordField.setReadOnly(False)
        self.passwordField.setObjectName("passwordField")
        self.gridLayout_2.addWidget(self.passwordField, 6, 1, 1, 1)
        self.usernameField = QtWidgets.QLineEdit(self.widget)
        self.usernameField.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameField.sizePolicy().hasHeightForWidth())
        self.usernameField.setSizePolicy(sizePolicy)
        self.usernameField.setMinimumSize(QtCore.QSize(400, 25))
        self.usernameField.setMaximumSize(QtCore.QSize(400, 25))
        self.usernameField.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        self.usernameField.setFont(font)
        self.usernameField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.usernameField.setAcceptDrops(True)
        self.usernameField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usernameField.setAutoFillBackground(False)
        self.usernameField.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(0, 0, 200);\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    padding-left: 10px;\n"
                                         "    padding-right: 10px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(0, 0, 0);\n"
                                         "}")
        self.usernameField.setText("")
        self.usernameField.setFrame(True)
        self.usernameField.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.usernameField.setReadOnly(False)
        self.usernameField.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.usernameField.setClearButtonEnabled(True)
        self.usernameField.setObjectName("usernameField")
        self.gridLayout_2.addWidget(self.usernameField, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.MainWindow.setCentralWidget(self.centralwidget)

        # define user posible actions
        self.accessButton.clicked.connect(self.acessButton_clicked_or_returnPressed)
        self.passwordField.returnPressed.connect(self.acessButton_clicked_or_returnPressed)
        self.comboBox.currentIndexChanged.connect(self.configChanges)
        self.checkBox.stateChanged.connect(self.configChanges)

        # create load animation widget
        self.movie.start()

        # create error message box
        self.msgBoxDomain.setText(self.config.get('LoginViewSection', 'messageBox_alert_domainError_text'))

        # change view language statements
        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        # change view to saved configuration values
        if self.configGeneral.get('USERINFO', 'usernamesavecheck') == 'true':
            self.usernameField.setText(self.configGeneral.get('USERINFO', 'username'))
            self.checkBox.setCheckState(2)

        for i in range(0, self.comboBox.count()-1):
            self.comboBox.setCurrentIndex(i)
            if self.comboBox.currentText() == self.configGeneral.get('LANGUAGE', 'code'):
                break

    def configChanges(self):

        configFileWriter = ConfigWriter.ConfigWriter()
        if self.comboBox.currentText() == '':
            language = self.configGeneral.get('LANGUAGE', 'code')
        else:
            language = self.comboBox.currentText()

        if self.checkBox.checkState() == 2:
            configFileWriter.configFileWriter('true', self.usernameField.text(), language)
        else:
            configFileWriter.configFileWriter('false', "", language)

        self.config.read('./Languages/AppConfig' + self.comboBox.currentText() + '.cfg')
        self.retranslateUi(self.MainWindow)

    def thread_authentication_correctly(self):
        searchView = QtWidgets.QWidget(self.centralwidget)
        self.GUI.setupUi(searchView, self.thread.connection, self.centralwidget)
        self.widget.close()
        searchView.show()

    def thread_authentication_error(self):
        self.loadBox.clear()
        self.usernameField.setEnabled(True)
        self.passwordField.setEnabled(True)
        self.accessButton.setEnabled(True)
        msgBoxLogin = QMessageBox()
        msgBoxLogin.setText(self.config.get('LoginViewSection', 'messageBox_alert_loginError_text'))
        msgBoxLogin.exec()

    def loadViewThread(self):
        # change login view
        self.loadBox.clear()
        self.loadBox.setMovie(self.movie)
        self.usernameField.setEnabled(False)
        self.passwordField.setEnabled(False)
        self.accessButton.setEnabled(False)

    def acessButton_clicked_or_returnPressed(self):
        # takes values introduced
        self.username = self.usernameField.text()
        self.password = self.passwordField.text()
        self.password = self.password.replace(" ", "")

        data = DomainLogic.username_domain(self.username)
        self.username = data.__getitem__(0)
        loadView = threading.Thread(name="loadViewThread", target=self.loadViewThread)

        # Very Important to not blocked the main thread
        self.thread = LoginAction.LoginAction(self.username, self.password, data.__getitem__(1))
        self.thread.authentication_success.connect(self.thread_authentication_correctly)
        self.thread.authentication_error.connect(self.thread_authentication_error)

        if data.__getitem__(2) is True:
            loadView.start()
            self.thread.start()
        else:
            self.msgBoxDomain.exec()

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpyDocument"))

        # set text of item depending to the selected languages
        self.usernameField.setPlaceholderText(_translate("MainWindow", str(
                                                         self.config.get('LoginViewSection',
                                                                         'usernameField_placeholder_text')).encode('ansi')))
        self.passwordField.setPlaceholderText(_translate("MainWindow", str(
                                                         self.config.get(
                                                             'LoginViewSection',
                                                             'passwordField_placeholder_text')).encode('ansi')))
        self.accessButton.setText(_translate("MainWindow", str(self.config.get('LoginViewSection',
                                                                           'accessButton_text')).encode('ansi')))
        self.checkBox.setText(_translate("MainWindow", str(self.config.get('LoginViewSection',
                                                                           'checkButton_text')).encode('ansi')))
        self.comboBox.setItemText(0, _translate("MainWindow", "EN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ES"))
        self.comboBox.setItemText(2, _translate("MainWindow", "EUS"))
