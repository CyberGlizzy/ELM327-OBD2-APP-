import configparser

class Settings:
    def __init__(self, config_file="settings.ini"):
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self.defaults = {
            "connection": {
                "port": "COM1",
                "baud_rate": "9600"
            },
            "appearance": {
                "theme": "dark",
                "font_size": "20"
            }
        }
        self.load_settings()

    def load_settings(self):
        self.config.read(self.config_file)
        for section, options in self.defaults.items():
            if not self.config.has_section(section):
                self.config.add_section(section)
            for option, value in options.items():
                if not self.config.has_option(section, option):
                    self.config.set(section, option, value)
        self.save_settings()

    def save_settings(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def get(self, section, option):
        return self.config.get(section, option)

    def set(self, section, option, value):
        self.config.set(section, option, value)
        self.save_settings()
