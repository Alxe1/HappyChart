from matplotlib import patheffects

from charts.base.base_chart import BaseChart


class LineChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(LineChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        super().update_plot()
        self.base_line_layer()

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

    def base_line_layer(self):
        if not self.parent.df.empty:
            x_col = self.parent.chart_tool.x_series_combo.currentText()
            y_col = self.parent.chart_tool.y_series_combo.currentText()
            if not y_col.strip():
                return self.canvas.axs.plot()
            data_label_line = self.parent.chart_tool.data_label_line.text().strip()

            x_series = self.parent.df[x_col].values

            cols = y_col.split(",")
            data_labels = data_label_line.split(",")
            colors = (self.parent.chart_tool.line_color_series_line.text().strip().split(",")
                      if self.parent.chart_tool.line_color_series_line.text().strip() else [])

            if len(data_labels) < len(cols):
                data_labels.extend((len(cols) - len(data_labels)) * [None])

            if len(colors) < len(cols):
                colors.extend((len(cols) - len(colors)) * [None])

            if len(self.parent.chart_tool.line_types) < len(cols):
                self.parent.chart_tool.line_types.extend(
                    (len(cols) - len(self.parent.chart_tool.line_types)) * [None]
                )

            if len(self.parent.chart_tool.markers) < len(cols):
                self.parent.chart_tool.markers.extend(
                    (len(cols) - len(self.parent.chart_tool.markers)) * [None]
                )

            if self.parent.chart_tool.path_checked:
                path_effects = [patheffects.withTickedStroke(
                    spacing=self.parent.chart_tool.path_interval,
                    angle=self.parent.chart_tool.path_angle
                )]
            else:
                path_effects = []

            value_label_colors = (
                self.parent.chart_tool.line_value_label_color_series_line.text().strip().split(",")
                if self.parent.chart_tool.line_value_label_color_series_line.text().strip() else []
            )

            if len(value_label_colors) < len(cols):
                value_label_colors.extend((len(cols) - len(value_label_colors)) * [None])

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                line = self.canvas.axs.plot(x_series, y_series, color=colors[i], label=data_labels[i],
                                            linestyle=self.parent.chart_tool.line_types[i],
                                            linewidth=self.parent.chart_tool.line_width,
                                            marker=self.parent.chart_tool.markers[i],
                                            markersize=self.parent.chart_tool.marker_size,
                                            path_effects=path_effects
                                            )
                if self.parent.chart_tool.value_label_check:
                    for j in range(len(x_series)):
                        self.canvas.axs.text(
                            x_series[j],
                            y_series[j] + self.parent.chart_tool.value_label_interval,
                            y_series[j],
                            ha=("left" if self.parent.chart_tool.value_labels_horiz_pos == "right"
                                else "right" if self.parent.chart_tool.value_labels_horiz_pos == "left"
                            else "center"),
                            va=("bottom" if self.parent.chart_tool.value_label_vertic_pos == "top"
                                else "top" if self.parent.chart_tool.value_labels_horiz_pos == "bottom"
                            else "center"),
                            fontsize=self.parent.chart_tool.value_label_size,
                            color=value_label_colors[i]
                        )
