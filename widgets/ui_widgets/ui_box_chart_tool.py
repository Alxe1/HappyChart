# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boxChartToolUIXPoKJE.ui'
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
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(316, 1011)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_38 = QLabel(Form)
        self.label_38.setObjectName(u"label_38")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_38)

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

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")
        self.data_label_line.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_label_line)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_33)

        self.color_series_btn = QToolButton(Form)
        self.color_series_btn.setObjectName(u"color_series_btn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.color_series_btn)

        self.color_series_line = QLineEdit(Form)
        self.color_series_line.setObjectName(u"color_series_line")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.color_series_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(34, QFormLayout.FieldRole, self.verticalSpacer)

        self.notch_check = QCheckBox(Form)
        self.notch_check.setObjectName(u"notch_check")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.notch_check)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.vert_check = QCheckBox(Form)
        self.vert_check.setObjectName(u"vert_check")
        self.vert_check.setChecked(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.vert_check)

        self.label_43 = QLabel(Form)
        self.label_43.setObjectName(u"label_43")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_43)

        self.box_width_spin = QDoubleSpinBox(Form)
        self.box_width_spin.setObjectName(u"box_width_spin")
        self.box_width_spin.setMaximum(100.000000000000000)
        self.box_width_spin.setSingleStep(0.010000000000000)
        self.box_width_spin.setValue(0.300000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.box_width_spin)

        self.label_44 = QLabel(Form)
        self.label_44.setObjectName(u"label_44")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_44)

        self.patch_artist_check = QCheckBox(Form)
        self.patch_artist_check.setObjectName(u"patch_artist_check")
        self.patch_artist_check.setChecked(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.patch_artist_check)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_3)

        self.show_box_check = QCheckBox(Form)
        self.show_box_check.setObjectName(u"show_box_check")
        self.show_box_check.setChecked(True)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.show_box_check)

        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_25)

        self.box_linestyle_combo = QComboBox(Form)
        self.box_linestyle_combo.addItem("")
        self.box_linestyle_combo.addItem("")
        self.box_linestyle_combo.addItem("")
        self.box_linestyle_combo.addItem("")
        self.box_linestyle_combo.setObjectName(u"box_linestyle_combo")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.box_linestyle_combo)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_4)

        self.box_linewidth_spin = QDoubleSpinBox(Form)
        self.box_linewidth_spin.setObjectName(u"box_linewidth_spin")
        self.box_linewidth_spin.setSingleStep(0.100000000000000)
        self.box_linewidth_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.box_linewidth_spin)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_5)

        self.box_color_btn = QToolButton(Form)
        self.box_color_btn.setObjectName(u"box_color_btn")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.box_color_btn)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_6)

        self.median_linestyle_combo = QComboBox(Form)
        self.median_linestyle_combo.addItem("")
        self.median_linestyle_combo.addItem("")
        self.median_linestyle_combo.addItem("")
        self.median_linestyle_combo.addItem("")
        self.median_linestyle_combo.setObjectName(u"median_linestyle_combo")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.median_linestyle_combo)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_8)

        self.median_linewidth_spin = QDoubleSpinBox(Form)
        self.median_linewidth_spin.setObjectName(u"median_linewidth_spin")
        self.median_linewidth_spin.setSingleStep(0.100000000000000)
        self.median_linewidth_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.median_linewidth_spin)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_9)

        self.median_line_color_btn = QToolButton(Form)
        self.median_line_color_btn.setObjectName(u"median_line_color_btn")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.median_line_color_btn)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_10)

        self.show_means_check = QCheckBox(Form)
        self.show_means_check.setObjectName(u"show_means_check")
        self.show_means_check.setChecked(False)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.show_means_check)

        self.label_48 = QLabel(Form)
        self.label_48.setObjectName(u"label_48")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_48)

        self.mean_marker_combo = QComboBox(Form)
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.addItem("")
        self.mean_marker_combo.setObjectName(u"mean_marker_combo")

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.mean_marker_combo)

        self.label_35 = QLabel(Form)
        self.label_35.setObjectName(u"label_35")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_35)

        self.mean_edge_color_btn = QToolButton(Form)
        self.mean_edge_color_btn.setObjectName(u"mean_edge_color_btn")

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.mean_edge_color_btn)

        self.label_32 = QLabel(Form)
        self.label_32.setObjectName(u"label_32")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_32)

        self.mean_face_color_btn = QToolButton(Form)
        self.mean_face_color_btn.setObjectName(u"mean_face_color_btn")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.mean_face_color_btn)

        self.label_36 = QLabel(Form)
        self.label_36.setObjectName(u"label_36")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_36)

        self.show_mean_line_check = QCheckBox(Form)
        self.show_mean_line_check.setObjectName(u"show_mean_line_check")

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.show_mean_line_check)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_2)

        self.mean_linestyle_combo = QComboBox(Form)
        self.mean_linestyle_combo.addItem("")
        self.mean_linestyle_combo.addItem("")
        self.mean_linestyle_combo.addItem("")
        self.mean_linestyle_combo.addItem("")
        self.mean_linestyle_combo.setObjectName(u"mean_linestyle_combo")

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.mean_linestyle_combo)

        self.label_46 = QLabel(Form)
        self.label_46.setObjectName(u"label_46")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_46)

        self.mean_linewidth_spin = QDoubleSpinBox(Form)
        self.mean_linewidth_spin.setObjectName(u"mean_linewidth_spin")
        self.mean_linewidth_spin.setSingleStep(0.100000000000000)
        self.mean_linewidth_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.mean_linewidth_spin)

        self.label_47 = QLabel(Form)
        self.label_47.setObjectName(u"label_47")

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.label_47)

        self.mean_line_color_btn = QToolButton(Form)
        self.mean_line_color_btn.setObjectName(u"mean_line_color_btn")

        self.formLayout.setWidget(23, QFormLayout.FieldRole, self.mean_line_color_btn)

        self.label_39 = QLabel(Form)
        self.label_39.setObjectName(u"label_39")

        self.formLayout.setWidget(23, QFormLayout.LabelRole, self.label_39)

        self.show_caps_check = QCheckBox(Form)
        self.show_caps_check.setObjectName(u"show_caps_check")
        self.show_caps_check.setChecked(True)

        self.formLayout.setWidget(24, QFormLayout.FieldRole, self.show_caps_check)

        self.label_34 = QLabel(Form)
        self.label_34.setObjectName(u"label_34")

        self.formLayout.setWidget(24, QFormLayout.LabelRole, self.label_34)

        self.cap_linestyle_combo = QComboBox(Form)
        self.cap_linestyle_combo.addItem("")
        self.cap_linestyle_combo.addItem("")
        self.cap_linestyle_combo.addItem("")
        self.cap_linestyle_combo.addItem("")
        self.cap_linestyle_combo.setObjectName(u"cap_linestyle_combo")

        self.formLayout.setWidget(25, QFormLayout.FieldRole, self.cap_linestyle_combo)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")

        self.formLayout.setWidget(25, QFormLayout.LabelRole, self.label_23)

        self.cap_linewidth_spin = QDoubleSpinBox(Form)
        self.cap_linewidth_spin.setObjectName(u"cap_linewidth_spin")
        self.cap_linewidth_spin.setSingleStep(0.100000000000000)
        self.cap_linewidth_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(26, QFormLayout.FieldRole, self.cap_linewidth_spin)

        self.label_30 = QLabel(Form)
        self.label_30.setObjectName(u"label_30")

        self.formLayout.setWidget(26, QFormLayout.LabelRole, self.label_30)

        self.cap_color_btn = QToolButton(Form)
        self.cap_color_btn.setObjectName(u"cap_color_btn")

        self.formLayout.setWidget(27, QFormLayout.FieldRole, self.cap_color_btn)

        self.label_27 = QLabel(Form)
        self.label_27.setObjectName(u"label_27")

        self.formLayout.setWidget(27, QFormLayout.LabelRole, self.label_27)

        self.cap_width_spin = QDoubleSpinBox(Form)
        self.cap_width_spin.setObjectName(u"cap_width_spin")
        self.cap_width_spin.setSingleStep(0.100000000000000)
        self.cap_width_spin.setValue(0.500000000000000)

        self.formLayout.setWidget(28, QFormLayout.FieldRole, self.cap_width_spin)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(28, QFormLayout.LabelRole, self.label_7)

        self.show_outlier_check = QCheckBox(Form)
        self.show_outlier_check.setObjectName(u"show_outlier_check")
        self.show_outlier_check.setChecked(True)

        self.formLayout.setWidget(29, QFormLayout.FieldRole, self.show_outlier_check)

        self.label_40 = QLabel(Form)
        self.label_40.setObjectName(u"label_40")

        self.formLayout.setWidget(29, QFormLayout.LabelRole, self.label_40)

        self.outlier_marker_combo = QComboBox(Form)
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.addItem("")
        self.outlier_marker_combo.setObjectName(u"outlier_marker_combo")

        self.formLayout.setWidget(30, QFormLayout.FieldRole, self.outlier_marker_combo)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(30, QFormLayout.LabelRole, self.label_11)

        self.outlier_marker_size_spin = QDoubleSpinBox(Form)
        self.outlier_marker_size_spin.setObjectName(u"outlier_marker_size_spin")
        self.outlier_marker_size_spin.setSingleStep(0.100000000000000)
        self.outlier_marker_size_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(31, QFormLayout.FieldRole, self.outlier_marker_size_spin)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(31, QFormLayout.LabelRole, self.label_14)

        self.outlier_edge_color_btn = QToolButton(Form)
        self.outlier_edge_color_btn.setObjectName(u"outlier_edge_color_btn")

        self.formLayout.setWidget(32, QFormLayout.FieldRole, self.outlier_edge_color_btn)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(32, QFormLayout.LabelRole, self.label_12)

        self.outlier_face_color_btn = QToolButton(Form)
        self.outlier_face_color_btn.setObjectName(u"outlier_face_color_btn")

        self.formLayout.setWidget(33, QFormLayout.FieldRole, self.outlier_face_color_btn)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(33, QFormLayout.LabelRole, self.label_13)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"ColorSeries", None))
        self.color_series_btn.setText("")
        self.notch_check.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Notch", None))
        self.vert_check.setText("")
        self.label_43.setText(QCoreApplication.translate("Form", u"Vertical", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"BoxWidth", None))
        self.patch_artist_check.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"PatchArtist", None))
        self.show_box_check.setText("")
        self.label_25.setText(QCoreApplication.translate("Form", u"ShowBox", None))
        self.box_linestyle_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.box_linestyle_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.box_linestyle_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.box_linestyle_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"BoxLineStyle", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"BoxLineWidth", None))
        self.box_color_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"BoxColor", None))
        self.median_linestyle_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.median_linestyle_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.median_linestyle_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.median_linestyle_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"MedianLineStyle", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"MedianLineWidth", None))
        self.median_line_color_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"MedianLineColor", None))
        self.show_means_check.setText("")
        self.label_48.setText(QCoreApplication.translate("Form", u"ShowMeans", None))
        self.mean_marker_combo.setItemText(0, QCoreApplication.translate("Form", u".", None))
        self.mean_marker_combo.setItemText(1, QCoreApplication.translate("Form", u"v", None))
        self.mean_marker_combo.setItemText(2, QCoreApplication.translate("Form", u"o", None))
        self.mean_marker_combo.setItemText(3, QCoreApplication.translate("Form", u"^", None))
        self.mean_marker_combo.setItemText(4, QCoreApplication.translate("Form", u"<", None))
        self.mean_marker_combo.setItemText(5, QCoreApplication.translate("Form", u">", None))
        self.mean_marker_combo.setItemText(6, QCoreApplication.translate("Form", u"1", None))
        self.mean_marker_combo.setItemText(7, QCoreApplication.translate("Form", u"2", None))
        self.mean_marker_combo.setItemText(8, QCoreApplication.translate("Form", u"3", None))
        self.mean_marker_combo.setItemText(9, QCoreApplication.translate("Form", u"4", None))
        self.mean_marker_combo.setItemText(10, QCoreApplication.translate("Form", u"8", None))
        self.mean_marker_combo.setItemText(11, QCoreApplication.translate("Form", u"s", None))
        self.mean_marker_combo.setItemText(12, QCoreApplication.translate("Form", u"p", None))
        self.mean_marker_combo.setItemText(13, QCoreApplication.translate("Form", u"P", None))
        self.mean_marker_combo.setItemText(14, QCoreApplication.translate("Form", u"*", None))
        self.mean_marker_combo.setItemText(15, QCoreApplication.translate("Form", u"h", None))
        self.mean_marker_combo.setItemText(16, QCoreApplication.translate("Form", u"H", None))
        self.mean_marker_combo.setItemText(17, QCoreApplication.translate("Form", u"+", None))
        self.mean_marker_combo.setItemText(18, QCoreApplication.translate("Form", u"x", None))
        self.mean_marker_combo.setItemText(19, QCoreApplication.translate("Form", u"X", None))
        self.mean_marker_combo.setItemText(20, QCoreApplication.translate("Form", u"D", None))
        self.mean_marker_combo.setItemText(21, QCoreApplication.translate("Form", u"d", None))
        self.mean_marker_combo.setItemText(22, QCoreApplication.translate("Form", u"|", None))
        self.mean_marker_combo.setItemText(23, QCoreApplication.translate("Form", u"_", None))

        self.label_35.setText(QCoreApplication.translate("Form", u"MeanMarker", None))
        self.mean_edge_color_btn.setText("")
        self.label_32.setText(QCoreApplication.translate("Form", u"MeanEdgeColor", None))
        self.mean_face_color_btn.setText("")
        self.label_36.setText(QCoreApplication.translate("Form", u"MeanFaceColor", None))
        self.show_mean_line_check.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"ShowMeanLine", None))
        self.mean_linestyle_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.mean_linestyle_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.mean_linestyle_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.mean_linestyle_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_46.setText(QCoreApplication.translate("Form", u"MeanLineStyle", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"MeanLineWidth", None))
        self.mean_line_color_btn.setText("")
        self.label_39.setText(QCoreApplication.translate("Form", u"MeanLineColor", None))
        self.show_caps_check.setText("")
        self.label_34.setText(QCoreApplication.translate("Form", u"ShowCaps", None))
        self.cap_linestyle_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.cap_linestyle_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.cap_linestyle_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.cap_linestyle_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_23.setText(QCoreApplication.translate("Form", u"CapLineStyle", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"CapLineWidth", None))
        self.cap_color_btn.setText("")
        self.label_27.setText(QCoreApplication.translate("Form", u"CapColor", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"CapWidth", None))
        self.show_outlier_check.setText("")
        self.label_40.setText(QCoreApplication.translate("Form", u"ShowOutliers", None))
        self.outlier_marker_combo.setItemText(0, QCoreApplication.translate("Form", u".", None))
        self.outlier_marker_combo.setItemText(1, QCoreApplication.translate("Form", u"o", None))
        self.outlier_marker_combo.setItemText(2, QCoreApplication.translate("Form", u"v", None))
        self.outlier_marker_combo.setItemText(3, QCoreApplication.translate("Form", u"^", None))
        self.outlier_marker_combo.setItemText(4, QCoreApplication.translate("Form", u"<", None))
        self.outlier_marker_combo.setItemText(5, QCoreApplication.translate("Form", u">", None))
        self.outlier_marker_combo.setItemText(6, QCoreApplication.translate("Form", u"8", None))
        self.outlier_marker_combo.setItemText(7, QCoreApplication.translate("Form", u"s", None))
        self.outlier_marker_combo.setItemText(8, QCoreApplication.translate("Form", u"p", None))
        self.outlier_marker_combo.setItemText(9, QCoreApplication.translate("Form", u"P", None))
        self.outlier_marker_combo.setItemText(10, QCoreApplication.translate("Form", u"*", None))
        self.outlier_marker_combo.setItemText(11, QCoreApplication.translate("Form", u"h", None))
        self.outlier_marker_combo.setItemText(12, QCoreApplication.translate("Form", u"H", None))
        self.outlier_marker_combo.setItemText(13, QCoreApplication.translate("Form", u"X", None))
        self.outlier_marker_combo.setItemText(14, QCoreApplication.translate("Form", u"d", None))
        self.outlier_marker_combo.setItemText(15, QCoreApplication.translate("Form", u"D", None))

        self.label_11.setText(QCoreApplication.translate("Form", u"OutlierMarker", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"OutlierMarkerSize", None))
        self.outlier_edge_color_btn.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"OutlieEdgeColor", None))
        self.outlier_face_color_btn.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"OutlierFaceColor", None))
    # retranslateUi

