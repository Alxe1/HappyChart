from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_stem_chart_tool import Ui_Form


class StemChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(StemChartToolFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        # 茎线颜色
        self.base_line_color = "#0000ff"
        self.base_line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.base_line_color)
        self.base_line_color_series_btn.clicked.connect(self.base_line_color_series_btn_clicked)
        self.base_line_color_series_line.editingFinished.connect(self.base_line_color_series_line_changed)
        # 茎线类型
        self.base_line_type = self.base_line_type_combo.currentText()
        self.base_line_type_combo.currentTextChanged.connect(self.base_line_type_changed)

        # 叶线颜色
        self.stem_line_color = "#0000ff"
        self.stem_line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.stem_line_color)
        self.stem_line_color_series_btn.clicked.connect(self.stem_line_color_series_btn_clicked)
        self.stem_line_color_series_line.editingFinished.connect(self.stem_line_color_series_line_changed)
        # 叶线类型
        self.stem_line_type = self.stem_line_type_combo.currentText()
        self.stem_line_type_combo.currentTextChanged.connect(self.stem_line_type_changed)

        # marker 颜色
        self.marker_color = "#0000ff"
        self.marker_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.marker_color)
        self.marker_color_series_btn.clicked.connect(self.marker_color_series_btn_clicked)
        self.marker_color_series_line.editingFinished.connect(self.marker_color_series_line_changed)
        # marker 类型
        self.marker_type = self.marker_type_combo.currentText()
        self.marker_type_combo.currentTextChanged.connect(self.marker_type_changed)

        # 值标签
        self.value_label_checked = self.stem_value_label_check.isChecked()
        self.stem_value_label_check.checkStateChanged.connect(self.value_label_checked_changed)
        # 值标签系列
        self.value_labels = self.stem_value_label_line.text()
        self.stem_value_label_line.textChanged.connect(self.value_labels_changed)
        # 值标签间隔
        self.value_label_interval = self.stem_value_label_interval_spin.value()
        self.stem_value_label_interval_spin.valueChanged.connect(self.value_label_interval_changed)
        # 值标签颜色
        self.value_label_color = "#0000ff"
        self.stem_value_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.value_label_color)
        self.stem_value_label_color_btn.clicked.connect(self.value_label_color_btn_clicked)
        # 值标签大小
        self.value_label_size = self.stem_value_label_size_spin.value()
        self.stem_value_label_size_spin.valueChanged.connect(self.value_label_size_changed)

    def base_line_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        base_line_color = color_dialog.getColor()
        self.base_line_color = base_line_color.name(QColor.NameFormat.HexRgb)
        self.base_line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.base_line_color)

        colors = self.base_line_color_series_line.text()
        if colors == "":
            colors = self.base_line_color
        else:
            colors += "," + self.base_line_color
        self.base_line_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def base_line_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def base_line_type_changed(self, e):
        self.base_line_type = e
        self.parent.chart.update_plot()

    def stem_line_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        stem_line_color = color_dialog.getColor()
        self.stem_line_color = stem_line_color.name(QColor.NameFormat.HexRgb)
        self.stem_line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.stem_line_color)

        colors = self.stem_line_color_series_line.text()
        if colors == "":
            colors = self.stem_line_color
        else:
            colors += "," + self.stem_line_color
        self.stem_line_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def stem_line_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def stem_line_type_changed(self, e):
        self.stem_line_type = e
        self.parent.chart.update_plot()

    def marker_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        marker_color = color_dialog.getColor()
        self.marker_color = marker_color.name(QColor.NameFormat.HexRgb)
        self.marker_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.marker_color)

        colors = self.marker_color_series_line.text()
        if colors == "":
            colors = self.marker_color
        else:
            colors += "," + self.marker_color
        self.marker_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def marker_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def marker_type_changed(self, e):
        self.marker_type = e
        self.parent.chart.update_plot()

    def value_label_checked_changed(self, e):
        self.value_label_checked = self.stem_value_label_check.isChecked()
        if self.value_label_checked:
            self.stem_value_label_line.setEnabled(True)
            self.stem_value_label_interval_spin.setEnabled(True)
            self.stem_value_label_color_btn.setEnabled(True)
            self.stem_value_label_size_spin.setEnabled(True)
        else:
            self.stem_value_label_line.setEnabled(False)
            self.stem_value_label_interval_spin.setEnabled(False)
            self.stem_value_label_color_btn.setEnabled(False)
            self.stem_value_label_size_spin.setEnabled(False)
        self.parent.chart.update_plot()

    def value_labels_changed(self, e):
        self.value_labels = e
        self.parent.chart.update_plot()

    def value_label_interval_changed(self, e):
        self.value_label_interval = e
        self.parent.chart.update_plot()

    def value_label_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        value_label_color = color_dialog.getColor()
        self.value_label_color = value_label_color.name(QColor.NameFormat.HexRgb)
        self.stem_value_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.value_label_color)
        self.parent.chart.update_plot()

    def value_label_size_changed(self, e):
        self.value_label_size = e
        self.parent.chart.update_plot()
