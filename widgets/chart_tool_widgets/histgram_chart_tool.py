from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_histgram_chart_tool import Ui_Form


class HistgramChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(HistgramChartToolFrame, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        self.bin_num = self.bin_num_spin.value()
        self.bin_num_spin.valueChanged.connect(self.bin_num_changed)

        self.bin_range_min = self.bin_range_min_spin.value()
        self.bin_range_min_spin.valueChanged.connect(self.bin_range_min_changed)
        self.bin_range_max = self.bin_range_max_spin.value()
        self.bin_range_max_spin.valueChanged.connect(self.bin_range_max_changed)

        self.bihist_checked = self.bihist_check.isChecked()
        self.bihist_check.stateChanged.connect(self.bihist_changed)

        self.density_checked = self.density_check.isChecked()
        self.density_check.stateChanged.connect(self.density_changed)

        self.cumulative_checked = self.cumulative_check.isChecked()
        self.cumulative_check.stateChanged.connect(self.cumulative_changed)

        self.log_checked = self.log_check.isChecked()
        self.log_check.stateChanged.connect(self.log_changed)

        self.bottom_distance = self.bottom_distance_spin.value()
        self.bottom_distance_spin.valueChanged.connect(self.bottom_distance_changed)

        self.hist_type = self.hist_type_combo.currentText()
        self.hist_type_combo.currentTextChanged.connect(self.hist_type_changed)

        self.align = self.align_combo.currentText()
        self.align_combo.currentTextChanged.connect(self.align_changed)

        self.orientation = self.orientation_combo.currentText()
        self.orientation_combo.currentTextChanged.connect(self.orientation_changed)

        self.hist_color = "#0000ff"
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.hist_color)
        self.color_series_btn.clicked.connect(self.color_series_changed)
        self.color_series_line.editingFinished.connect(self.color_series_line_changed)

        self.stacked_checked = self.stacked_check.isChecked()
        self.stacked_check.stateChanged.connect(self.stacked_changed)

        self.transparency = self.transparent_slider.value() / 100
        self.transparent_slider.valueChanged.connect(self.transparent_slider_changed)

    def bin_num_changed(self, e):
        self.bin_num = e
        self.parent.chart.update_plot()

    def bin_range_min_changed(self, e):
        self.bin_range_min = e
        self.parent.chart.update_plot()

    def bin_range_max_changed(self, e):
        self.bin_range_max = e
        self.parent.chart.update_plot()

    def bihist_changed(self, e):
        self.bihist_checked = self.bihist_check.isChecked()
        self.parent.chart.update_plot()

    def density_changed(self, e):
        self.density_checked = self.density_check.isChecked()
        self.parent.chart.update_plot()

    def cumulative_changed(self, e):
        self.cumulative_checked = self.cumulative_check.isChecked()
        self.parent.chart.update_plot()

    def log_changed(self, e):
        self.log_checked = self.log_check.isChecked()
        self.parent.chart.update_plot()

    def bottom_distance_changed(self, e):
        self.bottom_distance = e
        self.parent.chart.update_plot()

    def hist_type_changed(self, e):
        self.hist_type = e
        self.parent.chart.update_plot()

    def align_changed(self, e):
        self.align = e
        self.parent.chart.update_plot()

    def orientation_changed(self, e):
        self.orientation = e
        self.parent.chart.update_plot()

    def color_series_changed(self, e):
        color_dialog = QColorDialog(self)
        hist_color = color_dialog.getColor()
        self.hist_color = hist_color.name(QColor.NameFormat.HexRgb)
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.hist_color)

        colors = self.color_series_line.text()
        if colors == "":
            colors = self.hist_color
        else:
            colors += "," + self.hist_color
        self.color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def color_series_line_changed(self):
        self.parent.chart.update_plot()

    def stacked_changed(self, e):
        self.stacked_checked = self.stacked_check.isChecked()
        self.parent.chart.update_plot()

    def transparent_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()
