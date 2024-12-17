# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activationUIsooJDq.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 320)
        Dialog.setMinimumSize(QSize(460, 320))
        Dialog.setMaximumSize(QSize(460, 320))
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.series_no_line = QLineEdit(Dialog)
        self.series_no_line.setObjectName(u"series_no_line")
        self.series_no_line.setEnabled(True)
        self.series_no_line.setFont(font1)
        self.series_no_line.setFrame(True)
        self.series_no_line.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.series_no_line)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.activation_code_text = QTextEdit(Dialog)
        self.activation_code_text.setObjectName(u"activation_code_text")
        self.activation_code_text.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.activation_code_text)


        self.verticalLayout.addLayout(self.formLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.activate_btn = QPushButton(Dialog)
        self.activate_btn.setObjectName(u"activate_btn")
        self.activate_btn.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.activate_btn, 0, 0, 1, 1)

        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.cancel_btn, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Activation", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Series Number", None))
        self.series_no_line.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Activation Code", None))
        self.activate_btn.setText(QCoreApplication.translate("Dialog", u"Activate", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

