from charts.base.base_chart import BaseChart


class ErrorBarChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(ErrorBarChart, self).__init__(parent=parent, *args, **kwargs)
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
            x_series = self.parent.df[x_col]

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

            _x_err_series_col = self.parent.chart_tool.x_err_series
            _y_err_series_col = self.parent.chart_tool.y_err_series

            x_err_series = None
            y_err_series = None
            if _x_err_series_col != "none":
                x_err_series = self.parent.df[_x_err_series_col]
            if _y_err_series_col != "none":
                y_err_series = self.parent.df[_y_err_series_col]

            err_line_width = self.parent.chart_tool.err_line_width
            cap_size = self.parent.chart_tool.cap_size
            err_every = self.parent.chart_tool.err_every

            marker = self.parent.chart_tool.marker
            marker_size = self.parent.chart_tool.marker_size
            marker_edge_width = self.parent.chart_tool.marker_edge_width
            marker_edge_color = self.parent.chart_tool.marker_edge_color
            marker_face_color = self.parent.chart_tool.marker_face_color
            line_style = self.parent.chart_tool.line_style
            line_colors = (self.parent.chart_tool.line_color_line.text().strip().split(",")
                           if self.parent.chart_tool.line_color_line.text() else [])
            if len(line_colors) < len(cols):
                line_colors.extend(["C{}".format(i) for i in range((len(cols) - len(line_colors)))])

            bar_above_checked = self.parent.chart_tool.bars_above_checked
            lower_limits_checked = self.parent.chart_tool.lower_limits_checked
            upper_limits_checked = self.parent.chart_tool.upper_limits_checked
            xlower_limits_checked = self.parent.chart_tool.xlower_limits_checked
            xupper_limits_checked = self.parent.chart_tool.xupper_limits_checked


            for i, col in enumerate(cols):
                y_series = self.parent.df[col]

                self.canvas.axs.errorbar(
                    x_series,
                    y_series,
                    xerr=x_err_series,
                    yerr=y_err_series,
                    ecolor=color_series[i],
                    elinewidth=err_line_width,
                    capsize=cap_size,
                    errorevery=err_every,
                    fmt=marker,
                    markersize=marker_size,
                    markerfacecolor=marker_face_color,
                    markeredgecolor=marker_edge_color,
                    markeredgewidth=marker_edge_width,
                    linestyle=line_style,
                    color=line_colors[i],
                    label=data_labels[i],
                    barsabove=bar_above_checked,
                    lolims=lower_limits_checked,
                    uplims=upper_limits_checked,
                    xlolims=xlower_limits_checked,
                    xuplims=xupper_limits_checked,
                )




