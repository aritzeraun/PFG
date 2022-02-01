import threading
import urllib
import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox
from Connecttion import scrihub, Connection
from Excel.ExcelFileTreatment import ExcelFileTreatment
from Logic import DomainLogic


class Ui_MainWindow:

    connection = Connection.Connections()

    def __init__(self):
        self.movie = QMovie("./GUI/process.gif")
        self.config = configparser.RawConfigParser()
        self.msgBoxDomain = QMessageBox()
        self.username = ""
        self.password = ""

    def setupUi(self, MainWindow):
        # open language configuration file
        self.config.read('./Languages/AppConfigEN.cfg')

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1064, 792)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./GUI/bitmap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setIconSize(QtCore.QSize(60, 60))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks |
                                  QtWidgets.QMainWindow.AnimatedDocks | QtWidgets.QMainWindow.ForceTabbedDocks |
                                  QtWidgets.QMainWindow.GroupedDragging | QtWidgets.QMainWindow.VerticalTabs)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setStyleSheet("QWidget {\n"
                                  "qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255))\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setObjectName("formLayout")
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
                                         "    padding-right: 10px;}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(0, 0, 0);}")
        self.usernameField.setText("")
        self.usernameField.setFrame(True)
        self.usernameField.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.usernameField.setReadOnly(False)
        self.usernameField.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.usernameField.setClearButtonEnabled(True)
        self.usernameField.setObjectName("usernameField")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.usernameField)
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
                                         "    padding-right: 10px;}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(0, 0, 0);}")
        self.passwordField.setText("")
        self.passwordField.setFrame(True)
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordField.setDragEnabled(False)
        self.passwordField.setReadOnly(False)
        self.passwordField.setObjectName("passwordField")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.passwordField)
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
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.widget_2)
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
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.loadBox)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        # define user posible actions
        self.accessButton.clicked.connect(self.acessButton_clicked_or_returnPressed)
        self.passwordField.returnPressed.connect(self.acessButton_clicked_or_returnPressed)

        # create load animation widget
        self.movie.start()

        # create error message box
        self.msgBoxDomain.setText(self.config.get('LoginViewSection', 'messageBox_alert_domainError_text'))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        loadView = threading.Thread(name="loadViewThread", target=self.loadViewThread)
        requestSender = threading.Thread(name="requestSenderThread", target=self.requestSenderThread, args=(data, ))

        if data.__getitem__(2) is True:
            loadView.start()
            requestSender.start()
        else:
            self.msgBoxDomain.exec()

        # MainWindow = QtWidgets.QWidget(self.centralwidget)
        # GUI = Search.Ui_Form()
        # GUI.setupUi(MainWindow)
        # MainWindow.show()

    def requestSenderThread(self, userTipology):
        self.connection.driverCreator()
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        if not ip == "193.146.227.236":
            self.loginActionSucess = self.connection.loginWebOfScience(self.username, self.password, userTipology.__getitem__(1))
        else:
            self.loginActionSucess = True
        if self.loginActionSucess is False:
            self.loadBox.clear()
            self.usernameField.setEnabled(True)
            self.passwordField.setEnabled(True)
            self.accessButton.setEnabled(True)

            con = configparser.RawConfigParser()
            con.read('./Languages/AppConfigEN.cfg')
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(con.get('LoginViewSection', 'messageBox_alert_loginError_text'))
            msgBoxLogin.exec()
        else:
            filesName = self.connection.dataSearch("web scraping")
            for a in filesName:
                array = ExcelFileTreatment.openFile(self, a)
                for i in array:
                    scrihub.main(i.__getitem__(1))
                    print(i.__getitem__(1))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpyDocument"))

        # set text of item depending to the selected languages
        self.usernameField.setPlaceholderText(_translate("MainWindow",
                                                         self.config.get('LoginViewSection',
                                                                         'usernameField_placeholder_text')))
        self.passwordField.setPlaceholderText(_translate("MainWindow",
                                                         self.config.get(
                                                             'LoginViewSection', 'passwordField_placeholder_text')))
        self.accessButton.setText(_translate("MainWindow", self.config.get('LoginViewSection', 'accessButton_text')))
