import numpy as np

from charts.chart_layers.base_chart_layer import BaseChartLayer


class RegressionLayer(BaseChartLayer):
    def __init__(self, parent):
        super(RegressionLayer, self).__init__()
        self.parent = parent

    def chart_layer_plot(self, layer_pos, canvas):
        if not self.parent.df.empty:
            x_col = self.parent.chart_tool.x_series_combo.currentText()
            y_col = self.parent._tool_instances[layer_pos].y_series_combo.currentText()
            if not y_col.strip():
                return canvas.axs.plot()
            data_label_line = self.parent._tool_instances[layer_pos].data_label_line.text().strip()

            x_series = self.parent.df[x_col].values

            cols = y_col.split(",")
            data_labels = data_label_line.split(",")
            if len(data_labels) < len(cols):
                data_labels.extend((len(cols) - len(data_labels)) * [None])

            line_colors = (self.parent._tool_instances[layer_pos].line_color_series_line.text().strip().split(",")
                      if self.parent._tool_instances[layer_pos].line_color_series_line.text().strip() else [])
            if len(line_colors) < len(cols):
                line_colors.extend(["C{}".format(i) for i in range((len(cols) - len(line_colors)))])

            line_style = self.parent._tool_instances[layer_pos].line_style
            line_width = self.parent._tool_instances[layer_pos].line_width
            line_transparency = self.parent._tool_instances[layer_pos].line_transparency

            ci_colors = (self.parent._tool_instances[layer_pos].ci_color_series_line.text().strip().split(",")
                      if self.parent._tool_instances[layer_pos].ci_color_series_line.text().strip() else [])
            if len(ci_colors) < len(cols):
                ci_colors.extend(["C{}".format(i) for i in range((len(cols) - len(ci_colors)))])

            ci_transparency = self.parent._tool_instances[layer_pos].ci_transparency

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                a, b = np.polyfit(x_series, y_series, deg=1)
                y_est = a * x_series + b
                y_err = x_series.std() * np.sqrt(1 / len(x_series) + (x_series - x_series.mean()) ** 2 / np.sum((x_series - x_series.mean()) ** 2))

                canvas.axs.plot(
                    x_series,
                    y_est,
                    color=line_colors[i],
                    label=data_labels[i],
                    alpha=line_transparency,
                    linewidth=line_width,
                    linestyle=line_style
                )

                canvas.axs.fill_between(
                    x_series,
                    y_est - y_err,
                    y_est + y_err,
                    color=ci_colors[i],
                    alpha=ci_transparency
                )



