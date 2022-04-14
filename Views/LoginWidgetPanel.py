import threading
import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox
from Logic import DomainLogic, LoginAction, ConfigurationFileWriter
from Views import SearchWidgetPanel


class LoginWidgetPanel(object):

    def __init__(self, Form, CentralWidget, MainWindow):

        self.Form = Form
        self.MainWindow = MainWindow
        self.centralWidget = CentralWidget
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.widget = QtWidgets.QWidget(Form)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.buttonWidget = QtWidgets.QWidget(self.widget)
        self.accessButton = QtWidgets.QPushButton(self.buttonWidget)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.loadBox = QtWidgets.QLabel(self.widget)
        self.passwordField = QtWidgets.QLineEdit(self.widget)
        self.usernameField = QtWidgets.QLineEdit(self.widget)

        self.movie = QMovie("./GUI/process.gif")
        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.msgBoxDomain = QMessageBox()
        self.username = ""
        self.password = ""
        self.thread = None
        self.setupUi(self.Form)

    def setupUi(self, Form):
        # open language configuration file
        Form.setObjectName("Form")
        Form.resize(1360, 650)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
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
        self.widget.setObjectName("widget")
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 3)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonWidget.sizePolicy().hasHeightForWidth())
        self.buttonWidget.setSizePolicy(sizePolicy)
        self.buttonWidget.setMinimumSize(QtCore.QSize(400, 40))
        self.buttonWidget.setMaximumSize(QtCore.QSize(400, 40))
        self.buttonWidget.setObjectName("widget_2")
        self.accessButton.setGeometry(QtCore.QRect(130, 10, 111, 28))
        self.accessButton.setAutoFillBackground(False)
        self.accessButton.setStyleSheet("QPushButton {\n"
                                        "border: 2px solid;\n"
                                        " border-radius: 10px;\n"
                                        "    background-color: rgb" + self.secondaryColor + ";\n"
                                        "padding-right: 20px;\n"
                                        "    padding-left: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb" + self.mainColor + ";\n"
                                        "}")
        self.accessButton.setObjectName("accessButton")
        self.gridLayout_2.addWidget(self.buttonWidget, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.checkBox.setMinimumSize(QtCore.QSize(200, 0))
        self.checkBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadBox.sizePolicy().hasHeightForWidth())
        self.loadBox.setSizePolicy(sizePolicy)
        self.loadBox.setMinimumSize(QtCore.QSize(400, 100))
        self.loadBox.setMaximumSize(QtCore.QSize(400, 100))
        self.loadBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.loadBox.setFont(font)
        self.loadBox.setPixmap(QtGui.QPixmap('./Resources/img/recent_projects_icon.png'))
        self.loadBox.setText("")
        self.loadBox.setAlignment(QtCore.Qt.AlignJustify)
        self.loadBox.setWordWrap(True)
        self.loadBox.setOpenExternalLinks(True)
        self.loadBox.setObjectName("loadBox")
        self.gridLayout_2.addWidget(self.loadBox, 8, 0, 1, 1)
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
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.passwordField.setFont(font)
        self.passwordField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passwordField.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb" + self.secondaryColor + ";\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    padding-left: 10px;\n"
                                         "    padding-right: 10px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb" + self.mainColor + ";\n"
                                         "}")
        self.passwordField.setText("")
        self.passwordField.setFrame(True)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.passwordField.setDragEnabled(False)
        self.passwordField.setReadOnly(False)
        self.passwordField.setObjectName("passwordField")
        self.gridLayout_2.addWidget(self.passwordField, 5, 0, 1, 1)
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
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.usernameField.setFont(font)
        self.usernameField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.usernameField.setAcceptDrops(True)
        self.usernameField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usernameField.setAutoFillBackground(False)
        self.usernameField.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb" + self.secondaryColor + ";\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    padding-left: 10px;\n"
                                         "    padding-right: 10px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb" + self.mainColor + ";\n"
                                         "}")
        self.usernameField.setText("")
        self.usernameField.setFrame(True)
        self.usernameField.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.usernameField.setReadOnly(False)
        self.usernameField.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.usernameField.setClearButtonEnabled(True)
        self.usernameField.setObjectName("usernameField")
        self.gridLayout_2.addWidget(self.usernameField, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        # define user possible actions
        self.accessButton.clicked.connect(lambda: self.accessButton_clicked_or_returnPressed())
        self.passwordField.returnPressed.connect(lambda: self.accessButton_clicked_or_returnPressed())
        self.checkBox.stateChanged.connect(lambda: self.configChanges())

        # create load animation widget
        self.loadBox.setText(self.config.get('LoginWidgetPanelSection', 'load_box_initial_text'))
        self.movie.start()

        # create error message box
        self.msgBoxDomain.setText(self.config.get('LoginWidgetPanelSection', 'messageBox_alert_domainError_text'))

        # change view language statements
        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # change view to saved configuration values
        if self.configGeneral.get('USERINFO', 'user_name_save_check') == 'True':
            self.usernameField.setText(self.configGeneral.get('USERINFO', 'username_web_of_science_saved'))
            self.checkBox.setCheckState(2)

    def configChanges(self):

        configFileWriter = ConfigurationFileWriter.ConfigurationFileWriter()
        configFileWriter.writeUserConfiguration(self.checkBox.isChecked(), self.usernameField.text())

    def thread_authentication_correctly(self):
        searchView = QtWidgets.QWidget(self.centralWidget)
        cont = SearchWidgetPanel.SearchWidgetPanel(searchView, self.thread.connection, self.centralWidget,
                                                   self.MainWindow)
        self.MainWindow.gridLayout.addWidget(cont.Form)
        searchView.show()
        self.Form.close()

    def thread_authentication_error(self):
        self.loadBox.clear()
        self.loadBox.setAlignment(QtCore.Qt.AlignJustify)
        self.usernameField.setEnabled(True)
        self.passwordField.setEnabled(True)
        self.accessButton.setEnabled(True)

        msgBoxLogin = QMessageBox()
        msgBoxLogin.setText(self.config.get('LoginWidgetPanelSection', 'messageBox_alert_loginError_text'))
        msgBoxLogin.exec()

    def loadViewThread(self):
        # change login view
        self.loadBox.clear()
        self.loadBox.setAlignment(QtCore.Qt.AlignCenter)
        self.loadBox.setMovie(self.movie)
        self.usernameField.setEnabled(False)
        self.passwordField.setEnabled(False)
        self.accessButton.setEnabled(False)

    def accessButton_clicked_or_returnPressed(self):
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

    def translateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # set text of item depending to the selected languages
        self.usernameField.setPlaceholderText(_translate("MainWindow", str(
                                                         self.config.get('LoginWidgetPanelSection',
                                                                         'usernameField_placeholder_text')).
                                                         encode('ansi')))
        self.passwordField.setPlaceholderText(_translate("MainWindow", str(
                                                         self.config.get(
                                                             'LoginWidgetPanelSection',
                                                             'passwordField_placeholder_text')).encode('ansi')))
        self.accessButton.setText(_translate("MainWindow", str(self.config.get('LoginWidgetPanelSection',
                                                                               'accessButton_text')).encode('ansi')))
        self.checkBox.setText(_translate("MainWindow", str(self.config.get('LoginWidgetPanelSection',
                                                                           'checkButton_text')).encode('ansi')))
