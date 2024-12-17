from matplotlib import patheffects

from charts.chart_layers.base_chart_layer import BaseChartLayer


class LineLayer(BaseChartLayer):
    def __init__(self, parent=None):
        super(LineLayer, self).__init__()
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
            colors = (self.parent._tool_instances[layer_pos].line_color_series_line.text().strip().split(",")
                      if self.parent._tool_instances[layer_pos].line_color_series_line.text().strip() else [])

            if len(data_labels) < len(cols):
                data_labels.extend((len(cols) - len(data_labels)) * [None])

            if len(colors) < len(cols):
                colors.extend((len(cols) - len(colors)) * [None])

            if len(self.parent._tool_instances[layer_pos].line_types) < len(cols):
                self.parent._tool_instances[layer_pos].line_types.extend(
                    (len(cols) - len(self.parent._tool_instances[layer_pos].line_types)) * [None]
                )

            if len(self.parent._tool_instances[layer_pos].markers) < len(cols):
                self.parent._tool_instances[layer_pos].markers.extend(
                    (len(cols) - len(self.parent._tool_instances[layer_pos].markers)) * [None]
                )

            if self.parent._tool_instances[layer_pos].path_checked:
                path_effects = [patheffects.withTickedStroke(
                    spacing=self.parent._tool_instances[layer_pos].path_interval,
                    angle=self.parent._tool_instances[layer_pos].path_angle
                )]
            else:
                path_effects = []

            value_label_colors = (
                self.parent._tool_instances[layer_pos].line_value_label_color_series_line.text().strip().split(",")
                if self.parent._tool_instances[layer_pos].line_value_label_color_series_line.text().strip() else []
            )

            if len(value_label_colors) < len(cols):
                value_label_colors.extend((len(cols) - len(value_label_colors)) * [None])

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                line = canvas.axs.plot(x_series, y_series, color=colors[i], label=data_labels[i],
                                            linestyle=self.parent._tool_instances[layer_pos].line_types[i],
                                            linewidth=self.parent._tool_instances[layer_pos].line_width,
                                            marker=self.parent._tool_instances[layer_pos].markers[i],
                                            markersize=self.parent._tool_instances[layer_pos].marker_size,
                                            path_effects=path_effects
                                            )
                if self.parent._tool_instances[layer_pos].value_label_check:
                    for j in range(len(x_series)):
                        canvas.axs.text(
                            x_series[j],
                            y_series[j] + self.parent._tool_instances[layer_pos].value_label_interval,
                            y_series[j],
                            ha=("left" if self.parent._tool_instances[layer_pos].value_labels_horiz_pos == "right"
                                else "right" if self.parent._tool_instances[layer_pos].value_labels_horiz_pos == "left"
                            else "center"),
                            va=("bottom" if self.parent._tool_instances[layer_pos].value_label_vertic_pos == "top"
                                else "top" if self.parent._tool_instances[layer_pos].value_labels_horiz_pos == "bottom"
                            else "center"),
                            fontsize=self.parent._tool_instances[layer_pos].value_label_size,
                            color=value_label_colors[i]
                        )
