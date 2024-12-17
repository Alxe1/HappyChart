# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hbarChartToolUISfOMiO.ui'
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
        Form.resize(322, 538)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_30 = QLabel(Form)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_30)

        self.bar_selector_combo = QComboBox(Form)
        self.bar_selector_combo.addItem("")
        self.bar_selector_combo.addItem("")
        self.bar_selector_combo.addItem("")
        self.bar_selector_combo.setObjectName(u"bar_selector_combo")
        self.bar_selector_combo.setMinimumSize(QSize(0, 0))
        self.bar_selector_combo.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.bar_selector_combo)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.x_series_combo = QComboBox(Form)
        self.x_series_combo.setObjectName(u"x_series_combo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.x_series_combo)

        self.y_series_label_2 = QLabel(Form)
        self.y_series_label_2.setObjectName(u"y_series_label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.y_series_label_2)

        self.y_series_combo = CheckableComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.y_series_combo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.data_label_line)

        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 21))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.base_chart_color_series_btn = QToolButton(Form)
        self.base_chart_color_series_btn.setObjectName(u"base_chart_color_series_btn")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.base_chart_color_series_btn)

        self.base_chart_color_series_line = QLineEdit(Form)
        self.base_chart_color_series_line.setObjectName(u"base_chart_color_series_line")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.base_chart_color_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(14, QFormLayout.FieldRole, self.verticalSpacer)

        self.base_chart_interval_spin = QDoubleSpinBox(Form)
        self.base_chart_interval_spin.setObjectName(u"base_chart_interval_spin")
        self.base_chart_interval_spin.setMinimum(0.000000000000000)
        self.base_chart_interval_spin.setMaximum(0.500000000000000)
        self.base_chart_interval_spin.setSingleStep(0.010000000000000)
        self.base_chart_interval_spin.setValue(0.350000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.base_chart_interval_spin)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_14)

        self.y_err_series_line = QLineEdit(Form)
        self.y_err_series_line.setObjectName(u"y_err_series_line")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.y_err_series_line)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.err_bar_color_btn = QToolButton(Form)
        self.err_bar_color_btn.setObjectName(u"err_bar_color_btn")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.err_bar_color_btn)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_15)

        self.bar_value_label_check = QCheckBox(Form)
        self.bar_value_label_check.setObjectName(u"bar_value_label_check")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.bar_value_label_check)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_17)

        self.bar_value_label_line = QLineEdit(Form)
        self.bar_value_label_line.setObjectName(u"bar_value_label_line")
        self.bar_value_label_line.setEnabled(False)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.bar_value_label_line)

        self.label_26 = QLabel(Form)
        self.label_26.setObjectName(u"label_26")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_26)

        self.bar_value_label_interval_spin = QDoubleSpinBox(Form)
        self.bar_value_label_interval_spin.setObjectName(u"bar_value_label_interval_spin")
        self.bar_value_label_interval_spin.setEnabled(False)
        self.bar_value_label_interval_spin.setDecimals(2)
        self.bar_value_label_interval_spin.setMaximum(100.000000000000000)
        self.bar_value_label_interval_spin.setValue(3.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.bar_value_label_interval_spin)

        self.label_28 = QLabel(Form)
        self.label_28.setObjectName(u"label_28")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_28)

        self.bar_value_label_color_btn = QToolButton(Form)
        self.bar_value_label_color_btn.setObjectName(u"bar_value_label_color_btn")
        self.bar_value_label_color_btn.setEnabled(False)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.bar_value_label_color_btn)

        self.label_29 = QLabel(Form)
        self.label_29.setObjectName(u"label_29")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_29)

        self.bar_value_label_size_spin = QSpinBox(Form)
        self.bar_value_label_size_spin.setObjectName(u"bar_value_label_size_spin")
        self.bar_value_label_size_spin.setEnabled(False)
        self.bar_value_label_size_spin.setValue(9)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.bar_value_label_size_spin)

        self.label_27 = QLabel(Form)
        self.label_27.setObjectName(u"label_27")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_27)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"selectedChart", None))
        self.bar_selector_combo.setItemText(0, QCoreApplication.translate("Form", u"grouped", None))
        self.bar_selector_combo.setItemText(1, QCoreApplication.translate("Form", u"stacked", None))
        self.bar_selector_combo.setItemText(2, QCoreApplication.translate("Form", u"proportion", None))

        self.label.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.y_series_label_2.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"ColorSeries", None))
        self.base_chart_color_series_btn.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Interval", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"ErrorDataSeries", None))
        self.err_bar_color_btn.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"ErrorBarColor", None))
        self.bar_value_label_check.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"AddValueLabel", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"ValueLabelSeries", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"ValueLabelInterval", None))
        self.bar_value_label_color_btn.setText("")
        self.label_29.setText(QCoreApplication.translate("Form", u"ValueLabelColor", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"ValueLabelSize", None))
    # retranslateUi

