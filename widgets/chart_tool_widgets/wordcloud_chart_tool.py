import os

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QColorDialog, QFileDialog

from widgets.ui_widgets.ui_wordcloud_chart_tool import Ui_Form


class WordcloudChartToolFrame(QFrame, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(WordcloudChartToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())

        self.width = self.width_spin.value()
        self.width_spin.valueChanged.connect(self.width_spin_changed)
        self.height = self.height_spin.value()
        self.height_spin.valueChanged.connect(self.height_spin_changed)

        self.scale = self.scale_spin.value()
        self.scale_spin.valueChanged.connect(self.scale_spin_changed)

        self.background_color = "black"
        self.background_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.background_color)
        self.background_color_btn.clicked.connect(self.background_color_btn_changed)

        self.max_font_size = self.max_font_size_spin.value()
        self.max_font_size_spin.valueChanged.connect(self.max_font_size_spin_changed)

        self.color_map = self.color_map_combo.currentText()
        self.color_map_combo.currentTextChanged.connect(self.color_map_combo_changed)

        self.mask_image_line.clicked.connect(self.mask_image_line_clicked)

    def width_spin_changed(self, e):
        self.width = e
        self.parent.chart.update_plot()

    def height_spin_changed(self, e):
        self.height = e
        self.parent.chart.update_plot()

    def scale_spin_changed(self, e):
        self.scale = e
        self.parent.chart.update_plot()

    def background_color_btn_changed(self, e):
        color = QColorDialog(self)
        background_color = color.getColor()
        self.background_color = background_color.name(QColor.NameFormat.HexRgb)
        self.background_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.background_color)
        self.parent.chart.update_plot()

    def max_font_size_spin_changed(self, e):
        self.max_font_size = e
        self.parent.chart.update_plot()

    def color_map_combo_changed(self, e):
        self.color_map = e
        self.parent.chart.update_plot()

    def mask_image_line_clicked(self, e):
        file_filter = "Image file (*.png *.jpg *.jpeg *.gif)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select image",
            filter=file_filter,
            selectedFilter=os.getcwd()
        )
        if response[0] == "":
            self.mask_image_line.setText("")
            return

        self.mask_image_line.setText(response[0])
        self.parent.chart.update_plot()

