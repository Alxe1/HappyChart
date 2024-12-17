from scipy.stats import gaussian_kde

from charts.chart_layers.base_chart_layer import BaseChartLayer


class DensityLayer(BaseChartLayer):
    def __init__(self, parent):
        super(DensityLayer, self).__init__()
        self.parent = parent

    def chart_layer_plot(self, layer_pos, canvas):
        if not self.parent.df.empty:
            x_col = self.parent.chart_tool.x_series_combo.currentText()
            x_series = self.parent.df[x_col].values

            y_col = self.parent._tool_instances[layer_pos].y_series_combo.currentText()
            data_label_line = self.parent._tool_instances[layer_pos].data_label_line.text().strip()
            if not y_col.strip():
                return canvas.axs.plot()

            cols = y_col.split(",")
            data_labels = data_label_line.split(",")
            if len(data_labels) < len(cols):
                data_labels.extend([None] * (len(cols) - len(data_labels)))

            color_series = (self.parent._tool_instances[layer_pos].color_series_line.text().strip().split(",")
                            if self.parent._tool_instances[layer_pos].color_series_line.text().strip() else [])
            if len(color_series) < len(cols):
                color_series.extend(["C{}".format(i) for i in range((len(cols) - len(color_series)))])

            bw_method = self.parent._tool_instances[layer_pos].bw_method
            line_width = self.parent._tool_instances[layer_pos].line_width
            line_style = self.parent._tool_instances[layer_pos].line_style
            transparency = self.parent._tool_instances[layer_pos].transparency

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                density = gaussian_kde(y_series, bw_method=bw_method)
                canvas.axs.plot(
                    x_series,
                    density(x_series),
                    color=color_series[i],
                    linestyle=line_style,
                    linewidth=line_width,
                    label=data_labels[i],
                    alpha=transparency
                )
