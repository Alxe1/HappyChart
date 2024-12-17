# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'heatmapChartToolUIaRvgtd.ui'
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
    QLabel, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

from widgets.inherited_widgets.checkable_combo_box_widget import CheckableComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(286, 591)
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

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.normalization_check = QCheckBox(Form)
        self.normalization_check.setObjectName(u"normalization_check")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.normalization_check)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.show_text_check = QCheckBox(Form)
        self.show_text_check.setObjectName(u"show_text_check")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.show_text_check)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.text_color_btn = QToolButton(Form)
        self.text_color_btn.setObjectName(u"text_color_btn")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.text_color_btn)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.cmap_combo = QComboBox(Form)
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.addItem("")
        self.cmap_combo.setObjectName(u"cmap_combo")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cmap_combo)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.show_colorbar_check = QCheckBox(Form)
        self.show_colorbar_check.setObjectName(u"show_colorbar_check")
        self.show_colorbar_check.setChecked(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.show_colorbar_check)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"XDataSeries", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"YDataSeries", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Normalization", None))
        self.normalization_check.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"ShowText", None))
        self.show_text_check.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"TextColor", None))
        self.text_color_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"CMap", None))
        self.cmap_combo.setItemText(0, QCoreApplication.translate("Form", u"viridis", None))
        self.cmap_combo.setItemText(1, QCoreApplication.translate("Form", u"plasma", None))
        self.cmap_combo.setItemText(2, QCoreApplication.translate("Form", u"inferno", None))
        self.cmap_combo.setItemText(3, QCoreApplication.translate("Form", u"magma", None))
        self.cmap_combo.setItemText(4, QCoreApplication.translate("Form", u"cividis", None))
        self.cmap_combo.setItemText(5, QCoreApplication.translate("Form", u"Greys", None))
        self.cmap_combo.setItemText(6, QCoreApplication.translate("Form", u"Purples", None))
        self.cmap_combo.setItemText(7, QCoreApplication.translate("Form", u"Blues", None))
        self.cmap_combo.setItemText(8, QCoreApplication.translate("Form", u"Greens", None))
        self.cmap_combo.setItemText(9, QCoreApplication.translate("Form", u"Oranges", None))
        self.cmap_combo.setItemText(10, QCoreApplication.translate("Form", u"Reds", None))
        self.cmap_combo.setItemText(11, QCoreApplication.translate("Form", u"YlOrBr", None))
        self.cmap_combo.setItemText(12, QCoreApplication.translate("Form", u"YlOrRd", None))
        self.cmap_combo.setItemText(13, QCoreApplication.translate("Form", u"OrRd", None))
        self.cmap_combo.setItemText(14, QCoreApplication.translate("Form", u"PuRd", None))
        self.cmap_combo.setItemText(15, QCoreApplication.translate("Form", u"RdPu", None))
        self.cmap_combo.setItemText(16, QCoreApplication.translate("Form", u"BuPu", None))
        self.cmap_combo.setItemText(17, QCoreApplication.translate("Form", u"GnBu", None))
        self.cmap_combo.setItemText(18, QCoreApplication.translate("Form", u"PuBu", None))
        self.cmap_combo.setItemText(19, QCoreApplication.translate("Form", u"YlGnBu", None))
        self.cmap_combo.setItemText(20, QCoreApplication.translate("Form", u"PuBuGn", None))
        self.cmap_combo.setItemText(21, QCoreApplication.translate("Form", u"BuGn", None))
        self.cmap_combo.setItemText(22, QCoreApplication.translate("Form", u"YlGn", None))
        self.cmap_combo.setItemText(23, QCoreApplication.translate("Form", u"binary", None))
        self.cmap_combo.setItemText(24, QCoreApplication.translate("Form", u"gist_yarg", None))
        self.cmap_combo.setItemText(25, QCoreApplication.translate("Form", u"gist_gray", None))
        self.cmap_combo.setItemText(26, QCoreApplication.translate("Form", u"gray", None))
        self.cmap_combo.setItemText(27, QCoreApplication.translate("Form", u"bone", None))
        self.cmap_combo.setItemText(28, QCoreApplication.translate("Form", u"pink", None))
        self.cmap_combo.setItemText(29, QCoreApplication.translate("Form", u"spring", None))
        self.cmap_combo.setItemText(30, QCoreApplication.translate("Form", u"summer", None))
        self.cmap_combo.setItemText(31, QCoreApplication.translate("Form", u"autumn", None))
        self.cmap_combo.setItemText(32, QCoreApplication.translate("Form", u"winter", None))
        self.cmap_combo.setItemText(33, QCoreApplication.translate("Form", u"cool", None))
        self.cmap_combo.setItemText(34, QCoreApplication.translate("Form", u"Wistia", None))
        self.cmap_combo.setItemText(35, QCoreApplication.translate("Form", u"hot", None))
        self.cmap_combo.setItemText(36, QCoreApplication.translate("Form", u"afmhot", None))
        self.cmap_combo.setItemText(37, QCoreApplication.translate("Form", u"gist_heat", None))
        self.cmap_combo.setItemText(38, QCoreApplication.translate("Form", u"copper", None))
        self.cmap_combo.setItemText(39, QCoreApplication.translate("Form", u"PiYG", None))
        self.cmap_combo.setItemText(40, QCoreApplication.translate("Form", u"PRGn", None))
        self.cmap_combo.setItemText(41, QCoreApplication.translate("Form", u"BrBG", None))
        self.cmap_combo.setItemText(42, QCoreApplication.translate("Form", u"PuOr", None))
        self.cmap_combo.setItemText(43, QCoreApplication.translate("Form", u"RdGy", None))
        self.cmap_combo.setItemText(44, QCoreApplication.translate("Form", u"RdBu", None))
        self.cmap_combo.setItemText(45, QCoreApplication.translate("Form", u"RdYlBu", None))
        self.cmap_combo.setItemText(46, QCoreApplication.translate("Form", u"RdYlGn", None))
        self.cmap_combo.setItemText(47, QCoreApplication.translate("Form", u"Spectral", None))
        self.cmap_combo.setItemText(48, QCoreApplication.translate("Form", u"coolwarm", None))
        self.cmap_combo.setItemText(49, QCoreApplication.translate("Form", u"bwr", None))
        self.cmap_combo.setItemText(50, QCoreApplication.translate("Form", u"seismic", None))
        self.cmap_combo.setItemText(51, QCoreApplication.translate("Form", u"twilight", None))
        self.cmap_combo.setItemText(52, QCoreApplication.translate("Form", u"twilight_shifted", None))
        self.cmap_combo.setItemText(53, QCoreApplication.translate("Form", u"hsv", None))
        self.cmap_combo.setItemText(54, QCoreApplication.translate("Form", u"Pastel1", None))
        self.cmap_combo.setItemText(55, QCoreApplication.translate("Form", u"Pastel2", None))
        self.cmap_combo.setItemText(56, QCoreApplication.translate("Form", u"Paired", None))
        self.cmap_combo.setItemText(57, QCoreApplication.translate("Form", u"Accent", None))
        self.cmap_combo.setItemText(58, QCoreApplication.translate("Form", u"Dark2", None))
        self.cmap_combo.setItemText(59, QCoreApplication.translate("Form", u"Set1", None))
        self.cmap_combo.setItemText(60, QCoreApplication.translate("Form", u"Set2", None))
        self.cmap_combo.setItemText(61, QCoreApplication.translate("Form", u"Set3", None))
        self.cmap_combo.setItemText(62, QCoreApplication.translate("Form", u"tab10", None))
        self.cmap_combo.setItemText(63, QCoreApplication.translate("Form", u"tab20", None))
        self.cmap_combo.setItemText(64, QCoreApplication.translate("Form", u"tab20b", None))
        self.cmap_combo.setItemText(65, QCoreApplication.translate("Form", u"tab20c", None))
        self.cmap_combo.setItemText(66, QCoreApplication.translate("Form", u"flag", None))
        self.cmap_combo.setItemText(67, QCoreApplication.translate("Form", u"prism", None))
        self.cmap_combo.setItemText(68, QCoreApplication.translate("Form", u"ocean", None))
        self.cmap_combo.setItemText(69, QCoreApplication.translate("Form", u"gist_earth", None))
        self.cmap_combo.setItemText(70, QCoreApplication.translate("Form", u"terrain", None))
        self.cmap_combo.setItemText(71, QCoreApplication.translate("Form", u"gist_stern", None))
        self.cmap_combo.setItemText(72, QCoreApplication.translate("Form", u"gnuplot", None))
        self.cmap_combo.setItemText(73, QCoreApplication.translate("Form", u"gnuplot2", None))
        self.cmap_combo.setItemText(74, QCoreApplication.translate("Form", u"CMRmap", None))
        self.cmap_combo.setItemText(75, QCoreApplication.translate("Form", u"cubehelix", None))
        self.cmap_combo.setItemText(76, QCoreApplication.translate("Form", u"brg", None))
        self.cmap_combo.setItemText(77, QCoreApplication.translate("Form", u"gist_rainbow", None))
        self.cmap_combo.setItemText(78, QCoreApplication.translate("Form", u"rainbow", None))
        self.cmap_combo.setItemText(79, QCoreApplication.translate("Form", u"jet", None))
        self.cmap_combo.setItemText(80, QCoreApplication.translate("Form", u"turbo", None))
        self.cmap_combo.setItemText(81, QCoreApplication.translate("Form", u"nipy_spectral", None))
        self.cmap_combo.setItemText(82, QCoreApplication.translate("Form", u"gist_ncar", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"ShowColorBar", None))
        self.show_colorbar_check.setText("")
    # retranslateUi

