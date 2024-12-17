import matplotlib.pyplot as plt

from charts.base.base_chart import BaseChart


class StemChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(StemChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        super().update_plot()
        self.base_layer()

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

    def base_layer(self):
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

            base_colors = (self.parent.chart_tool.base_line_color_series_line.text().strip().split(",")
                           if self.parent.chart_tool.base_line_color_series_line.text().strip() else [])
            if len(base_colors) < len(cols):
                for i in range((len(cols) - len(base_colors))):
                    base_colors.append("C{}".format(i))

            stem_colors = (self.parent.chart_tool.stem_line_color_series_line.text().strip().split(",")
                           if self.parent.chart_tool.stem_line_color_series_line.text().strip() else [])
            if len(stem_colors) < len(cols):
                for i in range((len(cols) - len(stem_colors))):
                    stem_colors.append("C{}".format(i))

            marker_colors = (self.parent.chart_tool.marker_color_series_line.text().strip().split(",")
                             if self.parent.chart_tool.marker_color_series_line.text().strip() else [])
            if len(marker_colors) < len(cols):
                for i in range((len(cols) - len(marker_colors))):
                    marker_colors.append("C{}".format(i))

            base_line_type = self.parent.chart_tool.base_line_type
            stem_line_type = self.parent.chart_tool.stem_line_type
            marker_type = self.parent.chart_tool.marker_type

            value_label_checked = self.parent.chart_tool.value_label_checked
            value_labels = (self.parent.chart_tool.value_labels.strip().split(",")
                            if self.parent.chart_tool.value_labels.strip() else [])
            if 0 < len(value_labels) < len(x_series):
                value_labels.extend([""] * (len(x_series) - len(value_labels)))
            value_label_interval = self.parent.chart_tool.value_label_interval
            value_label_color = self.parent.chart_tool.value_label_color
            value_label_size = self.parent.chart_tool.value_label_size

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                markerline, stemline, baseline = self.canvas.axs.stem(
                    x_series,
                    y_series,
                    markerfmt=marker_type,
                    linefmt=stem_line_type,
                    basefmt=base_line_type,
                    label=data_labels[i]
                )
                plt.setp(markerline, "color", marker_colors[i])
                plt.setp(stemline, "color", stem_colors[i])
                plt.setp(baseline, "color", base_colors[i])

                if value_label_checked:
                    print(value_labels)
                    if len(value_labels) == 0:
                        for j in range(len(x_series)):
                            self.canvas.axs.text(
                                x_series[j],
                                y_series[j] + value_label_interval,
                                y_series[j],
                                ha="center",
                                color=value_label_color,
                                fontsize=value_label_size
                            )
                    else:
                        for j in range(len(x_series)):
                            print(j)
                            self.canvas.axs.text(
                                x_series[j],
                                y_series[j] + value_label_interval,
                                value_labels[j],
                                ha="center",
                                color=value_label_color,
                                fontsize=value_label_size
                            )

