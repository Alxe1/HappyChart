from charts.chart_layers.base_chart_layer import BaseChartLayer


class FillBetweenLayer(BaseChartLayer):
    def __init__(self, parent=None):
        super(FillBetweenLayer, self).__init__()
        self.parent = parent

    def chart_layer_plot(self, layer_pos, canvas):
        if not self.parent.df.empty:
            x_col = self.parent.chart_tool.x_series_combo.currentText().strip()
            y_col1 = self.parent._tool_instances[layer_pos].y1_series_combo.currentText().strip()
            y_col2 = self.parent._tool_instances[layer_pos].y2_series_combo.currentText().strip()
            if not y_col1.strip():
                return canvas.axs.plot()

            where_first = self.parent._tool_instances[layer_pos].where_first_combo.currentText().strip()
            where_second = self.parent._tool_instances[layer_pos].where_second_combo.currentText().strip()

            data_label = self.parent._tool_instances[layer_pos].data_label_line.text().strip()

            where_eq = self.parent._tool_instances[layer_pos].where_eq

            x_series = self.parent.df[x_col].values

            try:
                y1_series = float(y_col1)
            except:
                y1_series = self.parent.df[y_col1].values
            try:
                if not y_col2:
                    y2_series = 0
                else:
                    y2_series = float(y_col2)
            except:
                y2_series = self.parent.df[y_col2].values
            try:
                if not where_first:
                    where_first_series = None
                else:
                    where_first_series = float(where_first)
            except:
                where_first_series = self.parent.df[where_first].values
            try:
                if not where_second:
                    where_second_series = None
                else:
                    where_second_series = float(where_second)
            except:
                where_second_series = self.parent.df[where_second].values

            if where_first_series is None or where_second_series is None:
                where = None
            else:
                if where_eq == "==":
                    where = where_first_series == where_second_series
                elif where_eq == ">=":
                    where = where_first_series >= where_second_series
                elif where_eq == "<=":
                    where = where_first_series <= where_second_series
                elif where_eq == ">":
                    where = where_first_series > where_second_series
                elif where_eq == "<":
                    where = where_first_series < where_second_series
                else:
                    where = None

            face_color = self.parent._tool_instances[layer_pos].face_color
            edge_color = self.parent._tool_instances[layer_pos].edge_color
            interpolate = self.parent._tool_instances[layer_pos].interpolate_checked
            step = self.parent._tool_instances[layer_pos].step
            transparency = self.parent._tool_instances[layer_pos].transparency

            canvas.axs.fill_between(
                x_series,
                y1_series,
                y2=y2_series,
                where=where,
                step=step,
                interpolate=interpolate,
                facecolor=face_color,
                edgecolor=edge_color,
                alpha=transparency,
                label=data_label
            )
