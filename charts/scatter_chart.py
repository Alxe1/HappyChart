import matplotlib.pyplot as plt

from charts.base.base_chart import BaseChart


class ScatterChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(ScatterChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        super().update_plot()
        self.base_scatter_layer()

        if len(self.parent._chart_instances) != 0:
            for i, layer in enumerate(self.parent._chart_instances):
                if layer:
                    layer.chart_layer_plot(i, self.canvas)

        # 设置x轴y轴标签和刻度
        self.set_x_label_and_ticks()
        self.set_y_label_and_ticks()
        # 设置标题
        self.set_title()
        # 其他设置
        self.set_other_settings()
        # 设置图例和tick范围
        self.set_legend()
        self.set_x_tick_range()
        self.set_y_tick_range()

        self.parent.chartScrollArea.setWidget(self.canvas)
        self.canvas.draw()

    def base_scatter_layer(self):
        if not self.parent.df.empty:
            x_col = self.parent.chart_tool.x_series_combo.currentText()
            y_col = self.parent.chart_tool.y_series_combo.currentText()
            if not y_col.strip():
                return self.canvas.axs.plot()

            data_label_line = self.parent.chart_tool.data_label_line.text().strip()

            x_series = self.parent.df[x_col].values
            cols = y_col.split(",")
            data_labels = data_label_line.split(",")

            if len(data_labels) < len(cols):
                data_labels.extend([None] * (len(cols) - len(data_labels)))

            if self.parent.chart_tool.scatter_size in self.parent.df.columns.tolist():
                scatter_size = self.parent.df[self.parent.chart_tool.scatter_size].values + self.parent.chart_tool.scatter_size_base
            else:
                try:
                    if self.parent.chart_tool.scatter_size:
                        scatter_size = float(self.parent.chart_tool.scatter_size) + self.parent.chart_tool.scatter_size_base
                    else:
                        scatter_size = None
                except ValueError:
                    scatter_size = None

            if self.parent.chart_tool.scatter_color in self.parent.df.columns.tolist():
                scatter_color = self.parent.df[self.parent.chart_tool.scatter_color].values
            else:
                scatter_color = self.parent.chart_tool.scatter_color if self.parent.chart_tool.scatter_color else None
            scatter_marker = self.parent.chart_tool.scatter_marker
            scatter_edge_color = self.parent.chart_tool.scatter_edge_color
            scatter_line_width = self.parent.chart_tool.scatter_line_width
            scatter_transparent = self.parent.chart_tool.scatter_transparent
            add_colorbar_checked = self.parent.chart_tool.add_colorbar_checked

            for i, col in enumerate(cols):
                scatter = self.canvas.axs.scatter(
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
