from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import QSize, QTimer

class DashboardScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        title = QLabel("Dashboard", self)
        title.setStyleSheet("font-size: 24px; color: green; font-weight: bold; font-family: Arial;")
        self.layout.addWidget(title)

        # Layout for dashboard metrics
        metrics_layout = QHBoxLayout()

        # RPM label
        self.rpm_label = QLabel("RPM: 0", self)
        self.rpm_label.setStyleSheet("font-size: 18px; color: green;")
        metrics_layout.addWidget(self.rpm_label)

        # Speed label
        self.speed_label = QLabel("Speed: 0 mph", self)
        self.speed_label.setStyleSheet("font-size: 18px; color: green;")
        metrics_layout.addWidget(self.speed_label)

        # Coolant temperature label
        self.coolant_label = QLabel("Coolant Temp: 0 °C", self)
        self.coolant_label.setStyleSheet("font-size: 18px; color: green;")
        metrics_layout.addWidget(self.coolant_label)

        self.layout.addLayout(metrics_layout)

        # Back button
        back_button = self.create_button("Back", parent.go_home)
        self.layout.addWidget(back_button)

        self.setStyleSheet("background-color: black;")

        # Timer to update the dashboard metrics
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)  # Update every second

    def create_button(self, text, callback):
        button = QPushButton(text, self)
        button.setIconSize(QSize(100, 100))
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

    def update_metrics(self):
        # Simulate retrieving data from OBD-II
        rpm = self.simulate_data(700, 3000)  # Example RPM range
        speed = self.simulate_data(0, 120)  # Example speed range in mph
        coolant_temp = self.simulate_data(70, 100)  # Example coolant temp in °C

        # Update the labels
        self.rpm_label.setText(f"RPM: {rpm}")
        self.speed_label.setText(f"Speed: {speed} mph")
        self.coolant_label.setText(f"Coolant Temp: {coolant_temp} °C")

    def simulate_data(self, min_value, max_value):
        # Simulate data fetching
        import random
        return random.randint(min_value, max_value)
