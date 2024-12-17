from charts.base.base_chart import BaseChart


class AreaChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(AreaChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        super().update_plot()
        self.base_area_layer()

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

    def base_area_layer(self):
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

            colors = (self.parent.chart_tool.area_color_series_line.text().strip().split(",")
                      if self.parent.chart_tool.area_color_series_line.text().strip() else [])
            if len(colors) < len(cols):
                colors.extend([None] * (len(cols) - len(colors)))

            area_baseline = self.parent.chart_tool.area_baseline
            area_transparent = self.parent.chart_tool.area_transparent

            self.canvas.axs.stackplot(
                x_series,
                *[self.parent.df[col].values for col in cols],
                labels=data_labels,
                colors=colors,
                baseline=area_baseline,
                alpha=area_transparent
            )
