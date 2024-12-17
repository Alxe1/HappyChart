from charts.chart_layers.base_chart_layer import BaseChartLayer


class AnnotationLayer(BaseChartLayer):

    def __init__(self, parent):
        super(AnnotationLayer, self).__init__()
        self.parent = parent

    def chart_layer_plot(self, layer_pos, canvas):
        x_pos = self.parent._tool_instances[layer_pos].x_pos
        y_pos = self.parent._tool_instances[layer_pos].y_pos
        x_text_pos = self.parent._tool_instances[layer_pos].x_text_pos
        y_text_pos = self.parent._tool_instances[layer_pos].y_text_pos
        text = self.parent._tool_instances[layer_pos].text
        text_color = self.parent._tool_instances[layer_pos].text_color
        font_size = self.parent._tool_instances[layer_pos].font_size
        background_color = self.parent._tool_instances[layer_pos].background_color
        rotation = self.parent._tool_instances[layer_pos].rotation
        annotation_clip = self.parent._tool_instances[layer_pos].annotation_clip_checked
        arrow_style = self.parent._tool_instances[layer_pos].arrow_style
        connection_style = self.parent._tool_instances[layer_pos].connection_style
        shrink_a = self.parent._tool_instances[layer_pos].shrink_a
        shrink_b = self.parent._tool_instances[layer_pos].shrink_b
        arrow_color = self.parent._tool_instances[layer_pos].arrow_color
        transparency = self.parent._tool_instances[layer_pos].transparency

        canvas.axs.annotate(
            text,
            xy=(x_pos, y_pos),
            xytext=(x_text_pos, y_text_pos),
            annotation_clip=annotation_clip,
            backgroundcolor=background_color,
            color=text_color,
            fontsize=font_size,
            rotation=rotation,
            alpha=transparency,
            arrowprops=dict(
                arrowstyle=arrow_style,
                connectionstyle=connection_style,
                shrinkA=shrink_a,
                shrinkB=shrink_b,
                color=arrow_color
            )
        )
