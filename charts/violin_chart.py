import numpy as np

from charts.box_chart import BoxChart


def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)

    return lower_adjacent_value, upper_adjacent_value


class ViolinChart(BoxChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(ViolinChart, self).__init__(parent, *args, **kwargs)
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

            y_series = self.parent.df[cols].values
            vert = self.parent.chart_tool.vertical_checked
            width = self.parent.chart_tool.width
            points = self.parent.chart_tool.points
            method = self.parent.chart_tool.method
            side = self.parent.chart_tool.side

            body_face_color = self.parent.chart_tool.body_face_color
            body_edge_color = self.parent.chart_tool.body_edge_color
            body_transparency = self.parent.chart_tool.transparency

            median_dot_checked = self.parent.chart_tool.median_dot_checked
            median_marker = self.parent.chart_tool.median_marker
            median_color = self.parent.chart_tool.median_color
            median_size = self.parent.chart_tool.median_size

            quantile_linestyle = self.parent.chart_tool.quantile_linestyle
            quantile_linewidth = self.parent.chart_tool.quantile_linewidth
            quantile_line_color = self.parent.chart_tool.quantile_line_color

            whisker_linestyle = self.parent.chart_tool.whisker_linestyle
            whisker_linewidth = self.parent.chart_tool.whisker_line_width
            whisker_line_color = self.parent.chart_tool.whisker_line_color

            parts = self.canvas.axs.violinplot(
                y_series,
                vert=vert,
                widths=width,
                points=points,
                showmedians=False,
                showmeans=False,
                showextrema=False,
                bw_method=method,
                side=side
            )
            for i, part in enumerate(parts['bodies']):
                part.set_facecolor(body_face_color)
                part.set_edgecolor(body_edge_color)
                part.set_alpha(body_transparency)

            quartile1, medians, quartile3 = np.percentile(y_series, [25, 50, 75], axis=0)
            sorted_array = np.sort(y_series.transpose(), axis=1)
            whiskers = np.array([adjacent_values(sa, q1, q3) for sa, q1, q3 in zip(sorted_array, quartile1, quartile3)])
            whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

            inds = np.arange(1, len(medians) + 1)

            if vert:
                if median_dot_checked:
                    self.canvas.axs.scatter(inds, medians, marker=median_marker, color=median_color, s=median_size,
                                            zorder=3)

                self.canvas.axs.vlines(inds, whiskers_min, whiskers_max, color=whisker_line_color,
                                       linestyle=whisker_linestyle, lw=whisker_linewidth)
                self.canvas.axs.vlines(inds, quartile1, quartile3, color=quantile_line_color,
                                       linestyle=quantile_linestyle, lw=quantile_linewidth)

                if not any(data_labels):
                    self.canvas.axs.set_xticks(inds)
                else:
                    self.canvas.axs.set_xticks(inds, labels=data_labels)
            else:
                if median_dot_checked:
                    self.canvas.axs.scatter(medians, inds, marker=median_marker, color=median_color, s=median_size,
                                            zorder=3)
                self.canvas.axs.hlines(inds, whiskers_min, whiskers_max, color=whisker_line_color,
                                       linestyle=whisker_linestyle, lw=whisker_linewidth)
                self.canvas.axs.hlines(inds, quartile1, quartile3, color=quantile_line_color,
                                       linestyle=quantile_linestyle, lw=quantile_linewidth)
                if not any(data_labels):
                    self.canvas.axs.set_yticks(inds)
                else:
                    self.canvas.axs.set_yticks(inds, labels=data_labels)
