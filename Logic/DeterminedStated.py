import configparser
from os import walk
from os.path import exists


class DeterminedState:

    def __init__(self, dockWidget, projectDirectory):

        self.dockWidget = dockWidget
        self.ProjectDirectory = projectDirectory

        self.configGeneral = configparser.RawConfigParser()
        self.configGeneral.read('./Configuration/AppGeneralConfiguration.cfg')

        # DOCUMENT_LIST_FOLDER
        self.documentListFolder = self.ProjectDirectory + '/'
        self.documentListFolder = self.documentListFolder + self.configGeneral.get('LOCATIONS',
                                                                                   'document_list_folder_name') + '/'
        # DOWNLOADED_FILES_FOLDER
        self.downloadedFolder = self.ProjectDirectory + '/'
        self.downloadedFolder = self.downloadedFolder + self.configGeneral.get('LOCATIONS',
                                                                               'downloaded_documents_folder_name')+'/'

        # DATA_EXTRACTION_FOLDER
        self.downloadFilesFolder = self.ProjectDirectory + '/'
        self.downloadFilesFolder = self.downloadFilesFolder + self.configGeneral.get('LOCATIONS',
                                                                                     'data_extraction_folder_name')+'/'
        # ANALYSIS_FOLDER
        self.keyExtractionFolder = self.ProjectDirectory + '/'
        self.keyExtractionFolder = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                     'analysis_folder_name') + '/'
        self.keyListFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS', 'key_list_file_name')
        self.stopPathFile = self.configGeneral.get('LOCATIONS', 'stop_file_relative_path')
        self.relationFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS', 'key_relation_file_name')
        self.uniqueKeysFilePath = self.keyExtractionFolder + self.configGeneral.get('LOCATIONS',
                                                                                    'unique_keys_file_name')
        # GRAPHICS_FOLDER
        self.GraphicsFolder = self.ProjectDirectory + '/'
        self.GraphicsFolder = self.GraphicsFolder + self.configGeneral.get('LOCATIONS', 'graphics_folder_name') + '/'
        self.graphImageName = self.GraphicsFolder + self.configGeneral.get('LOCATIONS', 'graph_graphic_name')
        self.circularImageName = self.GraphicsFolder + self.configGeneral.get('LOCATIONS', 'circular_graphic_name')

        self.finalState = 0

    def stateDetermination(self):

        files = []
        # DOCUMENT_LIST_FOLDER
        if exists(self.documentListFolder):

            for (dir_path, dir_names, filenames) in walk(self.documentListFolder):
                files.extend(filenames)
                break
            if len(files) > 0:
                self.finalState = 1

            # DOWNLOADED_FILES_FOLDER
            if exists(self.downloadedFolder):

                for (dir_path, dir_names, filenames) in walk(self.downloadedFolder):
                    files = []
                    files.extend(filenames)
                    break
                if len(files) > 0:

                    # DATA_EXTRACTION_FOLDER
                    if exists(self.downloadFilesFolder):

                        for (dir_path, dir_names, filenames) in walk(self.downloadFilesFolder):
                            files = []
                            files.extend(filenames)
                            break
                        if len(files) > 0:
                            self.finalState = 2

                        # ANALYSIS_FOLDER
                        if exists(self.keyExtractionFolder):

                            if exists(self.keyListFilePath) and exists(self.stopPathFile) and \
                                    exists(self.relationFilePath) and exists(self.uniqueKeysFilePath):
                                self.finalState = 3

                            # GRAPHICS_FOLDER
                            if exists(self.GraphicsFolder):

                                if exists(self.graphImageName) and exists(self.circularImageName):
                                    self.finalState = 4

        self.putButtonsEnable()

    def putButtonsEnable(self):

        self.dockWidget.searchButton.setEnabled(False)
        self.dockWidget.downloadButton.setEnabled(False)
        self.dockWidget.analiseButton.setEnabled(False)
        self.dockWidget.graphicsButton.setEnabled(False)

        if self.finalState >= 0:
            self.dockWidget.searchButton.setEnabled(True)
        if self.finalState >= 1:
            self.dockWidget.downloadButton.setEnabled(True)
        if self.finalState >= 2:
            self.dockWidget.analiseButton.setEnabled(True)
        if self.finalState >= 3:
            self.dockWidget.graphicsButton.setEnabled(True)
