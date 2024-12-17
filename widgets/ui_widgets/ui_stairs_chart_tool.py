# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stairsChartToolUIjdetDZ.ui'
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
    QSlider, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 644)
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

        self.y_series_combo = CheckableComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y_series_combo)

        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_18)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_label_line)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.base_line_spin = QDoubleSpinBox(Form)
        self.base_line_spin.setObjectName(u"base_line_spin")
        self.base_line_spin.setMaximum(100000.000000000000000)
        self.base_line_spin.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.base_line_spin)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.line_width_spin = QDoubleSpinBox(Form)
        self.line_width_spin.setObjectName(u"line_width_spin")
        self.line_width_spin.setMaximum(100.000000000000000)
        self.line_width_spin.setSingleStep(0.100000000000000)
        self.line_width_spin.setValue(2.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.line_width_spin)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.line_style_combo = QComboBox(Form)
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.setObjectName(u"line_style_combo")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.line_style_combo)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_4)

        self.fill_color_check = QCheckBox(Form)
        self.fill_color_check.setObjectName(u"fill_color_check")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.fill_color_check)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_14)

        self.edge_color_series_btn = QToolButton(Form)
        self.edge_color_series_btn.setObjectName(u"edge_color_series_btn")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.edge_color_series_btn)

        self.edge_color_series_line = QLineEdit(Form)
        self.edge_color_series_line.setObjectName(u"edge_color_series_line")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.edge_color_series_line)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_15)

        self.face_color_series_btn = QToolButton(Form)
        self.face_color_series_btn.setObjectName(u"face_color_series_btn")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.face_color_series_btn)

        self.face_color_series_line = QLineEdit(Form)
        self.face_color_series_line.setObjectName(u"face_color_series_line")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.face_color_series_line)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_16)

        self.transparency_slider = QSlider(Form)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMaximum(100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.transparency_slider)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_17)

        self.hatch_series_line = QLineEdit(Form)
        self.hatch_series_line.setObjectName(u"hatch_series_line")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.hatch_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(14, QFormLayout.FieldRole, self.verticalSpacer)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.orientation_combo = QComboBox(Form)
        self.orientation_combo.addItem("")
        self.orientation_combo.addItem("")
        self.orientation_combo.setObjectName(u"orientation_combo")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.orientation_combo)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"BaseLine", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"LineWidth", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"LineStyle", None))
        self.line_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.line_style_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.line_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.line_style_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"FillColor", None))
        self.fill_color_check.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"EdgeColorSeries", None))
        self.edge_color_series_btn.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"FaceColorSeries", None))
        self.face_color_series_btn.setText("")
        self.label_16.setText(QCoreApplication.translate("Form", u"Transparency", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"HatchSeries", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Orientation", None))
        self.orientation_combo.setItemText(0, QCoreApplication.translate("Form", u"vertical", None))
        self.orientation_combo.setItemText(1, QCoreApplication.translate("Form", u"horizontal", None))

    # retranslateUi

