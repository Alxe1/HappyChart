from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.layers.ui_fill_between_layer_tool import Ui_Form


class FillBetweenLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent, *args, **kwargs):
        super(FillBetweenLayerToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.parent.chart_tool.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y1_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y2_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.where_first_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.where_second_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        if not self.parent.df.empty:
            cols = self.parent.df.columns.tolist()
            self.y1_series_combo.clear()
            self.y1_series_combo.addItems(cols)
            self.y1_series_combo.setCurrentIndex(-1)

            self.y2_series_combo.clear()
            self.y2_series_combo.addItems(cols)
            self.y2_series_combo.setCurrentIndex(-1)

            self.where_first_combo.clear()
            self.where_first_combo.addItems(cols)
            self.where_first_combo.setCurrentIndex(-1)

            self.where_second_combo.clear()
            self.where_second_combo.addItems(cols)
            self.where_second_combo.setCurrentIndex(-1)

        self.where_eq = self.where_eq_combo.currentText()
        self.where_eq_combo.currentTextChanged.connect(self.where_eq_changed)

        self.face_color = "#cecece"
        self.face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.face_color)
        self.face_color_btn.clicked.connect(self.color_btn_clicked)

        self.edge_color = "white"
        self.edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.edge_color)
        self.edge_color_btn.clicked.connect(self.color_series_btn_clicked)

        self.interpolate_checked = self.interpolate_check.isChecked()
        self.interpolate_check.stateChanged.connect(self.interpolate_check_changed)

        self.step = self.step_combo.currentText()
        self.step_combo.currentTextChanged.connect(self.step_changed)

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

    def where_eq_changed(self, e):
        self.where_eq = e
        self.parent.chart.update_plot()

    def color_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.face_color = color.name(QColor.NameFormat.HexRgb)
        self.face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.face_color)
        self.parent.chart.update_plot()

    def color_series_btn_clicked(self, e):
        dialog = QColorDialog(self)
        color = dialog.getColor()
        self.edge_color = color.name(QColor.NameFormat.HexRgb)
        self.edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.edge_color)
        self.parent.chart.update_plot()

    def interpolate_check_changed(self, e):
        self.interpolate_checked = self.interpolate_check.isChecked()
        self.parent.chart.update_plot()

    def step_changed(self, e):
        self.step = e
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()
