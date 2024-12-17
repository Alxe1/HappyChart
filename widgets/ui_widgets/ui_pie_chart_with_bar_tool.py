# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pieChartWithBarToolUIPlCsaD.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDial,
    QDoubleSpinBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 1008)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.y_series_label = QLabel(Form)
        self.y_series_label.setObjectName(u"y_series_label")
        self.y_series_label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.y_series_label)

        self.y_series_combo = QComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")
        self.y_series_combo.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y_series_combo)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")
        self.data_label_line.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_label_line)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_33)

        self.color_series_btn = QToolButton(Form)
        self.color_series_btn.setObjectName(u"color_series_btn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.color_series_btn)

        self.color_series_line = QLineEdit(Form)
        self.color_series_line.setObjectName(u"color_series_line")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.color_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(31, QFormLayout.FieldRole, self.verticalSpacer)

        self.bind_wedge_index_spin = QSpinBox(Form)
        self.bind_wedge_index_spin.setObjectName(u"bind_wedge_index_spin")
        self.bind_wedge_index_spin.setMaximum(100)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.bind_wedge_index_spin)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.bar_data_series_line = QLineEdit(Form)
        self.bar_data_series_line.setObjectName(u"bar_data_series_line")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.bar_data_series_line)

        self.label_42 = QLabel(Form)
        self.label_42.setObjectName(u"label_42")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_42)

        self.bar_label_series_line = QLineEdit(Form)
        self.bar_label_series_line.setObjectName(u"bar_label_series_line")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.bar_label_series_line)

        self.label_43 = QLabel(Form)
        self.label_43.setObjectName(u"label_43")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_43)

        self.bar_color_btn = QToolButton(Form)
        self.bar_color_btn.setObjectName(u"bar_color_btn")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.bar_color_btn)

        self.label_44 = QLabel(Form)
        self.label_44.setObjectName(u"label_44")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_44)

        self.bar_title_line = QLineEdit(Form)
        self.bar_title_line.setObjectName(u"bar_title_line")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.bar_title_line)

        self.label_48 = QLabel(Form)
        self.label_48.setObjectName(u"label_48")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_48)

        self.bar_legend_pos_combo = QComboBox(Form)
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.addItem("")
        self.bar_legend_pos_combo.setObjectName(u"bar_legend_pos_combo")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.bar_legend_pos_combo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_2)

        self.tied_line_width_spin = QSpinBox(Form)
        self.tied_line_width_spin.setObjectName(u"tied_line_width_spin")
        self.tied_line_width_spin.setMinimum(1)
        self.tied_line_width_spin.setValue(1)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.tied_line_width_spin)

        self.label_45 = QLabel(Form)
        self.label_45.setObjectName(u"label_45")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_45)

        self.tied_line_style_combo = QComboBox(Form)
        self.tied_line_style_combo.addItem("")
        self.tied_line_style_combo.addItem("")
        self.tied_line_style_combo.addItem("")
        self.tied_line_style_combo.addItem("")
        self.tied_line_style_combo.setObjectName(u"tied_line_style_combo")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.tied_line_style_combo)

        self.label_46 = QLabel(Form)
        self.label_46.setObjectName(u"label_46")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_46)

        self.tied_line_color_btn = QToolButton(Form)
        self.tied_line_color_btn.setObjectName(u"tied_line_color_btn")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.tied_line_color_btn)

        self.label_47 = QLabel(Form)
        self.label_47.setObjectName(u"label_47")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_47)

        self.pct_combo = QComboBox(Form)
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.setObjectName(u"pct_combo")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.pct_combo)

        self.label_35 = QLabel(Form)
        self.label_35.setObjectName(u"label_35")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_35)

        self.pct_distance_spin = QDoubleSpinBox(Form)
        self.pct_distance_spin.setObjectName(u"pct_distance_spin")
        self.pct_distance_spin.setSingleStep(0.010000000000000)
        self.pct_distance_spin.setValue(0.500000000000000)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.pct_distance_spin)

        self.label_32 = QLabel(Form)
        self.label_32.setObjectName(u"label_32")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_32)

        self.label_distance_spin = QDoubleSpinBox(Form)
        self.label_distance_spin.setObjectName(u"label_distance_spin")
        self.label_distance_spin.setSingleStep(0.010000000000000)
        self.label_distance_spin.setValue(1.200000000000000)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.label_distance_spin)

        self.label_36 = QLabel(Form)
        self.label_36.setObjectName(u"label_36")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_36)

        self.explode_series_line = QLineEdit(Form)
        self.explode_series_line.setObjectName(u"explode_series_line")

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.explode_series_line)

        self.label_39 = QLabel(Form)
        self.label_39.setObjectName(u"label_39")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_39)

        self.start_angle_dial = QDial(Form)
        self.start_angle_dial.setObjectName(u"start_angle_dial")
        self.start_angle_dial.setMinimumSize(QSize(50, 50))
        self.start_angle_dial.setMaximumSize(QSize(50, 50))
        self.start_angle_dial.setMaximum(360)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.start_angle_dial)

        self.label_31 = QLabel(Form)
        self.label_31.setObjectName(u"label_31")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_31)

        self.radius_spin = QDoubleSpinBox(Form)
        self.radius_spin.setObjectName(u"radius_spin")
        self.radius_spin.setMaximum(100.000000000000000)
        self.radius_spin.setSingleStep(0.010000000000000)
        self.radius_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.radius_spin)

        self.label_34 = QLabel(Form)
        self.label_34.setObjectName(u"label_34")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_34)

        self.unticlockwise_check = QCheckBox(Form)
        self.unticlockwise_check.setObjectName(u"unticlockwise_check")

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.unticlockwise_check)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_23)

        self.shadow_check = QCheckBox(Form)
        self.shadow_check.setObjectName(u"shadow_check")

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.shadow_check)

        self.label_30 = QLabel(Form)
        self.label_30.setObjectName(u"label_30")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_30)

        self.text_props_check = QCheckBox(Form)
        self.text_props_check.setObjectName(u"text_props_check")

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.text_props_check)

        self.label_27 = QLabel(Form)
        self.label_27.setObjectName(u"label_27")

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.label_27)

        self.font_size_spin = QSpinBox(Form)
        self.font_size_spin.setObjectName(u"font_size_spin")
        self.font_size_spin.setEnabled(False)
        self.font_size_spin.setMinimum(1)
        self.font_size_spin.setValue(9)

        self.formLayout.setWidget(23, QFormLayout.FieldRole, self.font_size_spin)

        self.label_29 = QLabel(Form)
        self.label_29.setObjectName(u"label_29")

        self.formLayout.setWidget(23, QFormLayout.LabelRole, self.label_29)

        self.font_color_btn = QToolButton(Form)
        self.font_color_btn.setObjectName(u"font_color_btn")
        self.font_color_btn.setEnabled(False)

        self.formLayout.setWidget(24, QFormLayout.FieldRole, self.font_color_btn)

        self.label_26 = QLabel(Form)
        self.label_26.setObjectName(u"label_26")

        self.formLayout.setWidget(24, QFormLayout.LabelRole, self.label_26)

        self.wedge_props_check = QCheckBox(Form)
        self.wedge_props_check.setObjectName(u"wedge_props_check")

        self.formLayout.setWidget(25, QFormLayout.FieldRole, self.wedge_props_check)

        self.label_28 = QLabel(Form)
        self.label_28.setObjectName(u"label_28")

        self.formLayout.setWidget(25, QFormLayout.LabelRole, self.label_28)

        self.wedge_width_spin = QDoubleSpinBox(Form)
        self.wedge_width_spin.setObjectName(u"wedge_width_spin")
        self.wedge_width_spin.setEnabled(False)
        self.wedge_width_spin.setMaximum(100.000000000000000)
        self.wedge_width_spin.setSingleStep(0.010000000000000)
        self.wedge_width_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(26, QFormLayout.FieldRole, self.wedge_width_spin)

        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(26, QFormLayout.LabelRole, self.label_22)

        self.edge_color_btn = QToolButton(Form)
        self.edge_color_btn.setObjectName(u"edge_color_btn")
        self.edge_color_btn.setEnabled(False)

        self.formLayout.setWidget(27, QFormLayout.FieldRole, self.edge_color_btn)

        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(27, QFormLayout.LabelRole, self.label_25)

        self.line_width_spin = QSpinBox(Form)
        self.line_width_spin.setObjectName(u"line_width_spin")
        self.line_width_spin.setEnabled(False)
        self.line_width_spin.setValue(1)

        self.formLayout.setWidget(28, QFormLayout.FieldRole, self.line_width_spin)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(28, QFormLayout.LabelRole, self.label_21)

        self.line_style_combo = QComboBox(Form)
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.setObjectName(u"line_style_combo")
        self.line_style_combo.setEnabled(False)

        self.formLayout.setWidget(29, QFormLayout.FieldRole, self.line_style_combo)

        self.label_40 = QLabel(Form)
        self.label_40.setObjectName(u"label_40")

        self.formLayout.setWidget(29, QFormLayout.LabelRole, self.label_40)

        self.transparent_slider = QSlider(Form)
        self.transparent_slider.setObjectName(u"transparent_slider")
        self.transparent_slider.setEnabled(False)
        self.transparent_slider.setMaximum(100)
        self.transparent_slider.setValue(100)
        self.transparent_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(30, QFormLayout.FieldRole, self.transparent_slider)

        self.label_37 = QLabel(Form)
        self.label_37.setObjectName(u"label_37")

        self.formLayout.setWidget(30, QFormLayout.LabelRole, self.label_37)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.x_series_combo = QComboBox(Form)
        self.x_series_combo.setObjectName(u"x_series_combo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_series_combo)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"ColorSeries", None))
        self.color_series_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"BindWedgeIndex", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"BarDataSeries", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"BarLabelSeries", None))
        self.bar_color_btn.setText("")
        self.label_44.setText(QCoreApplication.translate("Form", u"BarColor", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"BarTitle", None))
        self.bar_legend_pos_combo.setItemText(0, QCoreApplication.translate("Form", u"best", None))
        self.bar_legend_pos_combo.setItemText(1, QCoreApplication.translate("Form", u"upper right", None))
        self.bar_legend_pos_combo.setItemText(2, QCoreApplication.translate("Form", u"upper left", None))
        self.bar_legend_pos_combo.setItemText(3, QCoreApplication.translate("Form", u"lower left", None))
        self.bar_legend_pos_combo.setItemText(4, QCoreApplication.translate("Form", u"lower right", None))
        self.bar_legend_pos_combo.setItemText(5, QCoreApplication.translate("Form", u"right", None))
        self.bar_legend_pos_combo.setItemText(6, QCoreApplication.translate("Form", u"center left", None))
        self.bar_legend_pos_combo.setItemText(7, QCoreApplication.translate("Form", u"center right", None))
        self.bar_legend_pos_combo.setItemText(8, QCoreApplication.translate("Form", u"lower center", None))
        self.bar_legend_pos_combo.setItemText(9, QCoreApplication.translate("Form", u"upper center", None))
        self.bar_legend_pos_combo.setItemText(10, QCoreApplication.translate("Form", u"center", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"BarLegendPosition", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"TiedLineWidth", None))
        self.tied_line_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.tied_line_style_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.tied_line_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.tied_line_style_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_46.setText(QCoreApplication.translate("Form", u"TiedLineStyle", None))
        self.tied_line_color_btn.setText("")
        self.label_47.setText(QCoreApplication.translate("Form", u"TiedLineColor", None))
        self.pct_combo.setItemText(0, QCoreApplication.translate("Form", u"none", None))
        self.pct_combo.setItemText(1, QCoreApplication.translate("Form", u"0", None))
        self.pct_combo.setItemText(2, QCoreApplication.translate("Form", u"1", None))
        self.pct_combo.setItemText(3, QCoreApplication.translate("Form", u"2", None))
        self.pct_combo.setItemText(4, QCoreApplication.translate("Form", u"3", None))
        self.pct_combo.setItemText(5, QCoreApplication.translate("Form", u"4", None))

        self.label_35.setText(QCoreApplication.translate("Form", u"ShowPct", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"PctDistance", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"LabelDistance", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"ExplodeSeries", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"StartAngle", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Radius", None))
        self.unticlockwise_check.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"UntiClockWise", None))
        self.shadow_check.setText("")
        self.label_30.setText(QCoreApplication.translate("Form", u"Shadow", None))
        self.text_props_check.setText("")
        self.label_27.setText(QCoreApplication.translate("Form", u"TextProps", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"FontSize", None))
        self.font_color_btn.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"FontColor", None))
        self.wedge_props_check.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", u"WedgeProps", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"WedgeWidth", None))
        self.edge_color_btn.setText("")
        self.label_25.setText(QCoreApplication.translate("Form", u"EdgeColor", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"LineWidth", None))
        self.line_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.line_style_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.line_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.line_style_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_40.setText(QCoreApplication.translate("Form", u"LineStyle", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Transparency", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
    # retranslateUi

