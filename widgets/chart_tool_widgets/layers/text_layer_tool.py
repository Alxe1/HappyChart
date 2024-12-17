from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_text_layer_tool import Ui_Form


class TextLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent=None, *args, **kwargs):
        super(TextLayerToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.x_pos = self.x_pos_spin.value()
        self.x_pos_spin.valueChanged.connect(self.x_pos_spin_changed)

        self.y_pos = self.y_pos_spin.value()
        self.y_pos_spin.valueChanged.connect(self.y_pos_spin_changed)

        self.text = self.text_line.text()
        self.text_line.textChanged.connect(self.text_changed)

        self.font_size = self.font_size_spin.value()
        self.font_size_spin.valueChanged.connect(self.font_size_spin_changed)

        self.font_color = "#000000"
        self.font_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.font_color)
        self.font_color_btn.clicked.connect(self.font_color_btn_clicked)

        self.background_color = "#ffffff"
        self.background_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.background_color)
        self.background_color_btn.clicked.connect(self.background_color_btn_clicked)

        self.horizontal_align = self.horizontal_align_combo.currentText()
        self.horizontal_align_combo.currentTextChanged.connect(self.horizontal_align_changed)

        self.vertical_align = self.vertical_align_combo.currentText()
        self.vertical_align_combo.currentTextChanged.connect(self.vertical_align_changed)

        self.multi_align = self.multi_align_combo.currentText()
        self.multi_align_combo.currentTextChanged.connect(self.multi_align_changed)

        self.rotation = self.rotation_dial.value()
        self.rotation_dial.valueChanged.connect(self.rotation_dial_changed)

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

    def x_pos_spin_changed(self, e):
        self.x_pos = e
        self.parent.chart.update_plot()

    def y_pos_spin_changed(self, e):
        self.y_pos = e
        self.parent.chart.update_plot()

    def text_changed(self, e):
        self.text = e
        self.parent.chart.update_plot()

    def font_size_spin_changed(self, e):
        self.font_size = e
        self.parent.chart.update_plot()

    def font_color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.font_color = color.name(QColor.NameFormat.HexRgb)
        self.font_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.font_color)
        self.parent.chart.update_plot()

    def background_color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.background_color = color.name(QColor.NameFormat.HexRgb)
        self.background_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.background_color)
        self.parent.chart.update_plot()

    def horizontal_align_changed(self, e):
        self.horizontal_align = e
        self.parent.chart.update_plot()

    def vertical_align_changed(self, e):
        self.vertical_align = e
        self.parent.chart.update_plot()

    def multi_align_changed(self, e):
        self.multi_align = e
        self.parent.chart.update_plot()

    def rotation_dial_changed(self, e):
        self.rotation = e
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()
