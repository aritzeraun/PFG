import errno
import os
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from Logic import RecentProjectFileWriter
from Views import LoginWidgetPanel, NewProjectDialog
import urllib.request


def connectionToEthernet():

    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False


class ApplicationView:
    def __init__(self, MainWindow, recentProjectsData, ProjectDirectory, ProjectName):
        self.MainWindow = MainWindow
        self.recentProjectsData = recentProjectsData
        self.projectDirectory = ProjectDirectory
        self.projectName = ProjectName
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 889)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuOpen_Recent = QtWidgets.QMenu(self.menuProject)
        self.menuOpen_Recent.setObjectName("menuOpen_Recent")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuLanguage = QtWidgets.QMenu(self.menuSettings)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuProject_2 = QtWidgets.QMenu(self.menubar)
        self.menuProject_2.setObjectName("menuProject_2")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuViews = QtWidgets.QMenu(self.menubar)
        self.menuViews.setObjectName("menuViews")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 439))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 85, 439))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.dockWidgetContents_4)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_4)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("deusto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionProject_1 = QtWidgets.QAction(MainWindow)
        self.actionProject_1.setObjectName("actionProject_1")
        self.actionProject_2 = QtWidgets.QAction(MainWindow)
        self.actionProject_2.setObjectName("actionProject_2")
        self.actionProject_3 = QtWidgets.QAction(MainWindow)
        self.actionProject_3.setObjectName("actionProject_3")
        self.actionProyect_4 = QtWidgets.QAction(MainWindow)
        self.actionProyect_4.setObjectName("actionProyect_4")
        self.actionProyect_5 = QtWidgets.QAction(MainWindow)
        self.actionProyect_5.setObjectName("actionProyect_5")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionProgressView = QtWidgets.QAction(MainWindow)
        self.actionProgressView.setCheckable(True)
        self.actionProgressView.setChecked(True)
        self.actionProgressView.setObjectName("actionProgressView")
        self.actionStatus_View = QtWidgets.QAction(MainWindow)
        self.actionStatus_View.setObjectName("actionStatus_View")
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionRename.setObjectName("actionRename")
        self.actionClose_Project = QtWidgets.QAction(MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.actionRename_2 = QtWidgets.QAction(MainWindow)
        self.actionRename_2.setObjectName("actionRename_2")
        self.actionChange_Location = QtWidgets.QAction(MainWindow)
        self.actionChange_Location.setObjectName("actionChange_Location")
        self.actionEN = QtWidgets.QAction(MainWindow)
        self.actionEN.setObjectName("actionEN")
        self.actionES = QtWidgets.QAction(MainWindow)
        self.actionES.setObjectName("actionES")
        self.actionEUS = QtWidgets.QAction(MainWindow)
        self.actionEUS.setObjectName("actionEUS")
        self.actionProgress_View = QtWidgets.QAction(MainWindow)
        self.actionProgress_View.setCheckable(True)
        self.actionProgress_View.setChecked(True)
        self.actionProgress_View.setObjectName("actionProgress_View")
        self.actionStatus_View_2 = QtWidgets.QAction(MainWindow)
        self.actionStatus_View_2.setCheckable(True)
        self.actionStatus_View_2.setChecked(True)
        self.actionStatus_View_2.setObjectName("actionStatus_View_2")
        self.menuOpen_Recent.addSeparator()
        self.menuOpen_Recent.addAction(self.actionProject_1)
        self.menuOpen_Recent.addAction(self.actionProject_2)
        self.menuOpen_Recent.addAction(self.actionProject_3)
        self.menuOpen_Recent.addAction(self.actionProyect_4)
        self.menuOpen_Recent.addAction(self.actionProyect_5)
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
        self.menuProject_2.addAction(self.actionRename_2)
        self.menuProject_2.addSeparator()
        self.menuProject_2.addAction(self.actionClose_Project)
        self.menuViews.addAction(self.actionProgress_View)
        self.menuViews.addAction(self.actionStatus_View_2)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuProject_2.menuAction())
        self.menubar.addAction(self.menuViews.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionExit.triggered.connect(lambda: self._actionExit())
        self.actionNew_Project.triggered.connect(lambda: self._createNewProject())
        self.actionProgress_View.triggered.connect(lambda: self.putDockVisible())

        thereIsInternetConnection = connectionToEthernet()

        if thereIsInternetConnection:
            LicenseView = QtWidgets.QWidget(self.centralWidget)
            LoginWidgetPanel.LoginWidgetPanel(LicenseView, self.centralWidget, self)
            self.gridLayout.addWidget(LicenseView)

        self.translateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _actionExit(self):
        self.MainWindow.close()

    def putDockVisible(self):

        if self.actionProgress_View.isChecked():
            self.dockWidget = QtWidgets.QDockWidget(self.MainWindow)
            self.dockWidget.setObjectName("dockWidget")
            self.dockWidgetContents = QtWidgets.QWidget()
            self.MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        else:
            self.dockWidget.close()

    def _createNewProject(self):
        dialog = QtWidgets.QDialog()
        newProjectDialog = NewProjectDialog.NewProjectDialog(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

        try:
            os.mkdir(str(newProjectDialog.newProjectLocation + '/' + newProjectDialog.newProjectName))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        RecentProjectFileWriter.RecentProjectFileWriter().RecentProjectFileWriter(newProjectDialog.newProjectName,
                                                                                  datetime.today().strftime('%Y-%m-%d'),
                                                                                  newProjectDialog.newProjectLocation,
                                                                                  self.recentProjectsData)

        ApplicationView(self.MainWindow, self.recentProjectsData, self.projectDirectory,
                        newProjectDialog.newProjectName)

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
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionProject_1.setText(_translate("MainWindow", "Project 1"))
        self.actionProject_2.setText(_translate("MainWindow", "Project 2"))
        self.actionProject_3.setText(_translate("MainWindow", "Project 3"))
        self.actionProyect_4.setText(_translate("MainWindow", "Proyect 4"))
        self.actionProyect_5.setText(_translate("MainWindow", "Proyect 5"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionProgressView.setText(_translate("MainWindow", "Progress View"))
        self.actionStatus_View.setText(_translate("MainWindow", "Status View"))
        self.actionRename.setText(_translate("MainWindow", "Rename..."))
        self.actionClose_Project.setText(_translate("MainWindow", "Close Project"))
        self.actionRename_2.setText(_translate("MainWindow", "Rename..."))
        self.actionChange_Location.setText(_translate("MainWindow", "Change Location"))
        self.actionEN.setText(_translate("MainWindow", "EN"))
        self.actionES.setText(_translate("MainWindow", "ES"))
        self.actionEUS.setText(_translate("MainWindow", "EUS"))
        self.actionProgress_View.setText(_translate("MainWindow", "Progress View"))
        self.actionStatus_View_2.setText(_translate("MainWindow", "Status View"))
