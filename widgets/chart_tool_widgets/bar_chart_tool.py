from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_bar_chart_tool import Ui_Form


class BarChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(BarChartToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        # 选择图表
        self.selected_bar = self.bar_selector_combo.currentText()
        self.bar_selector_combo.currentTextChanged.connect(self.bar_selector_combo_changed)

        # X,Y轴数据
        self.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        # 颜色
        self.bar_color = "#0000ff"
        self.base_chart_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bar_color)
        self.base_chart_color_series_btn.clicked.connect(self.base_chart_color_series_btn_clicked)
        # 颜色列表
        # self.color_list = []
        self.base_chart_color_series_line.editingFinished.connect(self.base_chart_color_series_line_changed)
        # 图表间隔
        self.bar_interval = self.base_chart_interval_spin.value()
        self.base_chart_interval_spin.valueChanged.connect(self.base_chart_interval_spin_changed)
        self.width = 1 - 2 * self.bar_interval
        # 误差数据
        self.y_err_cols = (self.y_err_series_line.text().strip().split(",")
                           if self.y_err_series_line.text().strip() else [])
        self.y_err_series_line.textChanged.connect(self.y_err_cols_changed)
        # 误差条颜色
        self.err_bar_color = "#000000"
        self.err_bar_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.err_bar_color)
        self.err_bar_color_btn.clicked.connect(self.err_bar_color_btn_clicked)
        # 值标签
        self.bar_value_label_checked = self.bar_value_label_check.isChecked()
        self.bar_value_label_check.stateChanged.connect(self.is_bar_value_label_checked)
        # 值标签系列
        self.bar_value_label_series = self.get_init_bar_value_label_series()
        self.bar_value_label_line.textChanged.connect(self.bar_value_label_series_changed)
        # 值标签间隔
        self.bar_value_label_interval = self.bar_value_label_interval_spin.value()
        self.bar_value_label_interval_spin.valueChanged.connect(self.bar_value_label_interval_changed)
        # 值标签颜色
        self.bar_value_label_color = "#000000"
        self.bar_value_label_color_btn.setStyleSheet(
            "QToolButton{background-color: %s ;}" % self.bar_value_label_color)
        self.bar_value_label_color_btn.clicked.connect(self.bar_value_label_color_btn_clicked)
        # 值标签大小
        self.bar_value_label_size = self.bar_value_label_size_spin.value()
        self.bar_value_label_size_spin.valueChanged.connect(self.bar_value_label_size_changed)

    def bar_selector_combo_changed(self, e):
        self.selected_bar = e
        self.parent.chart.update_plot()

    def base_chart_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bar_color = color_dialog.getColor()
        self.bar_color = bar_color.name(QColor.NameFormat.HexRgb)
        self.base_chart_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bar_color)

        colors = self.base_chart_color_series_line.text()
        if colors == "":
            colors = self.bar_color
        else:
            colors += "," + self.bar_color
        self.base_chart_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def base_chart_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def base_chart_interval_spin_changed(self, e):
        self.bar_interval = e
        self.width = 1 - 2 * self.bar_interval
        self.parent.chart.update_plot()

    def y_err_cols_changed(self, e):
        self.y_err_cols = (e.strip().split(",") if e.strip() else [])
        self.parent.chart.update_plot()

    def err_bar_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        err_bar_color = color_dialog.getColor()
        self.err_bar_color = err_bar_color.name(QColor.NameFormat.HexRgb)
        self.err_bar_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.err_bar_color)
        self.parent.chart.update_plot()

    def is_bar_value_label_checked(self, e):
        self.bar_value_label_checked = self.bar_value_label_check.isChecked()
        if self.bar_value_label_checked:
            self.bar_value_label_line.setEnabled(True)
            self.bar_value_label_interval_spin.setEnabled(True)
            self.bar_value_label_color_btn.setEnabled(True)
            self.bar_value_label_size_spin.setEnabled(True)
        else:
            self.bar_value_label_line.setEnabled(False)
            self.bar_value_label_interval_spin.setEnabled(False)
            self.bar_value_label_color_btn.setEnabled(False)
            self.bar_value_label_size_spin.setEnabled(False)
        self.parent.chart.update_plot()

    def get_init_bar_value_label_series(self):
        bar_value_label_series = []
        if self.bar_value_label_line.text().strip():
            labels = self.bar_value_label_line.text().strip().split(";")
            for text in labels:
                _labels = text.split(",")
                bar_value_label_series.append(_labels)

        return bar_value_label_series

    def bar_value_label_series_changed(self, e):
        if e.strip():
            self.bar_value_label_series = []
            labels = e.strip().split(";")
            for text in labels:
                _labels = text.split(",")
                self.bar_value_label_series.append(_labels)
        else:
            self.bar_value_label_series = []

        self.parent.chart.update_plot()

    def bar_value_label_interval_changed(self, e):
        self.bar_value_label_interval = e
        self.parent.chart.update_plot()

    def bar_value_label_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bar_value_label_color = color_dialog.getColor()
        self.bar_value_label_color = bar_value_label_color.name(QColor.NameFormat.HexRgb)
        self.bar_value_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bar_value_label_color)
        self.parent.chart.update_plot()

    def bar_value_label_size_changed(self, e):
        self.bar_value_label_size = e
        self.parent.chart.update_plot()
