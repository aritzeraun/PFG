import configparser
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Logic import CreateNewProject, OpenProject, RecentProject, RenameProject, ChangeLocation, RecentProjectFileWriter
from Views import LoginWidgetPanel, LicenseWidgetPanel, DockWidgetPanel, WelcomeView


class ApplicationView:

    def __init__(self, MainWindow, recentProjectsData, ProjectDirectory, ProjectName):

        self.MainWindow = MainWindow
        self.recentProjectsData = recentProjectsData
        self.projectDirectory = ProjectDirectory
        self.projectName = ProjectName

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuProject = QtWidgets.QMenu(self.menuBar)
        self.menuOpen_Recent = QtWidgets.QMenu(self.menuProject)
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuLanguage = QtWidgets.QMenu(self.menuSettings)
        self.menuProject_2 = QtWidgets.QMenu(self.menuBar)
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuViews = QtWidgets.QMenu(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionProgressView = QtWidgets.QAction(MainWindow)
        self.actionStatus_View = QtWidgets.QAction(MainWindow)
        self.actionClose_Project = QtWidgets.QAction(MainWindow)
        self.actionDelete_Project = QtWidgets.QAction(MainWindow)
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionChange_Location = QtWidgets.QAction(MainWindow)
        self.actionEN = QtWidgets.QAction(MainWindow)
        self.actionES = QtWidgets.QAction(MainWindow)
        self.actionEUS = QtWidgets.QAction(MainWindow)
        self.actionProgress_View = QtWidgets.QAction(MainWindow)

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')
        self.config = configparser.RawConfigParser()
        self.config.read('./Languages/AppConfig' + self.configGeneral.get('SYSTEM', 'language_code') + '.cfg')
        self.recentProjectsDoc = configparser.RawConfigParser()
        self.recentProjectsDoc.read('./Configuration/RecentProjectData.cfg')

        self.font = self.configGeneral.get('SYSTEM', 'accessibility_current_font')
        self.fontSize = int(self.configGeneral.get('SYSTEM', 'accessibility_current_font_size'))
        self.mainColor = self.configGeneral.get('SYSTEM', 'theme_current_main_color')
        self.secondaryColor = self.configGeneral.get('SYSTEM', 'theme_current_secondary_color')

        self.visibleForm = None
        self.setupUi(self.MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 889)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout.setObjectName("gridLayout")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuProject.setObjectName("menuProject")
        self.menuOpen_Recent.setObjectName("menuOpen_Recent")
        self.menuSettings.setObjectName("menuSettings")
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuProject_2.setObjectName("menuProject_2")
        self.menuHelp.setObjectName("menuHelp")
        self.menuViews.setObjectName("menuViews")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionNew_Project.setObjectName("actionNew_Project")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("deusto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit.setObjectName("actionExit")
        self.actionLicense.setObjectName("actionLicense")
        self.actionProgressView.setCheckable(True)
        self.actionProgressView.setChecked(True)
        self.actionProgressView.setObjectName("actionProgressView")
        self.actionStatus_View.setObjectName("actionStatus_View")
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.actionDelete_Project.setObjectName("actionDelete_Project")
        self.actionRename.setObjectName("actionRename")
        self.actionChange_Location.setObjectName("actionChange_Location")
        self.actionEN.setObjectName("actionEN")
        self.actionES.setObjectName("actionES")
        self.actionEUS.setObjectName("actionEUS")
        self.actionProgress_View.setCheckable(True)
        self.actionProgress_View.setChecked(True)
        self.actionProgress_View.setObjectName("actionProgress_View")
        self.menuOpen_Recent.addSeparator()

        self.menuProject.addAction(self.actionNew_Project)
        self.menuProject.addAction(self.actionOpen)
        self.menuProject.addAction(self.menuOpen_Recent.menuAction())
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuLanguage.addAction(self.actionEN)
        self.menuLanguage.addAction(self.actionES)
        self.menuLanguage.addAction(self.actionEUS)
        self.menuSettings.addAction(self.menuLanguage.menuAction())
        self.menuSettings.addAction(self.actionLicense)
        self.menuProject_2.addAction(self.actionChange_Location)
        self.menuProject_2.addAction(self.actionRename)
        self.menuProject_2.addSeparator()
        self.menuProject_2.addAction(self.actionClose_Project)
        self.menuProject_2.addAction(self.actionDelete_Project)
        self.menuViews.addAction(self.actionProgress_View)
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuProject_2.menuAction())
        self.menuBar.addAction(self.menuViews.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.actionExit.triggered.connect(lambda: self._actionExit())
        self.actionNew_Project.triggered.connect(lambda: self._createNewProject())
        self.actionOpen.triggered.connect(lambda: self._openProject())
        self.actionProgress_View.triggered.connect(lambda: self.putDockVisible())
        self.actionLicense.triggered.connect(lambda: self._showLicenseView())
        self.actionRename.triggered.connect(lambda: self._renameProject())
        self.actionChange_Location.triggered.connect(lambda: self._changeLocation())
        self.actionDelete_Project.triggered.connect(lambda: self._deleteProject())
        self.actionClose_Project.triggered.connect(lambda: self._closeProject())

        self.actionExit.setShortcut("Ctrl+N")
        self.controller = DockWidgetPanel.DockWidgetPanel(QtWidgets.QWidget(), self.centralWidget, self,
                                                     self.projectDirectory)
        self.dockWidget.setWidget(self.controller.Form)

        self.translateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self._setRecentProjectName()
        self.menuHelp.addAction(self._showHelpMessage())

    def _deleteProject(self):
        print(self.projectDirectory)
        try:
            shutil.rmtree(self.projectDirectory + '/')
            recentProject = self.recentProjectsData.pop(0)
            controller = RecentProjectFileWriter.RecentProjectFileWriter()
            controller.RecentProjectFileWriter(recentProject[0], recentProject[1], recentProject[2],
                                               self.recentProjectsData)
            self._closeProject()
        except Exception as e:
            print(e)

    def _closeProject(self):
        MainWindow = QtWidgets.QMainWindow()
        WelcomeView.WelcomeView(MainWindow, 1)
        MainWindow.show()
        self.MainWindow.close()

    def _actionExit(self):
        self.MainWindow.close()

    def putDockVisible(self):

        if self.actionProgress_View.isChecked() and not self.dockWidget.isVisible():
            self.dockWidget = QtWidgets.QDockWidget(self.MainWindow)
            self.dockWidget.setObjectName("dockWidget")
            controller = DockWidgetPanel.DockWidgetPanel(QtWidgets.QWidget(), self.centralWidget, self,
                                                         self.projectDirectory)
            self.dockWidget.setWidget(controller.Form)
            self.MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        elif not self.actionProgress_View.isChecked() and not self.dockWidget.isVisible():
            self.dockWidget = QtWidgets.QDockWidget(self.MainWindow)
            self.dockWidget.setObjectName("dockWidget")
            controller = DockWidgetPanel.DockWidgetPanel(QtWidgets.QWidget(), self.centralWidget, self,
                                                         self.projectDirectory)
            self.dockWidget.setWidget(controller.Form)
            self.MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
            self.actionProgress_View.setChecked(True)

        else:
            self.dockWidget.close()

    def _showHelpMessage(self):
        _translate = QtCore.QCoreApplication.translate
        msgBoxLogin = QMessageBox()
        msgBoxLogin.setText(_translate("MainWindow", str(self.config.get('ApplicationViewSection',
                                                                         'messageBox_help_text')).encode('ansi')))
        # msgBoxLogin.setAlignment(Qt.AlignJustify)
        msgBoxLogin.exec()

    def _showLicenseView(self):

        if isinstance(self.visibleForm, LicenseWidgetPanel.LicenseWidgetPanel):
            LicenseView = QtWidgets.QWidget(self.centralWidget)
            LoginWidgetPanel.LoginWidgetPanel(LicenseView, self.centralWidget, self)
            self.gridLayout.addWidget(LicenseView)
            self.visibleForm.Form.close()
            self.visibleForm = LicenseView
        else:
            LicenseView = QtWidgets.QWidget(self.centralWidget)
            controller = LicenseWidgetPanel.LicenseWidgetPanel(LicenseView)
            self.gridLayout.addWidget(controller.Form)
            LicenseView.show()
            self.visibleForm.close()
            self.visibleForm = controller

    def _setRecentProjectName(self):

        if len(self.recentProjectsData) >= 1:
            self.actionProject_1 = QtWidgets.QAction(self.MainWindow)
            self.actionProject_1.setObjectName("actionProject_1")
            project = self.recentProjectsData[0]
            self.actionProject_1.setText(str(project[0]))
            self.menuOpen_Recent.addAction(self.actionProject_1)
            self.actionProject_1.triggered.connect(lambda: self._goToRecentProject(self.actionProject_1.text()))
        if len(self.recentProjectsData) >= 2:
            self.actionProject_2 = QtWidgets.QAction(self.MainWindow)
            self.actionProject_2.setObjectName("actionProject_2")
            project = self.recentProjectsData[1]
            self.actionProject_2.setText(str(project[0]))
            self.menuOpen_Recent.addAction(self.actionProject_2)
            self.actionProject_2.triggered.connect(lambda: self._goToRecentProject(self.actionProject_2.text()))
        if len(self.recentProjectsData) >= 3:
            self.actionProject_3 = QtWidgets.QAction(self.MainWindow)
            self.actionProject_3.setObjectName("actionProject_3")
            project = self.recentProjectsData[2]
            self.actionProject_3.setText(str(project[0]))
            self.menuOpen_Recent.addAction(self.actionProject_3)
            self.actionProject_3.triggered.connect(lambda: self._goToRecentProject(self.actionProject_3.text()))
        if len(self.recentProjectsData) >= 4:
            self.actionProject_4 = QtWidgets.QAction(self.MainWindow)
            self.actionProject_4.setObjectName("actionProject_4")
            project = self.recentProjectsData[3]
            self.actionProject_4.setText(str(project[0]))
            self.menuOpen_Recent.addAction(self.actionProject_4)
            self.actionProject_4.triggered.connect(lambda: self._goToRecentProject(self.actionProject_4.text()))

    def _createNewProject(self):
        self._actualiseRecentProjects()
        self.dockWidget.close()
        CreateNewProject.createNewProject(self.recentProjectsData, self.MainWindow,
                                          self.config.get('ApplicationViewSection',
                                                          'messageBox_project_already_exists_message'))

    def _goToRecentProject(self, projectName):

        self._actualiseRecentProjects()
        self.dockWidget.close()

        position = 0
        recentProjectFound = False

        for project in self.recentProjectsData:
            if project[0] == projectName:
                recentProjectFound = True
                recentProject = self.recentProjectsData.pop(position)
                RecentProject.RecentProject(recentProject, self.MainWindow, self.recentProjectsData,
                                            self.config.get('ApplicationViewSection',
                                                            'messageBox_project_directory_not_found_message'))
                break
            position = position + 1

        if not recentProjectFound:
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(self.config.get('ApplicationViewSection', 'messageBox_alert_loginError_text'))
            msgBoxLogin.exec()

    def _openProject(self):
        self._actualiseRecentProjects()
        self.dockWidget.close()
        OpenProject.openProject(self.recentProjectsData, self.MainWindow,
                                self.config.get('ApplicationViewSection',
                                                'open_project_QFileDialog_title'))

    def _changeLocation(self):
        self._actualiseRecentProjects()
        ChangeLocation.changeProjectLocation(self.recentProjectsData, self,
                                             self.config.get('ApplicationViewSection',
                                                             'messageBox_successfully_folder_change_text'),
                                             self.config.get('ApplicationViewSection',
                                                             'messageBox_error_folder_change_text'))

    def _renameProject(self):
        self._actualiseRecentProjects()
        RenameProject.renameProject(self.recentProjectsData, self, "fff", "aa")

        print(self.projectName)
        self.MainWindow.setWindowTitle(str(self.projectName))

    def _actualiseRecentProjects(self):

        recentProjects = []
        if int(self.recentProjectsDoc.get('RECENT_PROJECT', 'accessible_project_number')) > 0:
            for i in range(1, 6):
                try:
                    projectName = self.recentProjectsDoc.get('RECENT_PROJECT', 'project_name_' + str(i))
                    projectLastAccess = self.recentProjectsDoc.get('RECENT_PROJECT', 'project_access_' + str(i))
                    projectLocation = self.recentProjectsDoc.get('RECENT_PROJECT', 'project_location_' + str(i))
                except Exception:
                    break
                project = [projectName, projectLastAccess, projectLocation]
                recentProjects.append(project)
        self.recentProjectsData = recentProjects

    def translateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", str(self.projectName)))
        self.menuProject.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_Recent.setTitle(_translate("MainWindow", "Open Recent"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuProject_2.setTitle(_translate("MainWindow", "Project"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuViews.setTitle(_translate("MainWindow", "Views"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionProgressView.setText(_translate("MainWindow", "Progress View"))
        self.actionStatus_View.setText(_translate("MainWindow", "Status View"))
        self.actionClose_Project.setText(_translate("MainWindow", "Close Project"))
        self.actionDelete_Project.setText(_translate("MainWindow", "Delete Project"))
        self.actionRename.setText(_translate("MainWindow", "Rename..."))
        self.actionChange_Location.setText(_translate("MainWindow", "Change Location"))
        self.actionEN.setText(_translate("MainWindow", "EN"))
        self.actionES.setText(_translate("MainWindow", "ES"))
        self.actionEUS.setText(_translate("MainWindow", "EUS"))
        self.actionProgress_View.setText(_translate("MainWindow", "Progress View"))
