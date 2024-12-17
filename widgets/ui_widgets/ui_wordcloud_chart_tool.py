# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wordcloudChartToolUIGRTbsM.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)

from widgets.inherited_widgets.clickable_line_edit_widget import ClickableLineEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(290, 577)
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

        self.y_series_combo = QComboBox(Form)
        self.y_series_combo.setObjectName(u"y_series_combo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y_series_combo)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.width_spin = QSpinBox(Form)
        self.width_spin.setObjectName(u"width_spin")
        self.width_spin.setMinimum(1)
        self.width_spin.setMaximum(10000)
        self.width_spin.setValue(400)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.width_spin)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.height_spin = QSpinBox(Form)
        self.height_spin.setObjectName(u"height_spin")
        self.height_spin.setMinimum(1)
        self.height_spin.setMaximum(10000)
        self.height_spin.setValue(400)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.height_spin)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.scale_spin = QDoubleSpinBox(Form)
        self.scale_spin.setObjectName(u"scale_spin")
        self.scale_spin.setMinimum(0.100000000000000)
        self.scale_spin.setMaximum(100.000000000000000)
        self.scale_spin.setSingleStep(0.100000000000000)
        self.scale_spin.setValue(1.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.scale_spin)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_14)

        self.background_color_btn = QToolButton(Form)
        self.background_color_btn.setObjectName(u"background_color_btn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.background_color_btn)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_17)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(9, QFormLayout.FieldRole, self.verticalSpacer)

        self.max_font_size_spin = QDoubleSpinBox(Form)
        self.max_font_size_spin.setObjectName(u"max_font_size_spin")
        self.max_font_size_spin.setMinimum(1.000000000000000)
        self.max_font_size_spin.setMaximum(10000.000000000000000)
        self.max_font_size_spin.setValue(100.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.max_font_size_spin)

        self.color_map_combo = QComboBox(Form)
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.addItem("")
        self.color_map_combo.setObjectName(u"color_map_combo")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.color_map_combo)

        self.mask_image_line = ClickableLineEdit(Form)
        self.mask_image_line.setObjectName(u"mask_image_line")
        self.mask_image_line.setEnabled(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.mask_image_line)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"WordsSeries", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"FrequencySeries", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Width", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Height", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Scale", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"BackgroundColor", None))
        self.background_color_btn.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"MaxFontSize", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"ColorMap", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"MaskImage", None))
        self.color_map_combo.setItemText(0, QCoreApplication.translate("Form", u"viridis", None))
        self.color_map_combo.setItemText(1, QCoreApplication.translate("Form", u"plasma", None))
        self.color_map_combo.setItemText(2, QCoreApplication.translate("Form", u"inferno", None))
        self.color_map_combo.setItemText(3, QCoreApplication.translate("Form", u"magma", None))
        self.color_map_combo.setItemText(4, QCoreApplication.translate("Form", u"cividis", None))
        self.color_map_combo.setItemText(5, QCoreApplication.translate("Form", u"Greys", None))
        self.color_map_combo.setItemText(6, QCoreApplication.translate("Form", u"Purples", None))
        self.color_map_combo.setItemText(7, QCoreApplication.translate("Form", u"Blues", None))
        self.color_map_combo.setItemText(8, QCoreApplication.translate("Form", u"Greens", None))
        self.color_map_combo.setItemText(9, QCoreApplication.translate("Form", u"Oranges", None))
        self.color_map_combo.setItemText(10, QCoreApplication.translate("Form", u"Reds", None))
        self.color_map_combo.setItemText(11, QCoreApplication.translate("Form", u"YlOrBr", None))
        self.color_map_combo.setItemText(12, QCoreApplication.translate("Form", u"YlOrRd", None))
        self.color_map_combo.setItemText(13, QCoreApplication.translate("Form", u"OrRd", None))
        self.color_map_combo.setItemText(14, QCoreApplication.translate("Form", u"PuRd", None))
        self.color_map_combo.setItemText(15, QCoreApplication.translate("Form", u"RdPu", None))
        self.color_map_combo.setItemText(16, QCoreApplication.translate("Form", u"BuPu", None))
        self.color_map_combo.setItemText(17, QCoreApplication.translate("Form", u"GnBu", None))
        self.color_map_combo.setItemText(18, QCoreApplication.translate("Form", u"PuBu", None))
        self.color_map_combo.setItemText(19, QCoreApplication.translate("Form", u"YlGnBu", None))
        self.color_map_combo.setItemText(20, QCoreApplication.translate("Form", u"PuBuGn", None))
        self.color_map_combo.setItemText(21, QCoreApplication.translate("Form", u"BuGn", None))
        self.color_map_combo.setItemText(22, QCoreApplication.translate("Form", u"YlGn", None))
        self.color_map_combo.setItemText(23, QCoreApplication.translate("Form", u"binary", None))
        self.color_map_combo.setItemText(24, QCoreApplication.translate("Form", u"gist_yarg", None))
        self.color_map_combo.setItemText(25, QCoreApplication.translate("Form", u"gist_gray", None))
        self.color_map_combo.setItemText(26, QCoreApplication.translate("Form", u"gray", None))
        self.color_map_combo.setItemText(27, QCoreApplication.translate("Form", u"bone", None))
        self.color_map_combo.setItemText(28, QCoreApplication.translate("Form", u"pink", None))
        self.color_map_combo.setItemText(29, QCoreApplication.translate("Form", u"spring", None))
        self.color_map_combo.setItemText(30, QCoreApplication.translate("Form", u"summer", None))
        self.color_map_combo.setItemText(31, QCoreApplication.translate("Form", u"autumn", None))
        self.color_map_combo.setItemText(32, QCoreApplication.translate("Form", u"winter", None))
        self.color_map_combo.setItemText(33, QCoreApplication.translate("Form", u"cool", None))
        self.color_map_combo.setItemText(34, QCoreApplication.translate("Form", u"Wistia", None))
        self.color_map_combo.setItemText(35, QCoreApplication.translate("Form", u"hot", None))
        self.color_map_combo.setItemText(36, QCoreApplication.translate("Form", u"afmhot", None))
        self.color_map_combo.setItemText(37, QCoreApplication.translate("Form", u"gist_heat", None))
        self.color_map_combo.setItemText(38, QCoreApplication.translate("Form", u"copper", None))
        self.color_map_combo.setItemText(39, QCoreApplication.translate("Form", u"PiYG", None))
        self.color_map_combo.setItemText(40, QCoreApplication.translate("Form", u"PRGn", None))
        self.color_map_combo.setItemText(41, QCoreApplication.translate("Form", u"BrBG", None))
        self.color_map_combo.setItemText(42, QCoreApplication.translate("Form", u"PuOr", None))
        self.color_map_combo.setItemText(43, QCoreApplication.translate("Form", u"RdGy", None))
        self.color_map_combo.setItemText(44, QCoreApplication.translate("Form", u"RdBu", None))
        self.color_map_combo.setItemText(45, QCoreApplication.translate("Form", u"RdYlBu", None))
        self.color_map_combo.setItemText(46, QCoreApplication.translate("Form", u"RdYlGn", None))
        self.color_map_combo.setItemText(47, QCoreApplication.translate("Form", u"Spectral", None))
        self.color_map_combo.setItemText(48, QCoreApplication.translate("Form", u"coolwarm", None))
        self.color_map_combo.setItemText(49, QCoreApplication.translate("Form", u"bwr", None))
        self.color_map_combo.setItemText(50, QCoreApplication.translate("Form", u"seismic", None))
        self.color_map_combo.setItemText(51, QCoreApplication.translate("Form", u"twilight", None))
        self.color_map_combo.setItemText(52, QCoreApplication.translate("Form", u"twilight_shifted", None))
        self.color_map_combo.setItemText(53, QCoreApplication.translate("Form", u"hsv", None))
        self.color_map_combo.setItemText(54, QCoreApplication.translate("Form", u"Pastel1", None))
        self.color_map_combo.setItemText(55, QCoreApplication.translate("Form", u"Pastel2", None))
        self.color_map_combo.setItemText(56, QCoreApplication.translate("Form", u"Paired", None))
        self.color_map_combo.setItemText(57, QCoreApplication.translate("Form", u"Accent", None))
        self.color_map_combo.setItemText(58, QCoreApplication.translate("Form", u"Dark2", None))
        self.color_map_combo.setItemText(59, QCoreApplication.translate("Form", u"Set1", None))
        self.color_map_combo.setItemText(60, QCoreApplication.translate("Form", u"Set2", None))
        self.color_map_combo.setItemText(61, QCoreApplication.translate("Form", u"Set3", None))
        self.color_map_combo.setItemText(62, QCoreApplication.translate("Form", u"tab10", None))
        self.color_map_combo.setItemText(63, QCoreApplication.translate("Form", u"tab20", None))
        self.color_map_combo.setItemText(64, QCoreApplication.translate("Form", u"tab20b", None))
        self.color_map_combo.setItemText(65, QCoreApplication.translate("Form", u"tab20c", None))
        self.color_map_combo.setItemText(66, QCoreApplication.translate("Form", u"flag", None))
        self.color_map_combo.setItemText(67, QCoreApplication.translate("Form", u"prism", None))
        self.color_map_combo.setItemText(68, QCoreApplication.translate("Form", u"ocean", None))
        self.color_map_combo.setItemText(69, QCoreApplication.translate("Form", u"gist_earth", None))
        self.color_map_combo.setItemText(70, QCoreApplication.translate("Form", u"terrain", None))
        self.color_map_combo.setItemText(71, QCoreApplication.translate("Form", u"gist_stern", None))
        self.color_map_combo.setItemText(72, QCoreApplication.translate("Form", u"gnuplot", None))
        self.color_map_combo.setItemText(73, QCoreApplication.translate("Form", u"gnuplot2", None))
        self.color_map_combo.setItemText(74, QCoreApplication.translate("Form", u"CMRmap", None))
        self.color_map_combo.setItemText(75, QCoreApplication.translate("Form", u"cubehelix", None))
        self.color_map_combo.setItemText(76, QCoreApplication.translate("Form", u"brg", None))
        self.color_map_combo.setItemText(77, QCoreApplication.translate("Form", u"gist_rainbow", None))
        self.color_map_combo.setItemText(78, QCoreApplication.translate("Form", u"rainbow", None))
        self.color_map_combo.setItemText(79, QCoreApplication.translate("Form", u"jet", None))
        self.color_map_combo.setItemText(80, QCoreApplication.translate("Form", u"turbo", None))
        self.color_map_combo.setItemText(81, QCoreApplication.translate("Form", u"nipy_spectral", None))
        self.color_map_combo.setItemText(82, QCoreApplication.translate("Form", u"gist_ncar", None))

    # retranslateUi

