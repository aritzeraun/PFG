import datetime
import errno
import os

from PyQt5.QtWidgets import QMessageBox

from Logic import RecentProjectFileWriter
from Views import ApplicationView, NewProjectDialog
from datetime import datetime
from PyQt5 import QtCore, QtWidgets


def createNewProject(recentProjectsData, MainWindow, alertText):

    projectExist = False

    dialog = QtWidgets.QDialog()
    newProjectDialog = NewProjectDialog.NewProjectDialog(dialog, 0)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.exec_()

    if newProjectDialog.creationState:
        ProjectDirectory = str(newProjectDialog.newProjectLocation + '/' + newProjectDialog.newProjectName)

        if os.path.isdir(ProjectDirectory):
            projectExist = True
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(str(alertText))
            msgBoxLogin.exec()
        else:
            try:
                os.mkdir(ProjectDirectory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if not projectExist:
            ApplicationView.ApplicationView(MainWindow, recentProjectsData, ProjectDirectory,
                                            newProjectDialog.newProjectName)

            RecentProjectFileWriter.RecentProjectFileWriter() \
                .RecentProjectFileWriter(newProjectDialog.newProjectName, datetime.today().strftime('%Y-%m-%d'),
                                         newProjectDialog.newProjectLocation, recentProjectsData)
