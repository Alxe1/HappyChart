# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barChartToolUIUDtbqd.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(326, 419)
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
        self.toolButton.setStyleSheet(u"border-radius: 10rpx;")
        icon = QIcon()
        icon.addFile(u":/icon/icons/minus-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bar_value_label_interval_spin = QDoubleSpinBox(self.frame_2)
        self.bar_value_label_interval_spin.setObjectName(u"bar_value_label_interval_spin")
        self.bar_value_label_interval_spin.setEnabled(False)
        self.bar_value_label_interval_spin.setDecimals(2)
        self.bar_value_label_interval_spin.setMaximum(100.000000000000000)
        self.bar_value_label_interval_spin.setValue(3.000000000000000)

        self.gridLayout_3.addWidget(self.bar_value_label_interval_spin, 10, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.data_label_line = QLineEdit(self.frame_2)
        self.data_label_line.setObjectName(u"data_label_line")

        self.gridLayout_3.addWidget(self.data_label_line, 2, 1, 1, 1)

        self.bar_value_label_color_btn = QToolButton(self.frame_2)
        self.bar_value_label_color_btn.setObjectName(u"bar_value_label_color_btn")
        self.bar_value_label_color_btn.setEnabled(False)

        self.gridLayout_3.addWidget(self.bar_value_label_color_btn, 11, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.bar_value_label_check = QCheckBox(self.frame_2)
        self.bar_value_label_check.setObjectName(u"bar_value_label_check")

        self.gridLayout_3.addWidget(self.bar_value_label_check, 8, 1, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 7, 0, 1, 1)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 9, 0, 1, 1)

        self.err_bar_color_btn = QToolButton(self.frame_2)
        self.err_bar_color_btn.setObjectName(u"err_bar_color_btn")

        self.gridLayout_3.addWidget(self.err_bar_color_btn, 7, 1, 1, 1)

        self.bar_value_label_size_spin = QSpinBox(self.frame_2)
        self.bar_value_label_size_spin.setObjectName(u"bar_value_label_size_spin")
        self.bar_value_label_size_spin.setEnabled(False)
        self.bar_value_label_size_spin.setValue(9)

        self.gridLayout_3.addWidget(self.bar_value_label_size_spin, 12, 1, 1, 1)

        self.bar_selector_combo = QComboBox(self.frame_2)
        self.bar_selector_combo.addItem("")
        self.bar_selector_combo.addItem("")
        self.bar_selector_combo.addItem("")
        self.bar_selector_combo.setObjectName(u"bar_selector_combo")
        self.bar_selector_combo.setMinimumSize(QSize(0, 0))
        self.bar_selector_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.bar_selector_combo, 0, 1, 1, 1)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 12, 0, 1, 1)

        self.base_chart_color_series_line = QLineEdit(self.frame_2)
        self.base_chart_color_series_line.setObjectName(u"base_chart_color_series_line")

        self.gridLayout_3.addWidget(self.base_chart_color_series_line, 4, 1, 1, 1)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 10, 0, 1, 1)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 11, 0, 1, 1)

        self.base_chart_interval_spin = QDoubleSpinBox(self.frame_2)
        self.base_chart_interval_spin.setObjectName(u"base_chart_interval_spin")
        self.base_chart_interval_spin.setMinimum(0.000000000000000)
        self.base_chart_interval_spin.setMaximum(0.500000000000000)
        self.base_chart_interval_spin.setSingleStep(0.010000000000000)
        self.base_chart_interval_spin.setValue(0.350000000000000)

        self.gridLayout_3.addWidget(self.base_chart_interval_spin, 5, 1, 1, 1)

        self.bar_value_label_line = QLineEdit(self.frame_2)
        self.bar_value_label_line.setObjectName(u"bar_value_label_line")
        self.bar_value_label_line.setEnabled(False)

        self.gridLayout_3.addWidget(self.bar_value_label_line, 9, 1, 1, 1)

        self.y_series_label = QLabel(self.frame_2)
        self.y_series_label.setObjectName(u"y_series_label")

        self.gridLayout_3.addWidget(self.y_series_label, 1, 0, 1, 1)

        self.base_chart_color_series_btn = QToolButton(self.frame_2)
        self.base_chart_color_series_btn.setObjectName(u"base_chart_color_series_btn")

        self.gridLayout_3.addWidget(self.base_chart_color_series_btn, 3, 1, 1, 1)

        self.y_series_combo = QComboBox(self.frame_2)
        self.y_series_combo.setObjectName(u"y_series_combo")

        self.gridLayout_3.addWidget(self.y_series_combo, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 13, 1, 1, 1)

        self.y_err_series_line = QLineEdit(self.frame_2)
        self.y_err_series_line.setObjectName(u"y_err_series_line")

        self.gridLayout_3.addWidget(self.y_err_series_line, 6, 1, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 8, 0, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 21))

        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.label_25, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u67f1\u72b6\u56fe\u5c42", None))
        self.toolButton.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u56fe\u8868\u95f4\u9694", None))
        self.bar_value_label_color_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u6807\u7b7e", None))
        self.bar_value_label_check.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u8bef\u5dee\u6761\u989c\u8272", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u503c\u6807\u7b7e\u7cfb\u5217", None))
        self.err_bar_color_btn.setText("")
        self.bar_selector_combo.setItemText(0, QCoreApplication.translate("Form", u"\u5206\u7ec4\u67f1\u72b6\u56fe", None))
        self.bar_selector_combo.setItemText(1, QCoreApplication.translate("Form", u"\u5806\u79ef\u67f1\u72b6\u56fe", None))
        self.bar_selector_combo.setItemText(2, QCoreApplication.translate("Form", u"\u6bd4\u4f8b\u67f1\u72b6\u56fe", None))

        self.label_24.setText(QCoreApplication.translate("Form", u"\u503c\u6807\u7b7e\u5927\u5c0f", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u503c\u6807\u7b7e\u95f4\u9694", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u503c\u6807\u7b7e\u989c\u8272", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"Y\u8f74\u7cfb\u5217\u6570\u636e", None))
        self.base_chart_color_series_btn.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"\u8bef\u5dee\u6570\u636e\u5217", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u503c\u6807\u7b7e", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u56fe\u8868\u989c\u8272\u7cfb\u5217", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u56fe\u8868", None))
    # retranslateUi

