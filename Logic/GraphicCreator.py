import subprocess
import time

from PyQt5.QtCore import QThread, pyqtSignal


class GraphicCreatorAction(QThread):

    image_creation_correctly = pyqtSignal()

    def __init__(self, directoryToDataFile, width, height, support, confidence, circularDirectory, graphDirectory):
        super(QThread, self).__init__()
        self.directoryToDataFile = directoryToDataFile
        self.width = width
        self.height = height
        self.support = support
        self.confidence = confidence
        self.circularDirectory = circularDirectory
        self.graphDirectory = graphDirectory

    def run(self):
        call = "Rscript ./Graphics/GraphicsCreator.R " + str(self.directoryToDataFile) + " " + str(self.width)
        call = call + " " + str(self.height) + " " + str(self.support) + " " + str(self.confidence) + " "
        call = call + str(self.circularDirectory) + " " + str(self.graphDirectory)

        subprocess.call(call, shell=True)
        time.sleep(10)
        self.image_creation_correctly.emit()
