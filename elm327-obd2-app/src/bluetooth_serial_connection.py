# bluetooth_serial_connection.py

import serial
import time

class ELM327Serial:
    def __init__(self, port="COMx", baudrate=9600, timeout=1):
        self.port = port  # Replace "COMx" with your Bluetooth serial COM port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None

    def connect(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print("Connected to ELM327 via Serial")
            self.initialize_elm327()
        except serial.SerialException as e:
            print(f"Serial connection failed: {e}")
            return False
        return True

    def initialize_elm327(self):
        self.send_command("ATZ")  # Reset ELM327
        self.send_command("ATE0")  # Echo Off
        self.send_command("ATSP0")  # Set Protocol to Auto
        print("ELM327 Initialized")

    def send_command(self, command):
        if self.serial_connection:
            self.serial_connection.write(f"{command}\r".encode())
            time.sleep(0.1)
            response = self.serial_connection.read_all().decode('utf-8').strip()
            return response
        return None

    def disconnect(self):
        if self.serial_connection:
            self.serial_connection.close()
            print("Serial connection closed")
