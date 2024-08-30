from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class EcuTuningScreen(QWidget):
    def __init__(self, parent=None):
        super(EcuTuningScreen, self).__init__(parent)
        self.layout = QVBoxLayout()

        self.label = QLabel("ECU Tuning Dashboard")
        self.layout.addWidget(self.label)

        self.speed_input = QLineEdit()
        self.speed_input.setPlaceholderText("Set Speed")
        self.layout.addWidget(self.speed_input)

        self.temp_input = QLineEdit()
        self.temp_input.setPlaceholderText("Set Temperature")
        self.layout.addWidget(self.temp_input)

        self.submit_button = QPushButton("Submit Changes")
        self.layout.addWidget(self.submit_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(parent.go_home)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def apply_color_settings(self, color_settings):
        self.setStyleSheet(f"background-color: {color_settings['Background Color']};")
        self.submit_button.setStyleSheet(f"background-color: {color_settings['Button Color']}; color: {color_settings['Label Color']};")
        self.back_button.setStyleSheet(f"background-color: {color_settings['Button Color']}; color: {color_settings['Label Color']};")
        self.label.setStyleSheet(f"color: {color_settings['Label Color']};")
        self.speed_input.setStyleSheet(f"color: {color_settings['Label Color']};")
        self.temp_input.setStyleSheet(f"color: {color_settings['Label Color']};")
