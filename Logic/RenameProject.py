import os

from PyQt5.QtWidgets import QMessageBox

from Logic import RecentProjectFileWriter
from Views import NewProjectDialog
from PyQt5 import QtCore, QtWidgets


def renameProject(recentProjectsData, MainWindow, alertText, alertTextError):

    projectExist = False

    dialog = QtWidgets.QDialog()
    newProjectDialog = NewProjectDialog.NewProjectDialog(dialog, 1)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.exec_()

    if newProjectDialog.creationState:
        oldName = MainWindow.projectName
        projectDirectory = MainWindow.projectDirectory

        if os.path.isdir(projectDirectory):
            projectExist = True
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(str(alertText))
            msgBoxLogin.exec()
        else:
            msgBoxLogin = QMessageBox()
            msgBoxLogin.setText(str(alertTextError))
            msgBoxLogin.exec()

        if projectExist:

            os.chdir(str(projectDirectory).replace(oldName, ''))
            os.rename(oldName, newProjectDialog.newProjectName)
            MainWindow.projectName = newProjectDialog.newProjectName
            projectDirectory = str(projectDirectory).replace(str('/' + oldName), '')
            controller = RecentProjectFileWriter.RecentProjectFileWriter()
            print(newProjectDialog.newProjectName)
            print(recentProjectsData)
            controller.actualice(str(newProjectDialog.newProjectName))
