from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_pie_chart_with_bar_tool import Ui_Form


class PieChartWithBarToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        # pie颜色系列
        self.pie_color = "#000000"
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.pie_color)
        self.color_series_btn.clicked.connect(self.color_series_changed)
        self.color_series_line.editingFinished.connect(self.color_series_line_changed)

        self.pct = None if self.pct_combo.currentText() == "none" else "%1.{}f%%".format(self.pct_combo.currentText())
        self.pct_combo.currentTextChanged.connect(self.pct_changed)

        self.pct_distance = self.pct_distance_spin.value()
        self.pct_distance_spin.valueChanged.connect(self.pct_distance_changed)

        self.label_distance = self.label_distance_spin.value()
        self.label_distance_spin.valueChanged.connect(self.label_distance_changed)

        self.explode_series = self.init_explode_series()
        self.explode_series_line.editingFinished.connect(self.explode_series_changed)

        self.start_angle = self.start_angle_dial.value()
        self.start_angle_dial.valueChanged.connect(self.start_angle_changed)

        self.radius = self.radius_spin.value()
        self.radius_spin.valueChanged.connect(self.radius_changed)

        self.unticlockwise_checked = self.unticlockwise_check.isChecked()
        self.unticlockwise_check.stateChanged.connect(self.unticlockwise_changed)

        self.shadow_checked = self.shadow_check.isChecked()
        self.shadow_check.stateChanged.connect(self.shadow_changed)

        self.text_props_checked = self.text_props_check.isChecked()
        self.text_props_check.stateChanged.connect(self.text_props_changed)
        self.font_size = self.font_size_spin.value()
        self.font_size_spin.valueChanged.connect(self.font_size_changed)
        self.font_color = "#000000"
        self.font_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.font_color)
        self.font_color_btn.clicked.connect(self.font_color_btn_clicked)

        self.wedge_props_checked = self.wedge_props_check.isChecked()
        self.wedge_props_check.stateChanged.connect(self.wedge_props_changed)
        self.wedge_width = self.wedge_width_spin.value()
        self.wedge_width_spin.valueChanged.connect(self.wedge_width_changed)
        self.edge_color = "#000000"
        self.edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.edge_color)
        self.edge_color_btn.clicked.connect(self.edge_color_btn_clicked)
        self.line_width = self.line_width_spin.value()
        self.line_width_spin.valueChanged.connect(self.line_width_changed)
        self.line_style = self.line_style_combo.currentText()
        self.line_style_combo.currentTextChanged.connect(self.line_style_changed)
        self.transparency = self.transparent_slider.value() / 100
        self.transparent_slider.valueChanged.connect(self.transparent_slider_changed)

        self.bar_data_series = self.init_bar_data_series()
        self.bar_data_series_line.editingFinished.connect(self.bar_data_series_changed)

        self.bar_label_series = self.bar_label_series_line.text()
        self.bar_label_series_line.editingFinished.connect(self.bar_label_series_changed)

        self.bar_color = "#0000ff"
        self.bar_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bar_color)
        self.bar_color_btn.clicked.connect(self.bar_color_btn_clicked)

        self.bar_title = self.bar_title_line.text()
        self.bar_title_line.editingFinished.connect(self.bar_title_changed)

        self.bar_legend_pos = self.bar_legend_pos_combo.currentText()
        self.bar_legend_pos_combo.currentTextChanged.connect(self.bar_legend_pos_changed)

        self.tied_line_width = self.tied_line_width_spin.value()
        self.tied_line_width_spin.valueChanged.connect(self.tied_line_width_changed)

        self.tied_line_style = self.tied_line_style_combo.currentText()
        self.tied_line_style_combo.currentTextChanged.connect(self.tied_line_style_changed)

        self.tied_line_color = "#000000"
        self.tied_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.tied_line_color)
        self.tied_line_color_btn.clicked.connect(self.tied_line_color_btn_clicked)

        self.bind_wedge_index = self.bind_wedge_index_spin.value()
        self.bind_wedge_index_spin.valueChanged.connect(self.bind_wedge_index_changed)

    def color_series_changed(self, e):
        color_dialog = QColorDialog(self)
        pie_color = color_dialog.getColor()
        self.pie_color = pie_color.name(QColor.NameFormat.HexRgb)
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.pie_color)

        colors = self.color_series_line.text()
        if colors == "":
            colors = self.pie_color
        else:
            colors += "," + self.pie_color
        self.color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def color_series_line_changed(self):
        self.parent.chart.update_plot()

    def pct_changed(self, e):
        self.pct = None if e == "none" else "%1.{}f%%".format(e)
        self.parent.chart.update_plot()

    def pct_distance_changed(self, e):
        self.pct_distance = e
        self.parent.chart.update_plot()

    def label_distance_changed(self, e):
        self.label_distance = e
        self.parent.chart.update_plot()

    def init_explode_series(self):
        text = self.explode_series_line.text().strip()

        explode_series = []
        if text:
            try:
                explode_series = [float(i) for i in text.split(",")]
            except:
                pass
        return explode_series

    def explode_series_changed(self):
        self.explode_series = self.init_explode_series()
        self.parent.chart.update_plot()

    def start_angle_changed(self, e):
        self.start_angle = e
        self.parent.chart.update_plot()

    def radius_changed(self, e):
        self.radius = e
        self.parent.chart.update_plot()

    def unticlockwise_changed(self, e):
        self.unticlockwise_checked = self.unticlockwise_check.isChecked()
        self.parent.chart.update_plot()

    def shadow_changed(self, e):
        self.shadow_checked = self.shadow_check.isChecked()
        self.parent.chart.update_plot()

    def text_props_changed(self, e):
        self.text_props_checked = self.text_props_check.isChecked()
        if self.text_props_checked:
            self.font_size_spin.setEnabled(True)
            self.font_color_btn.setEnabled(True)
        else:
            self.font_size_spin.setEnabled(False)
            self.font_color_btn.setEnabled(False)
        self.parent.chart.update_plot()

    def font_size_changed(self, e):
        self.font_size = e
        self.parent.chart.update_plot()

    def font_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        font_color = color_dialog.getColor()
        self.font_color = font_color.name(QColor.NameFormat.HexRgb)
        self.font_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.font_color)
        self.parent.chart.update_plot()

    def wedge_props_changed(self, e):
        self.wedge_props_checked = self.wedge_props_check.isChecked()
        if self.wedge_props_checked:
            self.wedge_width_spin.setEnabled(True)
            self.edge_color_btn.setEnabled(True)
            self.line_width_spin.setEnabled(True)
            self.line_style_combo.setEnabled(True)
            self.transparent_slider.setEnabled(True)
        else:
            self.wedge_width_spin.setEnabled(False)
            self.edge_color_btn.setEnabled(False)
            self.line_width_spin.setEnabled(False)
            self.line_style_combo.setEnabled(False)
            self.transparent_slider.setEnabled(False)
        self.parent.chart.update_plot()

    def wedge_width_changed(self, e):
        self.wedge_width = e
        self.parent.chart.update_plot()

    def edge_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        edge_color = color_dialog.getColor()
        self.edge_color = edge_color.name(QColor.NameFormat.HexRgb)
        self.edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.edge_color)
        self.parent.chart.update_plot()

    def line_width_changed(self, e):
        self.line_width = e
        self.parent.chart.update_plot()

    def line_style_changed(self, e):
        self.line_style = e
        self.parent.chart.update_plot()

    def transparent_slider_changed(self, e):
        self.transparency = e / 100
        self.parent.chart.update_plot()

    def init_bar_data_series(self):
        text = self.bar_data_series_line.text().strip()

        bar_data_series = []
        if text:
            try:
                bar_data_series = [float(i) for i in text.split(",")]
            except:
                pass
        return bar_data_series

    def bar_data_series_changed(self):
        self.bar_data_series = self.init_bar_data_series()
        self.parent.chart.update_plot()

    def bar_label_series_changed(self):
        self.bar_label_series = self.bar_label_series_line.text()
        self.parent.chart.update_plot()

    def bar_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bar_color = color_dialog.getColor()
        self.bar_color = bar_color.name(QColor.NameFormat.HexRgb)
        self.bar_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bar_color)
        self.parent.chart.update_plot()

    def bar_title_changed(self):
        self.bar_title = self.bar_title_line.text()
        self.parent.chart.update_plot()

    def bar_legend_pos_changed(self, e):
        self.bar_legend_pos = e
        self.parent.chart.update_plot()

    def tied_line_width_changed(self, e):
        self.tied_line_width = e
        self.parent.chart.update_plot()

    def tied_line_style_changed(self, e):
        self.tied_line_style = e
        self.parent.chart.update_plot()

    def tied_line_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        tied_line_color = color_dialog.getColor()
        self.tied_line_color = tied_line_color.name(QColor.NameFormat.HexRgb)
        self.tied_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.tied_line_color)
        self.parent.chart.update_plot()

    def bind_wedge_index_changed(self, e):
        self.bind_wedge_index = e
        self.parent.chart.update_plot()
