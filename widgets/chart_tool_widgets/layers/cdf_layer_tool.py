from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_cdf_layer_tool import Ui_Form


class CDFLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent=None, *args, **kwargs):
        super(CDFLayerToolFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        if not self.parent.df.empty:
            cols = self.parent.df.columns.tolist()
            self.y_series_combo.clear()
            self.y_series_combo.addCheckableItems(cols)
            self.y_series_combo.setCurrentIndex(-1)

        self.cdf_color = "black"
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.cdf_color)
        self.color_series_btn.clicked.connect(self.color_series_btn_changed)
        self.color_series_line.editingFinished.connect(self.color_series_line_changed)

        self.complementary_checked = self.complementary_check.isChecked()
        self.complementary_check.clicked.connect(self.complementary_check_changed)

        self.compress_checked = self.compress_check.isChecked()
        self.compress_check.clicked.connect(self.compress_check_changed)

        self.orientation = self.orientation_combo.currentText()
        self.orientation_combo.currentTextChanged.connect(self.orientation_combo_changed)

        self.line_style = self.line_style_combo.currentText()
        self.line_style_combo.currentTextChanged.connect(self.line_style_changed)

        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_changed)

        self.transparency = self.transparency_slider.value() / 100
        self.transparency_slider.valueChanged.connect(self.transparency_slider_changed)

        # 删除按钮
        self.toolButton.clicked.connect(self.tool_button_clicked)

    def tool_button_clicked(self):
        widget = self.parent._tool_instances.pop(self._id)
        self.parent._tool_instances.insert(self._id, None)
        self.parent._chart_instances.pop(self._id)
        self.parent._chart_instances.insert(self._id, None)
        self.parent.chart.update_plot()
        widget.deleteLater()

    def color_series_btn_changed(self, e):
        color = QColorDialog(self)
        cdf_color = color.getColor()
        self.cdf_color = cdf_color.name(QColor.NameFormat.HexRgb)
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.cdf_color)

        colors = self.color_series_line.text()
        if colors == "":
            colors = self.cdf_color
        else:
            colors += "," + self.cdf_color
        self.color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def color_series_line_changed(self):
        self.parent.chart.update_plot()

    def complementary_check_changed(self, e):
        self.complementary_checked = self.complementary_check.isChecked()
        self.parent.chart.update_plot()

    def compress_check_changed(self, e):
        self.compress_checked = self.compress_check.isChecked()
        self.parent.chart.update_plot()

    def orientation_combo_changed(self, e):
        self.orientation = e
        self.parent.chart.update_plot()

    def line_style_changed(self, e):
        self.line_style = e
        self.parent.chart.update_plot()

    def line_width_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()
