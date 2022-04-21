import datetime
import os
import shutil

from PyQt5.QtWidgets import QMessageBox

from Logic import RecentProjectFileWriter
from Views import NewProjectDialog
from datetime import datetime
from PyQt5 import QtCore, QtWidgets


def changeProjectLocation(recentProjectsData, MainWindow, alertText, alertTextError):

    projectExist = False

    dialog = QtWidgets.QDialog()
    newProjectDialog = NewProjectDialog.NewProjectDialog(dialog, 2)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.exec_()

    if newProjectDialog.creationState:
        oldName = MainWindow.projectName
        oldProjectDirectory = MainWindow.projectDirectory

        if os.path.isdir(oldProjectDirectory):
            projectExist = True
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(str(alertText))
            msgBoxLogin.exec()
        else:
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(str(alertTextError))
            msgBoxLogin.exec()

        if projectExist:
            newDirectory = newProjectDialog.newProjectLocation + '/' + oldName
            shutil.move(oldProjectDirectory, newDirectory)
            MainWindow.projectDirectory = newDirectory
            controller = RecentProjectFileWriter.RecentProjectFileWriter()
            controller.RecentProjectFileWriter(oldName,
                                               datetime.today().strftime('%Y-%m-%d'),
                                               newProjectDialog.newProjectLocation, recentProjectsData)
