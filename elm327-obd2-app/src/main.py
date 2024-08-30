import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from HomeScreen import HomeScreen
from DashboardScreen import DashboardScreen
from EcuTuningScreen import EcuTuningScreen
from SettingsScreen import SettingsScreen
from LiveDataScreen import LiveDataScreen
from AllSensorsScreen import AllSensorsScreen
from DiagnosticTroubleCodesScreenModule import DiagnosticTroubleCodesScreen
from FreezeFrameScreen import FreezeFrameScreen
from NonContinuousMonitorsScreen import NonContinuousMonitorsScreen
from GarageScreen import GarageScreen
from StatisticsScreen import StatisticsScreen
from EcuIdentifiersScreen import EcuIdentifiersScreen
from DataRecordingScreen import DataRecordingScreen
from AccelerationTestsScreen import AccelerationTestsScreen
from EmissionTestScreen import EmissionTestScreen
from TerminalScreen import TerminalScreen
from GaugeScreen import GaugeScreen

class MyScreenManager(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.home_screen = HomeScreen(self)
        self.dashboard_screen = DashboardScreen(self)
        self.ecu_tuning_screen = EcuTuningScreen(self)
        self.settings_screen = SettingsScreen(self)
        self.live_data_screen = LiveDataScreen(self)
        self.all_sensors_screen = AllSensorsScreen(self)
        self.diagnostic_trouble_codes_screen = DiagnosticTroubleCodesScreen(self)
        self.freeze_frame_screen = FreezeFrameScreen(self)
        self.non_continuous_monitors_screen = NonContinuousMonitorsScreen(self)
        self.garage_screen = GarageScreen(self)
        self.statistics_screen = StatisticsScreen(self)
        self.ecu_identifiers_screen = EcuIdentifiersScreen(self)
        self.data_recording_screen = DataRecordingScreen(self)
        self.acceleration_tests_screen = AccelerationTestsScreen(self)
        self.emission_test_screen = EmissionTestScreen(self)
        self.terminal_screen = TerminalScreen(self)
        self.gauge_screen = GaugeScreen(self)

        self.addWidget(self.home_screen)
        self.addWidget(self.dashboard_screen)
        self.addWidget(self.ecu_tuning_screen)
        self.addWidget(self.settings_screen)
        self.addWidget(self.live_data_screen)
        self.addWidget(self.all_sensors_screen)
        self.addWidget(self.diagnostic_trouble_codes_screen)
        self.addWidget(self.freeze_frame_screen)
        self.addWidget(self.non_continuous_monitors_screen)
        self.addWidget(self.garage_screen)
        self.addWidget(self.statistics_screen)
        self.addWidget(self.ecu_identifiers_screen)
        self.addWidget(self.data_recording_screen)
        self.addWidget(self.acceleration_tests_screen)
        self.addWidget(self.emission_test_screen)
        self.addWidget(self.terminal_screen)
        self.addWidget(self.gauge_screen)

        self.setCurrentWidget(self.home_screen)  

    def go_home(self):
        self.setCurrentWidget(self.home_screen)

    def go_to_dashboard(self):
        self.setCurrentWidget(self.dashboard_screen)

    def go_to_ecu_tuning(self):
        self.setCurrentWidget(self.ecu_tuning_screen)

    def go_to_settings(self):
        self.setCurrentWidget(self.settings_screen)

    def go_to_live_data(self):
        self.setCurrentWidget(self.live_data_screen)

    def go_to_all_sensors(self):
        self.setCurrentWidget(self.all_sensors_screen)

    def go_to_diagnostic_trouble_codes(self):
        self.setCurrentWidget(self.diagnostic_trouble_codes_screen)

    def go_to_freeze_frame(self):
        self.setCurrentWidget(self.freeze_frame_screen)

    def go_to_non_continuous_monitors(self):
        self.setCurrentWidget(self.non_continuous_monitors_screen)

    def go_to_garage(self):
        self.setCurrentWidget(self.garage_screen)

    def go_to_statistics(self):
        self.setCurrentWidget(self.statistics_screen)

    def go_to_ecu_identifiers(self):
        self.setCurrentWidget(self.ecu_identifiers_screen)

    def go_to_data_recording(self):
        self.setCurrentWidget(self.data_recording_screen)

    def go_to_acceleration_tests(self):
        self.setCurrentWidget(self.acceleration_tests_screen)

    def go_to_emission_test(self):
        self.setCurrentWidget(self.emission_test_screen)

    def go_to_terminal(self):
        self.setCurrentWidget(self.terminal_screen)

    def go_to_gauge_screen(self):
        self.setCurrentWidget(self.gauge_screen)

class ELM327App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ELM327 PyQt App")
        self.setGeometry(100, 100, 800, 600)

        self.screen_manager = MyScreenManager(self)
        self.setCentralWidget(self.screen_manager)

    def apply_color_settings(self, color_settings):
        for i in range(self.screen_manager.count()):
            widget = self.screen_manager.widget(i)
            if isinstance(widget, QWidget):  
                widget.setStyleSheet(f"background-color: {color_settings['background-color']}; color: {color_settings['text-color']};")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ELM327App()
    window.show()
    sys.exit(app.exec_())
