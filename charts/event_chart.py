from charts.base.base_chart import BaseChart


class EventChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(EventChart, self).__init__(parent=parent, *args, **kwargs)
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
            y_col = self.parent.chart_tool.y_series_combo.currentText()
            if not y_col.strip():
                return self.canvas.axs.plot()
            data_label_line = self.parent.chart_tool.data_label_line.text().strip()

            cols = y_col.split(",")
            data_labels = data_label_line.split(",")
            if len(data_labels) < len(cols):
                data_labels.extend([None] * (len(cols) - len(data_labels)))

            color_series = (self.parent.chart_tool.color_series_line.text().strip().split(",")
                                 if self.parent.chart_tool.color_series_line.text() else [])
            if len(color_series) < len(cols):
                color_series.extend(["C{}".format(i) for i in range((len(cols) - len(color_series)))])

            orientation = self.parent.chart_tool.orientation
            line_offset = self.parent.chart_tool.line_offset
            line_offsets = [line_offset * i for i in range(1, len(cols)+1)]
            line_length = self.parent.chart_tool.line_length
            line_width = self.parent.chart_tool.line_width
            line_style = self.parent.chart_tool.line_style
            transparency = self.parent.chart_tool.transparency

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                self.canvas.axs.eventplot(
                    y_series,
                    orientation=orientation,
                    colors=color_series[i],
                    lineoffsets=line_offsets[i],
                    linelengths=line_length,
                    linewidths=line_width,
                    alpha=transparency,
                    linestyles=line_style,
                    label=data_labels[i]
                )
