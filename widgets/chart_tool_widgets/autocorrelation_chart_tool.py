from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_autocorrelation_chart_tool import Ui_Form


class AutoCorrelationChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(AutoCorrelationChartToolFrame, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())

        self.use_vline_checked = self.use_vline_check.isChecked()
        self.use_vline_check.stateChanged.connect(self.use_vline_check_changed)

        self.vline_color = "k"
        self.vline_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.vline_color)
        self.vline_color_btn.clicked.connect(self.vline_color_btn_clicked)

        self.vline_style = self.vline_style_combo.currentText()
        self.vline_style_combo.currentTextChanged.connect(self.vline_style_combo_changed)

        self.vline_width = self.vline_width_spin.value()
        self.vline_width_spin.valueChanged.connect(self.vline_width_spin_changed)

        self.hline_color = "k"
        self.hline_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.hline_color)
        self.hline_color_btn.clicked.connect(self.hline_color_btn_clicked)

        self.hline_style = self.hline_style_combo.currentText()
        self.hline_style_combo.currentTextChanged.connect(self.hline_style_combo_changed)

        self.hline_width = self.hline_width_spin.value()
        self.hline_width_spin.valueChanged.connect(self.hline_width_spin_changed)

        self.norm_checked = self.norm_check.isChecked()
        self.norm_check.stateChanged.connect(self.norm_check_changed)

        self.max_lag = self.max_lag_spin.value()
        self.max_lag_spin.valueChanged.connect(self.max_lag_spin_changed)

    def use_vline_check_changed(self, e):
        self.use_vline_checked = self.use_vline_check.isChecked()
        self.parent.chart.update_plot()

    def vline_color_btn_clicked(self, e):
        color = QColorDialog(self)
        vline_color = color.getColor()
        self.vline_color = vline_color.name(QColor.NameFormat.HexRgb)
        self.vline_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.vline_color)
        self.parent.chart.update_plot()

    def vline_style_combo_changed(self, e):
        self.vline_style = e
        self.parent.chart.update_plot()

    def vline_width_spin_changed(self, e):
        self.vline_width = e
        self.parent.chart.update_plot()

    def hline_color_btn_clicked(self, e):
        color = QColorDialog(self)
        hline_color = color.getColor()
        self.hline_color = hline_color.name(QColor.NameFormat.HexRgb)
        self.hline_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.hline_color)
        self.parent.chart.update_plot()

    def hline_style_combo_changed(self, e):
        self.hline_style = e
        self.parent.chart.update_plot()

    def hline_width_spin_changed(self, e):
        self.hline_width = e
        self.parent.chart.update_plot()

    def norm_check_changed(self, e):
        self.norm_checked = self.norm_check.isChecked()
        self.parent.chart.update_plot()

    def max_lag_spin_changed(self, e):
        self.max_lag = e
        self.parent.chart.update_plot()
