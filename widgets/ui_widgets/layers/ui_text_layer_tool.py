# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textLayerToolUIaZUMCH.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QDoubleSpinBox,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSlider, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 630)
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
        self.y_series_label = QLabel(Form)
        self.y_series_label.setObjectName(u"y_series_label")
        self.y_series_label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.y_series_label)

        self.x_pos_spin = QDoubleSpinBox(Form)
        self.x_pos_spin.setObjectName(u"x_pos_spin")
        self.x_pos_spin.setMinimum(-1000000.000000000000000)
        self.x_pos_spin.setMaximum(1000000.000000000000000)
        self.x_pos_spin.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.x_pos_spin)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.y_pos_spin = QDoubleSpinBox(Form)
        self.y_pos_spin.setObjectName(u"y_pos_spin")
        self.y_pos_spin.setMinimum(-1000000.000000000000000)
        self.y_pos_spin.setMaximum(1000000.000000000000000)
        self.y_pos_spin.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y_pos_spin)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.text_line = QLineEdit(Form)
        self.text_line.setObjectName(u"text_line")
        self.text_line.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.text_line)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.font_size_spin = QDoubleSpinBox(Form)
        self.font_size_spin.setObjectName(u"font_size_spin")
        self.font_size_spin.setMaximum(10000.000000000000000)
        self.font_size_spin.setSingleStep(0.100000000000000)
        self.font_size_spin.setValue(20.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.font_size_spin)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.font_color_btn = QToolButton(Form)
        self.font_color_btn.setObjectName(u"font_color_btn")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.font_color_btn)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.background_color_btn = QToolButton(Form)
        self.background_color_btn.setObjectName(u"background_color_btn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.background_color_btn)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.horizontal_align_combo = QComboBox(Form)
        self.horizontal_align_combo.addItem("")
        self.horizontal_align_combo.addItem("")
        self.horizontal_align_combo.addItem("")
        self.horizontal_align_combo.setObjectName(u"horizontal_align_combo")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.horizontal_align_combo)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.vertical_align_combo = QComboBox(Form)
        self.vertical_align_combo.addItem("")
        self.vertical_align_combo.addItem("")
        self.vertical_align_combo.addItem("")
        self.vertical_align_combo.addItem("")
        self.vertical_align_combo.addItem("")
        self.vertical_align_combo.setObjectName(u"vertical_align_combo")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.vertical_align_combo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_2)

        self.multi_align_combo = QComboBox(Form)
        self.multi_align_combo.addItem("")
        self.multi_align_combo.addItem("")
        self.multi_align_combo.addItem("")
        self.multi_align_combo.setObjectName(u"multi_align_combo")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.multi_align_combo)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_5)

        self.rotation_dial = QDial(Form)
        self.rotation_dial.setObjectName(u"rotation_dial")
        self.rotation_dial.setMaximumSize(QSize(50, 50))
        self.rotation_dial.setMaximum(360)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.rotation_dial)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_16)

        self.transparency_slider = QSlider(Form)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMaximum(100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.transparency_slider)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(11, QFormLayout.FieldRole, self.verticalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Text Layer", None))
        self.toolButton.setText("")
        self.y_series_label.setText(QCoreApplication.translate("Form", u"XPosition", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"YPosition", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Text", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"FontSize", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"FontColor", None))
        self.font_color_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"BackgroundColor", None))
        self.background_color_btn.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"HorizontalAlign", None))
        self.horizontal_align_combo.setItemText(0, QCoreApplication.translate("Form", u"left", None))
        self.horizontal_align_combo.setItemText(1, QCoreApplication.translate("Form", u"center", None))
        self.horizontal_align_combo.setItemText(2, QCoreApplication.translate("Form", u"right", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"VerticalAlign", None))
        self.vertical_align_combo.setItemText(0, QCoreApplication.translate("Form", u"baseline", None))
        self.vertical_align_combo.setItemText(1, QCoreApplication.translate("Form", u"bottom", None))
        self.vertical_align_combo.setItemText(2, QCoreApplication.translate("Form", u"center", None))
        self.vertical_align_combo.setItemText(3, QCoreApplication.translate("Form", u"center_baseline", None))
        self.vertical_align_combo.setItemText(4, QCoreApplication.translate("Form", u"top", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"MultiAlign", None))
        self.multi_align_combo.setItemText(0, QCoreApplication.translate("Form", u"left", None))
        self.multi_align_combo.setItemText(1, QCoreApplication.translate("Form", u"right", None))
        self.multi_align_combo.setItemText(2, QCoreApplication.translate("Form", u"center", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"Rotation", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Transparency", None))
    # retranslateUi

