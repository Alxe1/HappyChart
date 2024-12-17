# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vhlineLayerToolUIiAFzOx.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSlider, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 644)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

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
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.line_type_combo = QComboBox(Form)
        self.line_type_combo.addItem("")
        self.line_type_combo.addItem("")
        self.line_type_combo.setObjectName(u"line_type_combo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_type_combo)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.data_label_line)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.position_spin = QDoubleSpinBox(Form)
        self.position_spin.setObjectName(u"position_spin")
        self.position_spin.setMinimum(-1000000.000000000000000)
        self.position_spin.setMaximum(1000000.000000000000000)
        self.position_spin.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.position_spin)

        self.y_series_label = QLabel(Form)
        self.y_series_label.setObjectName(u"y_series_label")
        self.y_series_label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.y_series_label)

        self.min_value_spin = QDoubleSpinBox(Form)
        self.min_value_spin.setObjectName(u"min_value_spin")
        self.min_value_spin.setMinimum(-1000000.000000000000000)
        self.min_value_spin.setMaximum(1000000.000000000000000)
        self.min_value_spin.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.min_value_spin)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.max_value_spin = QDoubleSpinBox(Form)
        self.max_value_spin.setObjectName(u"max_value_spin")
        self.max_value_spin.setMinimum(-1000000.000000000000000)
        self.max_value_spin.setMaximum(1000000.000000000000000)
        self.max_value_spin.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.max_value_spin)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_33)

        self.color_btn = QToolButton(Form)
        self.color_btn.setObjectName(u"color_btn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.color_btn)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_2)

        self.line_style_combo = QComboBox(Form)
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.addItem("")
        self.line_style_combo.setObjectName(u"line_style_combo")
        self.line_style_combo.setFrame(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.line_style_combo)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.line_width_spin = QDoubleSpinBox(Form)
        self.line_width_spin.setObjectName(u"line_width_spin")
        self.line_width_spin.setMaximum(100.000000000000000)
        self.line_width_spin.setSingleStep(0.100000000000000)
        self.line_width_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.line_width_spin)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_16)

        self.transparency_slider = QSlider(Form)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMaximum(100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.transparency_slider)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(9, QFormLayout.FieldRole, self.verticalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"VHLine Layer", None))
        self.toolButton.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"LineTyle", None))
        self.line_type_combo.setItemText(0, QCoreApplication.translate("Form", u"vertical", None))
        self.line_type_combo.setItemText(1, QCoreApplication.translate("Form", u"horizontal", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"DataLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Position", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"MinValue", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"MaxValue", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Color", None))
        self.color_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"LineStyle", None))
        self.line_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.line_style_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.line_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.line_style_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"LineWidth", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Transparency", None))
    # retranslateUi

