import matplotlib.pyplot as plt

from charts.chart_layers.base_chart_layer import BaseChartLayer


class ScatterLayer(BaseChartLayer):
    def __init__(self, parent=None):
        super(ScatterLayer, self).__init__()
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
                data_labels.extend([None] * (len(cols) - len(data_labels)))

            if self.parent._tool_instances[layer_pos].scatter_size in self.parent.df.columns.tolist():
                scatter_size = (self.parent.df[self.parent._tool_instances[layer_pos].scatter_size].values
                                + self.parent._tool_instances[layer_pos].scatter_size_base)
            else:
                try:
                    if self.parent._tool_instances[layer_pos].scatter_size:
                        scatter_size = float(self.parent._tool_instances[layer_pos].scatter_size) + self.parent._tool_instances[layer_pos].scatter_size_base
                    else:
                        scatter_size = None
                except ValueError:
                    scatter_size = None

            if self.parent._tool_instances[layer_pos].scatter_color in self.parent.df.columns.tolist():
                scatter_color = self.parent.df[self.parent._tool_instances[layer_pos].scatter_color].values
            else:
                scatter_color = self.parent._tool_instances[layer_pos].scatter_color if self.parent._tool_instances[layer_pos].scatter_color else None
            scatter_marker = self.parent._tool_instances[layer_pos].scatter_marker
            scatter_edge_color = self.parent._tool_instances[layer_pos].scatter_edge_color
            scatter_line_width = self.parent._tool_instances[layer_pos].scatter_line_width
            scatter_transparent = self.parent._tool_instances[layer_pos].scatter_transparent
            add_colorbar_checked = self.parent._tool_instances[layer_pos].add_colorbar_checked

            for i, col in enumerate(cols):
                scatter = canvas.axs.scatter(
                    x_series,
                    self.parent.df[col].values,
                    s=scatter_size,
                    c=scatter_color,
                    marker=scatter_marker,
                    edgecolors=scatter_edge_color,
                    linewidth=scatter_line_width,
                    alpha=scatter_transparent,
                    label=data_labels[i]
                )
                if add_colorbar_checked:
                    plt.colorbar(scatter)
