# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lineChartToolUIXPLcGh.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(333, 648)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.x_series_label = QLabel(Form)
        self.x_series_label.setObjectName(u"x_series_label")
        self.x_series_label.setMinimumSize(QSize(100, 0))
        self.x_series_label.setMaximumSize(QSize(76, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.x_series_label)

        self.x_series_combo = QComboBox(Form)
        self.x_series_combo.setObjectName(u"x_series_combo")

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

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 21))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.line_color_series_btn = QToolButton(Form)
        self.line_color_series_btn.setObjectName(u"line_color_series_btn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_color_series_btn)

        self.line_color_series_line = QLineEdit(Form)
        self.line_color_series_line.setObjectName(u"line_color_series_line")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.line_color_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(19, QFormLayout.FieldRole, self.verticalSpacer)

        self.line_type_series_line = QLineEdit(Form)
        self.line_type_series_line.setObjectName(u"line_type_series_line")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.line_type_series_line)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.line_width_spin = QSpinBox(Form)
        self.line_width_spin.setObjectName(u"line_width_spin")
        self.line_width_spin.setMinimum(1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.line_width_spin)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.line_marker_series_line = QLineEdit(Form)
        self.line_marker_series_line.setObjectName(u"line_marker_series_line")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.line_marker_series_line)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_13)

        self.line_marker_size_spin = QSpinBox(Form)
        self.line_marker_size_spin.setObjectName(u"line_marker_size_spin")
        self.line_marker_size_spin.setMinimum(1)
        self.line_marker_size_spin.setValue(6)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.line_marker_size_spin)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_2)

        self.line_path_check = QCheckBox(Form)
        self.line_path_check.setObjectName(u"line_path_check")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.line_path_check)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_4)

        self.line_path_interval_spin = QSpinBox(Form)
        self.line_path_interval_spin.setObjectName(u"line_path_interval_spin")
        self.line_path_interval_spin.setEnabled(False)
        self.line_path_interval_spin.setMinimum(1)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.line_path_interval_spin)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_5)

        self.line_path_angle_spin = QSpinBox(Form)
        self.line_path_angle_spin.setObjectName(u"line_path_angle_spin")
        self.line_path_angle_spin.setEnabled(False)
        self.line_path_angle_spin.setMaximum(360)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.line_path_angle_spin)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_6)

        self.line_value_label_check = QCheckBox(Form)
        self.line_value_label_check.setObjectName(u"line_value_label_check")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.line_value_label_check)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_10)

        self.line_value_label_horiz_pos_combo = QComboBox(Form)
        self.line_value_label_horiz_pos_combo.addItem("")
        self.line_value_label_horiz_pos_combo.addItem("")
        self.line_value_label_horiz_pos_combo.addItem("")
        self.line_value_label_horiz_pos_combo.setObjectName(u"line_value_label_horiz_pos_combo")
        self.line_value_label_horiz_pos_combo.setEnabled(False)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.line_value_label_horiz_pos_combo)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_21)

        self.line_value_label_vertic_pos_combo = QComboBox(Form)
        self.line_value_label_vertic_pos_combo.addItem("")
        self.line_value_label_vertic_pos_combo.addItem("")
        self.line_value_label_vertic_pos_combo.addItem("")
        self.line_value_label_vertic_pos_combo.setObjectName(u"line_value_label_vertic_pos_combo")
        self.line_value_label_vertic_pos_combo.setEnabled(False)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.line_value_label_vertic_pos_combo)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_7)

        self.line_value_label_interval_spin = QDoubleSpinBox(Form)
        self.line_value_label_interval_spin.setObjectName(u"line_value_label_interval_spin")
        self.line_value_label_interval_spin.setEnabled(False)
        self.line_value_label_interval_spin.setDecimals(2)
        self.line_value_label_interval_spin.setMaximum(100.000000000000000)
        self.line_value_label_interval_spin.setSingleStep(0.100000000000000)
        self.line_value_label_interval_spin.setValue(0.500000000000000)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.line_value_label_interval_spin)

        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_22)

        self.line_value_label_color_series_btn = QToolButton(Form)
        self.line_value_label_color_series_btn.setObjectName(u"line_value_label_color_series_btn")
        self.line_value_label_color_series_btn.setEnabled(False)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.line_value_label_color_series_btn)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_23)

        self.line_value_label_color_series_line = QLineEdit(Form)
        self.line_value_label_color_series_line.setObjectName(u"line_value_label_color_series_line")
        self.line_value_label_color_series_line.setEnabled(False)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.line_value_label_color_series_line)

        self.line_value_label_size_spin = QSpinBox(Form)
        self.line_value_label_size_spin.setObjectName(u"line_value_label_size_spin")
        self.line_value_label_size_spin.setEnabled(False)
        self.line_value_label_size_spin.setValue(9)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.line_value_label_size_spin)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_24)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.x_series_label.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"ColorSeries", None))
        self.line_color_series_btn.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"LineStyleSeries", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"LineWidth", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"MarkerStyleSeries", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"MarkerSize", None))
        self.line_path_check.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"AddPath", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"PathInterval", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"PathAngle", None))
        self.line_value_label_check.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"AddValueLabel", None))
        self.line_value_label_horiz_pos_combo.setItemText(0, QCoreApplication.translate("Form", u"left", None))
        self.line_value_label_horiz_pos_combo.setItemText(1, QCoreApplication.translate("Form", u"center", None))
        self.line_value_label_horiz_pos_combo.setItemText(2, QCoreApplication.translate("Form", u"right", None))

        self.label_21.setText(QCoreApplication.translate("Form", u"HorizontalAlign", None))
        self.line_value_label_vertic_pos_combo.setItemText(0, QCoreApplication.translate("Form", u"top", None))
        self.line_value_label_vertic_pos_combo.setItemText(1, QCoreApplication.translate("Form", u"center", None))
        self.line_value_label_vertic_pos_combo.setItemText(2, QCoreApplication.translate("Form", u"bottom", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"VerticalAlign", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"ValueLabelInterval", None))
        self.line_value_label_color_series_btn.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"ValueLabelColorSeries", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"ValueLabelSize", None))
    # retranslateUi

