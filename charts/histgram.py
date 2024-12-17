import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as _colors

from charts.base.base_chart import BaseChart


class Histgram(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
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

            if len(cols) > len(data_labels):
                res_label_len = len(cols) - len(data_labels)
                data_labels.extend(res_label_len * [None])

            bin_num = self.parent.chart_tool.bin_num
            bin_range_min = self.parent.chart_tool.bin_range_min
            bin_range_max = self.parent.chart_tool.bin_range_max
            bihist_checked = self.parent.chart_tool.bihist_checked
            density_checked = self.parent.chart_tool.density_checked
            cumulative_checked = self.parent.chart_tool.cumulative_checked
            log_checked = self.parent.chart_tool.log_checked
            bottom_distance = self.parent.chart_tool.bottom_distance
            hist_type = self.parent.chart_tool.hist_type
            align = self.parent.chart_tool.align
            orientation = self.parent.chart_tool.orientation
            stacked_checked = self.parent.chart_tool.stacked_checked
            transparency = self.parent.chart_tool.transparency

            colors = (self.parent.chart_tool.color_series_line.text().strip().split(",")
                      if self.parent.chart_tool.color_series_line.text().strip() else [])
            if len(colors) < len(cols):
                colors.extend((len(cols) - len(colors)) * [None])

            if bihist_checked:
                if len(cols) >= 2:
                    cols = cols[:2]
                    data1 = self.parent.df[cols[0]]
                    data2 = self.parent.df[cols[1]]
                    if bin_range_min == 0 and bin_range_max == 0:
                        self.canvas.axs.hist(data1, bins=bin_num, range=None, density=density_checked,
                                             cumulative=cumulative_checked, bottom=bottom_distance, histtype=hist_type,
                                             align=align, orientation=orientation, log=log_checked, color=colors[0],
                                             label=data_labels[0], stacked=stacked_checked, alpha=transparency)
                        self.canvas.axs.hist(data2, bins=bin_num, range=None, density=density_checked,
                                             weights=-np.ones_like(data2), cumulative=cumulative_checked,
                                             bottom=bottom_distance, histtype=hist_type, align=align,
                                             orientation=orientation, log=log_checked, color=colors[1],
                                             label=data_labels[1], stacked=stacked_checked, alpha=transparency)
                    else:
                        self.canvas.axs.hist(data1, bins=bin_num, range=(bin_range_min, bin_range_max),
                                             density=density_checked, cumulative=cumulative_checked,
                                             bottom=bottom_distance, histtype=hist_type, align=align,
                                             orientation=orientation, log=log_checked, color=colors[0],
                                             label=data_labels[0], stacked=stacked_checked, alpha=transparency)
                        self.canvas.axs.hist(data2, bins=bin_num, range=(bin_range_min, bin_range_max),
                                             density=density_checked, weights=-np.ones_like(data2),
                                             cumulative=cumulative_checked, bottom=bottom_distance,
                                             histtype=hist_type, align=align, orientation=orientation, log=log_checked,
                                             color=colors[1], label=data_labels[1], stacked=stacked_checked,
                                             alpha=transparency)
            else:
                for i, col in enumerate(cols):
                    data = self.parent.df[col]
                    if bin_range_min == 0 and bin_range_max == 0:
                        self.canvas.axs.hist(data, bins=bin_num, range=None, density=density_checked,
                                             cumulative=cumulative_checked, bottom=bottom_distance, histtype=hist_type,
                                             align=align, orientation=orientation, log=log_checked, color=colors[i],
                                             label=data_labels[i], stacked=stacked_checked, alpha=transparency)
                    else:
                        self.canvas.axs.hist(data, bins=bin_num, range=(bin_range_min, bin_range_max),
                                             density=density_checked, cumulative=cumulative_checked,
                                             bottom=bottom_distance, histtype=hist_type, align=align,
                                             orientation=orientation, log=log_checked, color=colors[i],
                                             label=data_labels[i], stacked=stacked_checked, alpha=transparency)
