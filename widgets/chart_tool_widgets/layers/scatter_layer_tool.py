from PySide6.QtGui import Qt
from PySide6.QtWidgets import QFrame

from widgets.ui_widgets.layers.ui_scatter_layer_tool import Ui_Form


class ScatterLayerToolFrame(QFrame, Ui_Form):
    _id = None

    def __init__(self, parent=None, *args, **kwargs):
        super(ScatterLayerToolFrame, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.setupUi(self)

        self.parent.chart_tool.x_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.y_series_combo.currentTextChanged.connect(lambda _: self.parent.chart.update_plot())
        self.data_label_line.textChanged.connect(lambda _: self.parent.chart.update_plot())

        if not self.parent.df.empty:
            cols = self.parent.df.columns.tolist()
            self.y_series_combo.clear()
            self.y_series_combo.addCheckableItems(cols)
            self.y_series_combo.setCurrentIndex(-1)

        # 散点大小
        if not self.parent.df.empty:
            self.scatter_size_combo.addSelectableItems(self.parent.df.columns.tolist())
        self.scatter_size_combo.setCurrentIndex(-1)
        self.scatter_size = self.scatter_size_combo.currentText()
        self.scatter_size_combo.currentTextChanged.connect(self.scatter_size_changed)
        # 散点大小基准
        self.scatter_size_base = self.scatter_size_base_spin.value()
        self.scatter_size_base_spin.valueChanged.connect(self.scatter_size_base_changed)
        # 散点标识
        self.scatter_marker = self.scatter_marker_type_combo.currentText()
        self.scatter_marker_type_combo.currentTextChanged.connect(self.scatter_marker_changed)
        # 散点颜色
        if not self.parent.df.empty:
            self.scatter_color_combo.addSelectableItems(self.parent.df.columns.tolist())
        self.scatter_color_combo.setCurrentIndex(-1)
        self.scatter_color = self.scatter_color_combo.currentText()
        self.scatter_color_combo.currentTextChanged.connect(self.scatter_color_changed)
        # 边缘颜色
        self.scatter_edge_color = self.scatter_edge_color_combo.currentText()
        self.scatter_edge_color_combo.currentTextChanged.connect(self.scatter_edge_color_changed)
        # 线宽
        self.scatter_line_width = self.scatter_linewidth_spin.value()
        self.scatter_linewidth_spin.valueChanged.connect(self.scatter_line_width_changed)
        # 透明度
        self.scatter_transparent = self.scatter_transparent_slider.value() / 100
        self.scatter_transparent_slider.valueChanged.connect(self.scatter_transparent_slider_changed)
        # 添加色条
        self.add_colorbar_checked = self.scatter_colorbar_check.isChecked()
        self.scatter_colorbar_check.stateChanged.connect(self.is_add_colorbar_checked)

        self.toolButton.clicked.connect(self.tool_button_clicked)

    def tool_button_clicked(self):
        widget = self.parent._tool_instances.pop(self._id)
        self.parent._tool_instances.insert(self._id, None)
        self.parent._chart_instances.pop(self._id)
        self.parent._chart_instances.insert(self._id, None)
        self.parent.chart.update_plot()
        widget.deleteLater()

    def scatter_size_changed(self, e):
        self.scatter_size = e
        self.parent.chart.update_plot()

    def scatter_size_base_changed(self, e):
        self.scatter_size_base = e
        self.parent.chart.update_plot()

    def scatter_marker_changed(self, e):
        self.scatter_marker = e
        self.parent.chart.update_plot()

    def scatter_color_changed(self, e):
        self.scatter_color = e
        self.parent.chart.update_plot()

    def scatter_edge_color_changed(self, e):
        self.scatter_edge_color = e
        self.parent.chart.update_plot()

    def scatter_line_width_changed(self, e):
        self.scatter_line_width = e
        self.parent.chart.update_plot()

    def scatter_transparent_slider_changed(self, e):
        self.scatter_transparent = e / 100
        self.parent.chart.update_plot()

    def is_add_colorbar_checked(self, e):
        self.add_colorbar_checked = self.scatter_colorbar_check.isChecked()
        self.parent.chart.update_plot()
