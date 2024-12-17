from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QLineEdit


class EditableExclusiveComboBox(QComboBox):
    def __init__(self, parent=None):
        super(EditableExclusiveComboBox, self).__init__(parent)
        self.setLineEdit(QLineEdit())
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.lineEdit().setReadOnly(False)

    def addSelectableItem(self, text):
        super().addItem(text)
        item = self.model().item(self.count() - 1, 0)
        item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

    def addSelectableItems(self, texts):
        for text in texts:
            self.addSelectableItem(text)
