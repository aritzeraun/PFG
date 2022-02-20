from configparser import ConfigParser


class ConfigWriter:

    def __init__(self):
        # Get the configparser object
        self.config_object = ConfigParser()

    def configFileWriter(self, save_check, username, code):

        self.config_object["USERINFO"] = {
            "usernameSaveCheck": str(save_check),
            "username": str(username)
        }

        self.config_object["LANGUAGE"] = {
            "code": str(code)
        }

        # Write the above sections to config.ini file
        with open('./Languages/AppConfigGeneral.cfg', 'w') as conf:
            self.config_object.write(conf)
