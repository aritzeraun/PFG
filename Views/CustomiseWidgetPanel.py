import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog
from qtwidgets import AnimatedToggle

from Logic import ConfigurationFileWriter


class CustomiseWidgetPanel(object):

    def __init__(self, Form):

        self.Form = Form
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.mainWidget = QtWidgets.QGridLayout()
        self.secondaryColorButton = QtWidgets.QPushButton(Form)
        self.languageLabel = QtWidgets.QLabel(Form)
        self.secondaryColorLabel = QtWidgets.QLabel(Form)
        self.mainColorLabel = QtWidgets.QLabel(Form)
        self.accessibilityLabel = QtWidgets.QLabel(Form)
        self.fontSizeLabel = QtWidgets.QLabel(Form)
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontLabel = QtWidgets.QLabel(Form)
        self.styleLabel = QtWidgets.QLabel(Form)
        self.styleBox = QtWidgets.QComboBox(Form)
        self.languagesComboBox = QtWidgets.QComboBox(Form)
        self.mainColorButton = QtWidgets.QPushButton(Form)
        self.fontSizeBox = QtWidgets.QSpinBox(Form)
        self.themeLabel = QtWidgets.QLabel(Form)
        self.defaultThemeLabel = QtWidgets.QLabel(Form)
        self.themeLine = QtWidgets.QFrame(Form)
        self.accessibilityLine = QtWidgets.QFrame(Form)
        self.defaultAccessibilityLabel = QtWidgets.QLabel(Form)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color').replace('(', '')
        self.mainColor = self.mainColor.replace(')', '')
        self.mainColor = self.mainColor.split(',')
        color = '#'
        for i in range(0, 3):
            if int(self.mainColor[i].replace(' ', '')) < 10:
                color = color + '0' + str(hex(int(self.mainColor[i].replace(' ', ''))))
            else:
                color = color + str(hex(int(self.mainColor[i].replace(' ', ''))))

        color = str(color.replace('0x', ''))
        color_2 = '#44' + color.replace('#', '')
        self.accessibilityToggle = AnimatedToggle(checked_color=str(color), pulse_checked_color=str(color_2))
        self.themeToggle = AnimatedToggle(checked_color=str(color), pulse_checked_color=str(color_2))

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.setupUi(Form)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(813, 815)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout.setContentsMargins(30, -1, 30, 0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.mainWidget.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.mainWidget.setContentsMargins(-1, -1, 30, -1)
        self.mainWidget.setHorizontalSpacing(15)
        self.mainWidget.setVerticalSpacing(20)
        self.mainWidget.setObjectName("mainWidget")
        self.secondaryColorButton.setText("")
        self.secondaryColorButton.setCheckable(False)
        self.secondaryColorButton.setChecked(False)
        self.secondaryColorButton.setObjectName("secondaryColorButton")
        self.mainWidget.addWidget(self.secondaryColorButton, 14, 2, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.languageLabel.setFont(font)
        self.languageLabel.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.languageLabel.setObjectName("languageLabel")
        self.mainWidget.addWidget(self.languageLabel, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(8)
        self.secondaryColorLabel.setFont(font)
        self.secondaryColorLabel.setObjectName("secondaryColorLabel")
        self.mainWidget.addWidget(self.secondaryColorLabel, 14, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainWidget.addItem(spacerItem, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.mainColorLabel.setFont(font)
        self.mainColorLabel.setObjectName("mainColorLabel")
        self.mainWidget.addWidget(self.mainColorLabel, 13, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainWidget.addItem(spacerItem1, 6, 3, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.accessibilityLabel.setFont(font)
        self.accessibilityLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.accessibilityLabel.setObjectName("accessibilityLabel")
        self.mainWidget.addWidget(self.accessibilityLabel, 3, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.fontSizeLabel.setFont(font)
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.mainWidget.addWidget(self.fontSizeLabel, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainWidget.addItem(spacerItem2, 8, 0, 1, 1)
        self.fontComboBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.fontComboBox.setObjectName("fontComboBox")
        self.mainWidget.addWidget(self.fontComboBox, 6, 2, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.fontLabel.setFont(font)
        self.fontLabel.setObjectName("fontLabel")
        self.mainWidget.addWidget(self.fontLabel, 6, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.styleLabel.setFont(font)
        self.styleLabel.setScaledContents(False)
        self.styleLabel.setObjectName("styleLabel")
        self.mainWidget.addWidget(self.styleLabel, 12, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.styleBox.setFont(font)
        self.styleBox.setObjectName("styleBox")
        self.styleBox.addItem("")
        self.styleBox.addItem("")
        self.styleBox.addItem("")
        self.mainWidget.addWidget(self.styleBox, 12, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainWidget.addItem(spacerItem3, 15, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainWidget.addItem(spacerItem4, 2, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.languagesComboBox.setFont(font)
        self.languagesComboBox.setObjectName("languagesComboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('./Resources/img/language_english_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('./Resources/img/language_spanish_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap('./Resources/img/language_basque_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.languagesComboBox.addItem(icon1, "")
        self.languagesComboBox.addItem(icon2, "")
        self.languagesComboBox.addItem(icon3, "")
        self.mainWidget.addWidget(self.languagesComboBox, 1, 2, 1, 1)
        self.mainColorButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainColorButton.setSizeIncrement(QtCore.QSize(100, 0))
        self.mainColorButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainColorButton.setText("")
        self.mainColorButton.setObjectName("mainColorButton")
        self.mainWidget.addWidget(self.mainColorButton, 13, 2, 1, 1)
        self.fontSizeBox.setWrapping(False)
        self.fontSizeBox.setAlignment(QtCore.Qt.AlignCenter)
        self.fontSizeBox.setSuffix("")
        self.fontSizeBox.setMinimum(8)
        self.fontSizeBox.setMaximum(12)
        self.fontSizeBox.setObjectName("fontSizeBox")
        self.mainWidget.addWidget(self.fontSizeBox, 7, 2, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.themeLabel.setFont(font)
        self.themeLabel.setObjectName("themeLabel")
        self.mainWidget.addWidget(self.themeLabel, 9, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.defaultThemeLabel.setFont(font)
        self.defaultThemeLabel.setObjectName("defaultThemeLabel")
        self.mainWidget.addWidget(self.defaultThemeLabel, 10, 0, 1, 1)
        self.themeLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.themeLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.themeLine.setObjectName("themeLine")
        self.mainWidget.addWidget(self.themeLine, 11, 0, 1, 1)
        self.accessibilityLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.accessibilityLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.accessibilityLine.setObjectName("accessibilityLine")
        self.mainWidget.addWidget(self.accessibilityLine, 5, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        self.defaultAccessibilityLabel.setFont(font)
        self.defaultAccessibilityLabel.setObjectName("defaultAccessibilityLabel")
        self.mainWidget.addWidget(self.defaultAccessibilityLabel, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.mainWidget, 0, 0, 1, 1)

        self.mainColorButton.clicked.connect(lambda: self.selectMainColor('Main'))
        self.secondaryColorButton.clicked.connect(lambda: self.selectMainColor('Secondary'))
        self.accessibilityToggle.clicked.connect(lambda: self.setWidgetsEnable('A_changes'))
        self.themeToggle.clicked.connect(lambda: self.setWidgetsEnable('T_changes'))
        self.secondaryColorButton.objectNameChanged.connect(lambda: self.configChanges())
        self.mainColorButton.objectNameChanged.connect(lambda: self.configChanges())
        self.fontSizeBox.valueChanged.connect(lambda: self.configChanges())
        self.fontComboBox.currentIndexChanged.connect(lambda: self.configChanges())
        self.styleBox.currentIndexChanged.connect(lambda: self.configChanges())
        self.languagesComboBox.currentIndexChanged.connect(lambda: self.configChanges())

        self.themeToggle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.mainWidget.addWidget(self.themeToggle, 10, 2, 1, 1)
        self.accessibilityToggle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.mainWidget.addWidget(self.accessibilityToggle, 4, 2, 1, 1)

        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setTabOrder(self.languagesComboBox, self.fontComboBox)
        Form.setTabOrder(self.fontComboBox, self.styleBox)
        Form.setTabOrder(self.styleBox, self.mainColorButton)
        Form.setTabOrder(self.mainColorButton, self.secondaryColorButton)

        self.adaptViewToConfigurationSetting()

    def selectMainColor(self, selectedButton):
        color = QColorDialog.getColor()
        if selectedButton == 'Main':
            self.mainColorButton.setStyleSheet("background-color: rgb" + str(color.getRgb()) + ";")
            self.mainColorButton.setObjectName(str(color.getRgb()))
        elif selectedButton == 'Secondary':
            self.secondaryColorButton.setStyleSheet("background-color: rgb" + str(color.getRgb()) + ";")
            self.secondaryColorButton.setObjectName(str(color.getRgb()))

    def adaptViewToConfigurationSetting(self):

        for i in range(0, self.languagesComboBox.count()-1):
            self.languagesComboBox.setCurrentIndex(i)
            if self.languagesComboBox.currentText() == self.configGeneral.get('SYSTEM', 'language_code'):
                break

        if self.configGeneral.get('SYSTEM', 'accessibility_default') == 'True':
            self.accessibilityToggle.setChecked(True)

        for i in range(0, self.fontComboBox.count()-1):
            self.fontComboBox.setCurrentIndex(i)
            if self.fontComboBox.currentText() == self.configGeneral.get('SYSTEM', 'accessibility_current_font'):
                break

        self.fontSizeBox.setValue(int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size')))

        if self.configGeneral.get('SYSTEM', 'theme_default') == 'True':
            self.themeToggle.setChecked(True)

        for i in range(0, self.styleBox.count()-1):
            self.styleBox.setCurrentIndex(i)
            if self.styleBox.currentText() == self.configGeneral.get('SYSTEM', 'theme_current_style'):
                break

        self.mainColorButton.setStyleSheet("background-color: rgb" +
                                           self.configGeneral.get('SYSTEM', 'theme_current_main_color') + ";")
        self.secondaryColorButton.setStyleSheet("background-color: rgb" +
                                                self.configGeneral.get('SYSTEM', 'theme_current_secondary_color') + ";")

        self.mainColorButton.setObjectName(self.configGeneral.get('SYSTEM', 'theme_current_main_color'))
        self.secondaryColorButton.setObjectName(self.configGeneral.get('SYSTEM', 'theme_current_secondary_color'))

        self.setWidgetsEnable('login')

    def setWidgetsEnable(self, type_action):
        if self.accessibilityToggle.isChecked():
            self.fontComboBox.setEnabled(False)
            self.fontSizeBox.setEnabled(False)

            if type_action == 'A_changes':
                self.fontSizeBox.setValue(int(self.configGeneral.get('SYSTEM', 'accessibility_default_font_size')))

                for i in range(0, self.fontComboBox.count()-1):
                    self.fontComboBox.setCurrentIndex(i)
                    if self.fontComboBox.currentText() == self.configGeneral.get('SYSTEM',
                                                                                 'accessibility_default_font'):
                        break

        elif not self.accessibilityToggle.isChecked():
            self.fontComboBox.setEnabled(True)
            self.fontSizeBox.setEnabled(True)

        if type_action == 'T_changes':

            for i in range(0, self.styleBox.count()-1):
                self.styleBox.setCurrentIndex(i)
                if self.styleBox.currentText() == self.configGeneral.get('SYSTEM', 'theme_default_style'):
                    break

            self.mainColorButton.setStyleSheet("background-color: rgb" +
                                               self.configGeneral.get('SYSTEM', 'theme_default_main_color') + ";")
            self.secondaryColorButton.setStyleSheet("background-color: rgb" +
                                                    self.configGeneral.get('SYSTEM',
                                                                           'theme_default_secondary_color') + ";")

            self.mainColorButton.setObjectName(self.configGeneral.get('SYSTEM', 'theme_default_main_color'))
            self.secondaryColorButton.setObjectName(self.configGeneral.get('SYSTEM', 'theme_default_secondary_color'))

        if self.themeToggle.isChecked():
            self.mainColorButton.setEnabled(False)
            self.secondaryColorButton.setEnabled(False)
            self.styleBox.setEnabled(False)

        elif not self.themeToggle.isChecked():
            self.mainColorButton.setEnabled(True)
            self.secondaryColorButton.setEnabled(True)
            self.styleBox.setEnabled(True)

        self.configChanges()

    def configChanges(self):

        configFileWriter = ConfigurationFileWriter.ConfigWriter()

        configFileWriter.configFileWriter(self.languagesComboBox.currentText(), self.accessibilityToggle.isChecked(),
                                          self.fontComboBox.currentText(), self.fontSizeBox.text(),
                                          self.themeToggle.isChecked(), self.styleBox.currentText(),
                                          self.mainColorButton.objectName(), self.secondaryColorButton.objectName())

    def translateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.languageLabel.setText(_translate("Form", "Language:"))
        self.secondaryColorLabel.setText(_translate("Form", "        Secondary Color:"))
        self.mainColorLabel.setText(_translate("Form", "        Main Color:"))
        self.accessibilityLabel.setText(_translate("Form", "Accessibility:"))
        self.fontSizeLabel.setText(_translate("Form", "        Font Size: "))
        self.fontLabel.setText(_translate("Form", "        Font: "))
        self.styleLabel.setText(_translate("Form", "        Style:"))
        self.styleBox.setItemText(0, _translate("Form", "Fusion"))
        self.styleBox.setItemText(1, _translate("Form", "Windows Vista"))
        self.styleBox.setItemText(2, _translate("Form", "Windows"))
        self.languagesComboBox.setItemText(0, _translate("Form", "EN"))
        self.languagesComboBox.setItemText(1, _translate("Form", "ES"))
        self.languagesComboBox.setItemText(2, _translate("Form", "EUS"))
        self.themeLabel.setText(_translate("Form", "Theme:"))
        self.defaultThemeLabel.setText(_translate("Form", "        Default:"))
        self.defaultAccessibilityLabel.setText(_translate("Form", "        Default:"))
