from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from widgets.ui_widgets.ui_charts_dialog import Ui_Dialog


class CustomDialog(QDialog, Ui_Dialog):
    clicked = Signal(str)

    def __init__(self, parent=None):
        super(CustomDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)

        self.selected_chart = None
        self.scatter_layer.clicked.connect(self.scatter_layer_clicked)
        self.line_layer.clicked.connect(self.line_layer_clicked)
        self.stairs_layer.clicked.connect(self.stairs_layer_clicked)
        self.errorbar_layer.clicked.connect(self.errorbar_layer_clicked)
        self.density_layer.clicked.connect(self.density_layer_clicked)
        self.cdf_layer.clicked.connect(self.cdf_layer_clicked)
        self.regression_layer.clicked.connect(self.regression_layer_clicked)
        self.fill_between_layer.clicked.connect(self.fill_between_layer_clicked)
        self.span_layer.clicked.connect(self.span_layer_clicked)
        self.vhline_layer.clicked.connect(self.vhline_layer_clicked)
        self.text_layer.clicked.connect(self.text_layer_clicked)
        self.annotation_layer.clicked.connect(self.annotation_layer_clicked)

    def scatter_layer_clicked(self, e):
        self.selected_chart = "scatter_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def line_layer_clicked(self, e):
        self.selected_chart = "line_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def stairs_layer_clicked(self, e):
        self.selected_chart = "stairs_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def errorbar_layer_clicked(self, e):
        self.selected_chart = "errorbar_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def density_layer_clicked(self, e):
        self.selected_chart = "density_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def cdf_layer_clicked(self, e):
        self.selected_chart = "cdf_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def regression_layer_clicked(self, e):
        self.selected_chart = "regression_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def fill_between_layer_clicked(self, e):
        self.selected_chart = "fill_between_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def span_layer_clicked(self, e):
        self.selected_chart = "span_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def vhline_layer_clicked(self, e):
        self.selected_chart = "vhline_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def text_layer_clicked(self, e):
        self.selected_chart = "text_layer"
        self.clicked.emit(self.selected_chart)
        self.close()

    def annotation_layer_clicked(self, e):
        self.selected_chart = "annotation_layer"
        self.clicked.emit(self.selected_chart)
        self.close()
