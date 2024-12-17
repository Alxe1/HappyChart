from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_annotation_layer_tool import Ui_Form


class AnnotationLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent=None, *args, **kwargs):
        super(AnnotationLayerToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.x_pos = self.x_pos_spin.value()
        self.x_pos_spin.valueChanged.connect(self.x_pos_spin_changed)
        self.y_pos = self.y_pos_spin.value()
        self.y_pos_spin.valueChanged.connect(self.y_pos_spin_changed)

        self.x_text_pos = self.x_text_pos_spin.value()
        self.x_text_pos_spin.valueChanged.connect(self.x_text_pos_spin_changed)
        self.y_text_pos = self.y_text_pos_spin.value()
        self.y_text_pos_spin.valueChanged.connect(self.y_text_pos_spin_changed)

        self.text = self.text_line.text()
        self.text_line.textChanged.connect(self.text_line_changed)

        self.text_color = "#000000"
        self.text_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.text_color)
        self.text_color_btn.clicked.connect(self.text_color_btn_clicked)

        self.font_size = self.font_size_spin.value()
        self.font_size_spin.valueChanged.connect(self.font_size_spin_changed)

        self.background_color = "#FFFFFF"
        self.background_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.background_color)
        self.background_color_btn.clicked.connect(self.background_color_btn_clicked)

        self.rotation = self.rotation_dial.value()
        self.rotation_dial.valueChanged.connect(self.rotation_dial_changed)

        self.annotation_clip_checked = self.annotation_clip_check.isChecked()
        self.annotation_clip_check.stateChanged.connect(self.annotation_clip_check_changed)

        self.arrow_style = self.arrow_style_combo.currentText()
        self.arrow_style_combo.currentTextChanged.connect(self.arrow_style_combo_changed)

        self.connection_style = self.connection_style_combo.currentText()
        self.connection_style_combo.currentTextChanged.connect(self.connection_style_combo_changed)

        self.shrink_a = self.shrink_a_spin.value()
        self.shrink_a_spin.valueChanged.connect(self.shrink_a_spin_changed)

        self.shrink_b = self.shrink_b_spin.value()
        self.shrink_b_spin.valueChanged.connect(self.shrink_b_spin_changed)

        self.arrow_color = "#000000"
        self.arrow_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.arrow_color)
        self.arrow_color_btn.clicked.connect(self.arrow_color_btn_clicked)

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

    def x_text_pos_spin_changed(self, e):
        self.x_text_pos = e
        self.parent.chart.update_plot()

    def y_text_pos_spin_changed(self, e):
        self.y_text_pos = e
        self.parent.chart.update_plot()

    def text_line_changed(self, e):
        self.text = e
        self.parent.chart.update_plot()

    def text_color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.text_color = color.name(QColor.NameFormat.HexRgb)
        self.text_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.text_color)
        self.parent.chart.update_plot()

    def font_size_spin_changed(self, e):
        self.font_size = e
        self.parent.chart.update_plot()

    def background_color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.background_color = color.name(QColor.NameFormat.HexRgb)
        self.background_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.background_color)
        self.parent.chart.update_plot()

    def rotation_dial_changed(self, e):
        self.rotation = e
        self.parent.chart.update_plot()

    def annotation_clip_check_changed(self, e):
        self.annotation_clip_checked = self.annotation_clip_check.isChecked()
        self.parent.chart.update_plot()

    def arrow_style_combo_changed(self, e):
        self.arrow_style = e
        self.parent.chart.update_plot()

    def connection_style_combo_changed(self, e):
        self.connection_style = e
        self.parent.chart.update_plot()

    def shrink_a_spin_changed(self, e):
        self.shrink_a = e
        self.parent.chart.update_plot()

    def shrink_b_spin_changed(self, e):
        self.shrink_b = e
        self.parent.chart.update_plot()

    def arrow_color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.arrow_color = color.name(QColor.NameFormat.HexRgb)
        self.arrow_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.arrow_color)
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()
