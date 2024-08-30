from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRectF

class GaugeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.minValue = 0
        self.maxValue = 100
        self.currentValue = 50
        self.units = "Km/h"
        self.gauge_color_outer_radius_factor = 0.9
        self.gauge_color_inner_radius_factor = 0.7
        self.scale_angle_start_value = 135
        self.scale_angle_size = 270
        self.enableBarGraph = False
        self.enableNeedlePolygon = True
        self.enableScaleText = True
        self.enableValueText = True
        self.enableBigScaleGrid = True
        self.enableFineScaleGrid = True

    def setMinValue(self, value):
        self.minValue = value
        self.update()

    def setMaxValue(self, value):
        self.maxValue = value
        self.update()

    def updateValue(self, value):
        self.currentValue = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()

        # Draw gauge background
        painter.setRenderHint(QPainter.Antialiasing)
        outer_radius = min(rect.width(), rect.height()) * self.gauge_color_outer_radius_factor / 2
        inner_radius = min(rect.width(), rect.height()) * self.gauge_color_inner_radius_factor / 2
        painter.setBrush(QColor("#222222"))
        painter.drawEllipse(rect.center(), outer_radius, outer_radius)

        # Draw gauge needle
        painter.setPen(QColor("#00FF00"))
        painter.drawLine(rect.center(), rect.topLeft())  # Simplified needle drawing

        # Draw current value text
        painter.setFont(QFont("Arial", 14))
        painter.drawText(rect, Qt.AlignCenter, f"{self.currentValue} {self.units}")
