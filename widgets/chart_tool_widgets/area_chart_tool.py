from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog

from widgets.ui_widgets.ui_area_chart_tool import Ui_Form


class AreaChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(AreaChartToolFrame, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        # 图表颜色系列
        self.area_color = "#0000ff"
        self.area_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.area_color)
        self.area_color_series_btn.clicked.connect(self.area_color_series_btn_clicked)
        self.area_color_series_line.editingFinished.connect(self.area_color_series_line_changed)

        # 基准线
        self.area_baseline = self.area_baseline_combo.currentText()
        self.area_baseline_combo.currentTextChanged.connect(self.baseline_changed)

        # 透明度
        self.area_transparent = self.area_transparent_slider.value() / 100
        self.area_transparent_slider.valueChanged.connect(self.area_transparent_slider_changed)

    def area_color_series_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        area_color = color_dialog.getColor()
        self.area_color = area_color.name(QColor.NameFormat.HexRgb)
        self.area_color_series_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.area_color)

        colors = self.area_color_series_line.text()
        if colors == "":
            colors = self.area_color
        else:
            colors += "," + self.area_color
        self.area_color_series_line.setText(colors)
        self.parent.chart.update_plot()

    def area_color_series_line_changed(self):
        self.parent.chart.update_plot()

    def baseline_changed(self, e):
        self.area_baseline = e
        self.parent.chart.update_plot()

    def area_transparent_slider_changed(self, e):
        self.area_transparent = e / 100
        self.parent.chart.update_plot()
