import numpy as np
import matplotlib.pyplot as plt
from charts.base.base_polar_chart import BasePolarChart


class RadarChart(BasePolarChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(RadarChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        super().update_plot()
        self.base_layer()

        # 设置x轴y轴标签和刻度
        self.set_x_label_and_ticks()
        self.set_y_label_and_ticks()
        # 设置标题
        self.set_title()
        # 其他设置不生效
        # self.set_other_settings()
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

            theta_offset = self.parent.chart_tool.theta_offset
            theta_direction = self.parent.chart_tool.theta_direction
            line_width = self.parent.chart_tool.line_width
            line_type = self.parent.chart_tool.line_type

            line_colors = (self.parent.chart_tool.radar_line_color_series_line.text().strip().split(",")
                           if self.parent.chart_tool.radar_line_color_series_line.text().strip() else [])
            if len(line_colors) < len(cols):
                line_colors.extend(["C{}".format(i) for i in range(len(cols) - len(line_colors))])

            fill_colors = (self.parent.chart_tool.radar_fill_color_series_line.text().strip().split(",")
                          if self.parent.chart_tool.radar_fill_color_series_line.text().strip() else [])
            if len(fill_colors) < len(cols):
                fill_colors.extend(["C{}".format(i) for i in range(len(cols) - len(fill_colors))])

            fill_transparent = self.parent.chart_tool.fill_transparent

            value_label_checked = self.parent.chart_tool.value_label_checked

            value_label_color = self.parent.chart_tool.value_label_color
            value_label_interval = self.parent.chart_tool.value_label_interval
            value_labels_size = self.parent.chart_tool.value_labels_size

            for i, col in enumerate(cols):
                angles = np.linspace(0, 2 * np.pi, len(x_series), endpoint=False)
                angles = np.concatenate((angles, [angles[0]]))
                y_series = np.concatenate((self.parent.df[col].values, [self.parent.df[col].values[0]]))

                self.canvas.axs.set_theta_offset(theta_offset)
                self.canvas.axs.set_theta_direction(theta_direction)
                self.canvas.axs.plot(angles, y_series, linewidth=line_width, linestyle=line_type,
                                     color=line_colors[i], label=data_labels[i])
                self.canvas.axs.fill(angles, y_series, color=fill_colors[i], alpha=fill_transparent)
                self.canvas.axs.set_xticks(angles[:-1], labels=x_series)

                if value_label_checked:
                    for j in range(len(x_series)):
                        self.canvas.axs.text(angles[j],
                                             y_series[j] + value_label_interval,
                                             y_series[j],
                                             ha="center",
                                             color=value_label_color,
                                             fontsize=value_labels_size
                                             )

