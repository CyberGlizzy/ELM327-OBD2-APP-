from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QSize

class AccelerationTestsScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        title = QLabel("Acceleration Tests", self)
        title.setStyleSheet("font-size: 24px; color: green; font-weight: bold; font-family: Arial;")
        self.layout.addWidget(title)

        back_button = self.create_button("Back", parent.go_home)
        self.layout.addWidget(back_button)

        self.setStyleSheet("background-color: black;")

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
