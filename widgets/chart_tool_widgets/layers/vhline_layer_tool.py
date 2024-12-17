from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_vhline_layer_tool import Ui_Form


class VHLineLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent=None, *args, **kwargs):
        super(VHLineLayerToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.line_type = self.line_type_combo.currentText()
        self.line_type_combo.currentTextChanged.connect(self.line_type_changed)

        self.data_label = self.data_label_line.text()
        self.data_label_line.textChanged.connect(self.data_label_changed)

        self.position = self.position_spin.value()
        self.position_spin.valueChanged.connect(self.position_spin_changed)

        self.min_value = self.min_value_spin.value()
        self.min_value_spin.valueChanged.connect(self.min_value_spin_changed)

        self.max_value = self.max_value_spin.value()
        self.max_value_spin.valueChanged.connect(self.max_value_spin_changed)

        self.color = "#000000"
        self.color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.color)
        self.color_btn.clicked.connect(self.color_btn_clicked)

        self.line_style = self.line_style_combo.currentText()
        self.line_style_combo.currentTextChanged.connect(self.line_style_changed)

        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_spin_changed)

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

    def line_type_changed(self, e):
        self.line_type = e
        self.parent.chart.update_plot()

    def data_label_changed(self, e):
        self.data_label = e
        self.parent.chart.update_plot()

    def position_spin_changed(self, e):
        self.position = e
        self.parent.chart.update_plot()

    def min_value_spin_changed(self, e):
        self.min_value = e
        self.parent.chart.update_plot()

    def max_value_spin_changed(self, e):
        self.max_value = e
        self.parent.chart.update_plot()

    def color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.color = color.name(QColor.NameFormat.HexRgb)
        self.color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.color)
        self.parent.chart.update_plot()

    def line_style_changed(self, e):
        self.line_style = e
        self.parent.chart.update_plot()

    def line_width_spin_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()
