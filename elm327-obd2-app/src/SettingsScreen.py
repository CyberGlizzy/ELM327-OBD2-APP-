from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QColorDialog, QLabel, QComboBox, QHBoxLayout
from PyQt5.QtCore import Qt

class SettingsScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # Title section
        title_section = QHBoxLayout()
        title = QLabel("Settings", self)
        title.setStyleSheet("font-size: 24px; color: green; font-weight: bold; font-family: Arial;")
        title.setAlignment(Qt.AlignCenter)
        title_section.addWidget(title)
        self.layout.addLayout(title_section)

        # Theme selection
        theme_section = QHBoxLayout()
        theme_label = QLabel("Theme:", self)
        theme_label.setStyleSheet("font-size: 18px; color: white;")
        theme_section.addWidget(theme_label)

        self.theme_selector = QComboBox(self)
        self.theme_selector.addItem("Dark Theme")
        self.theme_selector.addItem("Light Theme")
        self.theme_selector.addItem("Custom Color")
        self.theme_selector.currentIndexChanged.connect(self.change_color_theme)
        theme_section.addWidget(self.theme_selector)
        self.layout.addLayout(theme_section)

        # Additional Settings Options
        font_size_section = QHBoxLayout()
        font_size_label = QLabel("Font Size:", self)
        font_size_label.setStyleSheet("font-size: 18px; color: white;")
        font_size_section.addWidget(font_size_label)

        self.font_size_selector = QComboBox(self)
        self.font_size_selector.addItem("Small")
        self.font_size_selector.addItem("Medium")
        self.font_size_selector.addItem("Large")
        font_size_section.addWidget(self.font_size_selector)
        self.layout.addLayout(font_size_section)

        sound_settings_section = QHBoxLayout()
        sound_settings_label = QLabel("Sound Settings:", self)
        sound_settings_label.setStyleSheet("font-size: 18px; color: white;")
        sound_settings_section.addWidget(sound_settings_label)

        self.sound_settings_selector = QComboBox(self)
        self.sound_settings_selector.addItem("On")
        self.sound_settings_selector.addItem("Off")
        sound_settings_section.addWidget(self.sound_settings_selector)
        self.layout.addLayout(sound_settings_section)

        # Back button
        back_button = self.create_button("Back", parent.go_home)
        self.layout.addWidget(back_button)

        self.setStyleSheet("background-color: black; color: white;")

    def create_button(self, text, callback):
        button = QPushButton(text, self)
        button.setStyleSheet("""
            QPushButton {
                background-color: #1E90FF;
                color: white;
                font-size: 18px;
                font-family: Arial;
                font-weight: bold;
                border: none;
                padding: 15px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #4682B4;
            }
        """)
        button.clicked.connect(callback)
        return button

    def change_color_theme(self):
        selected_theme = self.theme_selector.currentText()

        if selected_theme == "Dark Theme":
            self.parent().parent().apply_color_settings({"background-color": "#2E2E2E", "text-color": "#FFFFFF"})
        elif selected_theme == "Light Theme":
            self.parent().parent().apply_color_settings({"background-color": "#FFFFFF", "text-color": "#000000"})
        elif selected_theme == "Custom Color":
            self.pick_custom_color()

    def pick_custom_color(self):
        custom_color = QColorDialog.getColor()
        if custom_color.isValid():
            self.parent().parent().apply_color_settings({"background-color": custom_color.name(), "text-color": "#FFFFFF"})
