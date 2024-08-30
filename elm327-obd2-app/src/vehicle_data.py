import random
import time
from threading import Thread

class VehicleDataSimulator:
    def __init__(self, gauges):
        self.running = False
        self.rpm = 0
        self.speed = 0
        self.temp = 0
        self.gauges = gauges

    def start(self):
        self.running = True
        thread = Thread(target=self.generate_data)
        thread.start()

    def generate_data(self):
        while self.running:
            self.rpm = random.uniform(800, 6400)
            self.speed = random.uniform(0, 120)
            self.temp = random.uniform(20, 100)
            print(f"Generated data - RPM: {self.rpm}, Speed: {self.speed}, Temp: {self.temp}")
            self.update_gauges()
            time.sleep(1)

    def update_gauges(self):
        self.gauges["rpm"].setText(f"RPM: {self.rpm:.2f}")
        self.gauges["speed"].setText(f"Speed: {self.speed:.2f}")
        self.gauges["temp"].setText(f"Temp: {self.temp:.2f}")
