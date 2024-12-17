# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'violinChartToolUIHYrjJk.ui'
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
    QSlider, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(323, 692)
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

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.vertical_check = QCheckBox(Form)
        self.vertical_check.setObjectName(u"vertical_check")
        self.vertical_check.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.vertical_check)

        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"label_25")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_25)

        self.width_spin = QDoubleSpinBox(Form)
        self.width_spin.setObjectName(u"width_spin")
        self.width_spin.setMinimum(0.010000000000000)
        self.width_spin.setSingleStep(0.100000000000000)
        self.width_spin.setValue(0.500000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.width_spin)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_33)

        self.points_spin = QSpinBox(Form)
        self.points_spin.setObjectName(u"points_spin")
        self.points_spin.setMinimum(10)
        self.points_spin.setMaximum(1000000)
        self.points_spin.setValue(100)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.points_spin)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.method_combo = QComboBox(Form)
        self.method_combo.addItem("")
        self.method_combo.addItem("")
        self.method_combo.setObjectName(u"method_combo")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.method_combo)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.side_combo = QComboBox(Form)
        self.side_combo.addItem("")
        self.side_combo.addItem("")
        self.side_combo.addItem("")
        self.side_combo.setObjectName(u"side_combo")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.side_combo)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_5)

        self.body_face_color_btn = QToolButton(Form)
        self.body_face_color_btn.setObjectName(u"body_face_color_btn")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.body_face_color_btn)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label)

        self.body_edge_color_btn = QToolButton(Form)
        self.body_edge_color_btn.setObjectName(u"body_edge_color_btn")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.body_edge_color_btn)

        self.label_43 = QLabel(Form)
        self.label_43.setObjectName(u"label_43")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_43)

        self.transparency_slider = QSlider(Form)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMaximum(100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.transparency_slider)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_2)

        self.median_dot_check = QCheckBox(Form)
        self.median_dot_check.setObjectName(u"median_dot_check")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.median_dot_check)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_8)

        self.median_marker_combo = QComboBox(Form)
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.addItem("")
        self.median_marker_combo.setObjectName(u"median_marker_combo")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.median_marker_combo)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_9)

        self.median_color_btn = QToolButton(Form)
        self.median_color_btn.setObjectName(u"median_color_btn")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.median_color_btn)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_10)

        self.median_size_spin = QDoubleSpinBox(Form)
        self.median_size_spin.setObjectName(u"median_size_spin")
        self.median_size_spin.setMinimum(0.010000000000000)
        self.median_size_spin.setMaximum(100.000000000000000)
        self.median_size_spin.setSingleStep(0.100000000000000)
        self.median_size_spin.setValue(30.000000000000000)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.median_size_spin)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_7)

        self.quantile_linestyle_combo = QComboBox(Form)
        self.quantile_linestyle_combo.addItem("")
        self.quantile_linestyle_combo.addItem("")
        self.quantile_linestyle_combo.addItem("")
        self.quantile_linestyle_combo.addItem("")
        self.quantile_linestyle_combo.setObjectName(u"quantile_linestyle_combo")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.quantile_linestyle_combo)

        self.label_44 = QLabel(Form)
        self.label_44.setObjectName(u"label_44")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_44)

        self.quantile_line_color_btn = QToolButton(Form)
        self.quantile_line_color_btn.setObjectName(u"quantile_line_color_btn")

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.quantile_line_color_btn)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.label_11)

        self.quantile_linewidth_spin = QDoubleSpinBox(Form)
        self.quantile_linewidth_spin.setObjectName(u"quantile_linewidth_spin")
        self.quantile_linewidth_spin.setMinimum(0.000000000000000)
        self.quantile_linewidth_spin.setMaximum(100.000000000000000)
        self.quantile_linewidth_spin.setSingleStep(0.100000000000000)
        self.quantile_linewidth_spin.setValue(5.000000000000000)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.quantile_linewidth_spin)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_12)

        self.whisker_linestyle_combo = QComboBox(Form)
        self.whisker_linestyle_combo.addItem("")
        self.whisker_linestyle_combo.addItem("")
        self.whisker_linestyle_combo.addItem("")
        self.whisker_linestyle_combo.addItem("")
        self.whisker_linestyle_combo.setObjectName(u"whisker_linestyle_combo")

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.whisker_linestyle_combo)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_13)

        self.whisker_line_color_btn = QToolButton(Form)
        self.whisker_line_color_btn.setObjectName(u"whisker_line_color_btn")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.whisker_line_color_btn)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_14)

        self.whisker_line_width_spin = QDoubleSpinBox(Form)
        self.whisker_line_width_spin.setObjectName(u"whisker_line_width_spin")
        self.whisker_line_width_spin.setMinimum(0.000000000000000)
        self.whisker_line_width_spin.setMaximum(100.000000000000000)
        self.whisker_line_width_spin.setSingleStep(0.100000000000000)
        self.whisker_line_width_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.whisker_line_width_spin)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.y_series_label.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"DataLabelSeries", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Vertical", None))
        self.vertical_check.setText("")
        self.label_25.setText(QCoreApplication.translate("Form", u"Width", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"points", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"BWMethod", None))
        self.method_combo.setItemText(0, QCoreApplication.translate("Form", u"scott", None))
        self.method_combo.setItemText(1, QCoreApplication.translate("Form", u"silverman", None))

        self.label_16.setText(QCoreApplication.translate("Form", u"Side", None))
        self.side_combo.setItemText(0, QCoreApplication.translate("Form", u"both", None))
        self.side_combo.setItemText(1, QCoreApplication.translate("Form", u"low", None))
        self.side_combo.setItemText(2, QCoreApplication.translate("Form", u"high", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"BodyFaceColor", None))
        self.body_face_color_btn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"BodyEdgeColor", None))
        self.body_edge_color_btn.setText("")
        self.label_43.setText(QCoreApplication.translate("Form", u"Transparency", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ShowMedianDot", None))
        self.median_dot_check.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"MedianMarker", None))
        self.median_marker_combo.setItemText(0, QCoreApplication.translate("Form", u".", None))
        self.median_marker_combo.setItemText(1, QCoreApplication.translate("Form", u"o", None))
        self.median_marker_combo.setItemText(2, QCoreApplication.translate("Form", u"v", None))
        self.median_marker_combo.setItemText(3, QCoreApplication.translate("Form", u"^", None))
        self.median_marker_combo.setItemText(4, QCoreApplication.translate("Form", u"<", None))
        self.median_marker_combo.setItemText(5, QCoreApplication.translate("Form", u">", None))
        self.median_marker_combo.setItemText(6, QCoreApplication.translate("Form", u"1", None))
        self.median_marker_combo.setItemText(7, QCoreApplication.translate("Form", u"2", None))
        self.median_marker_combo.setItemText(8, QCoreApplication.translate("Form", u"3", None))
        self.median_marker_combo.setItemText(9, QCoreApplication.translate("Form", u"4", None))
        self.median_marker_combo.setItemText(10, QCoreApplication.translate("Form", u"8", None))
        self.median_marker_combo.setItemText(11, QCoreApplication.translate("Form", u"s", None))
        self.median_marker_combo.setItemText(12, QCoreApplication.translate("Form", u"p", None))
        self.median_marker_combo.setItemText(13, QCoreApplication.translate("Form", u"P", None))
        self.median_marker_combo.setItemText(14, QCoreApplication.translate("Form", u"*", None))
        self.median_marker_combo.setItemText(15, QCoreApplication.translate("Form", u"h", None))
        self.median_marker_combo.setItemText(16, QCoreApplication.translate("Form", u"H", None))
        self.median_marker_combo.setItemText(17, QCoreApplication.translate("Form", u"+", None))
        self.median_marker_combo.setItemText(18, QCoreApplication.translate("Form", u"x", None))
        self.median_marker_combo.setItemText(19, QCoreApplication.translate("Form", u"X", None))
        self.median_marker_combo.setItemText(20, QCoreApplication.translate("Form", u"D", None))
        self.median_marker_combo.setItemText(21, QCoreApplication.translate("Form", u"d", None))
        self.median_marker_combo.setItemText(22, QCoreApplication.translate("Form", u"|", None))
        self.median_marker_combo.setItemText(23, QCoreApplication.translate("Form", u"_", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"MedianColor", None))
        self.median_color_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"MedianSize", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"QuartileLineStyle", None))
        self.quantile_linestyle_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.quantile_linestyle_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.quantile_linestyle_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.quantile_linestyle_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_44.setText(QCoreApplication.translate("Form", u"QuartileLineColor", None))
        self.quantile_line_color_btn.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"QuartileLineWidth", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"WhiskerLineStyle", None))
        self.whisker_linestyle_combo.setItemText(0, QCoreApplication.translate("Form", u"-", None))
        self.whisker_linestyle_combo.setItemText(1, QCoreApplication.translate("Form", u"--", None))
        self.whisker_linestyle_combo.setItemText(2, QCoreApplication.translate("Form", u"-.", None))
        self.whisker_linestyle_combo.setItemText(3, QCoreApplication.translate("Form", u":", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"WhiskerLineColor", None))
        self.whisker_line_color_btn.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"WhiskerLineWidth", None))
    # retranslateUi

