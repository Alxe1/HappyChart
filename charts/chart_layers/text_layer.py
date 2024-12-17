from charts.chart_layers.base_chart_layer import BaseChartLayer


class TextLayer(BaseChartLayer):
    def __init__(self, parent):
        super(TextLayer, self).__init__()
        self.parent = parent

    def chart_layer_plot(self, layer_pos, canvas):
        x_pos = self.parent._tool_instances[layer_pos].x_pos
        y_pos = self.parent._tool_instances[layer_pos].y_pos
        text = self.parent._tool_instances[layer_pos].text
        font_size = self.parent._tool_instances[layer_pos].font_size
        font_color = self.parent._tool_instances[layer_pos].font_color
        background_color = self.parent._tool_instances[layer_pos].background_color
        horizontal_align = self.parent._tool_instances[layer_pos].horizontal_align
        vertical_align = self.parent._tool_instances[layer_pos].vertical_align
        multi_align = self.parent._tool_instances[layer_pos].multi_align
        rotation = self.parent._tool_instances[layer_pos].rotation
        transparency = self.parent._tool_instances[layer_pos].transparency

        canvas.axs.text(
            x_pos,
            y_pos,
            text,
            fontsize=font_size,
            color=font_color,
            backgroundcolor=background_color,
            horizontalalignment=horizontal_align,
            verticalalignment=vertical_align,
            multialignment=multi_align,
            rotation=rotation,
            alpha=transparency
        )
