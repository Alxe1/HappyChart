from charts.chart_layers.annotation_layer import AnnotationLayer
from charts.chart_layers.cdf_layer import CDFLayer
from charts.chart_layers.density_layer import DensityLayer
from charts.chart_layers.errorbar_layer import ErrorbarLayer
from charts.chart_layers.fill_between_layer import FillBetweenLayer
from charts.chart_layers.line_layer import LineLayer
from charts.chart_layers.regression_layer import RegressionLayer
from charts.chart_layers.scatter_layer import ScatterLayer
from charts.chart_layers.span_layer import SpanLayer
from charts.chart_layers.stairs_layer import StairsLayer
from charts.chart_layers.text_layer import TextLayer
from charts.chart_layers.vhline_layer import VHLineLayer


class ChartLayer(object):
    def __init__(self, parent):
        super(ChartLayer, self).__init__()
        self.parent = parent

    def chart_layer(self, selected_chart):
        chart_layer = None
        if selected_chart == "line_layer":
            chart_layer = LineLayer(self.parent)
        if selected_chart == "scatter_layer":
            chart_layer = ScatterLayer(self.parent)
        if selected_chart == "stairs_layer":
            chart_layer = StairsLayer(self.parent)
        if selected_chart == "errorbar_layer":
            chart_layer = ErrorbarLayer(self.parent)
        if selected_chart == "density_layer":
            chart_layer = DensityLayer(self.parent)
        if selected_chart == "cdf_layer":
            chart_layer = CDFLayer(self.parent)
        if selected_chart == "regression_layer":
            chart_layer = RegressionLayer(self.parent)
        if selected_chart == "fill_between_layer":
            chart_layer = FillBetweenLayer(self.parent)
        if selected_chart == "span_layer":
            chart_layer = SpanLayer(self.parent)
        if selected_chart == "vhline_layer":
            chart_layer = VHLineLayer(self.parent)
        if selected_chart == "text_layer":
            chart_layer = TextLayer(self.parent)
        if selected_chart == "annotation_layer":
            chart_layer = AnnotationLayer(self.parent)

        return chart_layer
