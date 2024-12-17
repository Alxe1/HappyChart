from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_density_layer_tool import Ui_Form


class DensityLayerToolFrame(QFrame, Ui_Form):
    _id = None
    def __init__(self, parent=None, *args, **kwargs):
        super(DensityLayerToolFrame, self).__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)

        self.parent.chart_tool.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        if not self.parent.df.empty:
            cols = self.parent.df.columns.tolist()
            self.y_series_combo.clear()
            self.y_series_combo.addCheckableItems(cols)
            self.y_series_combo.setCurrentIndex(-1)

        self.density_color = "C0"
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.density_color)
        self.color_series_btn.clicked.connect(self.color_series_btn_changed)
        self.color_series_line.editingFinished.connect(self.color_series_line_changed)

        self.bw_method = self.bw_method_combo.currentText()
        self.bw_method_combo.currentTextChanged.connect(self.bw_method_combo_changed)

        self.line_style = self.linestyle_combo.currentText()
        self.linestyle_combo.currentTextChanged.connect(self.line_style_changed)

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
        density_color = color.getColor()
        self.density_color = density_color.name(QColor.NameFormat.HexRgb)
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.density_color)

        colors = self.color_series_line.text()
        if colors == "":
            colors = self.density_color
        else:
            colors += "," + self.density_color
        self.color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def color_series_line_changed(self):
        self.parent.chart.update_plot()

    def bw_method_combo_changed(self, e):
        self.bw_method = e
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
