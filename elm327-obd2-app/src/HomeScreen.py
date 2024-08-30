from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class HomeScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        main_layout = QVBoxLayout()  

        # Top section with label and status
        top_section = QHBoxLayout()
        self.label = QLabel("ELM327 PyQt App")
        self.label.setStyleSheet("color: #00FF00; font-size: 24px;")
        top_section.addWidget(self.label)
        top_section.addStretch()
        connection_status = QLabel("ELM connection: Connected\nECU connection: Connected")
        connection_status.setStyleSheet("color: #00FF00; font-size: 14px;")
        top_section.addWidget(connection_status)
        
        main_layout.addLayout(top_section)

        # Add buttons with icons
        dashboard_button = self.create_button("Dashboard", 'icons/dashboard.png', parent.go_to_dashboard)
        live_data_button = self.create_button("Live Data", 'icons/data-transfer.png', parent.go_to_live_data)
        all_sensors_button = self.create_button("All Sensors", 'icons/sensor.png', parent.go_to_all_sensors)
        dtc_button = self.create_button("DTC Errors", 'icons/code-error.png', parent.go_to_diagnostic_trouble_codes)
        freeze_frame_button = self.create_button("Freeze Frame", 'icons/data-audit.png', parent.go_to_freeze_frame)
        non_cont_monitors_button = self.create_button("Non-Continuous Monitors", 'icons/monitor.png', parent.go_to_non_continuous_monitors)
        garage_button = self.create_button("Garage", 'icons/garage.png', parent.go_to_garage)
        settings_button = self.create_button("Settings", 'icons/settings.png', parent.go_to_settings)
        statistics_button = self.create_button("Statistics", 'icons/statistics.png', parent.go_to_statistics)
        ecu_identifiers_button = self.create_button("ECU Identifiers", 'icons/ecu.png', parent.go_to_ecu_identifiers)
        data_recording_button = self.create_button("Data Recording", 'icons/data_recording.png', parent.go_to_data_recording)
        accel_tests_button = self.create_button("Acceleration Tests", 'icons/speedometer.png', parent.go_to_acceleration_tests)
        terminal_button = self.create_button("OBD Terminal", 'icons/obd_terminal.png', parent.go_to_terminal)
        gauge_button = self.create_button("Gauges", 'icons/gauge.png', parent.go_to_gauge_screen)  

        # Layout for buttons in a grid
        buttons_layout = QGridLayout()
        buttons_layout.addWidget(dashboard_button, 0, 0)
        buttons_layout.addWidget(live_data_button, 0, 1)
        buttons_layout.addWidget(all_sensors_button, 1, 0)
        buttons_layout.addWidget(dtc_button, 1, 1)
        buttons_layout.addWidget(freeze_frame_button, 2, 0)
        buttons_layout.addWidget(non_cont_monitors_button, 2, 1)
        buttons_layout.addWidget(garage_button, 3, 0)
        buttons_layout.addWidget(settings_button, 3, 1)
        buttons_layout.addWidget(statistics_button, 4, 0)
        buttons_layout.addWidget(ecu_identifiers_button, 4, 1)
        buttons_layout.addWidget(data_recording_button, 5, 0)
        buttons_layout.addWidget(accel_tests_button, 5, 1)
        buttons_layout.addWidget(terminal_button, 6, 0, 1, 2)  # Span across two columns
        buttons_layout.addWidget(gauge_button, 7, 0, 1, 2)  # Gauge button across two columns

        main_layout.addLayout(buttons_layout)
       
        self.setLayout(main_layout)
        self.setStyleSheet("background-color: black;")  

    def create_button(self, text, icon_path, callback):
        button = QPushButton(text)
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(64, 64))  # Adjust size as needed
        button.setStyleSheet("color: white; background-color: #007BFF; font-size: 18px; padding: 15px; border-radius: 10px;")
        button.clicked.connect(callback)
        return button
