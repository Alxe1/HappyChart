import os
import sys

import pandas as pd
from PySide6.QtGui import QIcon, QGuiApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QFrame
from PySide6.QtCore import Qt
import qdarktheme

from charts.area_chart import AreaChart
from charts.autocorrelation_chart import AutoCorrelationChart
from charts.bar_chart import BarChart
from charts.box_chart import BoxChart
from charts.chart_layers.chart_layer import ChartLayer
from charts.errorbar_chart import ErrorBarChart
from charts.event_chart import EventChart
from charts.hbar_chart import HBarChart
from charts.heatmap_chart import HeatMapChart
from charts.histgram import Histgram
from charts.pie_chart import PieChart
from charts.pie_chart_with_bar import PieChartWithBar
from charts.radar_chart import RadarChart
from charts.scatter_chart import ScatterChart
from charts.stairs_chart import StairsChart
from charts.stem_chart import StemChart
from charts.violin_chart import ViolinChart
from charts.wordcloud_chart import WordcloudChart
from widgets.chart_tool_widgets.area_chart_tool import AreaChartToolFrame
from widgets.chart_tool_widgets.autocorrelation_chart_tool import AutoCorrelationChartToolFrame
from widgets.chart_tool_widgets.bar_chart_tool import BarChartToolFrame
from widgets.chart_tool_widgets.box_chart_tool import BoxChartToolFrame
from widgets.chart_tool_widgets.errorbar_chart_tool import ErrorBarChartToolFrame
from widgets.chart_tool_widgets.event_chart_tool import EventChartToolFrame
from widgets.chart_tool_widgets.hbar_chart_tool import HBarChartToolFrame
from widgets.chart_tool_widgets.heatmap_chart_tool import HeatMapChartToolFrame
from widgets.chart_tool_widgets.histgram_chart_tool import HistgramChartToolFrame
from widgets.chart_tool_widgets.layers.annotation_layer_tool import AnnotationLayerToolFrame
from widgets.chart_tool_widgets.layers.cdf_layer_tool import CDFLayerToolFrame
from widgets.chart_tool_widgets.layers.density_layer_tool import DensityLayerToolFrame
from widgets.chart_tool_widgets.layers.errorbar_layer_tool import ErrorbarLayerToolFrame
from widgets.chart_tool_widgets.layers.fill_between_layer_tool import FillBetweenLayerToolFrame
from widgets.chart_tool_widgets.layers.line_layer_tool import LineLayerToolFrame
from widgets.chart_tool_widgets.layers.regression_layer_tool import RegressionLayerToolFrame
from widgets.chart_tool_widgets.layers.scatter_layer_tool import ScatterLayerToolFrame
from widgets.chart_tool_widgets.layers.span_layer_tool import SpanLayerToolFrame
from widgets.chart_tool_widgets.layers.stairs_layer_tool import StairsLayerToolFrame
from widgets.chart_tool_widgets.layers.text_layer_tool import TextLayerToolFrame
from widgets.chart_tool_widgets.layers.vhline_layer_tool import VHLineLayerToolFrame
from widgets.chart_tool_widgets.line_chart_tool import LineChartToolFrame
from widgets.chart_tool_widgets.pie_chart_tool import PieChartToolFrame
from widgets.chart_tool_widgets.pie_chart_with_bar_tool import PieChartWithBarToolFrame
from widgets.chart_tool_widgets.radar_chart_tool import RadarChartToolFrame
from widgets.chart_tool_widgets.scatter_chart_tool import ScatterChartToolFrame
from widgets.chart_tool_widgets.stairs_chart_tool import StairsChartToolFrame
from widgets.chart_tool_widgets.stem_chart_tool import StemChartToolFrame
from widgets.chart_tool_widgets.violin_chart_tool import ViolinChartToolFrame
from widgets.chart_tool_widgets.wordcloud_chart_tool import WordcloudChartToolFrame
from widgets.inherited_widgets.custom_dialog_widget import CustomDialog
from widgets.ui_widgets.ui_mainWidget import Ui_MainWindow
from widgets.toolbar_action_widget import ToolbarActionWidget

from charts.line_chart import LineChart


class MainWindow(QMainWindow, Ui_MainWindow):
    _instances = []
    _tool_instances = []
    _chart_instances = []

    def __init__(self):
        super().__init__()
        self.procs = []

        self.df = pd.DataFrame({})
        self.selected_chart = None
        self.chart = None

        self.setupUi(self)

        screen = QGuiApplication.primaryScreen().geometry()
        width = screen.width()
        height = screen.height()
        self.resize(int(width*2/3), int(height*2/3))

        self.toolbar_action_widget = ToolbarActionWidget(self)

        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionImportData.triggered.connect(self.import_file)
        self.actionExportData.triggered.connect(self.export_file)
        self.actionExportImage.triggered.connect(self.export_image)
        self.actionHelp.triggered.connect(self.doc_help)

        self.actionScatterLayer.triggered.connect(self.scatter_layer_triggered)
        self.actionLineLayer.triggered.connect(self.line_layer_triggered)
        self.actionStairsLayer.triggered.connect(self.stairs_layer_triggered)
        self.actionErrorLayer.triggered.connect(self.errorbar_layer_triggered )
        self.actionDensityLayer.triggered.connect(self.density_layer_triggered)
        self.actionCDFLayer.triggered.connect(self.cdf_layer_triggered)
        self.actionRegressionLayer.triggered.connect(self.regression_layer_triggered)
        self.actionFillBetweenLayer.triggered.connect(self.fill_between_layer_triggered)
        self.actionSpanLayer.triggered.connect(self.span_layer_triggered)
        self.actionVHLineLayer.triggered.connect(self.vhline_layer_triggered)
        self.actionAnnotationLayer.triggered.connect(self.annotation_layer_triggered)
        self.actionTextLayer.triggered.connect(self.text_layer_triggered)

        self.actionBarChart.triggered.connect(self.bar_chart_triggered)
        self.actionLineChart.triggered.connect(self.line_chart_triggered)
        self.actionHBarChart.triggered.connect(self.hbar_chart_triggered)
        self.actionScatterChart.triggered.connect(self.scatter_chart_triggered)
        self.actionStackedAreaChart.triggered.connect(self.stacked_area_chart_triggered)
        self.actionStemChart.triggered.connect(self.stem_chart_triggered)
        self.actionRadarChart.triggered.connect(self.radar_chart_triggered)
        self.actionHistgram.triggered.connect(self.histgram_triggered)
        self.actionPieChart.triggered.connect(self.pie_chart_triggered)
        self.actionPieChartWithBar.triggered.connect(self.pie_chart_with_bar_triggered)
        self.actionBoxChart.triggered.connect(self.box_chart_triggered)
        self.actionErrorChart.triggered.connect(self.error_chart_triggered)
        self.actionViolinChart.triggered.connect(self.violin_chart_triggered)
        self.actionHeatmapChart.triggered.connect(self.heatmap_chart_triggered)
        self.actionEventChart.triggered.connect(self.event_chart_triggered)
        self.actionAutoCorrelationChart.triggered.connect(self.autocorrelation_chart_triggered)
        self.actionStairsChart.triggered.connect(self.stairs_chart_triggered)
        self.actionWordcloudChart.triggered.connect(self.wordcloud_chart_triggered)

        self.selected_chart = self.chart_type_combo.currentText()
        self.get_selected_chart()
        self.chart_type_combo.currentTextChanged.connect(self.chart_changed)

        self.custom_dialog = CustomDialog(self)
        self.custom_dialog.clicked.connect(self.chart_dialog_clicked)

        self.add_layer_btn.clicked.connect(self.add_layer_btn_clicked)

    def new_file(self, e):
        self.toolbar_action_widget.create_new_window()

    def open_file(self, e):
        self.toolbar_action_widget.open()

    def save_file(self, e):
        self.toolbar_action_widget.save()

    def import_file(self, e):
        self.toolbar_action_widget.import_file()

    def export_file(self, e):
        self.toolbar_action_widget.export_file()

    def export_image(self, e):
        self.toolbar_action_widget.export_image()

    def doc_help(self, e):
        self.toolbar_action_widget.doc_help()

    def scatter_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("scatter_layer")

    def line_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("line_layer")

    def stairs_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("stairs_layer")

    def errorbar_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("errorbar_layer")

    def density_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("density_layer")

    def cdf_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("cdf_layer")

    def regression_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("regression_layer")

    def fill_between_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("fill_between_layer")

    def vhline_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("vhline_layer")

    def annotation_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("annotation_layer")

    def text_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("text_layer")

    def bar_chart_triggered(self, e):
        self.chart_triggered("BarChart")

    def line_chart_triggered(self, e):
        self.chart_triggered("LineChart")

    def hbar_chart_triggered(self, e):
        self.chart_triggered("HBarChart")

    def scatter_chart_triggered(self, e):
        self.chart_triggered("ScatterChart")

    def stacked_area_chart_triggered(self, e):
        self.chart_triggered("StackedAreaChart")

    def stem_chart_triggered(self, e):
        self.chart_triggered("StemChart")

    def radar_chart_triggered(self, e):
        self.chart_triggered("RadarChart")

    def histgram_triggered(self, e):
        self.chart_triggered("Histgram")

    def pie_chart_triggered(self, e):
        self.chart_triggered("PieChart")

    def pie_chart_with_bar_triggered(self, e):
        self.chart_triggered("PieChartWithBar")

    def box_chart_triggered(self, e):
        self.chart_triggered("BoxChart")

    def error_chart_triggered(self, e):
        self.chart_triggered("ErrorChart")

    def violin_chart_triggered(self, e):
        self.chart_triggered("ViolinChart")

    def heatmap_chart_triggered(self, e):
        self.chart_triggered("HeatmapChart")

    def event_chart_triggered(self, e):
        self.chart_triggered("EventChart")

    def autocorrelation_chart_triggered(self, e):
        self.chart_triggered("AutoCorrelationChart")

    def stairs_chart_triggered(self, e):
        self.chart_triggered("StairsChart")

    def wordcloud_chart_triggered(self, e):
        self.chart_triggered("WordcloudChart")

    def span_layer_triggered(self, e):
        self.toolbar_action_widget.chart_layer_triggered("span_layer")

    def chart_triggered(self, e):
        self.selected_chart = e
        self.get_selected_chart()
        self.chart_type_combo.setCurrentText(self.selected_chart)

    def chart_dialog_clicked(self, e):
        chart_layer_tool = None
        if e == "scatter_layer":
            chart_layer_tool = ScatterLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "line_layer":
            chart_layer_tool = LineLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "stairs_layer":
            chart_layer_tool = StairsLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "errorbar_layer":
            chart_layer_tool = ErrorbarLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "density_layer":
            chart_layer_tool = DensityLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "cdf_layer":
            chart_layer_tool = CDFLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "regression_layer":
            chart_layer_tool = RegressionLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "fill_between_layer":
            chart_layer_tool = FillBetweenLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "span_layer":
            chart_layer_tool = SpanLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "vhline_layer":
            chart_layer_tool = VHLineLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "text_layer":
            chart_layer_tool = TextLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)
        elif e == "annotation_layer":
            chart_layer_tool = AnnotationLayerToolFrame(self)
            chart_layer_tool._id = len(self._tool_instances)

        current_index = self.stackedWidget_2.currentIndex()

        self._tool_instances.append(chart_layer_tool)
        self._chart_instances.append(ChartLayer(self).chart_layer(e))

        if current_index == 0:
            self.gridLayout_14.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 1:
            self.gridLayout_3.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 2:
            self.gridLayout_15.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 3:
            self.gridLayout_16.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 4:
            self.gridLayout_17.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 5:
            self.gridLayout_18.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 6:
            self.gridLayout_19.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 7:
            self.gridLayout_20.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 8:
            self.gridLayout_21.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 9:
            self.gridLayout_22.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 10:
            self.gridLayout_23.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 11:
            self.gridLayout_24.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 12:
            self.gridLayout_25.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 13:
            self.gridLayout_26.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 14:
            self.gridLayout_27.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 15:
            self.gridLayout_28.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)
        elif current_index == 16:
            self.gridLayout_29.addWidget(chart_layer_tool, len(self._tool_instances), 0, 1, 2)

    def add_layer_btn_clicked(self):
        self.custom_dialog.show()

    def set_df(self, df):
        self.df = df
        self.selected_chart = self.chart_type_combo.currentText()
        self.get_selected_chart()

    def chart_changed(self, e):
        self.selected_chart = e
        self.get_selected_chart()

    def get_selected_chart(self):
        self.canvas_grid_check_box.setCheckState(Qt.CheckState.Unchecked)
        self.grid_transparent_slider.setEnabled(False)
        self.grid_transparent_slider.setValue(50)

        if self.chart:
            self.chart.deleteLater()
            for widget in self._tool_instances:
                if widget:
                    widget.deleteLater()
            self._tool_instances = []
            self._chart_instances = []

        if self.selected_chart == "BarChart":
            self.stackedWidget_2.setCurrentIndex(0)
            self.chart = BarChart(self)

            self.chart_tool = BarChartToolFrame(self)
            self.chart_tool.setObjectName(u"bar_chart_tool")
            self.chart_tool.setFrameShape(QFrame.Shape.StyledPanel)
            self.chart_tool.setFrameShadow(QFrame.Shadow.Raised)
            self.gridLayout_14.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "LineChart":
            self.stackedWidget_2.setCurrentIndex(1)
            self.chart = LineChart(self)

            self.chart_tool = LineChartToolFrame(self)
            self.chart_tool.setObjectName(u"line_chart_tool")
            self.chart_tool.setFrameShape(QFrame.Shape.StyledPanel)
            self.chart_tool.setFrameShadow(QFrame.Shadow.Raised)
            self.gridLayout_3.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "HBarChart":
            self.stackedWidget_2.setCurrentIndex(2)
            self.chart = HBarChart(self)
            self.chart_tool = HBarChartToolFrame(self)
            self.gridLayout_15.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "ScatterChart":
            self.stackedWidget_2.setCurrentIndex(3)
            self.chart = ScatterChart(self)
            self.chart_tool = ScatterChartToolFrame(self)
            self.gridLayout_16.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "StackedAreaChart":
            self.stackedWidget_2.setCurrentIndex(4)
            self.chart = AreaChart(self)
            self.chart_tool = AreaChartToolFrame(self)
            self.gridLayout_17.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "StemChart":
            self.stackedWidget_2.setCurrentIndex(5)
            self.chart = StemChart(self)
            self.chart_tool = StemChartToolFrame(self)
            self.gridLayout_18.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "RadarChart":
            self.stackedWidget_2.setCurrentIndex(6)
            self.chart = RadarChart(self)
            self.chart_tool = RadarChartToolFrame(self)
            self.gridLayout_19.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "Histgram":
            self.stackedWidget_2.setCurrentIndex(7)
            self.chart = Histgram(self)
            self.chart_tool = HistgramChartToolFrame(self)
            self.gridLayout_20.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "PieChart":
            self.stackedWidget_2.setCurrentIndex(8)
            self.chart = PieChart(self)
            self.chart_tool = PieChartToolFrame(self)
            self.gridLayout_21.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "PieChartWithBar":
            self.stackedWidget_2.setCurrentIndex(17)
            self.chart = PieChartWithBar(self)
            self.chart_tool = PieChartWithBarToolFrame(self)
            self.gridLayout_30.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "BoxChart":
            self.stackedWidget_2.setCurrentIndex(9)
            self.chart = BoxChart(self)
            self.chart_tool = BoxChartToolFrame(self)
            self.gridLayout_22.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "ErrorChart":
            self.stackedWidget_2.setCurrentIndex(10)
            self.chart = ErrorBarChart(self)
            self.chart_tool = ErrorBarChartToolFrame(self)
            self.gridLayout_23.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "ViolinChart":
            self.stackedWidget_2.setCurrentIndex(11)
            self.chart = ViolinChart(self)
            self.chart_tool = ViolinChartToolFrame(self)
            self.gridLayout_24.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "HeatmapChart":
            self.stackedWidget_2.setCurrentIndex(12)
            self.chart = HeatMapChart(self)
            self.chart_tool = HeatMapChartToolFrame(self)
            self.gridLayout_25.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "EventChart":
            self.stackedWidget_2.setCurrentIndex(13)
            self.chart = EventChart(self)
            self.chart_tool = EventChartToolFrame(self)
            self.gridLayout_26.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "AutoCorrelationChart":
            self.stackedWidget_2.setCurrentIndex(14)
            self.chart = AutoCorrelationChart(self)
            self.chart_tool = AutoCorrelationChartToolFrame(self)
            self.gridLayout_27.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "StairsChart":
            self.stackedWidget_2.setCurrentIndex(15)
            self.chart = StairsChart(self)
            self.chart_tool = StairsChartToolFrame(self)
            self.gridLayout_28.addWidget(self.chart_tool, 0, 0, 1, 2)
        elif self.selected_chart == "WordcloudChart":
            self.stackedWidget_2.setCurrentIndex(16)
            self.chart = WordcloudChart(self)
            self.chart_tool = WordcloudChartToolFrame(self)
            self.gridLayout_29.addWidget(self.chart_tool, 0, 0, 1, 2)

        if not self.df.empty:
            cols = self.df.columns.tolist()
            self.chart_tool.x_series_combo.clear()
            self.chart_tool.x_series_combo.addItems(cols)
            self.chart_tool.y_series_combo.clear()
            if self.selected_chart in ["PieChart", "PieChartWithBar", "AutoCorrelationChart", "WordcloudChart"]:
                self.chart_tool.y_series_combo.addItems(cols)
            else:
                self.chart_tool.y_series_combo.addCheckableItems(cols)
                self.chart_tool.y_series_combo.setCurrentIndex(1)
                self.chart_tool.y_series_combo.model().item(1).setCheckState(Qt.CheckState.Checked)

        self.chart.update_plot()


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    window_icon_path = os.path.join(base_dir, "icon.ico")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(window_icon_path))
    qdarktheme.setup_theme("dark")
    w = MainWindow()
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
