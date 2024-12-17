from PySide6.QtWidgets import QComboBox, QToolTip, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        QToolTip.setFont(QFont('Times New Roman', 15))
        self.setLineEdit(QLineEdit())
        self.lineEdit().setReadOnly(True)
        self.view().clicked.connect(self.selectItemAction)
        self.addCheckableItem('ALL')
        self.SelectAllStatus = True

    def addCheckableItem(self, text):
        super().addItem(text)
        item = self.model().item(self.count() - 1, 0)
        item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        item.setCheckState(Qt.CheckState.Unchecked)
        item.setToolTip(text)

    def addCheckableItems(self, texts):
        for text in texts:
            self.addCheckableItem(text)

    def ifChecked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == Qt.CheckState.Checked

    def checkedItems(self):
        return [self.itemText(i) for i in range(self.count()) if self.ifChecked(i)]

    def notCheckedItems(self):
        return [self.itemText(i) for i in range(self.count()) if self.model().item(i, 0).checkState() == Qt.CheckState.Unchecked]

    def checkedItemsStr(self):
        return ','.join(self.checkedItems()).strip('ALL').strip(',')

    def selectItemAction(self, index):
        if index.row() == 0:
            for i in range(self.model().rowCount()):
                if self.SelectAllStatus:
                    self.model().item(i).setCheckState(Qt.CheckState.Checked)
                else:
                    self.model().item(i).setCheckState(Qt.CheckState.Unchecked)
            self.SelectAllStatus = not self.SelectAllStatus
        else:
            if len(self.checkedItems()) == self.count() - 1:
                self.model().item(0).setCheckState(Qt.CheckState.Checked)
                self.SelectAllStatus = False
            if len(self.notCheckedItems()) > 0:
                self.model().item(0).setCheckState(Qt.CheckState.Unchecked)
                self.SelectAllStatus = True

        self.lineEdit().clear()
        self.lineEdit().setText(self.checkedItemsStr())

    def clear(self) -> None:
        super().clear()
        self.addCheckableItem('ALL')

    def select_all(self):
        for i in range(self.model().rowCount()):
            self.model().item(i).setCheckState(Qt.CheckState.Checked)
        self.lineEdit().setText(self.checkedItemsStr())
