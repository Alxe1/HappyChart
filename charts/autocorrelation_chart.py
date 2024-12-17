from charts.base.base_chart import BaseChart


class AutoCorrelationChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(AutoCorrelationChart, self).__init__(parent=parent, *args, **kwargs)
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

            use_vline = self.parent.chart_tool.use_vline_checked
            vline_color = self.parent.chart_tool.vline_color
            vline_style = self.parent.chart_tool.vline_style
            vline_width = self.parent.chart_tool.vline_width

            hline_color = self.parent.chart_tool.hline_color
            hline_style = self.parent.chart_tool.hline_style
            hline_width = self.parent.chart_tool.hline_width

            norm = self.parent.chart_tool.norm_checked
            max_lag = self.parent.chart_tool.max_lag

            ac = self.canvas.axs.acorr(
                self.parent.df[y_col],
                usevlines=use_vline,
                normed=norm,
                maxlags=max_lag
            )

            ac[2].set_color(vline_color)
            ac[2].set_linestyle(vline_style)
            ac[2].set_linewidth(vline_width)

            if use_vline:
                ac[3].set_color(hline_color)
                ac[3].set_linestyle(hline_style)
                ac[3].set_linewidth(hline_width)

