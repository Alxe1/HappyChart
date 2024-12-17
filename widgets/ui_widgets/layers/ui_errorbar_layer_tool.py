# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorbarLayerToolUIOdDRbV.ui'
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
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)
import resources_rc
from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 1020)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"border-radius: 10px;")
        icon = QIcon()
        icon.addFile(u":/icon/icons/minus-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.y_series_label = QLabel(Form)
        self.y_series_label.setObjectName(u"y_series_label")
        self.y_series_label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.y_series_label)

        self.y_series_combo = CheckableComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")
        self.y_series_combo.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.y_series_combo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(22, QFormLayout.FieldRole, self.verticalSpacer)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")
        self.data_label_line.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.data_label_line)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_24)

        self.x_err_series_combo = QComboBox(Form)
        self.x_err_series_combo.setObjectName(u"x_err_series_combo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.x_err_series_combo)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.y_err_series_combo = QComboBox(Form)
        self.y_err_series_combo.setObjectName(u"y_err_series_combo")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.y_err_series_combo)

        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_25)

        self.color_series_btn = QToolButton(Form)
        self.color_series_btn.setObjectName(u"color_series_btn")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.color_series_btn)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_33)

        self.color_series_line = QLineEdit(Form)
        self.color_series_line.setObjectName(u"color_series_line")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.color_series_line)

        self.err_line_width_spin = QDoubleSpinBox(Form)
        self.err_line_width_spin.setObjectName(u"err_line_width_spin")
        self.err_line_width_spin.setMinimum(0.010000000000000)
        self.err_line_width_spin.setSingleStep(0.100000000000000)
        self.err_line_width_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.err_line_width_spin)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.err_every_spin = QSpinBox(Form)
        self.err_every_spin.setObjectName(u"err_every_spin")
        self.err_every_spin.setMinimum(1)
        self.err_every_spin.setMaximum(10000)
        self.err_every_spin.setValue(1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.err_every_spin)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.cap_size_spin = QDoubleSpinBox(Form)
        self.cap_size_spin.setObjectName(u"cap_size_spin")
        self.cap_size_spin.setMinimum(0.010000000000000)
        self.cap_size_spin.setSingleStep(0.100000000000000)
        self.cap_size_spin.setValue(4.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.cap_size_spin)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_5)

        self.marker_combo = QComboBox(Form)
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.addItem("")
        self.marker_combo.setObjectName(u"marker_combo")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.marker_combo)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label)

        self.marker_size_spin = QDoubleSpinBox(Form)
        self.marker_size_spin.setObjectName(u"marker_size_spin")
        self.marker_size_spin.setSingleStep(0.100000000000000)
        self.marker_size_spin.setValue(9.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.marker_size_spin)

        self.label_43 = QLabel(Form)
        self.label_43.setObjectName(u"label_43")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_43)

        self.marker_edge_width_spin = QDoubleSpinBox(Form)
        self.marker_edge_width_spin.setObjectName(u"marker_edge_width_spin")
        self.marker_edge_width_spin.setSingleStep(0.100000000000000)
        self.marker_edge_width_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.marker_edge_width_spin)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_8)

        self.marker_edge_color_btn = QToolButton(Form)
        self.marker_edge_color_btn.setObjectName(u"marker_edge_color_btn")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.marker_edge_color_btn)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_9)

        self.marker_face_color_btn = QToolButton(Form)
        self.marker_face_color_btn.setObjectName(u"marker_face_color_btn")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.marker_face_color_btn)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_10)

        self.linestyle_combo = QComboBox(Form)
        self.linestyle_combo.addItem("")
        self.linestyle_combo.addItem("")
        self.linestyle_combo.addItem("")
        self.linestyle_combo.addItem("")
        self.linestyle_combo.setObjectName(u"linestyle_combo")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.linestyle_combo)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_7)

        self.line_color_btn = QToolButton(Form)
        self.line_color_btn.setObjectName(u"line_color_btn")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.line_color_btn)

        self.label_44 = QLabel(Form)
        self.label_44.setObjectName(u"label_44")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_44)

        self.line_color_line = QLineEdit(Form)
        self.line_color_line.setObjectName(u"line_color_line")

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.line_color_line)

        self.bars_above_check = QCheckBox(Form)
        self.bars_above_check.setObjectName(u"bars_above_check")

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.bars_above_check)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_11)

        self.lower_limits_check = QCheckBox(Form)
        self.lower_limits_check.setObjectName(u"lower_limits_check")

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.lower_limits_check)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_12)

        self.upper_limits_check = QCheckBox(Form)
        self.upper_limits_check.setObjectName(u"upper_limits_check")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.upper_limits_check)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_13)

        self.xlower_limits_check = QCheckBox(Form)
        self.xlower_limits_check.setObjectName(u"xlower_limits_check")

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.xlower_limits_check)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_14)

        self.xupper_limits_check = QCheckBox(Form)
        self.xupper_limits_check.setObjectName(u"xupper_limits_check")

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.xupper_limits_check)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_15)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ErrorBar Layer", None))
        self.toolButton.setText("")
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"XErrorSeries", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"YErrorSeries", None))
        self.color_series_btn.setText("")
        self.label_33.setText(QCoreApplication.translate("Form", u"ErrorColorSeries", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ErrorLineWidth", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"ErrorEvery", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"CapSize", None))
        self.marker_combo.setItemText(0, QCoreApplication.translate("Form", u".", None))
        self.marker_combo.setItemText(1, QCoreApplication.translate("Form", u"v", None))
        self.marker_combo.setItemText(2, QCoreApplication.translate("Form", u"o", None))
        self.marker_combo.setItemText(3, QCoreApplication.translate("Form", u"^", None))
        self.marker_combo.setItemText(4, QCoreApplication.translate("Form", u"<", None))
        self.marker_combo.setItemText(5, QCoreApplication.translate("Form", u">", None))
        self.marker_combo.setItemText(6, QCoreApplication.translate("Form", u"1", None))
        self.marker_combo.setItemText(7, QCoreApplication.translate("Form", u"2", None))
        self.marker_combo.setItemText(8, QCoreApplication.translate("Form", u"3", None))
        self.marker_combo.setItemText(9, QCoreApplication.translate("Form", u"4", None))
        self.marker_combo.setItemText(10, QCoreApplication.translate("Form", u"8", None))
        self.marker_combo.setItemText(11, QCoreApplication.translate("Form", u"s", None))
        self.marker_combo.setItemText(12, QCoreApplication.translate("Form", u"p", None))
        self.marker_combo.setItemText(13, QCoreApplication.translate("Form", u"P", None))
        self.marker_combo.setItemText(14, QCoreApplication.translate("Form", u"*", None))
        self.marker_combo.setItemText(15, QCoreApplication.translate("Form", u"h", None))
        self.marker_combo.setItemText(16, QCoreApplication.translate("Form", u"H", None))
        self.marker_combo.setItemText(17, QCoreApplication.translate("Form", u"+", None))
        self.marker_combo.setItemText(18, QCoreApplication.translate("Form", u"x", None))
        self.marker_combo.setItemText(19, QCoreApplication.translate("Form", u"X", None))
        self.marker_combo.setItemText(20, QCoreApplication.translate("Form", u"D", None))
        self.marker_combo.setItemText(21, QCoreApplication.translate("Form", u"d", None))
        self.marker_combo.setItemText(22, QCoreApplication.translate("Form", u"|", None))
        self.marker_combo.setItemText(23, QCoreApplication.translate("Form", u"_", None))
        self.marker_combo.setItemText(24, QCoreApplication.translate("Form", u"none", None))

        self.label.setText(QCoreApplication.translate("Form", u"Marker", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"MarkerSize", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"MarkerEdgeWidth", None))
        self.marker_edge_color_btn.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"MarkerEdgeColor", None))
        self.marker_face_color_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"MarkerFaceColor", None))
        self.linestyle_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.linestyle_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.linestyle_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.linestyle_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"LineStyle", None))
        self.line_color_btn.setText("")
        self.label_44.setText(QCoreApplication.translate("Form", u"LineColorSeries", None))
        self.bars_above_check.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"BarsAbove", None))
        self.lower_limits_check.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"LowerLimits", None))
        self.upper_limits_check.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"UpperLimits", None))
        self.xlower_limits_check.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"XLowerLimits", None))
        self.xupper_limits_check.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"XUpperLimits", None))
    # retranslateUi

