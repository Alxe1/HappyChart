# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fillBetweenLayerToolUIkwHEOl.ui'
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
    QSizePolicy, QSlider, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc
from widgets.inherited_widgets.editable_exclusive_combo_box_widget import EditableExclusiveComboBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 852)
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

        self.y1_series_combo = EditableExclusiveComboBox(Form)
        self.y1_series_combo.setObjectName(u"y1_series_combo")
        self.y1_series_combo.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.y1_series_combo)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.y2_series_combo = EditableExclusiveComboBox(Form)
        self.y2_series_combo.setObjectName(u"y2_series_combo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.y2_series_combo)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.data_label_line = QLineEdit(Form)
        self.data_label_line.setObjectName(u"data_label_line")
        self.data_label_line.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_label_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(9, QFormLayout.FieldRole, self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.where_first_combo = EditableExclusiveComboBox(Form)
        self.where_first_combo.setObjectName(u"where_first_combo")
        self.where_first_combo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.where_first_combo)

        self.where_eq_combo = QComboBox(Form)
        self.where_eq_combo.addItem("")
        self.where_eq_combo.addItem("")
        self.where_eq_combo.addItem("")
        self.where_eq_combo.addItem("")
        self.where_eq_combo.addItem("")
        self.where_eq_combo.setObjectName(u"where_eq_combo")
        self.where_eq_combo.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_2.addWidget(self.where_eq_combo)

        self.where_second_combo = EditableExclusiveComboBox(Form)
        self.where_second_combo.setObjectName(u"where_second_combo")
        self.where_second_combo.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.where_second_combo)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.verticalLayout_2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.face_color_btn = QToolButton(Form)
        self.face_color_btn.setObjectName(u"face_color_btn")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.face_color_btn)

        self.label_33 = QLabel(Form)
        self.label_33.setObjectName(u"label_33")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_33)

        self.edge_color_btn = QToolButton(Form)
        self.edge_color_btn.setObjectName(u"edge_color_btn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.edge_color_btn)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.interpolate_check = QCheckBox(Form)
        self.interpolate_check.setObjectName(u"interpolate_check")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.interpolate_check)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.step_combo = QComboBox(Form)
        self.step_combo.addItem("")
        self.step_combo.addItem("")
        self.step_combo.addItem("")
        self.step_combo.setObjectName(u"step_combo")
        self.step_combo.setFrame(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.step_combo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_2)

        self.transparency_slider = QSlider(Form)
        self.transparency_slider.setObjectName(u"transparency_slider")
        self.transparency_slider.setMaximum(100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.setOrientation(Qt.Orientation.Horizontal)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.transparency_slider)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_16)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"FillBetween Layer", None))
        self.toolButton.setText("")
        self.y_series_label.setText(QCoreApplication.translate("Form", u"Y1DataSeries", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Y2DataSeries", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"DataLabel", None))
        self.where_eq_combo.setItemText(0, QCoreApplication.translate("Form", u"=", None))
        self.where_eq_combo.setItemText(1, QCoreApplication.translate("Form", u">", None))
        self.where_eq_combo.setItemText(2, QCoreApplication.translate("Form", u"<", None))
        self.where_eq_combo.setItemText(3, QCoreApplication.translate("Form", u">=", None))
        self.where_eq_combo.setItemText(4, QCoreApplication.translate("Form", u"<=", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"WhereCond", None))
        self.face_color_btn.setText("")
        self.label_33.setText(QCoreApplication.translate("Form", u"FaceColor", None))
        self.edge_color_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"EdgeColor", None))
        self.interpolate_check.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Interpolate", None))
        self.step_combo.setItemText(0, QCoreApplication.translate("Form", u"pre", None))
        self.step_combo.setItemText(1, QCoreApplication.translate("Form", u"post", None))
        self.step_combo.setItemText(2, QCoreApplication.translate("Form", u"mid", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Step", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Transparency", None))
    # retranslateUi

