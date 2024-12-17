from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_stairs_chart_tool import Ui_Form


class StairsChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(StairsChartToolFrame, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        self.orientation = self.orientation_combo.currentText()
        self.orientation_combo.currentTextChanged.connect(self.orientation_combo_changed)

        self.base_line = self.base_line_spin.value()
        self.base_line_spin.valueChanged.connect(self.base_line_spin_changed)

        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_spin_changed)

        self.line_style = self.line_style_combo.currentText()
        self.line_style_combo.currentTextChanged.connect(self.line_style_combo_changed)

        self.fill_color_checked = self.fill_color_check.isChecked()
        self.fill_color_check.stateChanged.connect(self.fill_color_check_changed)

        self.edge_color = "k"
        self.edge_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.edge_color)
        self.edge_color_series_btn.clicked.connect(self.edge_color_series_btn_clicked)
        self.edge_color_series_line.editingFinished.connect(self.edge_color_series_line_changed)

        self.face_color = "b"
        self.face_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.face_color)
        self.face_color_series_btn.clicked.connect(self.face_color_series_btn_clicked)
        self.face_color_series_line.editingFinished.connect(self.face_color_series_line_changed)

        self.transparency = self.transparency_slider.value() / 100
        self.transparency_slider.valueChanged.connect(self.transparency_slider_changed)

        self.hatch_series = self.hatch_series_line.text()
        self.hatch_series_line.textChanged.connect(self.hatch_series_line_changed)

    def orientation_combo_changed(self, e):
        self.orientation = e
        self.parent.chart.update_plot()

    def base_line_spin_changed(self, e):
        self.base_line = e
        self.parent.chart.update_plot()

    def line_width_spin_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def line_style_combo_changed(self, e):
        self.line_style = e
        self.parent.chart.update_plot()

    def fill_color_check_changed(self, e):
        self.fill_color_checked = self.fill_color_check.isChecked()
        self.parent.chart.update_plot()

    def edge_color_series_btn_clicked(self, e):
        color = QColorDialog(self)
        edge_color = color.getColor()
        self.edge_color = edge_color.name(QColor.NameFormat.HexRgb)
        self.edge_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.edge_color)

        colors = self.edge_color_series_line.text()
        if colors == "":
            colors = self.edge_color
        else:
            colors += "," + self.edge_color
        self.edge_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def edge_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def face_color_series_btn_clicked(self, e):
        color = QColorDialog(self)
        face_color = color.getColor()
        self.face_color = face_color.name(QColor.NameFormat.HexRgb)
        self.face_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.face_color)
        self.parent.chart.update_plot()

        colors = self.face_color_series_line.text()
        if colors == "":
            colors = self.face_color
        else:
            colors += "," + self.face_color
        self.face_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def face_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()

    def hatch_series_line_changed(self, e):
        self.hatch_series = e
        self.parent.chart.update_plot()
