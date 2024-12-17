from PIL import Image
import numpy as np

from wordcloud import WordCloud

from charts.base.base_chart import BaseChart

class WordcloudChart(BaseChart):
    def __init__(self, parent=None, *args, **kwargs):
        super(WordcloudChart, self).__init__(parent=parent, *args, **kwargs)
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
            x_col = self.parent.chart_tool.x_series_combo.currentText()
            y_col = self.parent.chart_tool.y_series_combo.currentText()
            if not y_col.strip():
                return self.canvas.axs.plot()

            x_series = self.parent.df[x_col].values
            y_series = self.parent.df[y_col].values

            _dict = dict()
            for (i, j) in zip(x_series, y_series):
                _dict[str(i)] = j

            width = self.parent.chart_tool.width
            height = self.parent.chart_tool.height
            scale = self.parent.chart_tool.scale
            background_color = self.parent.chart_tool.background_color
            max_font_size = self.parent.chart_tool.max_font_size
            color_map = self.parent.chart_tool.color_map

            mask_image_path = self.parent.chart_tool.mask_image_line.text()
            image_mask = None
            if mask_image_path:
                image_mask = np.array(Image.open(mask_image_path))

            if image_mask is not None:
                wc = WordCloud(
                    width=width,
                    height=height,
                    scale=scale,
                    background_color=background_color,
                    max_font_size=max_font_size,
                    colormap=color_map,
                    mask=image_mask
                ).fit_words(_dict)
            else:
                wc = WordCloud(
                    width=width,
                    height=height,
                    scale=scale,
                    background_color=background_color,
                    max_font_size=max_font_size,
                    colormap=color_map
                ).fit_words(_dict)

            self.canvas.axs.imshow(wc)
