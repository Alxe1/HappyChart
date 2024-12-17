from charts.chart_layers.base_chart_layer import BaseChartLayer


class VHLineLayer(BaseChartLayer):
    def __init__(self, parent):
        super(VHLineLayer, self).__init__()
        self.parent = parent

    def chart_layer_plot(self, layer_pos, canvas):

        line_type = self.parent._tool_instances[layer_pos].line_type
        data_label = self.parent._tool_instances[layer_pos].data_label
        position = self.parent._tool_instances[layer_pos].position
        min_value = self.parent._tool_instances[layer_pos].min_value
        max_value = self.parent._tool_instances[layer_pos].max_value
        color = self.parent._tool_instances[layer_pos].color
        line_style = self.parent._tool_instances[layer_pos].line_style
        line_width = self.parent._tool_instances[layer_pos].line_width
        transparency = self.parent._tool_instances[layer_pos].transparency

        if line_type == "horizontal":
            canvas.axs.hlines(
                position,
                min_value,
                max_value,
                color=color,
                linestyle=line_style,
                linewidth=line_width,
                alpha=transparency,
                label=data_label
            )
        else:
            canvas.axs.vlines(
                position,
                min_value,
                max_value,
                color=color,
                linestyle=line_style,
                linewidth=line_width,
                alpha=transparency,
                label=data_label
            )
