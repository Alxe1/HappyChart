# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radarChartToolUINJKjZS.ui'
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

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(354, 587)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.x_series_label = QLabel(Form)
        self.x_series_label.setObjectName(u"x_series_label")
        self.x_series_label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.x_series_label)

        self.x_series_combo = QComboBox(Form)
        self.x_series_combo.setObjectName(u"x_series_combo")
        self.x_series_combo.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_series_combo)

        self.y_series_label = QLabel(Form)
        self.y_series_label.setObjectName(u"y_series_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.y_series_label)

        self.y_series_combo = CheckableComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y_series_combo)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_label_line)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.theta_offset_dial = QDial(Form)
        self.theta_offset_dial.setObjectName(u"theta_offset_dial")
        self.theta_offset_dial.setMaximumSize(QSize(16777215, 50))
        self.theta_offset_dial.setMinimum(0)
        self.theta_offset_dial.setMaximum(360)
        self.theta_offset_dial.setSingleStep(10)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.theta_offset_dial)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.theta_direction_combo = QComboBox(Form)
        self.theta_direction_combo.addItem("")
        self.theta_direction_combo.addItem("")
        self.theta_direction_combo.addItem("")
        self.theta_direction_combo.setObjectName(u"theta_direction_combo")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.theta_direction_combo)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.line_width_spin = QSpinBox(Form)
        self.line_width_spin.setObjectName(u"line_width_spin")
        self.line_width_spin.setMinimum(1)
        self.line_width_spin.setMaximum(100)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.line_width_spin)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.line_type_combo = QComboBox(Form)
        self.line_type_combo.addItem("")
        self.line_type_combo.addItem("")
        self.line_type_combo.addItem("")
        self.line_type_combo.addItem("")
        self.line_type_combo.setObjectName(u"line_type_combo")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.line_type_combo)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 21))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_11)

        self.radar_line_color_series_btn = QToolButton(Form)
        self.radar_line_color_series_btn.setObjectName(u"radar_line_color_series_btn")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.radar_line_color_series_btn)

        self.radar_line_color_series_line = QLineEdit(Form)
        self.radar_line_color_series_line.setObjectName(u"radar_line_color_series_line")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.radar_line_color_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(16, QFormLayout.FieldRole, self.verticalSpacer)

        self.radar_fill_color_series_btn = QToolButton(Form)
        self.radar_fill_color_series_btn.setObjectName(u"radar_fill_color_series_btn")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.radar_fill_color_series_btn)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.radar_fill_color_series_line = QLineEdit(Form)
        self.radar_fill_color_series_line.setObjectName(u"radar_fill_color_series_line")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.radar_fill_color_series_line)

        self.radar_fill_transparent_slider = QSlider(Form)
        self.radar_fill_transparent_slider.setObjectName(u"radar_fill_transparent_slider")
        self.radar_fill_transparent_slider.setMaximum(100)
        self.radar_fill_transparent_slider.setValue(30)
        self.radar_fill_transparent_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.radar_fill_transparent_slider)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_9)

        self.radar_value_label_check = QCheckBox(Form)
        self.radar_value_label_check.setObjectName(u"radar_value_label_check")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.radar_value_label_check)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_10)

        self.radar_value_label_interval_spin = QDoubleSpinBox(Form)
        self.radar_value_label_interval_spin.setObjectName(u"radar_value_label_interval_spin")
        self.radar_value_label_interval_spin.setEnabled(False)
        self.radar_value_label_interval_spin.setDecimals(2)
        self.radar_value_label_interval_spin.setMaximum(100.000000000000000)
        self.radar_value_label_interval_spin.setSingleStep(0.010000000000000)
        self.radar_value_label_interval_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.radar_value_label_interval_spin)

        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_22)

        self.radar_value_label_color_btn = QToolButton(Form)
        self.radar_value_label_color_btn.setObjectName(u"radar_value_label_color_btn")
        self.radar_value_label_color_btn.setEnabled(False)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.radar_value_label_color_btn)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_23)

        self.radar_value_label_size_spin = QSpinBox(Form)
        self.radar_value_label_size_spin.setObjectName(u"radar_value_label_size_spin")
        self.radar_value_label_size_spin.setEnabled(False)
        self.radar_value_label_size_spin.setValue(9)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.radar_value_label_size_spin)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_24)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.x_series_label.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ThetaOffset", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ThetaDirection", None))
        self.theta_direction_combo.setItemText(0, QCoreApplication.translate("Form", u"clockwise", None))
        self.theta_direction_combo.setItemText(1, QCoreApplication.translate("Form", u"counterclockwise", None))
        self.theta_direction_combo.setItemText(2, QCoreApplication.translate("Form", u"anticlockwise", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"EdgeWidth", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"EdgeStyle", None))
        self.line_type_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.line_type_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.line_type_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.line_type_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_11.setText(QCoreApplication.translate("Form", u"EdgeColorSeries", None))
        self.radar_line_color_series_btn.setText("")
        self.radar_fill_color_series_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"FillColorSeries", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"FillTransparency", None))
        self.radar_value_label_check.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"AddValueLabel", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"ValueLabelInterval", None))
        self.radar_value_label_color_btn.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"ValueLabelColor", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"ValueLabelSize", None))
    # retranslateUi

