from configparser import ConfigParser


class RecentProjectFileWriter:

    def __init__(self):
        # Get the configparser object
        self.config_object = ConfigParser()
        self.config_object.read('./Configuration/RecentProjectData.cfg')

    def RecentProjectFileWriter(self, projectName, projectLastAccess, projectLocation, projects):

        if len(projects) < 5:
            self.config_object.set("RECENT_PROJECT",  "accessible_project_number", str(int(len(projects) + 1)))
        else:
            self.config_object.set("RECENT_PROJECT",  "accessible_project_number", "5")

        self.config_object.set("RECENT_PROJECT",  "project_name_1",  projectName)
        self.config_object.set("RECENT_PROJECT",  "project_access_1", projectLastAccess)
        self.config_object.set("RECENT_PROJECT",  "project_location_1", projectLocation)

        i = 2
        for project in projects:
            self.config_object.set("RECENT_PROJECT",  str("project_name_" + str(i)),  str(project[0]))
            self.config_object.set("RECENT_PROJECT",  str("project_access_" + str(i)), str(project[1]))
            self.config_object.set("RECENT_PROJECT",  str("project_location_" + str(i)), str(project[2]))
            i = i + 1
            if i > 5:
                break

        with open('./Configuration/RecentProjectData.cfg', 'w+')as conf:
            self.config_object.write(conf)
        conf.close()

    def actualice(self, newName):
        self.config_object.set('RECENT_PROJECT', 'project_name_1', str(newName))

        with open('./Configuration/RecentProjectData.cfg', 'w+') as conf:
            self.config_object.write(conf)
