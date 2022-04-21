import configparser
from PyQt5 import QtCore, QtGui, QtWidgets

from Logic import CreateNewProject, OpenProject, RecentProject


class ProjectWidgetPanel(object):

    def __init__(self, Form, MainWindow):

        self.Form = Form
        self.MainWindow = MainWindow
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.sectionViews = QtWidgets.QWidget(Form)
        self.gridLayout = QtWidgets.QGridLayout(self.sectionViews)
        self.mainWidget = QtWidgets.QGridLayout()
        self.slogan_second_line = QtWidgets.QLabel(self.sectionViews)
        self.slogan_first_line = QtWidgets.QLabel(self.sectionViews)
        self.welcome_label = QtWidgets.QLabel(self.sectionViews)
        self.widget = QtWidgets.QWidget(self.sectionViews)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.openButton = QtWidgets.QPushButton(self.widget)
        self.newProjectButton = QtWidgets.QPushButton(self.widget)
        self.newProjectLabel = QtWidgets.QLabel(self.widget)
        self.openLabel = QtWidgets.QLabel(self.widget)
        self.tableWidget = QtWidgets.QTableWidget(self.sectionViews)
        self.recentProjects_label = QtWidgets.QLabel(self.sectionViews)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        self.recentProjectsDoc = configparser.RawConfigParser()
        self.recentProjectsDoc.read('./Configuration/RecentProjectData.cfg')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color').replace('(', '')
        self.mainColor = self.mainColor.replace(')', '')
        self.mainColor = self.mainColor.split(',')

        self.newProjectName = None
        self.location = None
        self.recentProjectsData = []

        self.setupUi(Form)
        self.readDataFromRecentProjects()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.gridLayout_2.setObjectName("gridLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionViews.sizePolicy().hasHeightForWidth())
        self.sectionViews.setSizePolicy(sizePolicy)
        self.sectionViews.setObjectName("sectionViews")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.mainWidget.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.mainWidget.setObjectName("mainWidget")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainWidget.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainWidget.addItem(spacerItem1, 10, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.slogan_second_line.setFont(font)
        self.slogan_second_line.setAlignment(QtCore.Qt.AlignCenter)
        self.slogan_second_line.setObjectName("slogan_second_line")
        self.mainWidget.addWidget(self.slogan_second_line, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainWidget.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.mainWidget.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.mainWidget.addItem(spacerItem4, 0, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.slogan_first_line.setFont(font)
        self.slogan_first_line.setAlignment(QtCore.Qt.AlignCenter)
        self.slogan_first_line.setObjectName("slogan_first_line")
        self.mainWidget.addWidget(self.slogan_first_line, 3, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 6))
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.mainWidget.addWidget(self.welcome_label, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainWidget.addItem(spacerItem5, 6, 2, 1, 1)
        self.widget.setMinimumSize(QtCore.QSize(0, 120))
        self.widget.setObjectName("widget")
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 4, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        self.openButton.setMinimumSize(QtCore.QSize(80, 80))
        self.openButton.setMaximumSize(QtCore.QSize(100, 100))
        self.openButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.openButton.setStyleSheet("QPushButton {\n"
                                      "    border: 0px solid;\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: rgb" +
                                      self.configGeneral.get('SYSTEM', 'theme_current_secondary_color') + ";\n"
                                      "    padding-right:0px;\n"
                                      "    padding-left: 0px;\n"
                                      "}")
        self.openButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.openButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('./Resources/img/folder_open_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon)
        self.openButton.setIconSize(QtCore.QSize(80, 80))
        self.openButton.setObjectName("openButton")
        self.gridLayout_3.addWidget(self.openButton, 0, 3, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newProjectButton.sizePolicy().hasHeightForWidth())
        self.newProjectButton.setSizePolicy(sizePolicy)
        self.newProjectButton.setMinimumSize(QtCore.QSize(80, 80))
        self.newProjectButton.setMaximumSize(QtCore.QSize(100, 100))
        self.newProjectButton.setSizeIncrement(QtCore.QSize(80, 100))
        self.newProjectButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.newProjectButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.newProjectButton.setAcceptDrops(False)
        self.newProjectButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newProjectButton.setStyleSheet("QPushButton {\n"
                                            "    border: 0px solid;\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: rgb" +
                                            self.configGeneral.get('SYSTEM', 'theme_current_main_color') + ";\n"
                                            "    padding-right:0px;\n"
                                            "    padding-left: 0px;\n"
                                            "}")
        self.newProjectButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('./Resources/img/new_project_icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newProjectButton.setIcon(icon1)
        self.newProjectButton.setIconSize(QtCore.QSize(50, 50))
        self.newProjectButton.setFlat(False)
        self.newProjectButton.setObjectName("newProjectButton")
        self.gridLayout_3.addWidget(self.newProjectButton, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 2, 1, 1)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize))
        self.newProjectLabel.setFont(font)
        self.newProjectLabel.setObjectName("newProjectLabel")
        self.gridLayout_3.addWidget(self.newProjectLabel, 1, 1, 1, 1)
        self.openLabel.setFont(font)
        self.openLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.openLabel.setObjectName("openLabel")
        self.gridLayout_3.addWidget(self.openLabel, 1, 3, 1, 1)
        self.mainWidget.addWidget(self.widget, 6, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 200))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(17)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item1 = QtWidgets.QTableWidgetItem()
        item2 = QtWidgets.QTableWidgetItem()
        item3 = QtWidgets.QTableWidgetItem()
        item1.setTextAlignment(QtCore.Qt.AlignCenter)
        item2.setTextAlignment(QtCore.Qt.AlignCenter)
        item3.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        item1.setFont(font)
        item2.setFont(font)
        item3.setFont(font)
        item1.setBackground(QtGui.QColor(int(self.mainColor[0]), int(self.mainColor[1]), int(self.mainColor[2])))
        item2.setBackground(QtGui.QColor(int(self.mainColor[0]), int(self.mainColor[1]), int(self.mainColor[2])))
        item3.setBackground(QtGui.QColor(int(self.mainColor[0]), int(self.mainColor[1]), int(self.mainColor[2])))
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setHorizontalHeaderItem(1, item2)
        self.tableWidget.setHorizontalHeaderItem(2, item3)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.mainWidget.addWidget(self.tableWidget, 9, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.mainWidget.addItem(spacerItem9, 7, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainWidget.addItem(spacerItem10, 9, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainWidget.addItem(spacerItem11, 9, 0, 1, 1)
        self.recentProjects_label.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPointSize(int(self.fontSize + 1))
        self.recentProjects_label.setFont(font)
        self.recentProjects_label.setText("")
        self.recentProjects_label.setPixmap(QtGui.QPixmap('./Resources/img/recent_projects_icon.png'))
        self.recentProjects_label.setScaledContents(True)
        self.recentProjects_label.setObjectName("recentProjects_label")
        self.mainWidget.addWidget(self.recentProjects_label, 8, 1, 1, 1)
        self.gridLayout.addLayout(self.mainWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.sectionViews, 0, 0, 1, 1)

        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

        # define users possible actions
        self.newProjectButton.clicked.connect(lambda: self.createNewProject())
        self.openButton.clicked.connect(lambda: self.openProject())
        self.tableWidget.cellClicked.connect(self.changeItemState)

    def readDataFromRecentProjects(self):

        if int(self.recentProjectsDoc.get('RECENT_PROJECT', 'accessible_project_number')) > 0:

            self.tableWidget.setRowCount(int(self.recentProjectsDoc.get('RECENT_PROJECT', 'accessible_project_number')))

            for i in range(1, 6):
                try:
                    projectName = self.recentProjectsDoc.get('RECENT_PROJECT', 'project_name_' + str(i))
                    projectLastAccess = self.recentProjectsDoc.get('RECENT_PROJECT', 'project_access_' + str(i))
                    projectLocation = self.recentProjectsDoc.get('RECENT_PROJECT', 'project_location_' + str(i))
                except Exception:
                    break

                itemProjectName = QtWidgets.QTableWidgetItem(projectName)
                itemProjectName.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(int(i-1), 0, itemProjectName)

                itemAccess = QtWidgets.QTableWidgetItem(projectLastAccess)
                itemAccess.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(int(i-1), 1, itemAccess)

                itemLocation = QtWidgets.QTableWidgetItem(projectLocation)
                itemLocation.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(int(i-1), 2, itemLocation)

                projectData = [projectName, projectLastAccess, projectLocation]
                self.recentProjectsData.append(projectData)

        else:
            self.tableWidget.setVisible(False)
            self.recentProjects_label.setVisible(False)

    def openProject(self):
        OpenProject.openProject(self.recentProjectsData, self.MainWindow,
                                self.config.get('ProjectWidgetPanelSection',
                                                'open_project_QFileDialog_title'))

    def changeItemState(self, row):
        recentProject = self.recentProjectsData.pop(row)
        RecentProject.RecentProject(recentProject, self.MainWindow, self.recentProjectsData,
                                    self.config.get('ProjectWidgetPanelSection',
                                                    'messageBox_project_directory_not_found_message'))

    def createNewProject(self):
        CreateNewProject.createNewProject(self.recentProjectsData, self.MainWindow,
                                          self.config.get('ProjectWidgetPanelSection',
                                                          'messageBox_project_already_exists_message'))

    def translateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.slogan_second_line.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                                               'app_slogan_second_line_label_text'))
                                                   .encode('ansi')))
        self.slogan_first_line.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                                              'app_slogan_first_line_label_text'))
                                                  .encode('ansi')))
        self.welcome_label.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                                          'welcome_label_text')).encode('ansi')))
        self.newProjectLabel.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                                            'new_project_label_text')).encode('ansi')))
        self.openLabel.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                                      'open_project_label_text')).encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                            'recent_project_table_item_one')).encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                            'recent_project_table_item_two')).encode('ansi')))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", str(self.config.get('ProjectWidgetPanelSection',
                                                            'recent_project_table_item_three')).encode('ansi')))
