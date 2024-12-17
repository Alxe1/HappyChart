# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotationLayerToolUInuYCTQ.ui'
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
    QDoubleSpinBox, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSlider,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(273, 812)
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
        self.y_series_label = QLabel(Form)
        self.y_series_label.setObjectName(u"y_series_label")
        self.y_series_label.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.y_series_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.x_pos_spin = QDoubleSpinBox(Form)
        self.x_pos_spin.setObjectName(u"x_pos_spin")
        self.x_pos_spin.setMaximumSize(QSize(53, 16777215))
        self.x_pos_spin.setMinimum(-1000000.000000000000000)
        self.x_pos_spin.setMaximum(1000000.000000000000000)
        self.x_pos_spin.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.x_pos_spin)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(25, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.y_pos_spin = QDoubleSpinBox(Form)
        self.y_pos_spin.setObjectName(u"y_pos_spin")
        self.y_pos_spin.setMaximumSize(QSize(53, 16777215))
        self.y_pos_spin.setMinimum(-1000000.000000000000000)
        self.y_pos_spin.setMaximum(1000000.000000000000000)
        self.y_pos_spin.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.y_pos_spin)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.x_text_pos_spin = QDoubleSpinBox(Form)
        self.x_text_pos_spin.setObjectName(u"x_text_pos_spin")
        self.x_text_pos_spin.setMinimumSize(QSize(0, 0))
        self.x_text_pos_spin.setMaximumSize(QSize(53, 16777215))
        self.x_text_pos_spin.setMinimum(-1000000.000000000000000)
        self.x_text_pos_spin.setMaximum(1000000.000000000000000)
        self.x_text_pos_spin.setSingleStep(0.010000000000000)

        self.horizontalLayout_3.addWidget(self.x_text_pos_spin)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(25, 16777215))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.y_text_pos_spin = QDoubleSpinBox(Form)
        self.y_text_pos_spin.setObjectName(u"y_text_pos_spin")
        self.y_text_pos_spin.setMaximumSize(QSize(53, 16777215))
        self.y_text_pos_spin.setMinimum(-1000000.000000000000000)
        self.y_text_pos_spin.setMaximum(1000000.000000000000000)
        self.y_text_pos_spin.setSingleStep(0.010000000000000)

        self.horizontalLayout_3.addWidget(self.y_text_pos_spin)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.text_line = QLineEdit(Form)
        self.text_line.setObjectName(u"text_line")
        self.text_line.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.text_line)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.text_color_btn = QToolButton(Form)
        self.text_color_btn.setObjectName(u"text_color_btn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.text_color_btn)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.font_size_spin = QDoubleSpinBox(Form)
        self.font_size_spin.setObjectName(u"font_size_spin")
        self.font_size_spin.setMaximum(10000.000000000000000)
        self.font_size_spin.setSingleStep(0.100000000000000)
        self.font_size_spin.setValue(10.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.font_size_spin)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.background_color_btn = QToolButton(Form)
        self.background_color_btn.setObjectName(u"background_color_btn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.background_color_btn)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.rotation_dial = QDial(Form)
        self.rotation_dial.setObjectName(u"rotation_dial")
        self.rotation_dial.setMaximumSize(QSize(50, 50))
        self.rotation_dial.setMaximum(360)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.rotation_dial)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.annotation_clip_check = QCheckBox(Form)
        self.annotation_clip_check.setObjectName(u"annotation_clip_check")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.annotation_clip_check)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.arrow_style_combo = QComboBox(Form)
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.addItem("")
        self.arrow_style_combo.setObjectName(u"arrow_style_combo")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.arrow_style_combo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_2)

        self.connection_style_combo = QComboBox(Form)
        self.connection_style_combo.addItem("")
        self.connection_style_combo.addItem("")
        self.connection_style_combo.addItem("")
        self.connection_style_combo.addItem("")
        self.connection_style_combo.addItem("")
        self.connection_style_combo.setObjectName(u"connection_style_combo")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.connection_style_combo)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_13)

        self.shrink_a_spin = QDoubleSpinBox(Form)
        self.shrink_a_spin.setObjectName(u"shrink_a_spin")
        self.shrink_a_spin.setMaximum(1000.000000000000000)
        self.shrink_a_spin.setSingleStep(0.010000000000000)
        self.shrink_a_spin.setValue(2.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.shrink_a_spin)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_14)

        self.shrink_b_spin = QDoubleSpinBox(Form)
        self.shrink_b_spin.setObjectName(u"shrink_b_spin")
        self.shrink_b_spin.setMaximum(1000.000000000000000)
        self.shrink_b_spin.setSingleStep(0.010000000000000)
        self.shrink_b_spin.setValue(2.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.shrink_b_spin)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_15)

        self.arrow_color_btn = QToolButton(Form)
        self.arrow_color_btn.setObjectName(u"arrow_color_btn")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.arrow_color_btn)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_16)

        self.transparency_slider = QSlider(Form)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMaximum(100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.transparency_slider)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(14, QFormLayout.FieldRole, self.verticalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Annotation Layer", None))
        self.toolButton.setText("")
        self.y_series_label.setText(QCoreApplication.translate("Form", u"XYPosition", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"XYTextPosition", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u2014", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Text", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextColor", None))
        self.text_color_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"FontSize", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"BackgroundColor", None))
        self.background_color_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Rotation", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"AnnotationClip", None))
        self.annotation_clip_check.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"ArrowStyle", None))
        self.arrow_style_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.arrow_style_combo.setItemText(1, QCoreApplication.translate("Form", u"->", None))
        self.arrow_style_combo.setItemText(2, QCoreApplication.translate("Form", u"-[", None))
        self.arrow_style_combo.setItemText(3, QCoreApplication.translate("Form", u"-|>", None))
        self.arrow_style_combo.setItemText(4, QCoreApplication.translate("Form", u"<-", None))
        self.arrow_style_combo.setItemText(5, QCoreApplication.translate("Form", u"<->", None))
        self.arrow_style_combo.setItemText(6, QCoreApplication.translate("Form", u"<|-", None))
        self.arrow_style_combo.setItemText(7, QCoreApplication.translate("Form", u"<|-|>", None))
        self.arrow_style_combo.setItemText(8, QCoreApplication.translate("Form", u"]-", None))
        self.arrow_style_combo.setItemText(9, QCoreApplication.translate("Form", u"]-[", None))
        self.arrow_style_combo.setItemText(10, QCoreApplication.translate("Form", u"|-|", None))
        self.arrow_style_combo.setItemText(11, QCoreApplication.translate("Form", u"fancy", None))
        self.arrow_style_combo.setItemText(12, QCoreApplication.translate("Form", u"simple", None))
        self.arrow_style_combo.setItemText(13, QCoreApplication.translate("Form", u"wedge", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"ConnectionStyle", None))
        self.connection_style_combo.setItemText(0, QCoreApplication.translate("Form", u"arc3", None))
        self.connection_style_combo.setItemText(1, QCoreApplication.translate("Form", u"angle3", None))
        self.connection_style_combo.setItemText(2, QCoreApplication.translate("Form", u"angle", None))
        self.connection_style_combo.setItemText(3, QCoreApplication.translate("Form", u"arc", None))
        self.connection_style_combo.setItemText(4, QCoreApplication.translate("Form", u"bar", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"ShrinkA", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"ShrinkB", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"ArrowColor", None))
        self.arrow_color_btn.setText("")
        self.label_16.setText(QCoreApplication.translate("Form", u"Transparency", None))
    # retranslateUi

