from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_errorbar_layer_tool import Ui_Form


class ErrorbarLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent=None, *args, **kwargs):
        super(ErrorbarLayerToolFrame, self).__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)

        # X,Y轴数据
        self.parent.chart_tool.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        if not self.parent.df.empty:
            cols = self.parent.df.columns.tolist()
            self.y_series_combo.clear()
            self.y_series_combo.addCheckableItems(cols)
            self.y_series_combo.setCurrentIndex(-1)

        self.errorbar_color = "#000000"
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.errorbar_color)
        self.color_series_btn.clicked.connect(self.color_series_btn_clicked)
        self.color_series_line.editingFinished.connect(self.color_series_line_changed)

        if not self.parent.df.empty:
            self.x_err_series_combo.addItem("none")
            self.x_err_series_combo.addItems(self.parent.df.columns.tolist())
            self.y_err_series_combo.addItem("none")
            self.y_err_series_combo.addItems(self.parent.df.columns.tolist())
        self.x_err_series = self.x_err_series_combo.currentText()
        self.x_err_series_combo.currentTextChanged.connect(self.x_err_series_combo_changed)
        self.y_err_series = self.y_err_series_combo.currentText()
        self.y_err_series_combo.currentTextChanged.connect(self.y_err_series_combo_changed)

        self.err_line_width = self.err_line_width_spin.value()
        self.err_line_width_spin.valueChanged.connect(self.err_line_width_changed)

        self.err_every = self.err_every_spin.value()
        self.err_every_spin.valueChanged.connect(self.err_every_changed)

        self.cap_size = self.cap_size_spin.value()
        self.cap_size_spin.valueChanged.connect(self.cap_size_changed)

        self.marker = self.marker_combo.currentText()
        self.marker_combo.currentTextChanged.connect(self.marker_changed)

        self.marker_size = self.marker_size_spin.value()
        self.marker_size_spin.valueChanged.connect(self.marker_size_changed)

        self.marker_edge_width = self.marker_edge_width_spin.value()
        self.marker_edge_width_spin.valueChanged.connect(self.marker_edge_width_changed)

        self.marker_edge_color = "#C00000"
        self.marker_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.marker_edge_color)
        self.marker_edge_color_btn.clicked.connect(self.marker_edge_color_btn_clicked)

        self.marker_face_color = "yellow"
        self.marker_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.marker_face_color)
        self.marker_face_color_btn.clicked.connect(self.marker_face_color_btn_clicked)

        self.line_style = self.linestyle_combo.currentText()
        self.linestyle_combo.currentTextChanged.connect(self.line_style_changed)

        self.line_color = "green"
        self.line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.line_color)
        self.line_color_btn.clicked.connect(self.line_color_btn_clicked)
        self.line_color_line.editingFinished.connect(self.line_color_line_changed)

        self.bars_above_checked = self.bars_above_check.isChecked()
        self.bars_above_check.stateChanged.connect(self.bars_above_checked_changed)

        self.lower_limits_checked = self.lower_limits_check.isChecked()
        self.lower_limits_check.stateChanged.connect(self.lower_limits_checked_changed)

        self.upper_limits_checked = self.upper_limits_check.isChecked()
        self.upper_limits_check.stateChanged.connect(self.upper_limits_checked_changed)

        self.xlower_limits_checked = self.xlower_limits_check.isChecked()
        self.xlower_limits_check.stateChanged.connect(self.xlower_limits_checked_changed)

        self.xupper_limits_checked = self.xupper_limits_check.isChecked()
        self.xupper_limits_check.stateChanged.connect(self.xupper_limits_checked_changed)

        # 删除按钮
        self.toolButton.clicked.connect(self.tool_button_clicked)

    def tool_button_clicked(self):
        widget = self.parent._tool_instances.pop(self._id)
        self.parent._tool_instances.insert(self._id, None)
        self.parent._chart_instances.pop(self._id)
        self.parent._chart_instances.insert(self._id, None)
        self.parent.chart.update_plot()
        widget.deleteLater()

    def color_series_btn_clicked(self, e):
        color = QColorDialog(self)
        errorbar_color = color.getColor()
        self.errorbar_color = errorbar_color.name(QColor.NameFormat.HexRgb)
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.errorbar_color)

        colors = self.color_series_line.text()
        if colors == "":
            colors = self.errorbar_color
        else:
            colors += "," + self.errorbar_color
        self.color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def color_series_line_changed(self):
        self.parent.chart.update_plot()

    def x_err_series_combo_changed(self, e):
        self.x_err_series = e
        self.parent.chart.update_plot()

    def y_err_series_combo_changed(self, e):
        self.y_err_series = e
        self.parent.chart.update_plot()

        # def err_color_btn_clicked(self, e):
        #     color = QColorDialog(self)
        #     err_color = color.getColor()
        #     self.err_color = err_color.name(QColor.NameFormat.HexRgb)
        #     self.err_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.err_color)
        #     self.parent.chart.update_plot()

    def err_line_width_changed(self, e):
        self.err_line_width = e
        self.parent.chart.update_plot()

    def err_every_changed(self, e):
        self.err_every = e
        self.parent.chart.update_plot()

    def cap_size_changed(self, e):
        self.cap_size = e
        self.parent.chart.update_plot()

        # def cap_thick_changed(self, e):
        #     self.cap_thick = e
        #     self.parent.chart.update_plot()

    def marker_changed(self, e):
        self.marker = e
        self.parent.chart.update_plot()

    def marker_size_changed(self, e):
        self.marker_size = e
        self.parent.chart.update_plot()

    def marker_edge_width_changed(self, e):
        self.marker_edge_width = e
        self.parent.chart.update_plot()

    def marker_edge_color_btn_clicked(self, e):
        color = QColorDialog(self)
        marker_edge_color = color.getColor()
        self.marker_edge_color = marker_edge_color.name(QColor.NameFormat.HexRgb)
        self.marker_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.marker_edge_color)
        self.parent.chart.update_plot()

    def marker_face_color_btn_clicked(self, e):
        color = QColorDialog(self)
        marker_face_color = color.getColor()
        self.marker_face_color = marker_face_color.name(QColor.NameFormat.HexRgb)
        self.marker_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.marker_face_color)
        self.parent.chart.update_plot()

    def line_style_changed(self, e):
        self.line_style = e
        self.parent.chart.update_plot()

    def line_color_btn_clicked(self, e):
        color = QColorDialog(self)
        line_color = color.getColor()
        self.line_color = line_color.name(QColor.NameFormat.HexRgb)
        self.line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.line_color)

        colors = self.line_color_line.text()
        if colors == "":
            colors = self.line_color
        else:
            colors += "," + self.line_color
        self.line_color_line.setText(colors)
        self.parent.chart.update_plot()

    def line_color_line_changed(self):
        self.parent.chart.update_plot()

    def bars_above_checked_changed(self, e):
        self.bars_above_checked = self.bars_above_check.isChecked()
        self.parent.chart.update_plot()

    def lower_limits_checked_changed(self, e):
        self.lower_limits_checked = self.lower_limits_check.isChecked()
        self.parent.chart.update_plot()

    def upper_limits_checked_changed(self, e):
        self.upper_limits_checked = self.upper_limits_check.isChecked()
        self.parent.chart.update_plot()

    def xlower_limits_checked_changed(self, e):
        self.xlower_limits_checked = self.xlower_limits_check.isChecked()
        self.parent.chart.update_plot()

    def xupper_limits_checked_changed(self, e):
        self.xupper_limits_checked = self.xupper_limits_check.isChecked()
        self.parent.chart.update_plot()
