# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'histgramChartToolUIoGljCr.ui'
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
    QFormLayout, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(315, 584)
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

        self.y_series_combo = CheckableComboBox(Form)
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

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.bin_num_spin = QSpinBox(Form)
        self.bin_num_spin.setObjectName(u"bin_num_spin")
        self.bin_num_spin.setMaximumSize(QSize(16777215, 16777215))
        self.bin_num_spin.setMinimum(1)
        self.bin_num_spin.setMaximum(1000000)
        self.bin_num_spin.setValue(10)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.bin_num_spin)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(146, 30))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bin_range_min_spin = QSpinBox(self.frame)
        self.bin_range_min_spin.setObjectName(u"bin_range_min_spin")
        self.bin_range_min_spin.setMinimum(-1000000)
        self.bin_range_min_spin.setMaximum(1000000)

        self.gridLayout.addWidget(self.bin_range_min_spin, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.bin_range_max_spin = QSpinBox(self.frame)
        self.bin_range_max_spin.setObjectName(u"bin_range_max_spin")
        self.bin_range_max_spin.setMinimum(-1000000)
        self.bin_range_max_spin.setMaximum(1000000)

        self.gridLayout.addWidget(self.bin_range_max_spin, 0, 2, 1, 1)


        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.frame)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.bihist_check = QCheckBox(Form)
        self.bihist_check.setObjectName(u"bihist_check")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.bihist_check)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.density_check = QCheckBox(Form)
        self.density_check.setObjectName(u"density_check")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.density_check)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_4)

        self.cumulative_check = QCheckBox(Form)
        self.cumulative_check.setObjectName(u"cumulative_check")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.cumulative_check)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_13)

        self.log_check = QCheckBox(Form)
        self.log_check.setObjectName(u"log_check")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.log_check)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_5)

        self.bottom_distance_spin = QDoubleSpinBox(Form)
        self.bottom_distance_spin.setObjectName(u"bottom_distance_spin")
        self.bottom_distance_spin.setMaximum(1000000.000000000000000)
        self.bottom_distance_spin.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.bottom_distance_spin)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 21))

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_11)

        self.hist_type_combo = QComboBox(Form)
        self.hist_type_combo.addItem("")
        self.hist_type_combo.addItem("")
        self.hist_type_combo.addItem("")
        self.hist_type_combo.addItem("")
        self.hist_type_combo.setObjectName(u"hist_type_combo")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.hist_type_combo)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_6)

        self.align_combo = QComboBox(Form)
        self.align_combo.addItem("")
        self.align_combo.addItem("")
        self.align_combo.addItem("")
        self.align_combo.setObjectName(u"align_combo")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.align_combo)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_12)

        self.orientation_combo = QComboBox(Form)
        self.orientation_combo.addItem("")
        self.orientation_combo.addItem("")
        self.orientation_combo.setObjectName(u"orientation_combo")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.orientation_combo)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_14)

        self.color_series_btn = QToolButton(Form)
        self.color_series_btn.setObjectName(u"color_series_btn")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.color_series_btn)

        self.color_series_line = QLineEdit(Form)
        self.color_series_line.setObjectName(u"color_series_line")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.color_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(17, QFormLayout.FieldRole, self.verticalSpacer)

        self.stacked_check = QCheckBox(Form)
        self.stacked_check.setObjectName(u"stacked_check")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.stacked_check)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_15)

        self.transparent_slider = QSlider(Form)
        self.transparent_slider.setObjectName(u"transparent_slider")
        self.transparent_slider.setMaximum(100)
        self.transparent_slider.setValue(100)
        self.transparent_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.transparent_slider)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_9)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"BinNumber", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"BinRange", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u2014\u2014", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Bihistogram", None))
        self.bihist_check.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Density", None))
        self.density_check.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Cumulative", None))
        self.cumulative_check.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Log", None))
        self.log_check.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"BottomDistance", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"HistType", None))
        self.hist_type_combo.setItemText(0, QCoreApplication.translate("Form", u"bar", None))
        self.hist_type_combo.setItemText(1, QCoreApplication.translate("Form", u"barstacked", None))
        self.hist_type_combo.setItemText(2, QCoreApplication.translate("Form", u"step", None))
        self.hist_type_combo.setItemText(3, QCoreApplication.translate("Form", u"stepfilled", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"Align", None))
        self.align_combo.setItemText(0, QCoreApplication.translate("Form", u"mid", None))
        self.align_combo.setItemText(1, QCoreApplication.translate("Form", u"left", None))
        self.align_combo.setItemText(2, QCoreApplication.translate("Form", u"right", None))

        self.label_12.setText(QCoreApplication.translate("Form", u"Orientation", None))
        self.orientation_combo.setItemText(0, QCoreApplication.translate("Form", u"vertical", None))
        self.orientation_combo.setItemText(1, QCoreApplication.translate("Form", u"horizontal", None))

        self.label_14.setText(QCoreApplication.translate("Form", u"ColorSeries", None))
        self.color_series_btn.setText("")
        self.stacked_check.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"Stacked", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Transparency", None))
    # retranslateUi

