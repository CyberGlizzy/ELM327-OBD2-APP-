# gui.py

import asyncio  # Import asyncio at the top of the file
import logging
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from src.CustomButton import CustomButton
from src.GaugeScreen import Gauge
from vehicle_data import VehicleDataSimulator
from bluetooth_ble_connection import ELM327BLE
from bluetooth_serial_connection import ELM327Serial

# Set up logging configuration
logging.basicConfig(filename='elm327_app.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

class Dashboard(BoxLayout):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 20

        # Set up connection and logging
        logging.info("Initializing Dashboard...")

        # Choose connection method (BLE or Serial)
        self.connection_method = 'BLE'  # Change this to 'Serial' if using serial communication

        if self.connection_method == 'BLE':
            self.bt_address = "XX:XX:XX:XX:XX:XX"  # Replace with your BLE MAC address
            self.elm327 = ELM327BLE(self.bt_address)
        else:
            self.port = "COMx"  # Replace with your COM port for serial communication
            self.elm327 = ELM327Serial(self.port)

        # Initialize connection
        if self.connection_method == 'BLE':
            try:
                asyncio.run(self.elm327.connect())
                logging.info("BLE connection established")
            except Exception as e:
                logging.error(f"Failed to establish BLE connection: {e}")
        else:
            if self.elm327.connect():
                logging.info("Serial connection established")
            else:
                logging.error("Failed to establish serial connection")

        # Add a title
        title = Label(text="Car Tuning Dashboard", color=[1, 1, 1, 1], font_size='24sp')
        self.add_widget(title)

        # Add the gauges
        self.gauge_layout = BoxLayout(orientation='horizontal', spacing=20)
        self.rpm_gauge = Gauge(min_value=0, max_value=7000, label="RPM")
        self.speed_gauge = Gauge(min_value=0, max_value=160, label="Speed")
        self.temp_gauge = Gauge(min_value=0, max_value=250, label="Temp")

        self.gauge_layout.add_widget(self.rpm_gauge)
        self.gauge_layout.add_widget(self.speed_gauge)
        self.gauge_layout.add_widget(self.temp_gauge)

        self.add_widget(self.gauge_layout)

        # Add buttons for actions like start/stop logging, tuning, etc.
        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=50)

        start_button = CustomButton(text="Start Logging")
        start_button.bind(on_press=self.start_logging)
        button_layout.add_widget(start_button)

        tune_button = CustomButton(text="Tune ECU")
        tune_button.bind(on_press=self.tune_ecu)
        button_layout.add_widget(tune_button)

        add_gauge_button = CustomButton(text="Add Gauge")
        add_gauge_button.bind(on_press=self.add_gauge)
        button_layout.add_widget(add_gauge_button)

        self.add_widget(button_layout)

        # Simulated data for now
        self.simulator = VehicleDataSimulator()
        self.simulator.start({
            'rpm': self.rpm_gauge,
            'speed': self.speed_gauge,
            'temp': self.temp_gauge
        })

        # Build ECU tuning interface
        self.build_ecu_tuning_interface()

    def start_logging(self, instance):
        logging.info("Logging started...")
        print("Logging started...")

    def tune_ecu(self, instance):
        logging.info("ECU Tuning started...")
        print("ECU Tuning started...")

    def add_gauge(self, instance):
        new_gauge = Gauge(min_value=0, max_value=100, label="New Gauge")
        self.gauge_layout.add_widget(new_gauge)
        logging.info("New gauge added")

    def remove_gauge(self, instance):
        if self.gauge_layout.children:
            self.gauge_layout.remove_widget(self.gauge_layout.children[-1])
            logging.info("Gauge removed")

    def update_from_elm327(self):
        # Simulate ELM327 responses for now
        if self.connection_method == 'BLE':
            rpm = "1C40"  # Example simulated hex response for RPM (7200 RPM)
            speed = "0032"  # Example simulated hex response for Speed (50 km/h)
            temp = "005A"  # Example simulated hex response for Temp (90°C)
        else:
            rpm = "1C40"  # Simulated hex response for RPM (7200 RPM)
            speed = "0032"  # Simulated hex response for Speed (50 km/h)
            temp = "005A"  # Simulated hex response for Temp (90°C)

        logging.info(f"Simulated RPM: {rpm}, Speed: {speed}, Temp: {temp}")

        if rpm:
            self.rpm_gauge.value = int(rpm, 16) // 4  # Convert to RPM
            logging.info(f"RPM updated to {self.rpm_gauge.value}")

        if speed:
            self.speed_gauge.value = int(speed, 16)  # Convert to Speed
            logging.info(f"Speed updated to {self.speed_gauge.value}")

        if temp:
            self.temp_gauge.value = int(temp, 16) - 40  # Convert to Celsius
            logging.info(f"Temp updated to {self.temp_gauge.value}")

    def build_ecu_tuning_interface(self):
        # Create a layout for the ECU tuning interface
        tuning_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Add labels and input fields for different parameters
        rpm_label = Label(text="Set RPM", color=[1, 1, 1, 1], font_size='18sp')
        self.rpm_input = TextInput(text="", multiline=False, size_hint=(1, None), height=40)
        
        speed_label = Label(text="Set Speed", color=[1, 1, 1, 1], font_size='18sp')
        self.speed_input = TextInput(text="", multiline=False, size_hint=(1, None), height=40)
        
        temp_label = Label(text="Set Temperature", color=[1, 1, 1, 1], font_size='18sp')
        self.temp_input = TextInput(text="", multiline=False, size_hint=(1, None), height=40)
        
        # Add a submit button to send the commands
        submit_button = CustomButton(text="Submit Changes", size_hint=(1, None), height=50)
        submit_button.bind(on_press=self.submit_tuning_changes)
        
        # Add the labels and inputs to the layout
        tuning_layout.add_widget(rpm_label)
        tuning_layout.add_widget(self.rpm_input)
        tuning_layout.add_widget(speed_label)
        tuning_layout.add_widget(self.speed_input)
        tuning_layout.add_widget(temp_label)
        tuning_layout.add_widget(self.temp_input)
        tuning_layout.add_widget(submit_button)
        
        # Add the tuning layout to the main dashboard
        self.add_widget(tuning_layout)

    def submit_tuning_changes(self, instance):
        # Simulate sending tuning changes to the ELM327
        rpm_value = self.rpm_input.text
        speed_value = self.speed_input.text
        temp_value = self.temp_input.text
        
        logging.info(f"Submitting tuning changes: RPM={rpm_value}, Speed={speed_value}, Temp={temp_value}")
        
        # Simulate sending these values to the ELM327 (replace with actual send_command when ready)
        if self.connection_method == 'BLE':
            asyncio.run(self.elm327.send_command(f"AT+RPM={rpm_value}"))
            asyncio.run(self.elm327.send_command(f"AT+SPD={speed_value}"))
            asyncio.run(self.elm327.send_command(f"AT+TEMP={temp_value}"))
        else:
            self.elm327.send_command(f"AT+RPM={rpm_value}")
            self.elm327.send_command(f"AT+SPD={speed_value}")
            self.elm327.send_command(f"AT+TEMP={temp_value}")

class ELM327App(App):
    def build(self):
        return Dashboard()

if __name__ == '__main__':
    ELM327App().run()

