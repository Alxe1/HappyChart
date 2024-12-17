import numpy as np
from matplotlib.axes import Axes
from matplotlib.patches import ConnectionPatch

from charts.base.base_chart import BaseChart, MplCanvas


class PieChartWithBar(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(PieChartWithBar, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

    def update_plot(self):
        self.canvas = None
        self.get_canvas()
        self.base_layer()

        self.parent.chartScrollArea.setWidget(self.canvas)
        self.canvas.draw()

    def get_canvas(self, nrows=1, ncols=2):
        self.canvas = MplCanvas(self, nrows=nrows, ncols=ncols, width=self.canvas_width, height=self.canvas_height,
                                dpi=self.dpi)

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

            _bar_data_series = self.parent.chart_tool.bar_data_series
            bar_data_series = []
            if len(_bar_data_series) != 0:
                if sum(_bar_data_series) == 1:
                    bar_data_series = _bar_data_series
                else:
                    bar_data_series = [i / sum(_bar_data_series) for i in _bar_data_series]

            bar_label_series = (self.parent.chart_tool.bar_label_series.strip().split(",")
                                if self.parent.chart_tool.bar_label_series.strip() else [])
            if len(bar_label_series) < len(bar_data_series):
                bar_label_series.extend((len(bar_data_series) - len(bar_label_series)) * [None])

            bar_color = self.parent.chart_tool.bar_color
            bar_title = self.parent.chart_tool.bar_title
            tied_line_width = self.parent.chart_tool.tied_line_width
            tied_line_style = self.parent.chart_tool.tied_line_style
            tied_line_color = self.parent.chart_tool.tied_line_color
            bind_wedge_index = self.parent.chart_tool.bind_wedge_index
            bar_legend_pos = self.parent.chart_tool.bar_legend_pos
            _pct = (0 if self.parent.chart_tool.pct_combo.currentText() == "none"
                    else int(self.parent.chart_tool.pct_combo.currentText()))

            self.canvas.fig.subplots_adjust(wspace=0)
            wedges, *_ = self.canvas.axs[0].pie(
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

            bottom = 1
            width = .2

            for j, (height, label) in enumerate([*zip(bar_data_series, bar_label_series)]):
                bottom -= height
                bc = self.canvas.axs[1].bar(0, height, width, bottom=bottom, color=bar_color, label=label,
                                            alpha=0.25 + 0.15 * j)
                self.canvas.axs[1].bar_label(bc, labels=[f"{height:.{_pct}%}"], label_type='center')

            self.canvas.axs[1].set_title(bar_title)
            self.canvas.axs[1].legend(loc=bar_legend_pos)
            self.canvas.axs[1].axis('off')
            self.canvas.axs[1].set_xlim(- 2.5 * width, 2.5 * width)

            if bind_wedge_index > len(wedges) - 1:
                bind_wedge_index = len(wedges) - 1

            theta1, theta2 = wedges[bind_wedge_index].theta1, wedges[bind_wedge_index].theta2
            center, r = wedges[0].center, wedges[0].r
            bar_height = sum(bar_data_series)

            x = r * np.cos(np.pi / 180 * theta2) + center[0]
            y = r * np.sin(np.pi / 180 * theta2) + center[1]
            con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=self.canvas.axs[1].transData,
                                  xyB=(x, y), coordsB=self.canvas.axs[0].transData)
            con.set_linewidth(tied_line_width)
            con.set_linestyle(tied_line_style)
            con.set_color(tied_line_color)
            self.canvas.axs[1].add_artist(con)

            x = r * np.cos(np.pi / 180 * theta1) + center[0]
            y = r * np.sin(np.pi / 180 * theta1) + center[1]
            con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=self.canvas.axs[1].transData,
                                  xyB=(x, y), coordsB=self.canvas.axs[0].transData)

            con.set_linewidth(tied_line_width)
            con.set_linestyle(tied_line_style)
            con.set_color(tied_line_color)
            self.canvas.axs[1].add_artist(con)
