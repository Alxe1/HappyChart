from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_radar_chart_tool import Ui_Form


class RadarChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(RadarChartToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        # 偏移量
        self.theta_offset = self.theta_offset_dial.value()
        self.theta_offset_dial.valueChanged.connect(self.theta_offset_changed)
        # 偏移方向
        self.theta_direction = self.theta_direction_combo.currentText()
        self.theta_direction_combo.currentTextChanged.connect(self.theta_direction_changed)

        # 边线宽度
        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_changed)

        # 边线类型
        self.line_type = self.line_type_combo.currentText()
        self.line_type_combo.currentTextChanged.connect(self.line_type_changed)

        # 边线颜色
        self.line_color = "#000000"
        self.radar_line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.line_color)
        self.radar_line_color_series_btn.clicked.connect(self.line_color_series_btn_clicked)
        self.radar_line_color_series_line.editingFinished.connect(self.radar_line_color_series_line_changed)

        # 填充颜色
        self.fill_color = "#ffffff"
        self.radar_fill_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.fill_color)
        self.radar_fill_color_series_btn.clicked.connect(self.radar_fill_color_series_btn_clicked)
        self.radar_fill_color_series_line.editingFinished.connect(self.radar_fill_color_series_line_changed)

        # 填充透明度
        self.fill_transparent = self.radar_fill_transparent_slider.value() / 100
        self.radar_fill_transparent_slider.valueChanged.connect(self.radar_fill_transparent_slider_changed)

        # 值标签
        self.value_label_checked = self.radar_value_label_check.isChecked()
        self.radar_value_label_check.checkStateChanged.connect(self.radar_value_label_checked_changed)
        self.value_label_interval = self.radar_value_label_interval_spin.value()
        self.radar_value_label_interval_spin.valueChanged.connect(self.value_label_interval_changed)
        self.value_label_color = "#000000"
        self.radar_value_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.value_label_color)
        self.radar_value_label_color_btn.clicked.connect(self.value_label_color_btn_clicked)
        self.value_labels_size = self.radar_value_label_size_spin.value()
        self.radar_value_label_size_spin.valueChanged.connect(self.value_labels_size_changed)

    def theta_offset_changed(self, e):
        self.theta_offset = e
        self.parent.chart.update_plot()

    def theta_direction_changed(self, e):
        self.theta_direction = e
        self.parent.chart.update_plot()

    def line_width_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def line_type_changed(self, e):
        self.line_type = e
        self.parent.chart.update_plot()

    def line_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        line_color = color_dialog.getColor()
        self.line_color = line_color.name(QColor.NameFormat.HexRgb)
        self.radar_line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.line_color)

        colors = self.radar_line_color_series_line.text()
        if colors == "":
            colors = self.line_color
        else:
            colors += "," + self.line_color
        self.radar_line_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def radar_line_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def radar_fill_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        fill_color = color_dialog.getColor()
        self.fill_color = fill_color.name(QColor.NameFormat.HexRgb)
        self.radar_fill_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.fill_color)

        colors = self.radar_fill_color_series_line.text()
        if colors == "":
            colors = self.fill_color
        else:
            colors += "," + self.fill_color
        self.radar_fill_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def radar_fill_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def radar_fill_transparent_slider_changed(self, e):
        self.fill_transparent = e / 100
        self.parent.chart.update_plot()

    def radar_value_label_checked_changed(self, e):
        self.value_label_checked = self.radar_value_label_check.isChecked()
        if self.value_label_checked:
            self.radar_value_label_interval_spin.setEnabled(True)
            self.radar_value_label_color_btn.setEnabled(True)
            self.radar_value_label_size_spin.setEnabled(True)
        else:
            self.radar_value_label_interval_spin.setEnabled(False)
            self.radar_value_label_color_btn.setEnabled(False)
            self.radar_value_label_size_spin.setEnabled(False)
        self.parent.chart.update_plot()

    def value_label_interval_changed(self, e):
        self.value_label_interval = e
        self.parent.chart.update_plot()

    def value_label_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        value_label_color = color_dialog.getColor()
        self.value_label_color = value_label_color.name(QColor.NameFormat.HexRgb)
        self.radar_value_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.value_label_color)
        self.parent.chart.update_plot()

    def value_labels_size_changed(self, e):
        self.value_labels_size = e
        self.parent.chart.update_plot()
