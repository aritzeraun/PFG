import subprocess
import time

from PyQt5.QtCore import QThread, pyqtSignal


class GraphicCreatorAction(QThread):

    image_creation_correctly = pyqtSignal()

    def __init__(self, directoryToDataFile, width, height, circularDirectory, graphDirectory):
        super(QThread, self).__init__()
        self.directoryToDataFile = directoryToDataFile
        self.width = width
        self.height = height
        self.circularDirectory = circularDirectory
        self.graphDirectory = graphDirectory

    def run(self):
        call = "Rscript ./Graphics/circularGraphics.R " + str(self.directoryToDataFile) + " " + str(self.width)
        call = call + " " + str(self.height) + " " + str(self.circularDirectory) + " " + str(self.graphDirectory)
        subprocess.call(call, shell=True)
        time.sleep(10)
        self.image_creation_correctly.emit()
