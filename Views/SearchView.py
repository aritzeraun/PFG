import null
import configparser
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Logic import SearchAction
from Views import ResultView


class Ui_Form(object):

    def __init__(self):
        self.GUI = ResultView.Ui_Form()
        self.connection = null
        self.config = configparser.RawConfigParser()

    def setupUi(self, Form, connection, central):

        self.centralwidget = central
        self.connection = connection
        # open language configuration file
        self.config.read('./Languages/AppConfigEN.cfg')

        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(747, 569)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, -10, 751, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.pushButton.clicked.connect(self.search_data)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def thread_search_correctly(self):

        resultView = QtWidgets.QWidget(self.centralwidget)
        self.GUI.setupUi(resultView, self.thread.filesName)
        print(222)
        resultView.show()
        print(111)

    def thread_search_error(self):
        msgBoxLogin = QMessageBox()
        msgBoxLogin.setText('messageBox_alert_loginError_text')
        msgBoxLogin.exec()

    def search_data(self):
        self.thread = SearchAction.SearchAction(self.connection, self.lineEdit.text())
        self.thread.search_success.connect(self.thread_search_correctly)
        self.thread.search_error.connect(self.thread_search_error)

        self.thread.start()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", self.config.get('SearchViewSection',
                                                                            'search_topic_placeholder_text')))
        self.comboBox.setItemText(0, _translate("Form", self.config.get('SearchViewSection',
                                                                        'search_option_way_0')))
        self.comboBox.setItemText(1, _translate("Form", self.config.get('SearchViewSection',
                                                                        'search_option_way_1')))
        self.comboBox.setItemText(2, _translate("Form", self.config.get('SearchViewSection',
                                                                        'search_option_way_2')))
        self.pushButton.setText(_translate("Form",self.config.get('SearchViewSection',
                                                                  'searchButton_text')))
