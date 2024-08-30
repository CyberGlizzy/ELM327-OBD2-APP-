from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QHBoxLayout
from PyQt5.QtCore import QSize, QTimer

class TerminalScreen(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        title = QLabel("OBD Terminal", self)
        title.setStyleSheet("font-size: 24px; color: green; font-weight: bold; font-family: Arial;")
        self.layout.addWidget(title)

        # Text area for command input
        self.command_input = QTextEdit(self)
        self.command_input.setPlaceholderText("Enter OBD-II command here...")
        self.command_input.setFixedHeight(50)
        self.command_input.setStyleSheet("color: green; background-color: black; font-size: 16px;")
        self.layout.addWidget(self.command_input)

        # Text area for terminal output
        self.terminal_output = QTextEdit(self)
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setStyleSheet("color: green; background-color: black; font-size: 16px;")
        self.layout.addWidget(self.terminal_output)

        # Buttons layout
        buttons_layout = QHBoxLayout()

        # Send Command button
        send_button = self.create_button("Send Command", self.send_command)
        buttons_layout.addWidget(send_button)

        # Back button
        back_button = self.create_button("Back", parent.go_home)
        buttons_layout.addWidget(back_button)

        self.layout.addLayout(buttons_layout)

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

    def send_command(self):
        # Get the command from the input area
        command = self.command_input.toPlainText().strip()
        if command:
            # Simulate sending command to OBD-II adapter and getting a response
            response = self.simulate_obd_response(command)
            # Append the response to the terminal output
            self.terminal_output.append(f"> {command}")
            self.terminal_output.append(response)
            # Clear the input area
            self.command_input.clear()

    def simulate_obd_response(self, command):
        # This is a mock function to simulate OBD-II responses
        # You can replace this with actual OBD-II adapter communication logic
        return f"Simulated response for '{command}'"
