from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_span_layer_tool import Ui_Form


class SpanLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent=None, *args, **kwargs):
        super(SpanLayerToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.span_type = self.span_type_combo.currentText()
        self.span_type_combo.currentTextChanged.connect(self.span_type_changed)

        self.min_value = self.min_value_spin.value()
        self.min_value_spin.valueChanged.connect(self.min_value_spin_changed)

        self.max_value = self.max_value_spin.value()
        self.max_value_spin.valueChanged.connect(self.max_value_spin_changed)

        self.data_label = ""
        self.data_label_line.textChanged.connect(self.data_label_changed)

        self.fill_color_checked = self.fill_color_check.isChecked()
        self.fill_color_check.stateChanged.connect(self.fill_color_check_changed)

        self.face_color = "#d7d9ff"
        self.face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.face_color)
        self.face_color_btn.clicked.connect(self.face_color_btn_clicked)

        self.edge_color = "white"
        self.edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.edge_color)
        self.edge_color_btn.clicked.connect(self.edge_color_btn_clicked)

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

    def span_type_changed(self, e):
        self.span_type = e
        self.parent.chart.update_plot()

    def min_value_spin_changed(self, e):
        self.min_value = e
        self.parent.chart.update_plot()

    def max_value_spin_changed(self, e):
        self.max_value = e
        self.parent.chart.update_plot()

    def data_label_changed(self, e):
        self.data_label = e
        self.parent.chart.update_plot()

    def fill_color_check_changed(self, e):
        self.fill_color_checked = self.fill_color_check.isChecked()
        self.parent.chart.update_plot()

    def face_color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        face_color = color.name(QColor.NameFormat.HexRgb)
        self.face_color = face_color
        self.face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % face_color)
        self.parent.chart.update_plot()

    def edge_color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        edge_color = color.name(QColor.NameFormat.HexRgb)
        self.edge_color = edge_color
        self.edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % edge_color)
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
