# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'charts_dialogFJSKeU.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc
from widgets.inherited_widgets.clickable_label_widget import ClickableLabel


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 700)
        Dialog.setMinimumSize(QSize(1000, 700))
        Dialog.setMaximumSize(QSize(1000, 700))
        Dialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 996, 669))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 180))
        self.frame_10.setMaximumSize(QSize(240, 180))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.vhline_layer = ClickableLabel(self.frame_10)
        self.vhline_layer.setObjectName(u"vhline_layer")
        self.vhline_layer.setPixmap(QPixmap(u":/images/images/vhlines.png"))
        self.vhline_layer.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.vhline_layer)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_10)


        self.gridLayout.addWidget(self.frame_10, 2, 2, 1, 1)

        self.frame_1 = QFrame(self.scrollAreaWidgetContents)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(0, 180))
        self.frame_1.setMaximumSize(QSize(240, 180))
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scatter_layer = ClickableLabel(self.frame_1)
        self.scatter_layer.setObjectName(u"scatter_layer")
        self.scatter_layer.setPixmap(QPixmap(u":/images/images/scatter_plot.png"))
        self.scatter_layer.setScaledContents(True)
        self.scatter_layer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scatter_layer.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.scatter_layer)

        self.label_2 = QLabel(self.frame_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalLayout_3.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_1, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 180))
        self.frame_6.setMaximumSize(QSize(240, 180))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cdf_layer = ClickableLabel(self.frame_6)
        self.cdf_layer.setObjectName(u"cdf_layer")
        self.cdf_layer.setPixmap(QPixmap(u":/images/images/cdf.png"))
        self.cdf_layer.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.cdf_layer)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)


        self.gridLayout.addWidget(self.frame_6, 1, 2, 1, 1)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 180))
        self.frame_11.setMaximumSize(QSize(240, 180))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.text_layer = ClickableLabel(self.frame_11)
        self.text_layer.setObjectName(u"text_layer")
        self.text_layer.setPixmap(QPixmap(u":/images/images/text.png"))
        self.text_layer.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.text_layer)

        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addWidget(self.frame_11, 2, 3, 1, 1)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 180))
        self.frame_4.setMaximumSize(QSize(240, 180))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.errorbar_layer = ClickableLabel(self.frame_4)
        self.errorbar_layer.setObjectName(u"errorbar_layer")
        self.errorbar_layer.setPixmap(QPixmap(u":/images/images/error_plot.png"))
        self.errorbar_layer.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.errorbar_layer)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.gridLayout.addWidget(self.frame_4, 0, 4, 1, 1)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 180))
        self.frame_9.setMaximumSize(QSize(240, 180))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.span_layer = ClickableLabel(self.frame_9)
        self.span_layer.setObjectName(u"span_layer")
        self.span_layer.setPixmap(QPixmap(u":/images/images/span.png"))
        self.span_layer.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.span_layer)

        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)


        self.gridLayout.addWidget(self.frame_9, 2, 1, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 180))
        self.frame_2.setMaximumSize(QSize(240, 180))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line_layer = ClickableLabel(self.frame_2)
        self.line_layer.setObjectName(u"line_layer")
        self.line_layer.setPixmap(QPixmap(u":/images/images/line_plot.png"))
        self.line_layer.setScaledContents(True)
        self.line_layer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.line_layer)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.verticalLayout_4.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 180))
        self.frame_12.setMaximumSize(QSize(240, 180))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.annotation_layer = ClickableLabel(self.frame_12)
        self.annotation_layer.setObjectName(u"annotation_layer")
        self.annotation_layer.setPixmap(QPixmap(u":/images/images/annotation.png"))
        self.annotation_layer.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.annotation_layer)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_13)


        self.gridLayout.addWidget(self.frame_12, 2, 4, 1, 1)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 180))
        self.frame_3.setMaximumSize(QSize(240, 180))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stairs_layer = ClickableLabel(self.frame_3)
        self.stairs_layer.setObjectName(u"stairs_layer")
        self.stairs_layer.setPixmap(QPixmap(u":/images/images/stairs_plot.png"))
        self.stairs_layer.setScaledContents(True)
        self.stairs_layer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.stairs_layer)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_3, 0, 3, 1, 1)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 180))
        self.frame_7.setMaximumSize(QSize(240, 180))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.regression_layer = ClickableLabel(self.frame_7)
        self.regression_layer.setObjectName(u"regression_layer")
        self.regression_layer.setPixmap(QPixmap(u":/images/images/regression.png"))
        self.regression_layer.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.regression_layer)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)


        self.gridLayout.addWidget(self.frame_7, 1, 3, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 180))
        self.frame_5.setMaximumSize(QSize(240, 180))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.density_layer = ClickableLabel(self.frame_5)
        self.density_layer.setObjectName(u"density_layer")
        self.density_layer.setPixmap(QPixmap(u":/images/images/density.png"))
        self.density_layer.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.density_layer)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 180))
        self.frame_8.setMaximumSize(QSize(240, 180))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.fill_between_layer = ClickableLabel(self.frame_8)
        self.fill_between_layer.setObjectName(u"fill_between_layer")
        self.fill_between_layer.setPixmap(QPixmap(u":/images/images/fill_between.png"))
        self.fill_between_layer.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.fill_between_layer)

        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9)


        self.gridLayout.addWidget(self.frame_8, 1, 4, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Select Chart", None))
#if QT_CONFIG(tooltip)
        self.vhline_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/vhlines.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vhline_layer.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Horizontal/Vertical Line Layer", None))
#if QT_CONFIG(tooltip)
        self.scatter_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/scatter_plot.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.scatter_layer.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Scatter Layer", None))
#if QT_CONFIG(tooltip)
        self.cdf_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/cdf.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cdf_layer.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"CDF Layer", None))
#if QT_CONFIG(tooltip)
        self.text_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/text.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_layer.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Text Layer", None))
#if QT_CONFIG(tooltip)
        self.errorbar_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/error_plot.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.errorbar_layer.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"ErrorBar Layer", None))
#if QT_CONFIG(tooltip)
        self.span_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/span.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.span_layer.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Horizontal/Vertical Span Layer", None))
#if QT_CONFIG(tooltip)
        self.line_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/line_plot.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.line_layer.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Line Layer", None))
#if QT_CONFIG(tooltip)
        self.annotation_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/annotation.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.annotation_layer.setText("")
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Annotation Layer", None))
#if QT_CONFIG(tooltip)
        self.stairs_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/stairs_plot.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stairs_layer.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Stairs Layer", None))
#if QT_CONFIG(tooltip)
        self.regression_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/regression.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.regression_layer.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Regression Layer", None))
#if QT_CONFIG(tooltip)
        self.density_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/density.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.density_layer.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Density Layer", None))
#if QT_CONFIG(tooltip)
        self.fill_between_layer.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/images/images/fill_between.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fill_between_layer.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Fill Between Layer", None))
    # retranslateUi

