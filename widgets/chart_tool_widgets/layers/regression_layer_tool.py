from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_regression_layer_tool import Ui_Form


class RegressionLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent, *args, **kwargs):
        super(RegressionLayerToolFrame, self).__init__(parent=parent, *args, **kwargs)
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

        self.line_color = "black"
        self.line_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.line_color)
        self.line_color_series_btn.clicked.connect(self.line_color_series_btn_changed)
        self.line_color_series_line.editingFinished.connect(self.line_color_series_line_changed)

        self.line_style = self.line_style_combo.currentText()
        self.line_style_combo.currentTextChanged.connect(self.line_style_changed)

        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_changed)

        self.line_transparency = self.line_transparency_slider.value() / 100
        self.line_transparency_slider.valueChanged.connect(self.line_transparency_slider_changed)

        self.ci_color = "black"
        self.ci_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.ci_color)
        self.ci_color_series_btn.clicked.connect(self.ci_color_series_btn_changed)
        self.ci_color_series_line.editingFinished.connect(self.ci_color_series_line_changed)

        self.ci_transparency = self.ci_transparency_slider.value() / 100
        self.ci_transparency_slider.valueChanged.connect(self.ci_transparency_slider_changed)

        # 删除按钮
        self.toolButton.clicked.connect(self.tool_button_clicked)

    def tool_button_clicked(self):
        widget = self.parent._tool_instances.pop(self._id)
        self.parent._tool_instances.insert(self._id, None)
        self.parent._chart_instances.pop(self._id)
        self.parent._chart_instances.insert(self._id, None)
        self.parent.chart.update_plot()
        widget.deleteLater()

    def line_color_series_btn_changed(self, e):
        color = QColorDialog(self)
        line_color = color.getColor()
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

    def line_style_changed(self, e):
        self.line_style = e
        self.parent.chart.update_plot()

    def line_width_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def line_transparency_slider_changed(self, e):
        self.line_transparency = e / 100
        self.parent.chart.update_plot()

    def ci_color_series_btn_changed(self, e):
        color = QColorDialog(self)
        ci_color = color.getColor()
        self.ci_color = ci_color.name(QColor.NameFormat.HexRgb)
        self.ci_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.ci_color)

        colors = self.ci_color_series_line.text()
        if colors == "":
            colors = self.ci_color
        else:
            colors += "," + self.ci_color
        self.ci_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def ci_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def ci_transparency_slider_changed(self, e):
        self.ci_transparency = e / 100
        self.parent.chart.update_plot()
