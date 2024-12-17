from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_violin_chart_tool import Ui_Form


class ViolinChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ViolinChartToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        self.vertical_checked = self.vertical_check.isChecked()
        self.vertical_check.stateChanged.connect(self.vertical_check_changed)

        self.width = self.width_spin.value()
        self.width_spin.valueChanged.connect(self.width_spin_changed)

        self.points = self.points_spin.value()
        self.points_spin.valueChanged.connect(self.points_spin_changed)

        self.method = self.method_combo.currentText()
        self.method_combo.currentTextChanged.connect(self.method_combo_changed)

        self.side = self.side_combo.currentText()
        self.side_combo.currentTextChanged.connect(self.side_combo_changed)

        self.body_face_color = "pink"
        self.body_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.body_face_color)
        self.body_face_color_btn.clicked.connect(self.body_face_color_btn_clicked)

        self.body_edge_color = "#000000"
        self.body_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.body_edge_color)
        self.body_edge_color_btn.clicked.connect(self.body_edge_color_btn_clicked)

        self.transparency = self.transparency_slider.value()/100
        self.transparency_slider.valueChanged.connect(self.transparency_slider_changed)

        self.median_dot_checked = self.median_dot_check.isChecked()
        self.median_dot_check.stateChanged.connect(self.median_dot_check_changed)

        self.median_marker = self.median_marker_combo.currentText()
        self.median_marker_combo.currentTextChanged.connect(self.median_marker_combo_changed)

        self.median_color = "white"
        self.median_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.median_color)
        self.median_color_btn.clicked.connect(self.median_color_btn_clicked)

        self.median_size = self.median_size_spin.value()
        self.median_size_spin.valueChanged.connect(self.median_size_spin_changed)

        self.quantile_linestyle = self.quantile_linestyle_combo.currentText()
        self.quantile_linestyle_combo.currentTextChanged.connect(self.quantile_linestyle_combo_changed)

        self.quantile_line_color = "#000000"
        self.quantile_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.quantile_line_color)
        self.quantile_line_color_btn.clicked.connect(self.quantile_line_color_btn_clicked)

        self.quantile_linewidth = self.quantile_linewidth_spin.value()
        self.quantile_linewidth_spin.valueChanged.connect(self.quantile_linewidth_spin_changed)

        self.whisker_linestyle = self.whisker_linestyle_combo.currentText()
        self.whisker_linestyle_combo.currentTextChanged.connect(self.whisker_linestyle_combo_changed)

        self.whisker_line_color = "#000000"
        self.whisker_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.whisker_line_color)
        self.whisker_line_color_btn.clicked.connect(self.whisker_line_color_btn_clicked)

        self.whisker_line_width = self.whisker_line_width_spin.value()
        self.whisker_line_width_spin.valueChanged.connect(self.whisker_linewidth_spin_changed)

    def vertical_check_changed(self, e):
        self.vertical_checked = self.vertical_check.isChecked()
        self.parent.chart.update_plot()

    def width_spin_changed(self, e):
        self.width = e
        self.parent.chart.update_plot()

    def points_spin_changed(self, e):
        self.points = e
        self.parent.chart.update_plot()

    def method_combo_changed(self, e):
        self.method = e
        self.parent.chart.update_plot()

    def side_combo_changed(self, e):
        self.side = e
        self.parent.chart.update_plot()

    def body_face_color_btn_clicked(self, e):
        color = QColorDialog(self)
        body_face_color = color.getColor()
        self.body_face_color = body_face_color.name(QColor.NameFormat.HexRgb)
        self.body_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.body_face_color)
        self.parent.chart.update_plot()

    def body_edge_color_btn_clicked(self, e):
        color = QColorDialog(self)
        body_edge_color = color.getColor()
        self.body_edge_color = body_edge_color.name(QColor.NameFormat.HexRgb)
        self.body_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.body_edge_color)
        self.parent.chart.update_plot()

    def transparency_slider_changed(self, e):
        self.transparency = e/100
        self.parent.chart.update_plot()

    def median_dot_check_changed(self, e):
        self.median_dot_checked = self.median_dot_check.isChecked()
        self.parent.chart.update_plot()

    def median_marker_combo_changed(self, e):
        self.median_marker = e
        self.parent.chart.update_plot()

    def median_color_btn_clicked(self, e):
        color = QColorDialog(self)
        median_color = color.getColor()
        self.median_color = median_color.name(QColor.NameFormat.HexRgb)
        self.median_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.median_color)
        self.parent.chart.update_plot()

    def median_size_spin_changed(self, e):
        self.median_size = e
        self.parent.chart.update_plot()

    def quantile_linestyle_combo_changed(self, e):
        self.quantile_linestyle = e
        self.parent.chart.update_plot()

    def quantile_line_color_btn_clicked(self, e):
        color = QColorDialog(self)
        quantile_line_color = color.getColor()
        self.quantile_line_color = quantile_line_color.name(QColor.NameFormat.HexRgb)
        self.quantile_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.quantile_line_color)
        self.parent.chart.update_plot()

    def quantile_linewidth_spin_changed(self, e):
        self.quantile_linewidth = e
        self.parent.chart.update_plot()

    def whisker_linestyle_combo_changed(self, e):
        self.whisker_linestyle = e
        self.parent.chart.update_plot()

    def whisker_line_color_btn_clicked(self, e):
        color = QColorDialog(self)
        whisker_line_color = color.getColor()
        self.whisker_line_color = whisker_line_color.name(QColor.NameFormat.HexRgb)
        self.whisker_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.whisker_line_color)
        self.parent.chart.update_plot()

    def whisker_linewidth_spin_changed(self, e):
        self.whisker_line_width = e
        self.parent.chart.update_plot()

        