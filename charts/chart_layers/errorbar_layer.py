from charts.chart_layers.base_chart_layer import BaseChartLayer


class ErrorbarLayer(BaseChartLayer):
    def __init__(self, parent):
        super(ErrorbarLayer, self).__init__()
        self.parent = parent
        
    def chart_layer_plot(self, layer_pos, canvas):
        if not self.parent.df.empty:
            x_col = self.parent.chart_tool.x_series_combo.currentText()
            x_series = self.parent.df[x_col]

            y_col = self.parent._tool_instances[layer_pos].y_series_combo.currentText()
            data_label_line = self.parent._tool_instances[layer_pos].data_label_line.text().strip()
            if not y_col.strip():
                return canvas.axs.plot()

            cols = y_col.split(",")
            data_labels = data_label_line.split(",")
            if len(data_labels) < len(cols):
                data_labels.extend([None] * (len(cols) - len(data_labels)))
            color_series = (self.parent._tool_instances[layer_pos].color_series_line.text().strip().split(",")
                             if self.parent._tool_instances[layer_pos].color_series_line.text() else [])
            if len(color_series) < len(cols):
                color_series.extend(["C{}".format(i) for i in range((len(cols) - len(color_series)))])

            _x_err_series_col = self.parent._tool_instances[layer_pos].x_err_series
            _y_err_series_col = self.parent._tool_instances[layer_pos].y_err_series

            x_err_series = None
            y_err_series = None
            if _x_err_series_col != "none":
                x_err_series = self.parent.df[_x_err_series_col]
            if _y_err_series_col != "none":
                y_err_series = self.parent.df[_y_err_series_col]

            err_line_width = self.parent._tool_instances[layer_pos].err_line_width
            cap_size = self.parent._tool_instances[layer_pos].cap_size
            err_every = self.parent._tool_instances[layer_pos].err_every

            marker = self.parent._tool_instances[layer_pos].marker
            marker_size = self.parent._tool_instances[layer_pos].marker_size
            marker_edge_width = self.parent._tool_instances[layer_pos].marker_edge_width
            marker_edge_color = self.parent._tool_instances[layer_pos].marker_edge_color
            marker_face_color = self.parent._tool_instances[layer_pos].marker_face_color
            line_style = self.parent._tool_instances[layer_pos].line_style
            line_colors = (self.parent._tool_instances[layer_pos].line_color_line.text().strip().split(",")
                           if self.parent._tool_instances[layer_pos].line_color_line.text() else [])
            if len(line_colors) < len(cols):
                line_colors.extend(["C{}".format(i) for i in range((len(cols) - len(line_colors)))])

            bar_above_checked = self.parent._tool_instances[layer_pos].bars_above_checked
            lower_limits_checked = self.parent._tool_instances[layer_pos].lower_limits_checked
            upper_limits_checked = self.parent._tool_instances[layer_pos].upper_limits_checked
            xlower_limits_checked = self.parent._tool_instances[layer_pos].xlower_limits_checked
            xupper_limits_checked = self.parent._tool_instances[layer_pos].xupper_limits_checked


            for i, col in enumerate(cols):
                y_series = self.parent.df[col]

                canvas.axs.errorbar(
                    x_series,
                    y_series,
                    xerr=x_err_series,
                    yerr=y_err_series,
                    ecolor=color_series[i],
                    elinewidth=err_line_width,
                    capsize=cap_size,
                    errorevery=err_every,
                    fmt=marker,
                    markersize=marker_size,
                    markerfacecolor=marker_face_color,
                    markeredgecolor=marker_edge_color,
                    markeredgewidth=marker_edge_width,
                    linestyle=line_style,
                    color=line_colors[i],
                    label=data_labels[i],
                    barsabove=bar_above_checked,
                    lolims=lower_limits_checked,
                    uplims=upper_limits_checked,
                    xlolims=xlower_limits_checked,
                    xuplims=xupper_limits_checked,
                )
