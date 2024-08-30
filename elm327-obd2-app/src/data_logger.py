# src/data_logger.py

import time

class DataLogger:
    def __init__(self, log_file="vehicle_data.log"):
        self.log_file = log_file
        self.logging = False

    def start_logging(self):
        self.logging = True
        with open(self.log_file, 'a') as file:
            file.write(f"--- Logging started at {time.ctime()} ---\n")
        print("Logging started.")

    def log_data(self, data):
        if self.logging:
            with open(self.log_file, 'a') as file:
                file.write(f"{time.ctime()} - {data}\n")
            print(f"Logged data: {data}")

    def stop_logging(self):
        if self.logging:
            self.logging = False
            with open(self.log_file, 'a') as file:
                file.write(f"--- Logging stopped at {time.ctime()} ---\n")
            print("Logging stopped.")
