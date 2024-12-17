from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit


class ClickableLineEdit(QLineEdit):
    clicked = QtCore.Signal(bool)

    def __init__(self, parent=None, *args, **kwargs):
        super(ClickableLineEdit, self).__init__(parent=parent, *args, **kwargs)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(True)
