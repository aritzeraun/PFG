import datetime

from PyQt5.QtWidgets import QFileDialog

from Logic import RecentProjectFileWriter
from Views import ApplicationView


def openProject(recentProjectsData, MainWindow, FileDialogName):
    folder = str(QFileDialog.getExistingDirectory(None, str(FileDialogName)))

    if folder != '':

        projectName = folder.split('/')
        projectName = projectName[len(projectName) - 1]
        projectDirectory = folder.replace(projectName, '')
        projectDirectory = projectDirectory[0:len(projectDirectory) - 1]
        position = 0

        for project in recentProjectsData:
            if project[0] == projectName and project[2] == projectDirectory:
                recentProjectsData.pop(position)
            position = position + 1

        ApplicationView.ApplicationView(MainWindow, recentProjectsData, projectDirectory, projectName)

        RecentProjectFileWriter.RecentProjectFileWriter()\
            .RecentProjectFileWriter(projectName, datetime.datetime.today().strftime('%Y-%m-%d'), projectDirectory,
                                     recentProjectsData)
