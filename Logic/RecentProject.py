import datetime
import os

from PyQt5.QtWidgets import QMessageBox

from Logic import RecentProjectFileWriter
from Views import ApplicationView


def RecentProject(recentProject, MainWindow, recentProjectsData, message):

    RecentProjectFileWriter.RecentProjectFileWriter().RecentProjectFileWriter(recentProject[0],
                                                                              datetime.datetime.today()
                                                                              .strftime('%Y-%m-%d'),
                                                                              recentProject[2],
                                                                              recentProjectsData)
    projectDirectory = recentProject[2] + '/' + recentProject[0]
    if os.path.exists(projectDirectory):
        ApplicationView.ApplicationView(MainWindow, recentProjectsData, projectDirectory, recentProject[0])
    else:
        msgBoxLogin = QMessageBox()
        msgBoxLogin.setText(str(message))
        msgBoxLogin.exec()
