from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout

from charts.base.base_chart import BaseChart


class StairsChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(StairsChart, self).__init__(parent=parent, *args, **kwargs)
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

            orientation = self.parent.chart_tool.orientation
            base_line = self.parent.chart_tool.base_line
            line_width = self.parent.chart_tool.line_width
            line_style = self.parent.chart_tool.line_style

            fill_color_checked = self.parent.chart_tool.fill_color_checked

            edge_color_series = (self.parent.chart_tool.edge_color_series_line.text().strip().split(",")
                                 if self.parent.chart_tool.edge_color_series_line.text().strip() else [])
            if len(edge_color_series) < len(cols):
                edge_color_series.extend(["C{}".format(i) for i in range((len(cols) - len(edge_color_series)))])
            face_color_series = (self.parent.chart_tool.face_color_series_line.text().strip().split(",")
                                if self.parent.chart_tool.face_color_series_line.text().strip() else [])
            if len(face_color_series) < len(cols):
                face_color_series.extend(["C{}".format(i) for i in range((len(cols) - len(face_color_series)))])

            transparency = self.parent.chart_tool.transparency

            hatch_series = (self.parent.chart_tool.hatch_series.strip().split(",")
                            if self.parent.chart_tool.hatch_series.strip() else [])
            if len(hatch_series) != 0 and len(hatch_series) < len(cols):
                hatch_series.extend([""] * (len(cols) - len(hatch_series)))

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                if len(hatch_series) != 0:
                    self.canvas.axs.stairs(
                        y_series,
                        orientation=orientation,
                        baseline=base_line,
                        linewidth=line_width,
                        linestyle=line_style,
                        fill=fill_color_checked,
                        alpha=transparency,
                        edgecolor=edge_color_series[i],
                        facecolor=face_color_series[i],
                        hatch=hatch_series[i],
                        label=data_labels[i]
                    )
                else:
                    self.canvas.axs.stairs(
                        y_series,
                        orientation=orientation,
                        baseline=base_line,
                        linewidth=line_width,
                        linestyle=line_style,
                        fill=fill_color_checked,
                        alpha=transparency,
                        edgecolor=edge_color_series[i],
                        facecolor=face_color_series[i],
                        label=data_labels[i]
                    )
