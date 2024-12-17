import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QColorDialog

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties


dir_path = os.path.dirname(os.path.abspath(__file__))

if getattr(sys, "frozen", False):
    simsun_bold_font = FontProperties(fname=os.path.join(dir_path, "..", "..", "fonts", "simsun-bold.ttf"))
    font_manager.fontManager.addfont(os.path.join(dir_path, "..", "..", "fonts", "out_0.ttf"))
else:
    simsun_bold_font = FontProperties(fname=os.path.join(dir_path, "..", "..", "resources", "fonts", "simsun-bold.ttf"))
    font_manager.fontManager.addfont(os.path.join(dir_path, "..", "..", "resources", "fonts", "out_0.ttf"))


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent, nrows, ncols, width, height, width_ratios=None, height_ratios=None, dpi=100):
        self.parent = parent
        # matplotlib.rcParams['font.sans-serif'] = ['SimSun']
        matplotlib.rcParams['font.family'] = "Times New Roman + SimSun + WFM Sans SC"
        matplotlib.rcParams['axes.unicode_minus'] = False

        self.fig, self.axs = plt.subplots(nrows, ncols, figsize=(width, height), width_ratios=width_ratios,
                                          height_ratios=height_ratios, dpi=dpi)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        super(MplCanvas, self).__init__(self.fig)


class BaseChart(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(BaseChart, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent

        self.get_canvas_settings()

        # 获取X轴标签和刻度
        self.get_x_label_and_ticks()
        # 获取Y轴标签和刻度
        self.get_y_label_and_ticks()
        # 标题设置
        self.get_title()
        # 图例设置
        self.get_legend()
        # 其他设置
        self.get_other_settings()

    def update_plot(self):
        plt.close("all")

        self.get_canvas()
        self.set_canvas_settings()

    def get_canvas(self, nrows=1, ncols=1):
        self.canvas = MplCanvas(self, nrows=nrows, ncols=ncols, width=self.canvas_width, height=self.canvas_height,
                                dpi=self.dpi)

    def get_canvas_settings(self):
        self.canvas_width = self.parent.canvas_width_spin.value()
        self.parent.canvas_width_spin.valueChanged.connect(self.canvas_width_changed)
        self.canvas_height = self.parent.canvas_height_spin.value()
        self.parent.canvas_height_spin.valueChanged.connect(self.canvas_height_changed)
        self.dpi = self.parent.dpi_spin.value()
        self.parent.dpi_spin.valueChanged.connect(self.dpi_changed)
        # 画布颜色
        self.canvas_bg_color = "#ffffff"
        self.parent.canvas_bg_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.canvas_bg_color)
        self.parent.canvas_bg_color_btn.clicked.connect(self.canvas_bg_color_btn_clicked)

        # 图表颜色
        self.chart_bg_color = "#ffffff"
        self.parent.chart_bg_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.chart_bg_color)
        self.parent.chart_bg_color_btn.clicked.connect(self.chart_bg_color_btn_clicked)

        # 网格透明度
        self.grid_transparent_value = self.parent.grid_transparent_slider.value() / 100
        self.parent.grid_transparent_slider.setEnabled(False)
        self.parent.grid_transparent_slider.valueChanged.connect(self.grid_transparent_slider_changed)
        self.canvas_grid_check_value = False
        self.parent.canvas_grid_check_box.checkStateChanged.connect(self.canvas_grid_check)
        self.show_xy_grid_value = self.parent.show_xy_grid_slider.value()
        self.parent.show_xy_grid_slider.valueChanged.connect(self.show_xy_grid_slider_changed)

        self.grid_color = "#cecece"
        self.parent.grid_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.grid_color)
        self.parent.grid_color_btn.clicked.connect(self.grid_color_btn_clicked)

        self.grid_line_width = self.parent.grid_line_width_spin.value()
        self.parent.grid_line_width_spin.valueChanged.connect(self.grid_line_width_changed)

        self.grid_line_style = self.parent.grid_line_style_combo.currentText()
        self.parent.grid_line_style_combo.currentTextChanged.connect(self.grid_line_style_changed)

    def set_canvas_settings(self):
        self.canvas.fig.set_facecolor(self.canvas_bg_color)
        self.canvas.axs.set_facecolor(self.chart_bg_color)
        if self.canvas_grid_check_value:
            if self.show_xy_grid_value == -1:
                self.canvas.axs.yaxis.grid(True, alpha=self.grid_transparent_value, color=self.grid_color,
                                           linewidth=self.grid_line_width, linestyle=self.grid_line_style)
            elif self.show_xy_grid_value == 1:
                self.canvas.axs.xaxis.grid(True, alpha=self.grid_transparent_value, color=self.grid_color,
                                           linewidth=self.grid_line_width, linestyle=self.grid_line_style)
            else:
                self.canvas.axs.grid(True, alpha=self.grid_transparent_value, color=self.grid_color,
                                     linewidth=self.grid_line_width, linestyle=self.grid_line_style)
            self.canvas.axs.set_axisbelow(True)
        else:
            self.canvas.axs.grid(False)

    def get_x_label_and_ticks(self):
        # 是否启用X轴
        self.bs_x_checked = self.parent.bs_x_enable_check.isChecked()
        self.parent.bs_x_enable_check.checkStateChanged.connect(self.bs_x_enable_check_changed)
        # 标签名称
        self.bs_x_title = self.parent.bs_x_title_line_edit.text()
        self.parent.bs_x_title_line_edit.textChanged.connect(self.bs_x_title_changed)
        # # 字体
        # self.x_label_font = self.parent.bs_x_font_combo.currentText()
        # self.parent.bs_x_font_combo.currentTextChanged.connect(self.x_label_font_changed)
        # self.parent.bs_x_font_combo.currentFontChanged.connect(self.x_label_font_changed1)
        # 字号
        self.bs_x_label_size = self.parent.bs_x_label_size_spin.value()
        self.parent.bs_x_label_size_spin.valueChanged.connect(self.bs_x_label_size_changed)
        # 标签颜色
        self.bs_x_label_color = "#000000"
        self.parent.bs_x_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bs_x_label_color)
        self.parent.bs_x_label_color_btn.clicked.connect(self.bs_x_label_color_btn_clicked)
        # 加粗
        self.x_label_bold = self.parent.bs_x_bold_check.isChecked()
        self.parent.bs_x_bold_check.stateChanged.connect(self.x_label_bold_changed)
        # 刻度
        self.x_tick_direction = self.parent.bs_x_tick_combo.currentText()
        self.parent.bs_x_tick_combo.currentTextChanged.connect(self.x_tick_changed)
        # 刻度范围
        self.x_tick_min = self.parent.bs_x_tick_range_min_spin.value()
        self.x_tick_max = self.parent.bs_x_tick_range_max_spin.value()
        self.parent.bs_x_tick_range_min_spin.valueChanged.connect(self.x_tick_range_min_changed)
        self.parent.bs_x_tick_range_max_spin.valueChanged.connect(self.x_tick_range_max_changed)
        # 刻度大小
        self.x_tick_size = self.parent.bs_x_tick_size_spin.value()
        self.parent.bs_x_tick_size_spin.valueChanged.connect(self.x_tick_size_changed)
        # 刻度颜色
        self.x_tick_color = "#000000"
        self.parent.bs_x_tick_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.x_tick_color)
        self.parent.bs_x_tick_color_btn.clicked.connect(self.x_tick_color_btn_clicked)

        self.bs_x_show_top_ticks = self.parent.bs_x_show_top_ticks_check.isChecked()
        self.parent.bs_x_show_top_ticks_check.stateChanged.connect(self.bs_x_show_top_ticks_changed)

        self.bs_x_tick_label_size = self.parent.bs_x_tick_label_size_spin.value()
        self.parent.bs_x_tick_label_size_spin.valueChanged.connect(self.x_tick_label_size_changed)
        # 刻度标签颜色
        self.x_tick_label_color = "#000000"
        self.parent.bs_x_tick_label_color_btn.setStyleSheet(
            "QToolButton{background-color: %s ;}" % self.x_tick_label_color)
        self.parent.bs_x_tick_label_color_btn.clicked.connect(self.x_tick_label_color_btn_clicked)
        # x刻度值系列
        self.x_tick_value_series = self.get_x_tick_value_series()
        self.parent.bs_x_tick_value_series_line.editingFinished.connect(self.x_tick_value_series_changed)
        # x刻度标签系列
        self.x_tick_label_series = self.get_x_tick_label_series()
        self.parent.bs_x_tick_label_series_line.editingFinished.connect(self.x_tick_label_series_changed)
        # 次要刻度
        self.x_minor_ticks_checked = self.parent.bs_x_minor_tick_check.isChecked()
        self.parent.bs_x_minor_tick_check.stateChanged.connect(self.x_minor_ticks_changed)
        # 次要刻度间隔
        self.x_minor_tick_interval = self.parent.bs_x_minor_tick_interval_spin.value()
        self.parent.bs_x_minor_tick_interval_spin.valueChanged.connect(self.x_minor_tick_interval_changed)
        # 刻度标签斜度
        self.x_tick_label_slope = self.parent.bs_x_slope_dial.value()
        self.parent.bs_x_slope_dial.valueChanged.connect(self.x_tick_label_slope_changed)

    def set_x_label_and_ticks(self):
        if self.x_label_bold:
            font_dict = {"size": self.bs_x_label_size, "color": self.bs_x_label_color,
                         "fontproperties": simsun_bold_font}
        else:
            font_dict = {"size": self.bs_x_label_size, "color": self.bs_x_label_color}

        if not self.bs_x_checked:
            self.canvas.axs.xaxis.set_visible(False)

        if self.x_label_bold:
            self.canvas.axs.set_xlabel(self.bs_x_title, fontdict=font_dict)
        else:
            self.canvas.axs.set_xlabel(self.bs_x_title, fontdict=font_dict)

        if len(self.x_tick_value_series) != 0 and len(self.x_tick_label_series) == len(self.x_tick_value_series):
            self.canvas.axs.set_xticks(self.x_tick_value_series, labels=self.x_tick_label_series)

        if self.x_minor_ticks_checked:
            self.canvas.axs.xaxis.set_minor_locator(ticker.MultipleLocator(self.x_minor_tick_interval))

        self.canvas.axs.tick_params(which="both", axis='x', direction=self.x_tick_direction,
                                    color=self.x_tick_color, labelcolor=self.x_tick_label_color,
                                    labelrotation=self.x_tick_label_slope, length=self.x_tick_size,
                                    labelsize=self.bs_x_tick_label_size, top=self.bs_x_show_top_ticks)

    def set_x_tick_range(self):
        if self.x_tick_min == 0 and self.x_tick_max == 0:
            self.canvas.axs.set_xlim(*self.canvas.axs.get_xlim())
        else:
            self.canvas.axs.set_xlim(left=self.x_tick_min, right=self.x_tick_max)

    def get_y_label_and_ticks(self):
        # 是否启用X轴
        self.bs_y_checked = self.parent.bs_y_enable_check.isChecked()
        self.parent.bs_y_enable_check.checkStateChanged.connect(self.bs_y_enable_check_changed)
        # 标签名称
        self.bs_y_title = self.parent.bs_y_title_edit_line.text()
        self.parent.bs_y_title_edit_line.textChanged.connect(self.bs_y_title_changed)
        # # 字体
        # self.x_label_font = self.parent.bs_x_font_combo.currentText()
        # self.parent.bs_x_font_combo.currentTextChanged.connect(self.x_label_font_changed)
        # self.parent.bs_x_font_combo.currentFontChanged.connect(self.x_label_font_changed1)
        # 字号
        self.bs_y_label_size = self.parent.bs_y_label_size_spin.value()
        self.parent.bs_y_label_size_spin.valueChanged.connect(self.bs_y_label_size_changed)
        # 标签颜色
        self.bs_y_label_color = "#000000"
        self.parent.bs_y_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bs_y_label_color)
        self.parent.bs_y_label_color_btn.clicked.connect(self.bs_y_label_color_btn_clicked)
        # 加粗
        self.y_label_bold = self.parent.bs_y_bold_check.isChecked()
        self.parent.bs_y_bold_check.stateChanged.connect(self.y_label_bold_changed)
        # 刻度
        self.y_tick_direction = self.parent.bs_y_tick_combo.currentText()
        self.parent.bs_y_tick_combo.currentTextChanged.connect(self.y_tick_changed)
        # 刻度范围
        self.y_tick_min = self.parent.bs_y_tick_range_min_spin.value()
        self.y_tick_max = self.parent.bs_y_tick_range_max_spin.value()
        self.parent.bs_y_tick_range_min_spin.valueChanged.connect(self.y_tick_range_min_changed)
        self.parent.bs_y_tick_range_max_spin.valueChanged.connect(self.y_tick_range_max_changed)
        # 刻度大小
        self.y_tick_size = self.parent.bs_y_tick_size_spin.value()
        self.parent.bs_y_tick_size_spin.valueChanged.connect(self.y_tick_size_changed)
        # 刻度颜色
        self.y_tick_color = "#000000"
        self.parent.bs_y_tick_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.y_tick_color)
        self.parent.bs_y_tick_color_btn.clicked.connect(self.y_tick_color_btn_clicked)

        self.bs_y_show_right_ticks = self.parent.bs_y_show_right_ticks_check.isChecked()
        self.parent.bs_y_show_right_ticks_check.stateChanged.connect(self.y_show_right_ticks_changed)

        self.bs_y_tick_label_size = self.parent.bs_y_tick_label_size_spin.value()
        self.parent.bs_y_tick_label_size_spin.valueChanged.connect(self.y_tick_label_size_changed)

        # 刻度标签颜色
        self.y_tick_label_color = "#000000"
        self.parent.bs_y_tick_label_color_btn.setStyleSheet(
            "QToolButton{background-color: %s ;}" % self.y_tick_label_color)
        self.parent.bs_y_tick_label_color_btn.clicked.connect(self.y_tick_label_color_btn_clicked)
        # y刻度值系列
        self.y_tick_value_series = self.get_y_tick_value_series()
        self.parent.bs_y_tick_value_series_line.editingFinished.connect(self.y_tick_value_series_changed)
        # y刻度标签系列
        self.y_tick_label_series = self.get_y_tick_label_series()
        self.parent.bs_y_tick_label_series_line.editingFinished.connect(self.y_tick_label_series_changed)
        # 次要刻度
        self.y_minor_ticks_checked = self.parent.bs_y_minor_tick_check.isChecked()
        self.parent.bs_y_minor_tick_check.stateChanged.connect(self.y_minor_ticks_changed)
        # 次要刻度间隔
        self.y_minor_tick_interval = self.parent.bs_y_minor_tick_interval_spin.value()
        self.parent.bs_y_minor_tick_interval_spin.valueChanged.connect(self.y_minor_tick_interval_changed)
        # 刻度标签斜度
        self.y_tick_label_slope = self.parent.bs_y_slope_dial.value()
        self.parent.bs_y_slope_dial.valueChanged.connect(self.y_tick_label_slope_changed)

    def set_y_label_and_ticks(self):
        if self.y_label_bold:
            font_dict = {"size": self.bs_y_label_size, "color": self.bs_y_label_color,
                         "fontproperties": simsun_bold_font}
        else:
            font_dict = {"size": self.bs_y_label_size, "color": self.bs_y_label_color}

        if not self.bs_y_checked:
            self.canvas.axs.yaxis.set_visible(False)

        if self.y_label_bold:
            self.canvas.axs.set_ylabel(self.bs_y_title, fontdict=font_dict)
        else:
            self.canvas.axs.set_ylabel(self.bs_y_title, fontdict=font_dict)

        if len(self.y_tick_value_series) != 0 and len(self.y_tick_label_series) == len(self.y_tick_value_series):
            self.canvas.axs.set_yticks(self.y_tick_value_series, labels=self.y_tick_label_series)

        if self.y_minor_ticks_checked:
            self.canvas.axs.yaxis.set_minor_locator(ticker.MultipleLocator(self.y_minor_tick_interval))

        self.canvas.axs.tick_params(which="both", axis='y', direction=self.y_tick_direction,
                                    color=self.y_tick_color, labelcolor=self.y_tick_label_color,
                                    labelrotation=self.y_tick_label_slope, length=self.y_tick_size,
                                    labelsize=self.bs_y_tick_label_size, right=self.bs_y_show_right_ticks)

    def set_y_tick_range(self):
        if self.y_tick_min == 0 and self.y_tick_max == 0:
            self.canvas.axs.set_ylim(*self.canvas.axs.get_ylim())
        else:
            self.canvas.axs.set_ylim(bottom=self.y_tick_min, top=self.y_tick_max)

    def get_title(self):
        # 标题
        self.title_text = self.parent.bs_t_title_edit_line.text()
        self.parent.bs_t_title_edit_line.textChanged.connect(self.title_changed)
        # 标题大小
        self.title_size = self.parent.bs_t_title_size_spin.value()
        self.parent.bs_t_title_size_spin.valueChanged.connect(self.title_size_changed)
        # 标题颜色
        self.title_color = "#000000"
        self.parent.bs_t_title_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.title_color)
        self.parent.bs_t_title_color_btn.clicked.connect(self.title_color_btn_clicked)
        # 加粗
        self.title_bold = self.parent.bs_t_bold_check.isChecked()
        self.parent.bs_t_bold_check.stateChanged.connect(self.bs_t_bold_changed)
        # 标题位置
        self.title_pos = self.parent.bs_t_pos_combo.currentText()
        self.parent.bs_t_pos_combo.currentTextChanged.connect(self.title_pos_changed)

    def set_title(self):
        if self.title_bold:
            font_dict = {"size": self.title_size, "color": self.title_color,
                         "fontproperties": simsun_bold_font}
        else:
            font_dict = {"size": self.title_size, "color": self.title_color}

        self.canvas.axs.set_title(self.title_text, fontdict=font_dict, loc=self.title_pos)

    def get_legend(self):
        self.legend_checked = self.parent.bs_l_legend_enabled_check.isChecked()
        self.parent.bs_l_legend_enabled_check.stateChanged.connect(self.legend_changed)
        # legend title
        self.legend_title = self.parent.bs_l_legend_title_line.text()
        self.parent.bs_l_legend_title_line.textChanged.connect(self.legend_title_changed)
        # legend title size
        self.legend_title_size = self.parent.bs_l_legend_text_size_spin.value()
        self.parent.bs_l_legend_text_size_spin.valueChanged.connect(self.legend_title_size_changed)
        # legent text size
        self.legend_text_size = self.parent.bs_l_legend_size_spin.value()
        self.parent.bs_l_legend_size_spin.valueChanged.connect(self.legend_text_size_changed)
        # legend position
        self.legend_pos = self.parent.bs_l_pos_combo.currentText()
        self.parent.bs_l_pos_combo.currentTextChanged.connect(self.legend_pos_changed)
        # legend cols
        self.legend_cols = self.parent.bs_l_legend_col_spin.value()
        self.parent.bs_l_legend_col_spin.valueChanged.connect(self.legend_cols_changed)
        # legend text colors
        self.legend_text_color = "#000000"
        self.parent.bs_l_legend_text_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.legend_text_color)
        self.parent.bs_l_legend_text_color_btn.clicked.connect(self.legend_text_color_btn_clicked)
        # legend frame
        self.legend_frame_checked = self.parent.bs_l_legend_frame_check.isChecked()
        self.parent.bs_l_legend_frame_check.stateChanged.connect(self.legend_frame_changed)
        # legend frame color
        self.legend_frame_color = "#000000"
        self.parent.bs_l_legend_frame_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.legend_frame_color)
        self.parent.bs_l_legend_frame_color_btn.clicked.connect(self.legend_frame_color_btn_clicked)
        # legend background color
        self.legend_bg_color = "#ffffff"
        self.parent.bs_l_legend_bg_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.legend_bg_color)
        self.parent.bs_l_legend_bg_color_btn.clicked.connect(self.legend_bg_color_btn_clicked)
        # legend transparent
        self.legend_transparent_value = self.parent.bs_l_legend_transparent_slider.value() / 100
        self.parent.bs_l_legend_transparent_slider.valueChanged.connect(self.legend_transparent_slider_changed)

    def set_legend(self):
        if self.legend_checked:
            self.canvas.axs.legend(
                frameon=self.legend_frame_checked,
                title=self.legend_title,
                title_fontsize=self.legend_title_size,
                fontsize=self.legend_text_size,
                loc=self.legend_pos,
                ncol=self.legend_cols,
                framealpha=self.legend_transparent_value,
                facecolor=self.legend_bg_color,
                edgecolor=self.legend_frame_color,
                labelcolor=self.legend_text_color
            )

    def get_other_settings(self):
        self.chart_border = self.parent.bs_o_border_combo.currentText()
        self.parent.bs_o_border_combo.currentTextChanged.connect(self.chart_border_changed)
        # border color
        self.border_color = "#000000"
        self.parent.bs_o_border_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.border_color)
        self.parent.bs_o_border_color_btn.clicked.connect(self.border_color_btn_clicked)

    def set_other_settings(self):
        if self.chart_border == "standard":
            self.canvas.axs.spines["left"].set_color(self.border_color)
            self.canvas.axs.spines["bottom"].set_color(self.border_color)
            self.canvas.axs.spines["top"].set_color(self.border_color)
            self.canvas.axs.spines["right"].set_color(self.border_color)
        elif self.chart_border == "left bottom":
            self.canvas.axs.spines["left"].set_visible(True)
            self.canvas.axs.spines["bottom"].set_visible(True)
            self.canvas.axs.spines["top"].set_visible(False)
            self.canvas.axs.spines["right"].set_visible(False)

            self.canvas.axs.spines["left"].set_color(self.border_color)
            self.canvas.axs.spines["bottom"].set_color(self.border_color)
        elif self.chart_border == "top right":
            self.canvas.axs.spines["top"].set_visible(True)
            self.canvas.axs.spines["right"].set_visible(True)
            self.canvas.axs.spines["bottom"].set_visible(False)
            self.canvas.axs.spines["left"].set_visible(False)

            self.canvas.axs.spines["top"].set_color(self.border_color)
            self.canvas.axs.spines["right"].set_color(self.border_color)
        elif self.chart_border == "top":
            self.canvas.axs.spines["top"].set_visible(True)
            self.canvas.axs.spines["right"].set_visible(False)
            self.canvas.axs.spines["bottom"].set_visible(False)
            self.canvas.axs.spines["left"].set_visible(False)

            self.canvas.axs.spines["top"].set_color(self.border_color)
        elif self.chart_border == "bottom":
            self.canvas.axs.spines["bottom"].set_visible(True)
            self.canvas.axs.spines["top"].set_visible(False)
            self.canvas.axs.spines["right"].set_visible(False)
            self.canvas.axs.spines["left"].set_visible(False)

            self.canvas.axs.spines["bottom"].set_color(self.border_color)
        elif self.chart_border == "left":
            self.canvas.axs.spines["left"].set_visible(True)
            self.canvas.axs.spines["top"].set_visible(False)
            self.canvas.axs.spines["right"].set_visible(False)
            self.canvas.axs.spines["bottom"].set_visible(False)

            self.canvas.axs.spines["left"].set_color(self.border_color)
        elif self.chart_border == "right":
            self.canvas.axs.spines["right"].set_visible(True)
            self.canvas.axs.spines["top"].set_visible(False)
            self.canvas.axs.spines["bottom"].set_visible(False)
            self.canvas.axs.spines["left"].set_visible(False)

            self.canvas.axs.spines["right"].set_color(self.border_color)
        else:
            self.canvas.axs.spines["top"].set_visible(False)
            self.canvas.axs.spines["right"].set_visible(False)
            self.canvas.axs.spines["bottom"].set_visible(False)
            self.canvas.axs.spines["left"].set_visible(False)

    def chart_border_changed(self, e):
        self.chart_border = e
        self.update_plot()

    def border_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        border_color = color_dialog.getColor()
        self.border_color = border_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_o_border_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.border_color)
        self.update_plot()

    def legend_changed(self, e):
        self.legend_checked = self.parent.bs_l_legend_enabled_check.isChecked()
        self.update_plot()

    def legend_title_changed(self, e):
        self.legend_title = e
        self.update_plot()

    def legend_title_size_changed(self, e):
        self.legend_title_size = e
        self.update_plot()

    def legend_text_size_changed(self, e):
        self.legend_text_size = e
        self.update_plot()

    def legend_pos_changed(self, e):
        self.legend_pos = e
        self.update_plot()

    def legend_cols_changed(self, e):
        self.legend_cols = e
        self.update_plot()

    def legend_text_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        legend_text_color = color_dialog.getColor()
        self.legend_text_color = legend_text_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_l_legend_text_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.legend_text_color)
        self.update_plot()

    def legend_frame_changed(self, e):
        self.legend_frame_checked = self.parent.bs_l_legend_frame_check.isChecked()
        if self.legend_frame_checked:
            self.parent.bs_l_legend_frame_color_btn.setEnabled(True)
            self.parent.bs_l_legend_bg_color_btn.setEnabled(True)
            self.parent.bs_l_legend_transparent_slider.setEnabled(True)
        else:
            self.parent.bs_l_legend_frame_color_btn.setEnabled(False)
            self.parent.bs_l_legend_bg_color_btn.setEnabled(False)
            self.parent.bs_l_legend_transparent_slider.setEnabled(False)
        self.update_plot()

    def legend_frame_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        legend_frame_color = color_dialog.getColor()
        self.legend_frame_color = legend_frame_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_l_legend_frame_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.legend_frame_color)
        self.update_plot()

    def legend_bg_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        legend_bg_color = color_dialog.getColor()
        self.legend_bg_color = legend_bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_l_legend_bg_color_btn.setStyleSheet(
            "QToolButton{background-color: %s ;}" % self.legend_bg_color)
        self.update_plot()

    def legend_transparent_slider_changed(self, e):
        self.legend_transparent_value = e / 100
        self.update_plot()

    def title_changed(self, e):
        self.title_text = e
        self.update_plot()

    def title_size_changed(self, e):
        self.title_size = e
        self.update_plot()

    def title_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        title_color = color_dialog.getColor()
        self.title_color = title_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_t_title_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.title_color)
        self.update_plot()

    def bs_t_bold_changed(self, e):
        self.title_bold = self.parent.bs_t_bold_check.isChecked()
        self.update_plot()

    def title_pos_changed(self, e):
        self.title_pos = e
        self.update_plot()

    def canvas_bg_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.canvas_bg_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.canvas_bg_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.canvas_bg_color)
        # print(self.canvas_bg_color)
        self.update_plot()

    def canvas_width_changed(self, e):
        self.canvas_width = e
        self.update_plot()

    def canvas_height_changed(self, e):
        self.canvas_height = e
        self.update_plot()

    def dpi_changed(self, e):
        self.dpi = e
        self.update_plot()

    def chart_bg_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.chart_bg_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.chart_bg_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.chart_bg_color)
        self.update_plot()

    def canvas_grid_check(self, e):
        if e == Qt.CheckState.Checked:
            self.canvas_grid_check_value = True
            self.parent.grid_transparent_slider.setEnabled(True)
            self.parent.show_xy_grid_slider.setEnabled(True)
        else:
            self.canvas_grid_check_value = False
            self.parent.grid_transparent_slider.setEnabled(False)
            self.parent.show_xy_grid_slider.setEnabled(False)

        self.update_plot()

    def show_xy_grid_slider_changed(self, e):
        self.show_xy_grid_value = e
        self.update_plot()

    def grid_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        grid_color = color_dialog.getColor()
        self.grid_color = grid_color.name(QColor.NameFormat.HexRgb)
        self.parent.grid_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.grid_color)
        self.update_plot()

    def grid_line_width_changed(self, e):
        self.grid_line_width = e
        self.update_plot()

    def grid_line_style_changed(self, e):
        self.grid_line_style = e
        self.update_plot()

    def grid_transparent_slider_changed(self, e):
        self.grid_transparent_value = e / 100
        self.update_plot()

    def bs_x_enable_check_changed(self, e):
        self.bs_x_checked = self.parent.bs_x_enable_check.isChecked()
        self.update_plot()

    def bs_y_enable_check_changed(self, e):
        self.bs_y_checked = self.parent.bs_y_enable_check.isChecked()
        self.update_plot()

    def bs_x_title_changed(self, e):
        self.bs_x_title = e
        self.update_plot()

    def bs_y_title_changed(self, e):
        self.bs_y_title = e
        self.update_plot()

    def bs_x_label_size_changed(self, e):
        self.bs_x_label_size = e
        self.update_plot()

    def bs_y_label_size_changed(self, e):
        self.bs_y_label_size = e
        self.update_plot()

    def bs_x_label_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.bs_x_label_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_x_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bs_x_label_color)
        self.update_plot()

    def bs_y_label_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.bs_y_label_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_y_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.bs_y_label_color)
        self.update_plot()

    def x_tick_changed(self, e):
        self.x_tick_direction = e
        self.update_plot()

    def y_tick_changed(self, e):
        self.y_tick_direction = e
        self.update_plot()

    def y_tick_range_min_changed(self, e):
        self.y_tick_min = e
        self.update_plot()

    def y_tick_range_max_changed(self, e):
        self.y_tick_max = e
        self.update_plot()

    def x_tick_size_changed(self, e):
        self.x_tick_size = e
        self.update_plot()

    def x_tick_range_max_changed(self, e):
        self.x_tick_max = e
        self.update_plot()

    def x_tick_range_min_changed(self, e):
        self.x_tick_min = e
        self.update_plot()

    def y_tick_size_changed(self, e):
        self.y_tick_size = e
        self.update_plot()

    def x_label_bold_changed(self, e):
        self.x_label_bold = self.parent.bs_x_bold_check.isChecked()
        self.update_plot()

    def y_label_bold_changed(self, e):
        self.y_label_bold = self.parent.bs_y_bold_check.isChecked()
        self.update_plot()

    def x_tick_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.x_tick_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_x_tick_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.x_tick_color)
        self.update_plot()

    def bs_x_show_top_ticks_changed(self, e):
        self.bs_x_show_top_ticks = self.parent.bs_x_show_top_ticks_check.isChecked()
        self.update_plot()

    def x_tick_label_size_changed(self, e):
        self.bs_x_tick_label_size = e
        self.update_plot()

    def y_tick_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.y_tick_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_y_tick_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.y_tick_color)
        self.update_plot()

    def y_show_right_ticks_changed(self, e):
        self.bs_y_show_right_ticks = self.parent.bs_y_show_right_ticks_check.isChecked()
        self.update_plot()

    def y_tick_label_size_changed(self, e):
        self.bs_y_tick_label_size = e
        self.update_plot()

    def x_tick_label_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.x_tick_label_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_x_tick_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.x_tick_label_color)
        self.update_plot()

    def y_tick_label_color_btn_clicked(self, e):
        color_dialog = QColorDialog(self)
        bg_color = color_dialog.getColor()
        self.y_tick_label_color = bg_color.name(QColor.NameFormat.HexRgb)
        self.parent.bs_y_tick_label_color_btn.setStyleSheet("QToolButton{background-color: %s ;}" % self.y_tick_label_color)
        self.update_plot()

    def get_x_tick_value_series(self):
        text = self.parent.bs_x_tick_value_series_line.text().strip()
        if len(text) == 0:
            return []
        x_tick_value_series = text.split(",")
        try:
            x_tick_value_series = [float(i) for i in x_tick_value_series]
        except:
            x_tick_value_series = x_tick_value_series
        return x_tick_value_series

    def get_y_tick_value_series(self):
        text = self.parent.bs_y_tick_value_series_line.text().strip()
        if len(text) == 0:
            return []
        y_tick_value_series = text.split(",")
        try:
            y_tick_value_series = [float(i) for i in y_tick_value_series]
        except:
            y_tick_value_series = y_tick_value_series
        return y_tick_value_series

    def x_tick_value_series_changed(self):
        self.x_tick_value_series = self.get_x_tick_value_series()
        self.update_plot()

    def y_tick_value_series_changed(self):
        self.y_tick_value_series = self.get_y_tick_value_series()
        self.update_plot()

    def get_x_tick_label_series(self):
        text = self.parent.bs_x_tick_label_series_line.text().strip()
        if len(text) == 0:
            return []
        x_tick_label_series = text.split(",")
        return x_tick_label_series

    def get_y_tick_label_series(self):
        text = self.parent.bs_y_tick_label_series_line.text().strip()
        if len(text) == 0:
            return []
        y_tick_label_series = text.split(",")
        return y_tick_label_series

    def x_tick_label_series_changed(self):
        self.x_tick_label_series = self.get_x_tick_label_series()
        self.update_plot()

    def y_tick_label_series_changed(self):
        self.y_tick_label_series = self.get_y_tick_label_series()
        self.update_plot()

    def x_minor_ticks_changed(self, e):
        self.x_minor_ticks_checked = self.parent.bs_x_minor_tick_check.isChecked()
        if self.x_minor_ticks_checked:
            self.parent.bs_x_minor_tick_interval_spin.setEnabled(True)
        else:
            self.parent.bs_x_minor_tick_interval_spin.setEnabled(False)
        self.update_plot()

    def y_minor_ticks_changed(self, e):
        self.y_minor_ticks_checked = self.parent.bs_y_minor_tick_check.isChecked()
        if self.y_minor_ticks_checked:
            self.parent.bs_y_minor_tick_interval_spin.setEnabled(True)
        else:
            self.parent.bs_y_minor_tick_interval_spin.setEnabled(False)
        self.update_plot()

    def x_minor_tick_interval_changed(self, e):
        self.x_minor_tick_interval = e
        self.update_plot()

    def y_minor_tick_interval_changed(self, e):
        self.y_minor_tick_interval = e
        self.update_plot()

    def x_tick_label_slope_changed(self, e):
        self.x_tick_label_slope = e
        self.update_plot()

    def y_tick_label_slope_changed(self, e):
        self.y_tick_label_slope = e
        self.update_plot()