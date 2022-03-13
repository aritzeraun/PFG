import configparser
import threading
from PyQt5.QtCore import Qt
from Connecttion import scrihub
from PyQt5 import QtCore, QtGui, QtWidgets
import Excel.ExcelFileTreatment


class Ui_Form(object):

    def __init__(self):
        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Languages/AppConfigGeneral.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('LANGUAGE', 'code') + '.cfg')

    def setupUi(self, Form, filesName):

        self.filesName = filesName
        self.estadoSeleccion = Qt.CheckState.Unchecked

        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(694, 647)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./GUI/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 1)
        self.downloadButton = QtWidgets.QPushButton(self.frame)
        self.downloadButton.setObjectName("downloadButton")
        self.gridLayout_2.addWidget(self.downloadButton, 0, 2, 1, 1)
        self.timeBox = QtWidgets.QSpinBox(self.frame)
        self.timeBox.setObjectName("timeBox")
        self.timeBox.setValue(2)
        self.gridLayout_2.addWidget(self.timeBox, 0, 3, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 5, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.tableWidget.horizontalHeader().sectionPressed.connect(self.changeAllItemState)
        self.tableWidget.cellClicked.connect(self.changeItemState)
        # self.downloadButton.click.connect(self.downloadAction)
        self.search_data()

    def changeAllItemState(self, index):

        number = self.tableWidget.rowCount()

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
        icon = QtGui.QIcon()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)

        if index == 3:

            if self.estadoSeleccion == Qt.CheckState.Unchecked or self.estadoSeleccion == Qt.CheckState.PartiallyChecked:
                self.estadoSeleccion = Qt.CheckState.Checked
                icon.addPixmap(QtGui.QPixmap("./GUI/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                self.tableWidget.setHorizontalHeaderItem(3, item)

            else:
                self.estadoSeleccion = Qt.CheckState.Unchecked
                icon.addPixmap(QtGui.QPixmap("./GUI/unchecked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                self.tableWidget.setHorizontalHeaderItem(3, item)

        for i in range(0, number):
            self.tableWidget.item(i, 3).setCheckState(self.estadoSeleccion)

    def changeItemState(self, row, column):

        if column == 3:
            if self.tableWidget.item(row, column).checkState() == Qt.CheckState.Unchecked:
                self.tableWidget.item(row, column).setCheckState(Qt.CheckState.Checked)
            else:
                self.tableWidget.item(row, column).setCheckState(Qt.CheckState.Unchecked)

        number = self.tableWidget.rowCount()
        numberOfCoincidence = 0

        for i in range(0, number):
            if self.tableWidget.item(i, column).checkState() == Qt.CheckState.Checked:
                numberOfCoincidence = numberOfCoincidence + 1

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
        icon = QtGui.QIcon()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)

        if numberOfCoincidence == number:
            self.estadoSeleccion = Qt.CheckState.Checked
            icon.addPixmap(QtGui.QPixmap("./GUI/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.tableWidget.setHorizontalHeaderItem(3, item)

        elif number > numberOfCoincidence > 0:
            self.estadoSeleccion = Qt.CheckState.PartiallyChecked
            icon.addPixmap(QtGui.QPixmap("./GUI/intermediate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.tableWidget.setHorizontalHeaderItem(3, item)
        elif numberOfCoincidence == 0:
            self.estadoSeleccion = Qt.CheckState.Unchecked
            icon.addPixmap(QtGui.QPixmap("./GUI/unchecked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.tableWidget.setHorizontalHeaderItem(3, item)

    def downloadAction(self):
        # scihub_controller = scrihub.main()
        print(1)

    def chargeData(self):

        dataOfDocuments = Excel.ExcelFileTreatment.openFile(self.filesName)
        self.tableWidget.setRowCount(len(dataOfDocuments))
        rowNumber = 0
        for iterator in dataOfDocuments:

            self.tableWidget.setItem(rowNumber, 0, QtWidgets.QTableWidgetItem(iterator.__getitem__(0)))
            self.tableWidget.setItem(rowNumber, 1, QtWidgets.QTableWidgetItem(iterator.__getitem__(1)))
            self.tableWidget.setItem(rowNumber, 2, QtWidgets.QTableWidgetItem(iterator.__getitem__(2)))

            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Checked)
            self.tableWidget.setItem(rowNumber, 3, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignBottom)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./GUI/correct.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.tableWidget.setItem(rowNumber, 4, item)

            rowNumber = rowNumber + 1

    def search_data(self):
        loadView = threading.Thread(name="loadViewThread", target=self.chargeData)
        loadView.start()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Author"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "DOI"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("Form", "Downloaded"))
        self.downloadButton.setText(_translate("Form", str(self.config.get('ResultViewSection',
                                                                           'downloadButton_text')).encode('ansi')))
        self.toolButton.setText(_translate("Form", "..."))