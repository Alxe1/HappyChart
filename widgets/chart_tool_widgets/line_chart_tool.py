from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_line_chart_tool import Ui_Form


class LineChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(LineChartToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        # X,Y轴数据
        self.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())
        # 颜色
        self.line_color = "#0000ff"
        self.line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.line_color)
        self.line_color_series_btn.clicked.connect(self.line_color_series_btn_clicked)
        self.line_color_series_line.editingFinished.connect(self.line_color_series_line_changed)
        # 线条类型
        self.line_types = (self.line_type_series_line.text().strip().split(",")
                          if self.line_type_series_line.text().strip() else [])
        self.line_type_series_line.textChanged.connect(self.line_type_series_line_changed)
        # 线宽
        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_spin_changed)
        # marker
        self.markers = (self.line_marker_series_line.text().strip().split(",")
                        if self.line_marker_series_line.text().strip() else [])
        self.line_marker_series_line.textChanged.connect(self.line_marker_series_line_changed)
        # marker size
        self.marker_size = self.line_marker_size_spin.value()
        self.line_marker_size_spin.valueChanged.connect(self.marker_size_spin_changed)
        # 路径
        self.path_checked = self.line_path_check.isChecked()
        self.line_path_check.stateChanged.connect(self.path_check_changed)
        self.path_interval = self.line_path_interval_spin.value()
        self.line_path_interval_spin.valueChanged.connect(self.path_interval_spin_changed)
        self.path_angle = self.line_path_angle_spin.value()
        self.line_path_angle_spin.valueChanged.connect(self.path_angle_spin_changed)
        # 值标签
        self.value_label_check = self.line_value_label_check.isChecked()
        self.line_value_label_check.stateChanged.connect(self.value_label_check_changed)
        self.value_labels_horiz_pos = self.line_value_label_horiz_pos_combo.currentText()
        self.line_value_label_horiz_pos_combo.currentTextChanged.connect(self.value_labels_horiz_pos_changed)
        self.value_label_vertic_pos = self.line_value_label_vertic_pos_combo.currentText()
        self.line_value_label_vertic_pos_combo.currentTextChanged.connect(self.value_label_vertic_pos_changed)
        self.value_label_interval = self.line_value_label_interval_spin.value()
        self.line_value_label_interval_spin.valueChanged.connect(self.value_label_interval_spin_changed)
        self.value_label_color = "#000000"
        self.line_value_label_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.value_label_color)
        self.line_value_label_color_series_btn.clicked.connect(self.line_value_label_color_series_btn_clicked)
        self.line_value_label_color_series_line.editingFinished.connect(self.value_label_color_series_line_changed)
        self.value_label_size = self.line_value_label_size_spin.value()
        self.line_value_label_size_spin.valueChanged.connect(self.value_label_size_spin_changed)

    def line_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        line_color = color_dialog.getColor()
        self.line_color = line_color.name(QColor.NameFormat.HexRgb)
        self.line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.line_color)

        colors = self.line_color_series_line.text()
        if colors == "":
            colors = self.line_color
        else:
            colors += "," + self.line_color
        self.line_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def line_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def line_type_series_line_changed(self, e):
        self.line_types = (e.strip().split(",") if e.strip() else [])
        self.parent.chart.update_plot()

    def line_width_spin_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def line_marker_series_line_changed(self, e):
        self.markers = (e.strip().split(",") if e.strip() else [])
        self.parent.chart.update_plot()

    def marker_size_spin_changed(self, e):
        self.marker_size = e
        self.parent.chart.update_plot()

    def path_check_changed(self, e):
        self.path_checked = self.line_path_check.isChecked()
        if self.path_checked:
            self.line_path_interval_spin.setEnabled(True)
            self.line_path_angle_spin.setEnabled(True)
        else:
            self.line_path_interval_spin.setEnabled(False)
            self.line_path_angle_spin.setEnabled(False)
        self.parent.chart.update_plot()

    def path_interval_spin_changed(self, e):
        self.path_interval = e
        self.parent.chart.update_plot()

    def path_angle_spin_changed(self, e):
        self.path_angle = e
        self.parent.chart.update_plot()

    def value_label_check_changed(self, e):
        self.value_label_check = self.line_value_label_check.isChecked()
        if self.value_label_check:
            self.line_value_label_horiz_pos_combo.setEnabled(True)
            self.line_value_label_vertic_pos_combo.setEnabled(True)
            self.line_value_label_interval_spin.setEnabled(True)
            self.line_value_label_color_series_btn.setEnabled(True)
            self.line_value_label_color_series_line.setEnabled(True)
            self.line_value_label_size_spin.setEnabled(True)
        else:
            self.line_value_label_horiz_pos_combo.setEnabled(False)
            self.line_value_label_vertic_pos_combo.setEnabled(False)
            self.line_value_label_interval_spin.setEnabled(False)
            self.line_value_label_color_series_btn.setEnabled(False)
            self.line_value_label_color_series_line.setEnabled(False)
            self.line_value_label_size_spin.setEnabled(False)
        self.parent.chart.update_plot()

    # def value_label_line_changed(self, e):
    #     self.value_labels = (e.strip().split(",") if e.strip() else [])
    #     self.parent.chart.update_plot()

    def value_labels_horiz_pos_changed(self, e):
        self.value_labels_horiz_pos = e
        self.parent.chart.update_plot()

    def value_label_vertic_pos_changed(self, e):
        self.value_label_vertic_pos = e
        self.parent.chart.update_plot()

    def value_label_interval_spin_changed(self, e):
        self.value_label_interval = e
        self.parent.chart.update_plot()

    def line_value_label_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        value_label_color = color_dialog.getColor()
        self.value_label_color = value_label_color.name(QColor.NameFormat.HexRgb)
        self.line_value_label_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.value_label_color)
        colors = self.line_value_label_color_series_line.text()
        if colors == "":
            colors = self.value_label_color
        else:
            colors += "," + self.value_label_color
        self.line_value_label_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def value_label_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def value_label_size_spin_changed(self, e):
        self.value_label_size = e
        self.parent.chart.update_plot()
