from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_event_chart_tool import Ui_Form


class EventChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(EventChartToolFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        self.orientation = self.orientation_combo.currentText()
        self.orientation_combo.currentTextChanged.connect(self.orientation_changed)

        self.colors = "k"
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.colors)
        self.color_series_btn.clicked.connect(self.color_series_btn_changed)
        self.color_series_line.textChanged.connect(self.color_series_line_changed)

        self.line_offset = self.line_offset_spin.value()
        self.line_offset_spin.valueChanged.connect(self.line_offset_spin_changed)

        self.line_length = self.line_length_spin.value()
        self.line_length_spin.valueChanged.connect(self.line_length_spin_changed)

        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_spin_changed)

        self.transparency = self.transparency_slider.value() / 100
        self.transparency_slider.valueChanged.connect(self.transparency_slider_changed)

        self.line_style = self.line_style_combo.currentText()
        self.line_style_combo.currentTextChanged.connect(self.line_style_combo_changed)

    def orientation_changed(self, e):
        self.orientation = e
        self.parent.chart.update_plot()

    def color_series_btn_changed(self, e):
        color = QColorDialog(self)
        _color = color.getColor()
        self.colors = _color.name(QColor.NameFormat.HexRgb)
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.colors)

        colors = self.color_series_line.text()
        if colors == "":
            colors = self.colors
        else:
            colors += "," + self.colors
        self.color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def color_series_line_changed(self, e):
        self.parent.chart.update_plot()

    def line_offset_spin_changed(self, e):
        self.line_offset = e
        self.parent.chart.update_plot()

    def line_length_spin_changed(self, e):
        self.line_length = e
        self.parent.chart.update_plot()

    def line_width_spin_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()

    def line_style_combo_changed(self, e):
        self.line_style = e
        self.parent.chart.update_plot()
