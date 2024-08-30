from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class MainScreen(QWidget):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # Layout
        layout = QGridLayout(self)

        # Dashboard Button
        dashboard_button = self.create_button("Dashboard", "path/to/dashboard_icon.png")
        dashboard_button.clicked.connect(self.go_to_dashboard)
        layout.addWidget(dashboard_button, 0, 0)

        # Live Data Button
        live_data_button = self.create_button("Live Data", "path/to/live_data_icon.png")
        live_data_button.clicked.connect(self.go_to_live_data)
        layout.addWidget(live_data_button, 0, 1)

        # All Sensors Button
        sensors_button = self.create_button("All Sensors", "path/to/sensors_icon.png")
        sensors_button.clicked.connect(self.go_to_sensors)
        layout.addWidget(sensors_button, 0, 2)

        # Diagnostic Trouble Codes Button
        dtc_button = self.create_button("DTC", "path/to/dtc_icon.png")
        dtc_button.clicked.connect(self.go_to_dtc)
        layout.addWidget(dtc_button, 1, 0)

        # Freeze Frame Button
        freeze_frame_button = self.create_button("Freeze Frame", "path/to/freeze_frame_icon.png")
        freeze_frame_button.clicked.connect(self.go_to_freeze_frame)
        layout.addWidget(freeze_frame_button, 1, 1)

        # Noncontinuous Monitors Button
        monitors_button = self.create_button("Monitors", "path/to/monitors_icon.png")
        monitors_button.clicked.connect(self.go_to_monitors)
        layout.addWidget(monitors_button, 1, 2)

        # Garage Button
        garage_button = self.create_button("Garage", "path/to/garage_icon.png")
        garage_button.clicked.connect(self.go_to_garage)
        layout.addWidget(garage_button, 2, 0)

        # Settings Button
        settings_button = self.create_button("Settings", "path/to/settings_icon.png")
        settings_button.clicked.connect(self.go_to_settings)
        layout.addWidget(settings_button, 2, 1)

        # Statistics Button
        stats_button = self.create_button("Statistics", "path/to/statistics_icon.png")
        stats_button.clicked.connect(self.go_to_stats)
        layout.addWidget(stats_button, 2, 2)

        # ECU Identifiers Button
        ecu_button = self.create_button("ECU Identifiers", "path/to/ecu_icon.png")
        ecu_button.clicked.connect(self.go_to_ecu)
        layout.addWidget(ecu_button, 3, 0)

        # Data Recording Button
        recording_button = self.create_button("Data Recording", "path/to/recording_icon.png")
        recording_button.clicked.connect(self.go_to_recording)
        layout.addWidget(recording_button, 3, 1)

        # Acceleration Test Button
        accel_test_button = self.create_button("Acceleration Tests", "path/to/acceleration_icon.png")
        accel_test_button.clicked.connect(self.go_to_accel_test)
        layout.addWidget(accel_test_button, 3, 2)

        # Emission Test Button
        emission_test_button = self.create_button("Emission Test", "path/to/emission_icon.png")
        emission_test_button.clicked.connect(self.go_to_emission_test)
        layout.addWidget(emission_test_button, 4, 0)

        # Terminal Button
        terminal_button = self.create_button("Terminal", "path/to/terminal_icon.png")
        terminal_button.clicked.connect(self.go_to_terminal)
        layout.addWidget(terminal_button, 4, 1)

        # Set the layout
        self.setLayout(layout)

    def create_button(self, text, icon_path):
        button = QPushButton(text)
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(64, 64))  # Adjust the icon size as needed
        button.setStyleSheet("font-size: 18px;")  # Adjust font size as needed
        return button

    def go_to_dashboard(self):
        # Logic to switch to the dashboard screen
        pass

    def go_to_live_data(self):
        # Logic to switch to the live data screen
        pass

    def go_to_sensors(self):
        # Logic to switch to the all sensors screen
        pass

    def go_to_dtc(self):
        # Logic to switch to the diagnostic trouble codes screen
        pass

    def go_to_freeze_frame(self):
        # Logic to switch to the freeze frame screen
        pass

    def go_to_monitors(self):
        # Logic to switch to the noncontinuous monitors screen
        pass

    def go_to_garage(self):
        # Logic to switch to the garage screen
        pass

    def go_to_settings(self):
        # Logic to switch to the settings screen
        pass

    def go_to_stats(self):
        # Logic to switch to the statistics screen
        pass

    def go_to_ecu(self):
        # Logic to switch to the ECU identifiers screen
        pass

    def go_to_recording(self):
        # Logic to switch to the data recording screen
        pass

    def go_to_accel_test(self):
        # Logic to switch to the acceleration test screen
        pass

    def go_to_emission_test(self):
        # Logic to switch to the emission test screen
        pass

    def go_to_terminal(self):
        # Logic to switch to the terminal screen
        pass
