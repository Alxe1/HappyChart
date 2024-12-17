from charts.chart_layers.base_chart_layer import BaseChartLayer


class SpanLayer(BaseChartLayer):
    def __init__(self, parent):
        super(SpanLayer, self).__init__()
        self.parent = parent

    def chart_layer_plot(self, layer_pos, canvas):

        span_type = self.parent._tool_instances[layer_pos].span_type

        min_value = self.parent._tool_instances[layer_pos].min_value
        max_value = self.parent._tool_instances[layer_pos].max_value

        data_label = self.parent._tool_instances[layer_pos].data_label
        fill_color_checked = self.parent._tool_instances[layer_pos].fill_color_checked
        face_color = self.parent._tool_instances[layer_pos].face_color
        edge_color = self.parent._tool_instances[layer_pos].edge_color
        line_style = self.parent._tool_instances[layer_pos].line_style
        line_width = self.parent._tool_instances[layer_pos].line_width
        transparency = self.parent._tool_instances[layer_pos].transparency

        if span_type == "horizontal":
            canvas.axs.axhspan(
                min_value,
                max_value,
                label=data_label,
                fill=fill_color_checked,
                facecolor=face_color,
                edgecolor=edge_color,
                linewidth=line_width,
                linestyle=line_style,
                alpha=transparency
            )
        else:
            canvas.axs.axvspan(
                min_value,
                max_value,
                label=data_label,
                fill=fill_color_checked,
                facecolor=face_color,
                edgecolor=edge_color,
                linewidth=line_width,
                linestyle=line_style,
                alpha=transparency
            )
