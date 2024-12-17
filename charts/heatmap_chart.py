import numpy as np
import matplotlib.pyplot as plt

from charts.base.base_chart import BaseChart


class HeatMapChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(HeatMapChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.color_bar = None

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
            cols = y_col.split(",")

            normalization_checked = self.parent.chart_tool.normalization_checked
            show_text_checked = self.parent.chart_tool.show_text_checked
            text_color = self.parent.chart_tool.text_color
            cmap = self.parent.chart_tool.cmap
            show_colorbar_checked = self.parent.chart_tool.show_colorbar_checked

            y_series = self.parent.df[cols].values
            if normalization_checked:
                mins = y_series.min(axis=0)
                maxs = y_series.max(axis=0)
                y_series = (y_series - mins) / (maxs - mins)
                y_series = np.around(y_series, 2)

            im = self.canvas.axs.imshow(y_series, cmap=cmap)

            if show_text_checked:
                for i in range(y_series.shape[0]):
                    for j in range(y_series.shape[1]):
                        self.canvas.axs.text(j, i, y_series[i, j], ha="center", va="center", color=text_color)

            self.canvas.axs.set_xticks(range(len(cols)), cols)
            self.canvas.axs.set_yticks(range(len(cols)), cols)

            if show_colorbar_checked:
                plt.colorbar(im)
