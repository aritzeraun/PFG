from configparser import ConfigParser


class ConfigWriter:

    def __init__(self):
        # Get the configparser object
        self.config_object = ConfigParser()

    def configFileWriter(self, language_code, accessibility_default, current_font, current_font_size, theme_default,
                         theme_current_style, theme_current_main_color, theme_current_secondary_color):

        self.config_object["SYSTEM"] = {
            "language_code": str(language_code),
            "accessibility_default": str(accessibility_default),
            "accessibility_default_font": "Cascadia Mono",
            "accessibility_default_font_size": "8",
            "accessibility_current_font": str(current_font),
            "accessibility_current_font_size": str(current_font_size),

            "theme_default": str(theme_default),
            "theme_default_style": "Fusion",
            "theme_default_main_color": "(32, 111, 209)",
            "theme_default_secondary_color": "(59, 91, 134)",
            "theme_current_style": str(theme_current_style),
            "theme_current_main_color": str(theme_current_main_color),
            "theme_current_secondary_color": str(theme_current_secondary_color),
        }

        # Write the above sections to config.cfg file
        with open('./Configuration/AppGeneralConfiguration.cfg', 'w') as conf:
            self.config_object.write(conf)
