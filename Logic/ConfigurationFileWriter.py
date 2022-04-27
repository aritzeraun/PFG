from configparser import SafeConfigParser


class ConfigurationFileWriter:

    def __init__(self):
        # Get the configparser object
        self.config_object = SafeConfigParser()
        self.config_object.read('./Configuration/AppGeneralConfiguration.cfg')

    def configFileWriter(self, language_code, accessibility_default, current_font, current_font_size, theme_default,
                         theme_current_style, theme_current_main_color, theme_current_secondary_color):

        self.config_object.set('SYSTEM', 'language_code', str(language_code))
        self.config_object.set("SYSTEM", "accessibility_default", str(accessibility_default))
        self.config_object.set("SYSTEM", "accessibility_default_font", "Cascadia Mono")
        self.config_object.set("SYSTEM", "accessibility_default_font_size", "8")
        self.config_object.set("SYSTEM", "accessibility_current_font", str(current_font))
        self.config_object.set("SYSTEM", "accessibility_current_font_size", str(current_font_size))

        self.config_object.set("SYSTEM", "theme_default", str(theme_default))
        self.config_object.set("SYSTEM", "theme_default_style", "Fusion")
        self.config_object.set("SYSTEM", "theme_default_main_color", "(32, 111, 209)")
        self.config_object.set("SYSTEM", "theme_default_secondary_color", "(59, 91, 134)")
        self.config_object.set("SYSTEM", "theme_current_style", str(theme_current_style))
        self.config_object.set("SYSTEM", "theme_current_main_color", str(theme_current_main_color))
        self.config_object.set("SYSTEM", "theme_current_secondary_color", str(theme_current_secondary_color))

        # Write the above sections to config.cfg file
        with open('./Configuration/AppGeneralConfiguration.cfg', 'w') as conf:
            self.config_object.write(conf)

    def writeUserConfiguration(self, usernameSaved, lastUsernameSaved):

        self.config_object.set('USERINFO', 'user_name_save_check', str(usernameSaved))
        self.config_object.set('USERINFO', 'username_web_of_science_saved', str(lastUsernameSaved))

        # Write the above sections to config.cfg file
        with open('./Configuration/AppGeneralConfiguration.cfg', 'w') as conf:
            self.config_object.write(conf)

    def changeLanguage(self, language):
        self.config_object.set('SYSTEM', 'language_code', str(language))

        # Write the above sections to config.cfg file
        with open('./Configuration/AppGeneralConfiguration.cfg', 'w') as conf:
            self.config_object.write(conf)
