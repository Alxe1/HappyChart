# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'areaChartToolUIgTeypN.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QSizePolicy, QSlider, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(333, 598)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.x_series_label = QLabel(Form)
        self.x_series_label.setObjectName(u"x_series_label")

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

        self.area_color_series_btn = QToolButton(Form)
        self.area_color_series_btn.setObjectName(u"area_color_series_btn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.area_color_series_btn)

        self.area_color_series_line = QLineEdit(Form)
        self.area_color_series_line.setObjectName(u"area_color_series_line")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.area_color_series_line)

        self.area_baseline_combo = QComboBox(Form)
        self.area_baseline_combo.addItem("")
        self.area_baseline_combo.addItem("")
        self.area_baseline_combo.addItem("")
        self.area_baseline_combo.addItem("")
        self.area_baseline_combo.setObjectName(u"area_baseline_combo")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.area_baseline_combo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(7, QFormLayout.FieldRole, self.verticalSpacer)

        self.area_transparent_slider = QSlider(Form)
        self.area_transparent_slider.setObjectName(u"area_transparent_slider")
        self.area_transparent_slider.setMaximum(100)
        self.area_transparent_slider.setValue(100)
        self.area_transparent_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.area_transparent_slider)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)


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
        self.area_color_series_btn.setText("")
        self.area_baseline_combo.setItemText(0, QCoreApplication.translate("Form", u"zero", None))
        self.area_baseline_combo.setItemText(1, QCoreApplication.translate("Form", u"sym", None))
        self.area_baseline_combo.setItemText(2, QCoreApplication.translate("Form", u"wiggle", None))
        self.area_baseline_combo.setItemText(3, QCoreApplication.translate("Form", u"weighted_wiggle", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"BaseLine", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Transparency", None))
    # retranslateUi

