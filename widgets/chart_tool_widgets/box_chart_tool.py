from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_box_chart_tool import Ui_Form


class BoxChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(BoxChartToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        # 颜色系列
        self.box_color = "#000000"
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.box_color)
        self.color_series_btn.clicked.connect(self.color_series_btn_clicked)
        self.color_series_line.editingFinished.connect(self.color_series_line_changed)

        self.notch_checked = self.notch_check.isChecked()
        self.notch_check.stateChanged.connect(self.notch_changed)

        self.vert_checked = self.vert_check.isChecked()
        self.vert_check.stateChanged.connect(self.vert_changed)

        self.box_width = self.box_width_spin.value()
        self.box_width_spin.valueChanged.connect(self.box_width_changed)

        self.patch_artist_checked = self.patch_artist_check.isChecked()
        self.patch_artist_check.stateChanged.connect(self.patch_artist_changed)

        self.show_box_checked = self.show_box_check.isChecked()
        self.show_box_check.stateChanged.connect(self.show_box_changed)

        self.box_linestyle = self.box_linestyle_combo.currentText()
        self.box_linestyle_combo.currentTextChanged.connect(self.box_linestyle_changed)

        self.box_linewidth = self.box_linewidth_spin.value()
        self.box_linewidth_spin.valueChanged.connect(self.box_linewidth_changed)

        self.bbox_color = "#0000ff"
        self.box_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bbox_color)
        self.box_color_btn.clicked.connect(self.box_color_btn_clicked)

        self.median_linestyle = self.median_linestyle_combo.currentText()
        self.median_linestyle_combo.currentTextChanged.connect(self.median_linestyle_changed)

        self.median_linewidth = self.median_linewidth_spin.value()
        self.median_linewidth_spin.valueChanged.connect(self.median_linewidth_changed)

        self.median_line_color = "red"
        self.median_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.median_line_color)
        self.median_line_color_btn.clicked.connect(self.median_line_color_btn_clicked)

        self.show_means_checked = self.show_means_check.isChecked()
        self.show_means_check.stateChanged.connect(self.show_means_changed)

        self.mean_marker = self.mean_marker_combo.currentText()
        self.mean_marker_combo.currentTextChanged.connect(self.mean_marker_changed)

        self.mean_edge_color = "#000000"
        self.mean_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.mean_edge_color)
        self.mean_edge_color_btn.clicked.connect(self.mean_edge_color_btn_clicked)

        self.mean_face_color = "#000000"
        self.mean_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.mean_face_color)
        self.mean_face_color_btn.clicked.connect(self.mean_face_color_btn_clicked)

        self.show_mean_line_checked = self.show_mean_line_check.isChecked()
        self.show_mean_line_check.stateChanged.connect(self.show_mean_line_changed)

        self.mean_linestyle = self.mean_linestyle_combo.currentText()
        self.mean_linestyle_combo.currentTextChanged.connect(self.mean_linestyle_changed)

        self.mean_linewidth = self.mean_linewidth_spin.value()
        self.mean_linewidth_spin.valueChanged.connect(self.mean_linewidth_changed)

        self.mean_line_color = "#000000"
        self.mean_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.mean_line_color)
        self.mean_line_color_btn.clicked.connect(self.mean_line_color_btn_clicked)

        self.show_caps_checked = self.show_caps_check.isChecked()
        self.show_caps_check.stateChanged.connect(self.show_caps_changed)

        self.cap_linestyle = self.cap_linestyle_combo.currentText()
        self.cap_linestyle_combo.currentTextChanged.connect(self.cap_linestyle_changed)

        self.cap_linewidth = self.cap_linewidth_spin.value()
        self.cap_linewidth_spin.valueChanged.connect(self.cap_linewidth_changed)

        self.cap_color = "#000000"
        self.cap_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.cap_color)
        self.cap_color_btn.clicked.connect(self.cap_color_btn_clicked)

        self.cap_width = self.cap_width_spin.value()
        self.cap_width_spin.valueChanged.connect(self.cap_width_changed)

        self.show_outlier_checked = self.show_outlier_check.isChecked()
        self.show_outlier_check.stateChanged.connect(self.show_outlier_changed)

        self.outlier_marker = self.outlier_marker_combo.currentText()
        self.outlier_marker_combo.currentTextChanged.connect(self.outlier_marker_changed)

        self.outlier_marker_size = self.outlier_marker_size_spin.value()
        self.outlier_marker_size_spin.valueChanged.connect(self.outlier_marker_size_changed)

        self.outlier_edge_color = "red"
        self.outlier_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.outlier_edge_color)
        self.outlier_edge_color_btn.clicked.connect(self.outlier_edge_color_btn_clicked)

        self.outlier_face_color = "red"
        self.outlier_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.outlier_face_color)
        self.outlier_face_color_btn.clicked.connect(self.outlier_face_color_btn_clicked)

    def color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        box_color = color_dialog.getColor()
        self.box_color = box_color.name(QColor.NameFormat.HexRgb)
        self.color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.box_color)

        colors = self.color_series_line.text()
        if colors == "":
            colors = self.box_color
        else:
            colors += "," + self.box_color
        self.color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def color_series_line_changed(self):
        self.parent.chart.update_plot()

    def notch_changed(self, e):
        self.notch_checked = self.notch_check.isChecked()
        self.parent.chart.update_plot()

    def vert_changed(self, e):
        self.vert_checked = self.vert_check.isChecked()
        self.parent.chart.update_plot()

    def box_width_changed(self, e):
        self.box_width = e
        self.parent.chart.update_plot()

    def patch_artist_changed(self, e):
        self.patch_artist_checked = self.patch_artist_check.isChecked()
        self.parent.chart.update_plot()

    def show_box_changed(self, e):
        self.show_box_checked = self.show_box_check.isChecked()
        self.parent.chart.update_plot()

    def box_linestyle_changed(self, e):
        self.box_linestyle = e
        self.parent.chart.update_plot()

    def box_linewidth_changed(self, e):
        self.box_linewidth = e
        self.parent.chart.update_plot()

    def box_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bbox_color = color_dialog.getColor()
        self.bbox_color = bbox_color.name(QColor.NameFormat.HexRgb)
        self.box_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bbox_color)
        self.parent.chart.update_plot()

    def median_linestyle_changed(self, e):
        self.median_linestyle = e
        self.parent.chart.update_plot()

    def median_linewidth_changed(self, e):
        self.median_linewidth = e
        self.parent.chart.update_plot()

    def median_line_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        median_line_color = color_dialog.getColor()
        self.median_line_color = median_line_color.name(QColor.NameFormat.HexRgb)
        self.median_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.median_line_color)
        self.parent.chart.update_plot()

    def show_means_changed(self, e):
        self.show_means_checked = self.show_means_check.isChecked()
        self.parent.chart.update_plot()

    def mean_marker_changed(self, e):
        self.mean_marker = e
        self.parent.chart.update_plot()

    def mean_edge_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        mean_edge_color = color_dialog.getColor()
        self.mean_edge_color = mean_edge_color.name(QColor.NameFormat.HexRgb)
        self.mean_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.mean_edge_color)
        self.parent.chart.update_plot()

    def mean_face_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        mean_face_color = color_dialog.getColor()
        self.mean_face_color = mean_face_color.name(QColor.NameFormat.HexRgb)
        self.mean_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.mean_face_color)
        self.parent.chart.update_plot()

    def show_mean_line_changed(self, e):
        self.show_mean_line_checked = self.show_mean_line_check.isChecked()
        self.parent.chart.update_plot()

    def mean_linestyle_changed(self, e):
        self.mean_linestyle = e
        self.parent.chart.update_plot()

    def mean_linewidth_changed(self, e):
        self.mean_linewidth = e
        self.parent.chart.update_plot()

    def mean_line_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        mean_line_color = color_dialog.getColor()
        self.mean_line_color = mean_line_color.name(QColor.NameFormat.HexRgb)
        self.mean_line_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.mean_line_color)
        self.parent.chart.update_plot()

    def show_caps_changed(self, e):
        self.show_caps_checked = self.show_caps_check.isChecked()
        self.parent.chart.update_plot()

    def cap_linestyle_changed(self, e):
        self.cap_linestyle = e
        self.parent.chart.update_plot()

    def cap_linewidth_changed(self, e):
        self.cap_linewidth = e
        self.parent.chart.update_plot()

    def cap_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        cap_color = color_dialog.getColor()
        self.cap_color = cap_color.name(QColor.NameFormat.HexRgb)
        self.cap_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.cap_color)
        self.parent.chart.update_plot()

    def cap_width_changed(self, e):
        self.cap_width = e
        self.parent.chart.update_plot()

    def show_outlier_changed(self, e):
        self.show_outlier_checked = self.show_outlier_check.isChecked()
        self.parent.chart.update_plot()

    def outlier_marker_changed(self, e):
        self.outlier_marker = e
        self.parent.chart.update_plot()

    def outlier_marker_size_changed(self, e):
        self.outlier_marker_size = e
        self.parent.chart.update_plot()

    def outlier_edge_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        outlier_edge_color = color_dialog.getColor()
        self.outlier_edge_color = outlier_edge_color.name(QColor.NameFormat.HexRgb)
        self.outlier_edge_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.outlier_edge_color)
        self.parent.chart.update_plot()

    def outlier_face_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        outlier_face_color = color_dialog.getColor()
        self.outlier_face_color = outlier_face_color.name(QColor.NameFormat.HexRgb)
        self.outlier_face_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.outlier_face_color)
        self.parent.chart.update_plot()

