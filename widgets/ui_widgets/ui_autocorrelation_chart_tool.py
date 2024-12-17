# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autocorrelationChartToolUItaAHHU.ui'
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
    QFormLayout, QLabel, QSizePolicy, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(314, 534)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.x_series_combo = QComboBox(Form)
        self.x_series_combo.setObjectName(u"x_series_combo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_series_combo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.y_series_combo = QComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y_series_combo)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.use_vline_check = QCheckBox(Form)
        self.use_vline_check.setObjectName(u"use_vline_check")
        self.use_vline_check.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.use_vline_check)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.vline_color_btn = QToolButton(Form)
        self.vline_color_btn.setObjectName(u"vline_color_btn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.vline_color_btn)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.vline_style_combo = QComboBox(Form)
        self.vline_style_combo.addItem("")
        self.vline_style_combo.addItem("")
        self.vline_style_combo.addItem("")
        self.vline_style_combo.addItem("")
        self.vline_style_combo.setObjectName(u"vline_style_combo")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.vline_style_combo)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.vline_width_spin = QDoubleSpinBox(Form)
        self.vline_width_spin.setObjectName(u"vline_width_spin")
        self.vline_width_spin.setMinimum(0.010000000000000)
        self.vline_width_spin.setMaximum(100.000000000000000)
        self.vline_width_spin.setSingleStep(0.100000000000000)
        self.vline_width_spin.setValue(2.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.vline_width_spin)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_7)

        self.norm_check = QCheckBox(Form)
        self.norm_check.setObjectName(u"norm_check")
        self.norm_check.setChecked(True)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.norm_check)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_8)

        self.max_lag_spin = QSpinBox(Form)
        self.max_lag_spin.setObjectName(u"max_lag_spin")
        self.max_lag_spin.setMaximum(1000)
        self.max_lag_spin.setValue(1)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.max_lag_spin)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.hline_color_btn = QToolButton(Form)
        self.hline_color_btn.setObjectName(u"hline_color_btn")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.hline_color_btn)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_10)

        self.hline_style_combo = QComboBox(Form)
        self.hline_style_combo.addItem("")
        self.hline_style_combo.addItem("")
        self.hline_style_combo.addItem("")
        self.hline_style_combo.addItem("")
        self.hline_style_combo.setObjectName(u"hline_style_combo")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.hline_style_combo)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_11)

        self.hline_width_spin = QDoubleSpinBox(Form)
        self.hline_width_spin.setObjectName(u"hline_width_spin")
        self.hline_width_spin.setMinimum(0.010000000000000)
        self.hline_width_spin.setMaximum(100.000000000000000)
        self.hline_width_spin.setSingleStep(0.100000000000000)
        self.hline_width_spin.setValue(2.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.hline_width_spin)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"UseVlines", None))
        self.use_vline_check.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"VLineColor", None))
        self.vline_color_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"VLineStyle", None))
        self.vline_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.vline_style_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.vline_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.vline_style_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"VLineWidth", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Normalization", None))
        self.norm_check.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"MaxLags", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"HLineColor", None))
        self.hline_color_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"HLineStyle", None))
        self.hline_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.hline_style_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.hline_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.hline_style_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_11.setText(QCoreApplication.translate("Form", u"HLineWidth", None))
    # retranslateUi

