from charts.chart_layers.base_chart_layer import BaseChartLayer


class StairsLayer(BaseChartLayer):
    def __init__(self, parent):
        super(StairsLayer, self).__init__()
        self.parent = parent
        
    def chart_layer_plot(self, layer_pos, canvas):
        if not self.parent.df.empty:
            y_col = self.parent._tool_instances[layer_pos].y_series_combo.currentText()
            data_label_line = self.parent._tool_instances[layer_pos].data_label_line.text().strip()
            if not y_col.strip():
                return canvas.axs.plot()

            cols = y_col.split(",")
            data_labels = data_label_line.split(",")
            if len(data_labels) < len(cols):
                data_labels.extend([None] * (len(cols) - len(data_labels)))

            orientation = self.parent._tool_instances[layer_pos].orientation
            base_line = self.parent._tool_instances[layer_pos].base_line
            line_width = self.parent._tool_instances[layer_pos].line_width
            line_style = self.parent._tool_instances[layer_pos].line_style

            fill_color_checked = self.parent._tool_instances[layer_pos].fill_color_checked

            edge_color_series = (self.parent._tool_instances[layer_pos].edge_color_series_line.text().strip().split(",")
                                 if self.parent._tool_instances[layer_pos].edge_color_series_line.text().strip() else [])
            if len(edge_color_series) < len(cols):
                edge_color_series.extend(["C{}".format(i) for i in range((len(cols) - len(edge_color_series)))])
            face_color_series = (self.parent._tool_instances[layer_pos].face_color_series_line.text().strip().split(",")
                                 if self.parent._tool_instances[layer_pos].face_color_series_line.text().strip() else [])
            if len(face_color_series) < len(cols):
                face_color_series.extend(["C{}".format(i) for i in range((len(cols) - len(face_color_series)))])

            transparency = self.parent._tool_instances[layer_pos].transparency

            hatch_series = (self.parent._tool_instances[layer_pos].hatch_series.strip().split(",")
                            if self.parent._tool_instances[layer_pos].hatch_series.strip() else [])
            if len(hatch_series) != 0 and len(hatch_series) < len(cols):
                hatch_series.extend([""] * (len(cols) - len(hatch_series)))

            for i, col in enumerate(cols):
                y_series = self.parent.df[col].values
                if len(hatch_series) != 0:
                    canvas.axs.stairs(
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
                    canvas.axs.stairs(
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

    