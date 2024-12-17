from PySide6.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve
from PySide6 import QtCore
from PySide6.QtWidgets import QLabel


class ClickableLabel(QLabel):
    clicked = QtCore.Signal(bool)

    def __init__(self, parent=None):
        super(ClickableLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.animateButton()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.animateBack(self.animation)
            self.clicked.emit(True)

    def animateButton(self):
        # 获取按钮的初始和结束状态
        start_pos = self.pos()
        end_pos = start_pos + QPoint(3, 3)

        # 创建一个动画，目标对象是按钮，动画持续时间250毫秒
        self.animation = QPropertyAnimation(self, b'pos', self)
        self.animation.setDuration(150)
        self.animation.setStartValue(QPoint(start_pos))
        self.animation.setEndValue(QPoint(end_pos))
        # self.animation.setKeyValueAt(0.5, QPoint(final_pos))  # 在动画一半的时候改变方向
        self.animation.setEasingCurve(QEasingCurve.Linear)  # 设置动画曲线为二次加速曲线
        # animation.finished.connect(lambda: self.animateBack(animation))  # 动画结束后执行反向动画
        self.animation.start()

    def animateBack(self, animation):
        # 创建一个返回原位的动画
        return_animation = QPropertyAnimation(self, b'pos', self)
        return_animation.setDuration(150)
        return_animation.setStartValue(QPoint(animation.endValue()))
        return_animation.setEndValue(QPoint(animation.startValue()))
        return_animation.setEasingCurve(QEasingCurve.Linear)
        return_animation.start()
