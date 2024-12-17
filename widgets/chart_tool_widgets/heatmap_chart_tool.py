from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_hearmap_chart_tool import Ui_Form


class HeatMapChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(HeatMapChartToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())

        self.normalization_checked = self.normalization_check.isChecked()
        self.normalization_check.stateChanged.connect(self.normalization_changed)

        self.show_text_checked = self.show_text_check.isChecked()
        self.show_text_check.stateChanged.connect(self.show_text_changed)

        self.text_color = "w"
        self.text_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.text_color)
        self.text_color_btn.clicked.connect(self.text_color_btn_clicked)

        self.cmap = self.cmap_combo.currentText()
        self.cmap_combo.currentTextChanged.connect(self.cmap_combo_changed)

        self.show_colorbar_checked = self.show_colorbar_check.isChecked()
        self.show_colorbar_check.stateChanged.connect(self.show_colorbar_changed)

    def normalization_changed(self, e):
        self.normalization_checked = self.normalization_check.isChecked()
        self.parent.chart.update_plot()

    def show_text_changed(self, e):
        self.show_text_checked = self.show_text_check.isChecked()
        self.parent.chart.update_plot()

    def text_color_btn_clicked(self, e):
        color = QColorDialog(self)
        text_color = color.getColor()
        self.text_color = text_color.name(QColor.NameFormat.HexRgb)
        self.text_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.text_color)
        self.parent.chart.update_plot()

    def cmap_combo_changed(self, e):
        self.cmap = e
        self.parent.chart.update_plot()

    def show_colorbar_changed(self, e):
        self.show_colorbar_checked = self.show_colorbar_check.isChecked()
        self.parent.chart.update_plot()
