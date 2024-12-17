import numpy as np

from charts.base.base_chart import BaseChart


class HBarChart(BaseChart):

    def __init__(self, parent=None, *args, **kwargs):
        super(HBarChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        super().update_plot()
        self.base_hbar_layer()

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

    def base_hbar_layer(self):
        if not self.parent.df.empty:
            x_col = self.parent.chart_tool.x_series_combo.currentText()
            y_col = self.parent.chart_tool.y_series_combo.currentText()
            if not y_col.strip():
                return self.canvas.axs.plot()

            data_label_line = self.parent.chart_tool.data_label_line.text().strip()

            x_series = self.parent.df[x_col].values
            if isinstance(x_series[0], str):
                _x_series = np.arange(len(x_series))
            else:
                _x_series = np.array(x_series)

            cols = y_col.split(",")
            data_labels = data_label_line.split(",")
            colors = (self.parent.chart_tool.base_chart_color_series_line.text().strip().split(",")
                      if self.parent.chart_tool.base_chart_color_series_line.text().strip() else [])

            col_num = len(cols)
            if col_num > len(data_labels):
                res_label_len = col_num - len(data_labels)
                data_labels.extend(res_label_len * [None])
            if col_num > len(colors):
                colors.extend((col_num - len(colors)) * [None])

            _series = []
            if col_num % 2 == 0:
                a = [i for i in range(-col_num, 0) if i % 2 != 0]
                b = [i for i in range(col_num) if i % 2 != 0]
                _series.extend(a)
                _series.extend(b)
                rou = [_x_series + i * self.parent.chart_tool.width / 2 for i in _series]
            else:
                a = [i for i in range(-col_num, -1) if i % 2 == 0]
                b = [i for i in range(1, col_num) if i % 2 == 0]
                _series.extend(a)
                _series.append(0)
                _series.extend(b)
                rou = [_x_series + i * self.parent.chart_tool.width / 2 for i in _series]

            if col_num > len(self.parent.chart_tool.y_err_cols):
                self.parent.chart_tool.y_err_cols.extend((col_num - len(self.parent.chart_tool.y_err_cols))*[""])
                y_err_series_list = [self.parent.df[c].values.tolist() if c in self.parent.df.columns else None
                                     for c in self.parent.chart_tool.y_err_cols]
            else:
                y_err_series_list = [self.parent.df[c].values.tolist() if c in self.parent.df.columns else None
                                     for c in self.parent.chart_tool.y_err_cols]

            if self.parent.chart_tool.selected_bar == "grouped":
                for i, col in enumerate(cols):
                    y_series = self.parent.df[col].values
                    rect = self.canvas.axs.barh(rou[i], y_series, height=self.parent.chart_tool.width,
                                               color=colors[i], label=data_labels[i], xerr=y_err_series_list[i],
                                               ecolor=self.parent.chart_tool.err_bar_color, align="center")
                    if isinstance(x_series[0], str):
                        self.canvas.axs.set_yticks(rou[i]-(col_num-1)*self.parent.chart_tool.width/2, x_series)
                    if self.parent.chart_tool.bar_value_label_checked:
                        if len(self.parent.chart_tool.bar_value_label_series) < col_num:
                            self.parent.chart_tool.bar_value_label_series.extend(
                                (col_num-len(self.parent.chart_tool.bar_value_label_series))*[None]
                            )
                        self.canvas.axs.bar_label(rect, labels=self.parent.chart_tool.bar_value_label_series[i],
                                                  padding=self.parent.chart_tool.bar_value_label_interval,
                                                  color=self.parent.chart_tool.bar_value_label_color,
                                                  fontsize=self.parent.chart_tool.bar_value_label_size)
            elif self.parent.chart_tool.selected_bar == "stacked":
                left = np.zeros(self.parent.df.shape[0])
                for i, col in enumerate(cols):
                    y_series = self.parent.df[col].values
                    rect = self.canvas.axs.barh(x_series, y_series, height=self.parent.chart_tool.width,
                                                color=colors[i], label=data_labels[i], xerr=y_err_series_list[i],
                                                ecolor=self.parent.chart_tool.err_bar_color, left=left)
                    left += y_series
                    if self.parent.chart_tool.bar_value_label_checked:
                        if len(self.parent.chart_tool.bar_value_label_series) < col_num:
                            self.parent.chart_tool.bar_value_label_series.extend(
                                (col_num-len(self.parent.chart_tool.bar_value_label_series))*[None]
                            )
                        self.canvas.axs.bar_label(rect, label_type="center",
                                                  labels=self.parent.chart_tool.bar_value_label_series[i],
                                                  padding=self.parent.chart_tool.bar_value_label_interval,
                                                  color=self.parent.chart_tool.bar_value_label_color,
                                                  fontsize=self.parent.chart_tool.bar_value_label_size)
            else:
                values = self.parent.df[cols].values
                values_sum = values.sum(axis=1)
                value_props = np.around(values / values_sum.reshape(-1, 1) * 100, 2)
                left = np.zeros(self.parent.df.shape[0])
                for i, col in enumerate(cols):
                    rect = self.canvas.axs.barh(x_series, value_props[:, i], height=self.parent.chart_tool.width,
                                               color=colors[i], label=data_labels[i], xerr=y_err_series_list[i],
                                               ecolor=self.parent.chart_tool.err_bar_color, left=left)
                    left += value_props[:, i]
                    if self.parent.chart_tool.bar_value_label_checked:
                        if len(self.parent.chart_tool.bar_value_label_series) < col_num:
                            self.parent.chart_tool.bar_value_label_series.extend(
                                (col_num-len(self.parent.chart_tool.bar_value_label_series))*[None]
                            )
                        self.canvas.axs.bar_label(rect, label_type="center",
                                                  labels=self.parent.chart_tool.bar_value_label_series[i],
                                                  padding=self.parent.chart_tool.bar_value_label_interval,
                                                  color=self.parent.chart_tool.bar_value_label_color,
                                                  fontsize=self.parent.chart_tool.bar_value_label_size)

