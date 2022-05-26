import os

from PyQt5.QtWidgets import QMessageBox

from Logic import RecentProjectFileWriter
from Views import NewProjectDialog
from PyQt5 import QtCore, QtWidgets


def renameProject(recentProjectsData, MainWindow):

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

        if projectExist:

            os.chdir(str(projectDirectory).replace(oldName, ''))
            os.rename(oldName, newProjectDialog.newProjectName)
            MainWindow.projectName = newProjectDialog.newProjectName
            print(newProjectDialog.newProjectName)
            print(recentProjectsData)
            try:
                RecentProjectFileWriter.RecentProjectFileWriter().actualice(str(newProjectDialog.newProjectName))
            except Exception as e:
                print(e)
