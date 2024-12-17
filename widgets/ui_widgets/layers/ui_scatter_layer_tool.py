# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scatterLayerToolUIWEIXMJ.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)
import resources_rc
from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox
from widgets.inherited_widgets.editable_exclusive_combo_box_widget import EditableExclusiveComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(359, 709)
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
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.y_series_combo = CheckableComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.y_series_combo)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.data_label_line)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.scatter_size_combo = EditableExclusiveComboBox(Form)
        self.scatter_size_combo.setObjectName(u"scatter_size_combo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.scatter_size_combo)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.scatter_size_base_spin = QSpinBox(Form)
        self.scatter_size_base_spin.setObjectName(u"scatter_size_base_spin")
        self.scatter_size_base_spin.setMaximum(1000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.scatter_size_base_spin)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(10, QFormLayout.FieldRole, self.verticalSpacer)

        self.scatter_marker_type_combo = QComboBox(Form)
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.addItem("")
        self.scatter_marker_type_combo.setObjectName(u"scatter_marker_type_combo")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.scatter_marker_type_combo)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.scatter_color_combo = EditableExclusiveComboBox(Form)
        self.scatter_color_combo.setObjectName(u"scatter_color_combo")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.scatter_color_combo)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.scatter_edge_color_combo = QComboBox(Form)
        self.scatter_edge_color_combo.addItem("")
        self.scatter_edge_color_combo.addItem("")
        self.scatter_edge_color_combo.setObjectName(u"scatter_edge_color_combo")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.scatter_edge_color_combo)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.scatter_linewidth_spin = QSpinBox(Form)
        self.scatter_linewidth_spin.setObjectName(u"scatter_linewidth_spin")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.scatter_linewidth_spin)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.scatter_transparent_slider = QSlider(Form)
        self.scatter_transparent_slider.setObjectName(u"scatter_transparent_slider")
        self.scatter_transparent_slider.setMaximum(100)
        self.scatter_transparent_slider.setValue(100)
        self.scatter_transparent_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.scatter_transparent_slider)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.scatter_colorbar_check = QCheckBox(Form)
        self.scatter_colorbar_check.setObjectName(u"scatter_colorbar_check")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.scatter_colorbar_check)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_10)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Scatter Layer", None))
        self.toolButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Size", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"SizeBase", None))
        self.scatter_marker_type_combo.setItemText(0, QCoreApplication.translate("Form", u"o", None))
        self.scatter_marker_type_combo.setItemText(1, QCoreApplication.translate("Form", u"*", None))
        self.scatter_marker_type_combo.setItemText(2, QCoreApplication.translate("Form", u".", None))
        self.scatter_marker_type_combo.setItemText(3, QCoreApplication.translate("Form", u"s", None))
        self.scatter_marker_type_combo.setItemText(4, QCoreApplication.translate("Form", u"d", None))
        self.scatter_marker_type_combo.setItemText(5, QCoreApplication.translate("Form", u"D", None))
        self.scatter_marker_type_combo.setItemText(6, QCoreApplication.translate("Form", u"^", None))
        self.scatter_marker_type_combo.setItemText(7, QCoreApplication.translate("Form", u"v", None))
        self.scatter_marker_type_combo.setItemText(8, QCoreApplication.translate("Form", u">", None))
        self.scatter_marker_type_combo.setItemText(9, QCoreApplication.translate("Form", u"<", None))
        self.scatter_marker_type_combo.setItemText(10, QCoreApplication.translate("Form", u"p", None))
        self.scatter_marker_type_combo.setItemText(11, QCoreApplication.translate("Form", u"P", None))
        self.scatter_marker_type_combo.setItemText(12, QCoreApplication.translate("Form", u"h", None))
        self.scatter_marker_type_combo.setItemText(13, QCoreApplication.translate("Form", u"H", None))
        self.scatter_marker_type_combo.setItemText(14, QCoreApplication.translate("Form", u"none", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"Marker", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Color", None))
        self.scatter_edge_color_combo.setItemText(0, QCoreApplication.translate("Form", u"none", None))
        self.scatter_edge_color_combo.setItemText(1, QCoreApplication.translate("Form", u"face", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"EdgeColor", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"EdgeLineWidth", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Transparency", None))
        self.scatter_colorbar_check.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"AddColorBar", None))
    # retranslateUi

