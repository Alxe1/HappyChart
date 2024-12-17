from charts.base.base_chart import BaseChart


class PieChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(PieChart, self).__init__(parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        super().update_plot()
        self.base_layer()

        # 设置x轴y轴标签和刻度
        self.set_x_label_and_ticks()
        self.set_y_label_and_ticks()
        # 设置标题
        self.set_title()
        # 其他设置
        # self.set_other_settings()
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

            y_series = self.parent.df[y_col]
            data_labels = data_label_line.split(",")
            if len(y_series) > len(data_labels):
                data_labels.extend((len(y_series) - len(data_labels)) * [None])

            pie_colors = (self.parent.chart_tool.color_series_line.text().strip().split(",")
                          if self.parent.chart_tool.color_series_line.text().strip() else [])
            if len(pie_colors) < len(y_series):
                pie_colors.extend(["C{}".format(i) for i in range((len(y_series) - len(pie_colors)))])

            autopct = self.parent.chart_tool.pct
            pct_distance = self.parent.chart_tool.pct_distance
            label_distance = self.parent.chart_tool.label_distance
            explode_series = self.parent.chart_tool.explode_series
            if len(explode_series) < len(y_series):
                explode_series.extend((len(y_series) - len(explode_series)) * [0])
            start_angle = self.parent.chart_tool.start_angle
            radius = self.parent.chart_tool.radius
            unticlockwise = self.parent.chart_tool.unticlockwise_checked
            shadow = self.parent.chart_tool.shadow_checked
            text_props = None
            if self.parent.chart_tool.text_props_checked:
                text_props = {
                    "fontsize": self.parent.chart_tool.font_size,
                    "color": self.parent.chart_tool.font_color
                }
            wedge_props = None
            if self.parent.chart_tool.wedge_props_checked:
                wedge_props = {
                    "edgecolor": self.parent.chart_tool.edge_color,
                    "linewidth": self.parent.chart_tool.line_width,
                    "linestyle": self.parent.chart_tool.line_style,
                    "width": self.parent.chart_tool.wedge_width,
                    "alpha": self.parent.chart_tool.transparency
                }

            self.canvas.axs.pie(
                y_series,
                labels=data_labels,
                colors=pie_colors,
                autopct=autopct,
                pctdistance=pct_distance,
                labeldistance=label_distance,
                explode=explode_series,
                startangle=start_angle,
                radius=radius,
                counterclock=unticlockwise,
                shadow=shadow,
                textprops=text_props,
                wedgeprops=wedge_props
            )
