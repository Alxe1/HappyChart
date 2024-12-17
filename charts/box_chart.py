from charts.base.base_chart import BaseChart


class BoxChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(BoxChart, self).__init__(parent, *args, **kwargs)
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
            color_series = (self.parent.chart_tool.color_series_line.text().strip().split(",")
                             if self.parent.chart_tool.color_series_line.text() else [])
            if len(color_series) < len(cols):
                color_series.extend([None] * (len(cols) - len(color_series)))
            y_series = self.parent.df[cols].values

            notch = self.parent.chart_tool.notch_checked
            vert = self.parent.chart_tool.vert_checked
            box_width = self.parent.chart_tool.box_width
            patch_artist = self.parent.chart_tool.patch_artist_checked

            show_box = self.parent.chart_tool.show_box_checked
            box_line_style = self.parent.chart_tool.box_linestyle
            box_line_width = self.parent.chart_tool.box_linewidth
            bbox_color = self.parent.chart_tool.bbox_color
            boxprops = dict(color=bbox_color, linewidth=box_line_width, linestyle=box_line_style)

            median_line_style = self.parent.chart_tool.median_linestyle
            median_line_width = self.parent.chart_tool.median_linewidth
            median_line_color = self.parent.chart_tool.median_line_color
            medianprops = dict(color=median_line_color, linewidth=median_line_width, linestyle=median_line_style)

            show_means = self.parent.chart_tool.show_means_checked
            mean_marker = self.parent.chart_tool.mean_marker
            mean_edge_color = self.parent.chart_tool.mean_edge_color
            mean_face_color = self.parent.chart_tool.mean_face_color

            show_mean_line = self.parent.chart_tool.show_mean_line_checked
            mean_line_style = self.parent.chart_tool.mean_linestyle
            mean_line_width = self.parent.chart_tool.mean_linewidth
            mean_line_color = self.parent.chart_tool.mean_line_color
            meanprops = dict(marker=mean_marker, markeredgecolor=mean_edge_color, markerfacecolor=mean_face_color,
                             linestyle=mean_line_style, linewidth=mean_line_width, color=mean_line_color)

            show_caps = self.parent.chart_tool.show_caps_checked
            cap_line_style = self.parent.chart_tool.cap_linestyle
            cap_line_width = self.parent.chart_tool.cap_linewidth
            cap_color = self.parent.chart_tool.cap_color
            cap_width = self.parent.chart_tool.cap_width
            capprops = dict(color=cap_color, linewidth=cap_line_width, linestyle=cap_line_style)

            show_outlier = self.parent.chart_tool.show_outlier_checked
            outlier_marker = self.parent.chart_tool.outlier_marker
            outlier_marker_size = self.parent.chart_tool.outlier_marker_size
            outlier_face_color = self.parent.chart_tool.outlier_face_color
            outlier_edge_color = self.parent.chart_tool.outlier_edge_color
            outlierprops = dict(marker=outlier_marker, markersize=outlier_marker_size,
                                markerfacecolor=outlier_face_color, markeredgecolor=outlier_edge_color)

            bplot = self.canvas.axs.boxplot(y_series, notch=notch, vert=vert, patch_artist=patch_artist,
                                            showbox=show_box, boxprops=boxprops, medianprops=medianprops,
                                            showmeans=show_means, meanline=show_mean_line, meanprops=meanprops,
                                            showcaps=show_caps, capprops=capprops, capwidths=cap_width,
                                            showfliers=show_outlier, flierprops=outlierprops, widths=box_width,
                                            tick_labels=data_labels)
            if patch_artist:
                for patch, color in zip(bplot['boxes'], color_series):
                    patch.set_facecolor(color)


