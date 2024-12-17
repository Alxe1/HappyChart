# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pieChartToolUIkhhHBV.ui'
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
        Form.resize(346, 780)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.x_series_combo = QComboBox(Form)
        self.x_series_combo.setObjectName(u"x_series_combo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_series_combo)

        self.y_series_label = QLabel(Form)
        self.y_series_label.setObjectName(u"y_series_label")
        self.y_series_label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.y_series_label)

        self.y_series_combo = QComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")
        self.y_series_combo.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y_series_combo)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")
        self.data_label_line.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_label_line)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_14)

        self.color_series_btn = QToolButton(Form)
        self.color_series_btn.setObjectName(u"color_series_btn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.color_series_btn)

        self.color_series_line = QLineEdit(Form)
        self.color_series_line.setObjectName(u"color_series_line")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.color_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(22, QFormLayout.FieldRole, self.verticalSpacer)

        self.pct_combo = QComboBox(Form)
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.addItem("")
        self.pct_combo.setObjectName(u"pct_combo")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pct_combo)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.pct_distance_spin = QDoubleSpinBox(Form)
        self.pct_distance_spin.setObjectName(u"pct_distance_spin")
        self.pct_distance_spin.setMaximum(10.000000000000000)
        self.pct_distance_spin.setSingleStep(0.010000000000000)
        self.pct_distance_spin.setValue(0.500000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pct_distance_spin)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_2)

        self.label_distance_spin = QDoubleSpinBox(Form)
        self.label_distance_spin.setObjectName(u"label_distance_spin")
        self.label_distance_spin.setMaximum(10.000000000000000)
        self.label_distance_spin.setSingleStep(0.010000000000000)
        self.label_distance_spin.setValue(1.200000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_distance_spin)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_10)

        self.explode_series_line = QLineEdit(Form)
        self.explode_series_line.setObjectName(u"explode_series_line")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.explode_series_line)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_3)

        self.start_angle_dial = QDial(Form)
        self.start_angle_dial.setObjectName(u"start_angle_dial")
        self.start_angle_dial.setMinimumSize(QSize(50, 50))
        self.start_angle_dial.setMaximumSize(QSize(50, 50))
        self.start_angle_dial.setMaximum(360)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.start_angle_dial)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.radius_spin = QDoubleSpinBox(Form)
        self.radius_spin.setObjectName(u"radius_spin")
        self.radius_spin.setMaximum(100.000000000000000)
        self.radius_spin.setSingleStep(0.010000000000000)
        self.radius_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.radius_spin)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_12)

        self.unticlockwise_check = QCheckBox(Form)
        self.unticlockwise_check.setObjectName(u"unticlockwise_check")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.unticlockwise_check)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_15)

        self.shadow_check = QCheckBox(Form)
        self.shadow_check.setObjectName(u"shadow_check")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.shadow_check)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_4)

        self.text_props_check = QCheckBox(Form)
        self.text_props_check.setObjectName(u"text_props_check")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.text_props_check)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_5)

        self.font_size_spin = QSpinBox(Form)
        self.font_size_spin.setObjectName(u"font_size_spin")
        self.font_size_spin.setEnabled(False)
        self.font_size_spin.setMinimum(1)
        self.font_size_spin.setValue(9)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.font_size_spin)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_8)

        self.font_color_btn = QToolButton(Form)
        self.font_color_btn.setObjectName(u"font_color_btn")
        self.font_color_btn.setEnabled(False)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.font_color_btn)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_11)

        self.wedge_props_check = QCheckBox(Form)
        self.wedge_props_check.setObjectName(u"wedge_props_check")

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.wedge_props_check)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_13)

        self.wedge_width_spin = QDoubleSpinBox(Form)
        self.wedge_width_spin.setObjectName(u"wedge_width_spin")
        self.wedge_width_spin.setEnabled(False)
        self.wedge_width_spin.setMaximum(100.000000000000000)
        self.wedge_width_spin.setSingleStep(0.010000000000000)
        self.wedge_width_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.wedge_width_spin)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_17)

        self.edge_color_btn = QToolButton(Form)
        self.edge_color_btn.setObjectName(u"edge_color_btn")
        self.edge_color_btn.setEnabled(False)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.edge_color_btn)

        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_18)

        self.line_width_spin = QSpinBox(Form)
        self.line_width_spin.setObjectName(u"line_width_spin")
        self.line_width_spin.setEnabled(False)
        self.line_width_spin.setValue(1)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.line_width_spin)

        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_19)

        self.line_style_combo = QComboBox(Form)
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.setObjectName(u"line_style_combo")
        self.line_style_combo.setEnabled(False)

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.line_style_combo)

        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_20)

        self.transparent_slider = QSlider(Form)
        self.transparent_slider.setObjectName(u"transparent_slider")
        self.transparent_slider.setEnabled(False)
        self.transparent_slider.setMaximum(100)
        self.transparent_slider.setValue(100)
        self.transparent_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.transparent_slider)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_9)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"ColorSeries", None))
        self.color_series_btn.setText("")
        self.pct_combo.setItemText(0, QCoreApplication.translate("Form", u"none", None))
        self.pct_combo.setItemText(1, QCoreApplication.translate("Form", u"0", None))
        self.pct_combo.setItemText(2, QCoreApplication.translate("Form", u"1", None))
        self.pct_combo.setItemText(3, QCoreApplication.translate("Form", u"2", None))
        self.pct_combo.setItemText(4, QCoreApplication.translate("Form", u"3", None))
        self.pct_combo.setItemText(5, QCoreApplication.translate("Form", u"4", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"ShowPct", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"PctDistance", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"LabelDistance", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ExplodeSeries", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"StartAngle", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Radius", None))
        self.unticlockwise_check.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"UntiClockWise", None))
        self.shadow_check.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Shadow", None))
        self.text_props_check.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"TextProps", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"FontSize", None))
        self.font_color_btn.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"FontColor", None))
        self.wedge_props_check.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"WedgeProps", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"WedgeWidth", None))
        self.edge_color_btn.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"EdgeColor", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"LineWidth", None))
        self.line_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.line_style_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.line_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.line_style_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_20.setText(QCoreApplication.translate("Form", u"LineStyle", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Transparency", None))
    # retranslateUi

