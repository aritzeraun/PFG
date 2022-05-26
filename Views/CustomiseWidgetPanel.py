import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog
from qtwidgets import AnimatedToggle

from Logic import ConfigurationFileWriter


class CustomiseWidgetPanel(object):

    def __init__(self, Form, central, MainWindow):

        self.MainWindow = MainWindow
        self.central = central
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
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')
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
        self.state = 'init'
        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
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
        font.setPointSize(int(self.fontSize + 1))
        font.setBold(True)
        font.setWeight(75)
        self.languageLabel.setFont(font)
        self.languageLabel.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.languageLabel.setObjectName("languageLabel")
        self.mainWidget.addWidget(self.languageLabel, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.secondaryColorLabel.setFont(font)
        self.secondaryColorLabel.setObjectName("secondaryColorLabel")
        self.mainWidget.addWidget(self.secondaryColorLabel, 14, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainWidget.addItem(spacerItem, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.mainColorLabel.setFont(font)
        self.mainColorLabel.setObjectName("mainColorLabel")
        self.mainWidget.addWidget(self.mainColorLabel, 13, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainWidget.addItem(spacerItem1, 6, 3, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        font.setBold(True)
        font.setWeight(75)
        self.accessibilityLabel.setFont(font)
        self.accessibilityLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.accessibilityLabel.setObjectName("accessibilityLabel")
        self.mainWidget.addWidget(self.accessibilityLabel, 3, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
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
        font.setPointSize(int(self.fontSize))
        self.fontLabel.setFont(font)
        font.setPointSize(int(self.fontSize))
        self.fontLabel.setObjectName("fontLabel")
        self.mainWidget.addWidget(self.fontLabel, 6, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.styleLabel.setFont(font)
        self.styleLabel.setScaledContents(False)
        self.styleLabel.setObjectName("styleLabel")
        self.mainWidget.addWidget(self.styleLabel, 12, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
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
        font.setPointSize(int(self.fontSize))
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
        font.setPointSize(int(self.fontSize + 1))
        font.setBold(True)
        font.setWeight(75)
        self.themeLabel.setFont(font)
        self.themeLabel.setObjectName("themeLabel")
        self.mainWidget.addWidget(self.themeLabel, 9, 0, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
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
        font.setPointSize(int(self.fontSize))
        self.defaultAccessibilityLabel.setFont(font)
        self.defaultAccessibilityLabel.setObjectName("defaultAccessibilityLabel")
        self.mainWidget.addWidget(self.defaultAccessibilityLabel, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.mainWidget, 0, 0, 1, 1)

        self.translateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.adaptViewToConfigurationSetting()

        # here are defined the functions of the widgets added
        self.mainColorButton.clicked.connect(lambda: self.selectMainColor('Main'))
        self.secondaryColorButton.clicked.connect(lambda: self.selectMainColor('Secondary'))
        self.accessibilityToggle.clicked.connect(lambda: self.setWidgetsEnable('A_changes'))
        self.themeToggle.clicked.connect(lambda: self.setWidgetsEnable('T_changes'))
        self.secondaryColorButton.clicked.connect(lambda: self.configChanges())
        self.mainColorButton.clicked.connect(lambda: self.configChanges())
        self.fontSizeBox.valueChanged.connect(lambda: self.configChanges())
        self.fontComboBox.activated.connect(lambda: self.configChanges())
        self.styleBox.activated.connect(lambda: self.configChanges())
        self.languagesComboBox.currentTextChanged.connect(lambda: self.configChanges())

        # Toggle definitions
        self.themeToggle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.mainWidget.addWidget(self.themeToggle, 10, 2, 1, 1)
        self.accessibilityToggle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.mainWidget.addWidget(self.accessibilityToggle, 4, 2, 1, 1)

        # Defines TAB position between different widgets
        Form.setTabOrder(self.languagesComboBox, self.fontComboBox)
        Form.setTabOrder(self.fontComboBox, self.styleBox)
        Form.setTabOrder(self.styleBox, self.mainColorButton)
        Form.setTabOrder(self.mainColorButton, self.secondaryColorButton)

    def selectMainColor(self, selectedButton):
        color = QColorDialog.getColor()
        if selectedButton == 'Main':
            self.mainColorButton.setStyleSheet("background-color: rgb" + str(color.getRgb()) + ";")
            self.mainColorButton.setObjectName(str(color.getRgb()))
        elif selectedButton == 'Secondary':
            self.secondaryColorButton.setStyleSheet("background-color: rgb" + str(color.getRgb()) + ";")
            self.secondaryColorButton.setObjectName(str(color.getRgb()))

    def adaptViewToConfigurationSetting(self):

        self.MainWindow.translateUi()
        if self.configGeneral.get('SYSTEM', 'language_code') == 'EN':
            self.languagesComboBox.setCurrentIndex(0)
        elif self.configGeneral.get('SYSTEM', 'language_code') == 'ES':
            self.languagesComboBox.setCurrentIndex(1)
        elif self.configGeneral.get('SYSTEM', 'language_code') == 'EUS':
            self.languagesComboBox.setCurrentIndex(2)

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

        configFileWriter = ConfigurationFileWriter.ConfigurationFileWriter()
        configFileWriter.configFileWriter(self.languagesComboBox.currentText(), self.accessibilityToggle.isChecked(),
                                          self.fontComboBox.currentText(), self.fontSizeBox.text(),
                                          self.themeToggle.isChecked(), self.styleBox.currentText(),
                                          self.mainColorButton.objectName(), self.secondaryColorButton.objectName())

        if self.state != 'init':

            CustomiseView = QtWidgets.QWidget(self.central)
            self.MainWindow.horizontalLayout.addWidget(CustomiseView)
            customiseViewController = CustomiseWidgetPanel(CustomiseView, self.central, self.MainWindow)
            self.MainWindow.sectionViews.close()
            self.MainWindow.sectionViews = customiseViewController.Form

            # changes y de Option Column of Welcome View

            self.MainWindow.projectOptionButton.setStyleSheet("background-color: rgb" +
                                                              self.secondaryColorButton.objectName() +
                                                              "; border: none;")
            self.MainWindow.customiseOptionButton.setStyleSheet("background-color: rgb" +
                                                                self.mainColorButton.objectName() + "; border: none;")
            self.MainWindow.licenseOptionButton.setStyleSheet("background-color: rgb" +
                                                              self.secondaryColorButton.objectName() +
                                                              "; border: none;")
            self.MainWindow.optionsWidget.setStyleSheet("background-color: rgb" +
                                                        self.secondaryColorButton.objectName() + "; border: none;")

            self.MainWindow.mainColor = self.mainColorButton.objectName()
            self.MainWindow.secondaryColor = self.secondaryColorButton.objectName()

            # font changes

            font = QtGui.QFont()
            font.setFamily(self.fontComboBox.currentText())
            font.setPointSize(int(int(self.fontSizeBox.text()) + 1))
            self.MainWindow.projectOptionButton.setFont(font)
            self.MainWindow.customiseOptionButton.setFont(font)
            self.MainWindow.licenseOptionButton.setFont(font)

        self.state = 'second'

    def translateUi(self, Form):

        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.languageLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                          'language_label_text')).encode('ansi')))
        self.secondaryColorLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                                'secondary_color_label_text'))
                                                    .encode('ansi')))
        self.mainColorLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                           'main_color_label_text')).encode('ansi')))
        self.accessibilityLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                               'accessibility_label_text'))
                                                   .encode('ansi')))
        self.fontSizeLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                          'font_size_label_text')).encode('ansi')))
        self.fontLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                      'font_label_text')).encode('ansi')))
        self.styleLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                       'style_label_text')).encode('ansi')))
        self.styleBox.setItemText(0, _translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                            'style_box_option_1')).encode('ansi')))
        self.styleBox.setItemText(1, _translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                            'style_box_option_2')).encode('ansi')))
        self.styleBox.setItemText(2, _translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                            'style_box_option_3')).encode('ansi')))
        self.languagesComboBox.setItemText(0, _translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                                     'language_box_option_1'))
                                                         .encode('ansi')))
        self.languagesComboBox.setItemText(1, _translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                                     'language_box_option_2'))
                                                         .encode('ansi')))
        self.languagesComboBox.setItemText(2, _translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                                     'language_box_option_3'))
                                                         .encode('ansi')))
        self.themeLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                       'theme_label_text')).encode('ansi')))
        self.defaultThemeLabel.setText(_translate("Form", str(self.config.get('CustomiseWidgetPanelSection',
                                                                              'theme_default_toggle_text'))
                                                  .encode('ansi')))
        self.defaultAccessibilityLabel.setText(_translate("Form",
                                                          str(self.config.get('CustomiseWidgetPanelSection',
                                                                              'accessibility_default_toggle_text'))
                                                          .encode('ansi')))
